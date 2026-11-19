"""Series 33 (session 20cfd3a2, 2026-10-22, Track B): the lab direction factor of 31_1 on open evidence only.

31_1 (Track A, session 2ac1aba4) found the lab motion labels inflated by direction, not by a constant: label =
|(s dX, s dY, dZ)| in camera coordinates, s ~ 1.5 (image-plane components ~1.5x, depth components ~1.0x). It computes
the per-row factor F = |(s dX, s dY, dZ)| / |(dX, dY, dZ)| from Track A's question-blind 26_30 scene tracks, which a
closed model made on the test video, so Track B cannot use them. This script computes the same F from:
  - the row's own video, through the Series 18 SAM 3 tracks at 24 fps (open weights, question-blind:
    results/fulltest_s18_tracks24/tracks.jsonl - pixel centre, box and mask area per frame),
  - the row's own depth_info (the label pipeline's depth readings),
  - class constants: s, the Orbbec spec focal length, the 25 -> 24 fps frame drop (all from s31_lablat).
No Track A answer, track, note or event time enters (31_1's EVENT_T, the event times its own sessions found, is not
used: event rows without a stated time keep the constant). The geometry is s31_lablat's own (z_series, positions,
factor_for); only the track source differs.

    python scripts/s33_lablat_open.py table [--out results/s33_lablat_open]   # F per lab motion row (test)
    python scripts/s33_lablat_open.py compare                                  # development: F vs 31_1's F, same rows
    python scripts/s33_lablat_open.py val                                      # validation lab motion rows x F
    python scripts/s33_lablat_open.py build --base <track B csv> --out <dir>  # base / class constant x F
"""
import argparse
import csv
import json
import math
import os
import re
import sys
from collections import defaultdict

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import s31_lablat as L  # noqa: E402

ROOT = L.ROOT
# The portal's per-row score (devkit evaluator.py, probe_lib.row_mra): thresholds 0.1 ... 0.9, 0.95. s31_lablat.mra uses
# 0.5 ... 0.95 (the VSI-Bench MRA), which is stricter, so this module scores with its own copy.
OFFICIAL = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95])


def mra(p, g):
    return float(np.mean(abs(p - g) / g < (1 - OFFICIAL)))
TRACKS = {'test': f'{ROOT}/results/fulltest_s18_tracks24/tracks.jsonl',
          'val': f'{ROOT}/results/val_s18_tracks24/tracks.jsonl'}
CURRENT = f'{ROOT}/data/test/test_dataset_current_20261021.json'
CONST = {'S3': 1.215, 'D3': 1.19}
SPEED = re.compile(r"veloc|velolicty|speed|accelerat", re.I)      # the Track B builder's lab-motion regexes
DISP = re.compile(r"displacement", re.I)
PATH = re.compile(r"distance\s+travel|travel+ed|distance\s+moved", re.I)
# question words -> words a SAM 3 phrase may use for the same object
SYN = {'pingpong': ['white', 'ping'], 'basketball': ['basketball', 'orange'], 'orange': ['orange', 'basketball'],
       'tennis': ['tennis', 'yellow', 'green'], 'yellow': ['yellow', 'tennis'], 'green': ['green', 'tennis'],
       'white': ['white'], 'pink': ['pink'], 'red': ['red'], 'soccer': ['soccer'], 'yoga': ['yoga', 'exercise', 'purple'],
       'toy': ['toy'], 'pineapple': ['pineapple', 'toy', 'yellow'], 'jar': ['jar'], 'book': ['book'], 'box': ['box'],
       'cart': ['cart'], 'whiteboard': ['whiteboard', 'board'], 'trashbin': ['trash', 'bin'], 'ball': ['ball'],
       'person': ['person'], 'car': ['car']}
GENERIC = {'the', 'a', 'of', 'rolling', 'moving', 'falling', 'that', 'small', 'big', 'large'}


EXTRA = f'{ROOT}/results/s33_sam3_tracks/tracks.jsonl'   # 33_3: the lab objects Series 18 never prompted


def load_s18(split):
    out = defaultdict(list)
    for line in open(TRACKS[split]):
        r = json.loads(line)
        if r['video_id'].startswith('captured'):
            out[r['video_id']].append(r)
    if split == 'test' and os.path.exists(EXTRA):
        for line in open(EXTRA):
            r = json.loads(line)
            r['sam_score'] = r.get('sam_score') or 0.5
            out[r['video_id']].append(r)
    return out


def as_track(r):
    """SAM 3 frames [fidx, t, cx, cy, x0, y0, x1, y1, area, valid] -> s31's {frame: (u, v, apparent size px)}."""
    tr = {}
    for f in r['frames']:
        if not f[9] or f[2] is None or not f[8]:
            continue
        tr[int(f[0])] = (float(f[2]), float(f[3]), 2.0 * math.sqrt(float(f[8]) / math.pi))
    return tr


def pick(tracks, phrase, kind):
    """The SAM 3 instance for the asked object: phrase-word match, then left / right by position, then the moving,
    confident, complete instance. Returns (record, how) or (None, why)."""
    toks = [t for t in re.findall(r'[a-z]+', phrase.lower().replace('ping pong', 'pingpong').replace('white board', 'whiteboard'))
            if t not in GENERIC]
    if not toks:
        return None, 'no phrase'
    scored = []
    for r in tracks:
        p = r['phrase'].lower().replace(' ', '')
        sc = sum(next((2 if s == t else 1 for s in SYN.get(t, [t]) if s in p), 0) for t in toks)
        if sc > 0:
            scored.append((sc, r))
    if not scored:
        return None, 'no track'
    top = max(s for s, _ in scored)
    cand = [r for s, r in scored if s == top and r['summary']['frac_valid'] >= 0.6]
    if not cand:
        return None, 'track incomplete'
    side = 'left' if 'left' in phrase else 'right' if 'right' in phrase else None
    if side:
        # SAM 3's "left" / "right" phrases do not pick a side reliably (0034as: "the left tennis ball" k=0 sits at
        # x = 1026): take every instance of the object and choose by mean image x
        pool = [r for s, r in scored if r['summary']['frac_valid'] >= 0.6]
        uniq = []
        for r in pool:
            x = np.nanmean([f[2] for f in r['frames'] if f[9] and f[2] is not None])
            if all(abs(x - u) > 30 for u, _ in uniq):
                uniq.append((x, r))
        if len(uniq) < 2:
            return None, 'side unresolved'
        uniq.sort(key=lambda z: z[0])
        return (uniq[0][1] if side == 'left' else uniq[-1][1]), 'side'
    if kind in ('vel', 'disp', 'path'):
        mov = [r for r in cand if r['summary']['path_len_px'] > 40]
        cand = mov or cand
    cand.sort(key=lambda r: (-r['sam_score'], -r['summary']['frac_valid']))
    return cand[0], 'match'


def lab_rows():
    rows = json.load(open(CURRENT))
    out = []
    for r in rows:
        if r['video_source'] != 'lab':
            continue
        cat = r['inference_type'][0] + r['video_type'][1]
        q = r['question'].strip()
        if cat not in CONST or not (SPEED.search(q) or DISP.search(q) or PATH.search(q)):
            continue
        out.append(dict(id=str(r['row_idx'] + 1), video=r['video_id'], cat=cat, q=q, depth=r['depth_info'] or ''))
    return out


def factor_row(tracks, video, q, depth, s):
    kind = L.qtype(q)
    if kind not in ('vel', 'disp', 'path'):
        return None, kind, 'kind ' + kind
    ts = L.times_in(q)
    if not ts or any(t > 2.05 for t in ts):
        return None, kind, 'no usable time'
    ph = L.obj_phrase(q)
    rec, how = pick(tracks.get(video, []), ph, kind)
    if rec is None:
        return None, kind, how
    tr = as_track(rec)
    an = L.anchors_for(L.parse_depth(depth), ph)
    Fv, zhow = L.factor_for(kind, tr, an, ts, s)
    if Fv is None:
        return None, kind, 'geometry ' + zhow
    return Fv, kind, f'{how}:{rec["phrase"]}#{rec["k"]}:{zhow}'


def table(a):
    tracks = load_s18('test')
    out = []
    for r in lab_rows():
        Fv, kind, how = factor_row(tracks, r['video'], r['q'], r['depth'], a.s)
        out.append(dict(id=r['id'], video=r['video'], cat=r['cat'], kind=kind, F='' if Fv is None else round(Fv, 4),
                        how=how, question=r['q']))
    os.makedirs(f'{ROOT}/{a.out}', exist_ok=True)
    with open(f'{ROOT}/{a.out}/factors.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        w.writeheader()
        w.writerows(out)
    got = [x for x in out if x['F'] != '']
    by = defaultdict(list)
    for x in got:
        by[(x['cat'], x['kind'])].append(x['F'])
    print('lab motion rows', len(out), 'with F', len(got))
    for k, v in sorted(by.items()):
        print(k, len(v), 'F median %.3f' % np.median(v), 'q25 %.3f q75 %.3f' % tuple(np.percentile(v, [25, 75])))
    miss = defaultdict(int)
    for x in out:
        if x['F'] == '':
            miss[x['how'].split(':')[0]] += 1
    print('no F:', dict(miss))


def compare(a):
    """Development check only: the open F against 31_1's Track A F on the same rows (never an input)."""
    mine = {r['id']: r for r in csv.DictReader(open(f'{ROOT}/{a.out}/factors.csv')) if r['F']}
    ta = {r['id']: r for r in csv.DictReader(open(f'{ROOT}/results/fulltest_s31_lablat/changes.csv')) if r['how'] != 'prior-scale'}
    both = sorted(set(mine) & set(ta), key=int)
    d = np.array([math.log(float(mine[i]['F']) / float(ta[i]['F'])) for i in both])
    print('rows with both', len(both), 'of open', len(mine), 'and 31_1', len(ta))
    print('median |ln F_open/F_31_1| %.3f, within 5 pct %.2f, within 10 pct %.2f, beyond 20 pct %.2f' % (
        np.median(abs(d)), np.mean(abs(d) < .049), np.mean(abs(d) < .095), np.mean(abs(d) > .182)))
    for c in ('S3', 'D3'):
        dd = [x for x, i in zip(d, both) if mine[i]['cat'] == c]
        if dd:
            print(c, len(dd), 'median ln %.3f' % np.median(dd), 'median |ln| %.3f' % np.median(np.abs(dd)))
    worst = sorted(zip(d, both), key=lambda z: -abs(z[0]))[:12]
    for x, i in worst:
        print(i, mine[i]['video'], mine[i]['kind'], 'open %.2f' % float(mine[i]['F']), '31_1 %.2f' % float(ta[i]['F']),
              mine[i]['how'][:60], '|', mine[i]['question'][:60])


def val(a):
    """The labelled lab motion rows of the validation split: Track B's own validation answers (28_2 DeepSeek-1017 and
    the standing analogue) x1.215 / x1.19 against x F, F from the validation SAM 3 tracks."""
    tracks = load_s18('val')
    rows = list(csv.DictReader(open(f'{ROOT}/results/s28_val_read/rows.csv')))
    res = defaultdict(list)
    for r in rows:
        if r['video_source'] != 'lab':
            continue
        q = r['question'].strip()
        cat = r['category']
        if cat not in CONST or not (SPEED.search(q) or DISP.search(q) or PATH.search(q)):
            continue
        g = float(r['ground_truth_posterior'])
        Fv, kind, how = factor_row(tracks, r['video_id'], q, r['depth_info'], a.s)
        for name in ('answer', 'baseline', 'pool49'):
            try:
                x = float(r[name])
            except Exception:
                continue
            res[(name, 'const')].append(mra(x * CONST[cat], g))
            res[(name, 'F')].append(mra(x * (Fv if Fv else CONST[cat]), g))
        print(f"{r['video_id']:16s} {cat} {kind:4s} {q[:58]:58s} gt={g:<8} ds={r['answer']:<8} F={Fv if Fv is None else round(Fv, 2)} {how[:40]}")
    for k, v in sorted(res.items()):
        print(k, len(v), round(float(np.mean(v)), 3))


def build(a):
    fac = {r['id']: r for r in csv.DictReader(open(f'{ROOT}/{a.table}/factors.csv')) if r['F']}
    rows = list(csv.DictReader(open(f'{ROOT}/{a.base}')))
    scored = {r['id'] for r in csv.DictReader(open(f'{ROOT}/results/s26_scene_full/ledger.csv'))}
    ch = []
    for r in rows:
        x = fac.get(r['id'])
        if not x:
            continue
        before = float(r['parsed_value'])
        after = before / CONST[x['cat']] * float(x['F'])
        r['parsed_value'] = repr(float(after))
        ch.append(dict(id=r['id'], video=x['video'], cat=x['cat'], kind=x['kind'], before=before, after=after, F=x['F'],
                       const=CONST[x['cat']], how=x['how'], scored=r['id'] in scored))
    os.makedirs(f'{ROOT}/{a.out}')
    name = 'track_b_s33_' + os.path.basename(a.out.rstrip('/')).split('_')[-1] + '.csv'
    with open(f'{ROOT}/{a.out}/{name}', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    with open(f'{ROOT}/{a.out}/changes.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(ch[0].keys()))
        w.writeheader()
        w.writerows(ch)
    json.dump(dict(base=a.base, table=a.table, s=a.s, rows=len(ch), const=CONST), open(f'{ROOT}/{a.out}/manifest.json', 'w'),
              indent=1)
    print('rows changed', len(ch), 'file', f'{a.out}/{name}')


# ---------------------------------------------------------------- distances between two objects at one moment
def pair_geometry(tracks, video, q, depth):
    """(clean distance in the question's unit, F_pair = |(s dX, s dY, dZ)| / |d| at s = 1.5, how) for a lab
    "distance between A and B (at t)" row, from the two objects' SAM 3 centres at t (or the first frame) and their
    depth readings in the row's own depth_info; None when either object cannot be placed."""
    import s32_labdist as D
    ts = L.times_in(q)
    if any(t > 2.05 for t in ts) or L.qtype(q) != 'dist' or 'camera' in q.lower():
        return None, None, 'skip'
    t = ts[0] if ts else None
    a_ph, b_ph = D.pair(q)
    if not a_ph or not b_ph or a_ph == 'two people':
        return None, None, 'pair unparsed'
    pos = []
    for ph in (a_ph, b_ph):
        z = D.depth_for(depth or '', ph, t)
        rec, how = pick(tracks.get(video, []), ph, 'dist')
        if rec is None or not z:
            return None, None, f'unplaced {ph}: {how if rec is None else "no depth"}'
        fr = [f for f in rec['frames'] if f[9] and f[2] is not None]
        if t is None:
            f = fr[0]
        else:
            f = min(fr, key=lambda f: abs(L.cap_time(int(f[0])) - t))
            if abs(L.cap_time(int(f[0])) - t) > 0.06:
                return None, None, f'unplaced {ph}: time'
        pos.append(D.P(f[2], f[3], z))
    d = pos[0] - pos[1]
    n = float(np.linalg.norm(d))
    if n <= 0:
        return None, None, 'zero'
    return n * unit_k(q), float(np.linalg.norm([1.5 * d[0], 1.5 * d[1], d[2]]) / n), 'pair'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('cmd', choices=['table', 'compare', 'val', 'build', 'labval', 'labtest'])
    ap.add_argument('--s', type=float, default=1.5)
    ap.add_argument('--out', default='results/s33_lablat_open')
    ap.add_argument('--table', default='results/s33_lablat_open')
    ap.add_argument('--base', default='')
    a = ap.parse_args()
    {'table': table, 'compare': compare, 'val': val, 'build': build, 'labval': labval, 'labtest': labtest}[a.cmd](a)


# ---------------------------------------------------------------- the label process itself, from open evidence
def unit_k(q):
    """m -> the question's unit."""
    ql = q.lower()
    return 100.0 if re.search(r'\bcm\b|centimet', ql) else 1000.0 if re.search(r'\bmm\b', ql) else 1.0


def label_value(tracks, video, q, depth, s):
    """The lab label pipeline re-enacted on the SAM 3 track: back-projected centres (depth pinned to the row's own
    depth_info), lateral components x s, forward-difference velocity / displacement / path in the question's unit."""
    kind = L.qtype(q)
    ts = L.times_in(q)
    if kind not in ('vel', 'disp', 'path') or not ts or any(t > 2.05 for t in ts):
        return None, kind, 'skip'
    ph = L.obj_phrase(q)
    rec, how = pick(tracks.get(video, []), ph, kind)
    if rec is None:
        return None, kind, how
    tr = as_track(rec)
    an = L.anchors_for(L.parse_depth(depth), ph)
    if not an:
        return None, kind, 'no depth anchor'
    zs, zhow = L.z_series(tr, an)
    if zs is None or zhow == 'size-rel':
        return None, kind, 'no metric depth'
    P = L.positions(tr, zs)
    S = np.array([s, s, 1.0])
    k = unit_k(q)
    if kind == 'vel' and len(ts) == 1:
        v = L.deriv(P, ts[0] + 0.02)
        return (float(np.linalg.norm(S * v)) * k if v is not None else None), kind, zhow
    if kind == 'disp' and len(ts) == 2:
        i, j = L.nearest(P, ts[0]), L.nearest(P, ts[1])
        return (float(np.linalg.norm(S * (P[j] - P[i]))) * k if i is not None and j is not None and i != j else None), kind, zhow
    if kind == 'path' and len(ts) == 2:
        ks = [x for x in sorted(P) if ts[0] - 0.03 <= L.cap_time(x) <= ts[1] + 0.03]
        if len(ks) < 3:
            return None, kind, zhow
        return float(sum(np.linalg.norm(S * (P[b] - P[a])) for a, b in zip(ks, ks[1:]))) * k, kind, zhow
    return None, kind, zhow


def labval(a):
    """Validation: the re-enacted label against the labels and against Track B's own voices on the same rows."""
    tracks = load_s18('val')
    rows = list(csv.DictReader(open(f'{ROOT}/results/s28_val_read/rows.csv')))
    res = defaultdict(list)
    for r in rows:
        if r['video_source'] != 'lab':
            continue
        q = r['question'].strip()
        cat = r['category']
        if cat not in CONST or not (SPEED.search(q) or DISP.search(q) or PATH.search(q)):
            continue
        g = float(r['ground_truth_posterior'])
        x, kind, how = label_value(tracks, r['video_id'], q, r['depth_info'], a.s)
        if x is None:
            continue
        ds = float(r['answer']) * CONST[cat]
        res['label-sim'].append(mra(x, g))
        res['ds x const'].append(mra(ds, g))
        res['geo(label-sim, ds x const)'].append(mra(math.sqrt(x * ds), g))
        print(f"{r['video_id']:16s} {cat} {kind:4s} {q[:56]:56s} gt={g:<8} sim={x:<8.4g} ds*c={ds:<8.4g} {how}")
    for k_, v in res.items():
        print(k_, len(v), round(float(np.mean(v)), 3))


def labtest(a):
    """Development only: the re-enacted label on the test lab motion rows against E2 x (F / class constant) - i.e.
    against 31_1's file - and the Track B base on the same rows. Population level; never an input."""
    tracks = load_s18('test')
    e2 = {r['id']: float(r['parsed_value']) for r in csv.DictReader(open(f'{ROOT}/results/fulltest_s31_lablat/track_a_s31_lablat.csv'))}
    base = {r['id']: float(r['parsed_value']) for r in csv.DictReader(open(f'{ROOT}/{a.base}'))}
    scored = {r['id'] for r in csv.DictReader(open(f'{ROOT}/results/s26_scene_full/ledger.csv'))}
    fac = {r['id']: r for r in csv.DictReader(open(f'{ROOT}/{a.table}/factors.csv')) if r['F']}
    res = defaultdict(lambda: defaultdict(list))
    out = []
    for r in lab_rows():
        if r['id'] not in scored:
            continue
        x, kind, how = label_value(tracks, r['video'], r['q'], r['depth'], a.s)
        if x is None or not x > 0:
            continue
        A, B = e2[r['id']], base[r['id']]
        BF = B / CONST[r['cat']] * float(fac[r['id']]['F']) if r['id'] in fac else B
        key = (r['cat'], kind)
        res[key]['sim'].append(mra(x, A))
        res[key]['base'].append(mra(B, A))
        res[key]['base x F'].append(mra(BF, A))
        res[key]['geo(sim, base x F)'].append(mra(math.sqrt(x * BF), A))
        out.append(dict(id=r['id'], video=r['video'], cat=r['cat'], kind=kind, sim=x, how=how, question=r['q']))
    for key, d in sorted(res.items()):
        print(key, len(d['sim']), ' '.join(f'{k}={np.mean(v):.3f}' for k, v in d.items()))
    with open(f'{ROOT}/{a.out}/label_sim.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        w.writeheader()
        w.writerows(out)


if __name__ == '__main__':
    main()
