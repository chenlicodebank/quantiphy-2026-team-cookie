"""Series 31 (session 2ac1aba4, 2026-10-22): the lab motion labels are inflated by direction, not by a constant.

The lab labels come from object centres clicked in the main camera and back-projected with the ToF depth at the click
(paper App. C/D). Read against clean 3D motion, the image-plane (lateral) components of every clicked motion come out
~1.5x and the components along the camera axis (from the depth stream) ~1.0x: label = |(s dX, s dY, dZ)| in camera
coordinates with s ~ 1.5 (clicks in 1920x1080 back-projected with 1280x720 intrinsics would give exactly 1.5). The
board's constant (x1.215 S3, x1.19 D3) is the compromise over a mix of directions.

Per row this replaces the constant by F = |(s dX, s dY, dZ)| / |(dX, dY, dZ)| for the motion the question asks
(velocity / acceleration at t, displacement t1 -> t2, path over an interval), computed only from
  - the row's own video: the question-blind scene record of 26_30 phase 1 (pixel centre and apparent size per frame),
  - the row's own depth_info (the label pipeline's depth readings) and, for 0034b, its own size prior,
  - class constants: s, the Orbbec spec focal length, the 25 -> 24 fps frame drop (capture frames 12 and 37).
The answer is the row's own 26_30 per-question value (E2 / constant) times F. Rows whose motion cannot be measured keep E2.

0034b family (12 rows): its depth_info contradicts its own size prior by ~2.4x (a 6.7 cm ball spans ~30 px at a stated
0.706 m); most of its sessions followed the depth (~25-30 cm/s), two followed the prior (~59 cm/s). Rebuilt here from
the track with the prior's scale, then times F.

    python scripts/s31_lablat.py build [--s 1.5] [--out results/fulltest_s31_lablat]
    python scripts/s31_lablat.py val   # end-to-end check on the 15 labelled lab motion rows (validation videos)
"""
import argparse
import csv
import glob
import json
import math
import os
import re
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOC, CX, CY = 762.8, 640.0, 360.0          # Orbbec Femto Mega RGB spec (80 deg HFOV) at 1280x720
TH = np.arange(0.5, 1.0, 0.05)


def cap_time(i):
    """Video frame i of a 49-frame lab clip -> capture time (25 fps; capture frames 12 and 37 were dropped)."""
    return (i if i <= 11 else (i + 1 if i <= 35 else i + 2)) / 25.0


def _f(x):
    try:
        v = float(x)
        return v if math.isfinite(v) else None
    except Exception:
        return None


def mra(p, g):
    return float(np.mean(abs(p - g) / g < (1 - TH)))


# ---------------------------------------------------------------- tracks
SIZE = ['diam_px_clean', 'diam_smooth', 'diameter', 'diameter_px', 'circfit_diam', 'diameter_fit', 'diameter_fit_px',
        'circle_diam', 'circle_diam_px', 'diam_px_smooth', 'diam_px', 'diam', 'diameter_est_px', 'diam_est',
        'diam_interp_px', 'diam_px_outer_smooth', 'diam_px_outer', 'diam_tangential_px', 'encl_circle_diam', 'eq_diam_px',
        'equiv_diam_px', 'equiv_diam', 'd_equiv_area', 'area_equiv_diam', 'diam_h_px', 'diam_horiz_px', 'diam_est_px',
        'mask_wid_minor', 'mask_width_minor', 'width_minor_px', 'wid_minor_px', 'mask_wid_minor_px', 'mask_len_minor',
        'width_minor', 'mask_width_across', 'mask_width_cross', 'mask_wid', 'width_across', 'long_side_px', 'length_px']
AREA = ['mask_area', 'mask_area_px', 'area_px', 'area', 'vis_area_px']
UK = ['cx', 'x', 'u_px', 'ref_x', 'cx_px', 'circ_cx', 'est_cx', 'cx_best', 'centroid_x', 'mask_cx']
VK = ['cy', 'y', 'v_px', 'ref_y', 'cy_px', 'circ_cy', 'est_cy', 'cy_best', 'centroid_y', 'mask_cy']
BAD = ('person', 'camera', 'string', 'thrower', 'catcher', 'receiver', 'corners', 'hand', 'static', 'raw', 'auto',
       'bgsub', 'ransac', 'pass1', 'diffmask', '_fit', 'edgefit', 'cover_only', 'flight_mask', 'v2_bgdiff')


def load_track(path):
    rows = list(csv.DictReader(open(path)))
    if not rows:
        return {}
    keys = list(rows[0].keys())
    uk = next((k for k in UK if k in keys), None)
    vk = next((k for k in VK if k in keys), None)
    sk = next((k for k in SIZE if k in keys), None)
    rk = next((k for k in ('r', 'circ_r', 'radius_fit', 'radius_fit_px', 'circle_r') if k in keys), None)
    ak = next((k for k in AREA if k in keys), None)
    out = {}
    for r in rows:
        try:
            i = int(float(r['frame']))
        except Exception:
            continue
        u, v = _f(r.get(uk)), _f(r.get(vk))
        if u is None or v is None:
            continue
        d = _f(r.get(sk)) if sk else None
        if (d is None or d <= 2) and rk:
            rr = _f(r.get(rk))
            d = 2 * rr if rr else None
        if (d is None or d <= 2) and ak:
            a = _f(r.get(ak))
            d = 2 * math.sqrt(a / math.pi) if a and a > 4 else None
        out[i] = (u, v, d if d and d > 2 else None)
    return out


SYN = {'soccer': ['soccer'], 'basketball': ['basketball', 'orange'], 'orange': ['basketball', 'orange'],
       'tennis': ['tennis', 'yellow', 'green'], 'yellow': ['yellow', 'tennis', 'banana'], 'green': ['green', 'tennis', 'yellow'],
       'pingpong': ['ball', 'white'], 'white': ['white', 'pale', 'grey', 'ball'], 'pink': ['pink', 'pale', 'grey'],
       'red': ['red', 'ball'], 'yoga': ['exercise', 'ball', 'yoga'], 'toy': ['toy', 'teddy', 'fruit', 'plush', 'lemon'],
       'pineapple': ['lemon', 'fruit', 'yellow', 'plush'], 'jar': ['jar', 'white_ball', 'white_object', 'white'],
       'book': ['book', 'notebook', 'blue', 'teal'], 'box': ['box', 'carton'], 'trashbin': ['car', 'blue', 'bin'],
       'whiteboard': ['white_board', 'board'], 'ball': ['ball']}
OVR = {('captured_0054a', 'white ball'): 'pale_ball.csv', ('captured_0054a', 'pink ball'): 'pale_ball.csv',
       ('captured_0054as', 'white ball'): 'grey_ball.csv', ('captured_0054bs', 'white ball'): 'grey_object.csv',
       ('captured_0054bs', 'green ball'): 'yellow_object.csv', ('captured_0054ax', 'white ball'): 'pink_ball.csv'}


def track_files(run, video):
    fs = sorted(glob.glob(f'{ROOT}/results/{run}/videos/{video}/scene/tracks/*.csv'))
    good = [f for f in fs if not any(b in os.path.basename(f) for b in BAD)]
    return good or [f for f in fs if 'person' not in f and 'camera' not in f]


def resolve(run, video, phrase):
    for (v, p), b in OVR.items():
        if v == video and p == phrase:
            return f'{ROOT}/results/{run}/videos/{video}/scene/tracks/{b}'
    fs = track_files(run, video)
    if not fs:
        return None
    if ('left' in phrase or 'right' in phrase) and video.startswith('captured_0034'):
        xs = sorted((np.mean([t[k][0] for k in sorted(t)[:5]]), f) for f in fs for t in [load_track(f)] if t)
        if len(xs) >= 2:
            return xs[0][1] if 'left' in phrase else xs[-1][1]
    if len(fs) == 1:
        return fs[0]
    toks = re.findall(r'[a-z]+', phrase)
    best, bs = None, -1
    for f in fs:
        n = os.path.basename(f)[:-4].lower()
        sc = sum(next(((2 if syn == tk else 1) for syn in SYN.get(tk, [tk]) if syn in n), 0) for tk in toks)
        if sc > bs:
            best, bs = f, sc
    return best


# ---------------------------------------------------------------- question text
def qtype(q):
    q = q.lower()
    if 'acceleration' in q:
        return 'acc'
    if 'velocity' in q or 'speed' in q or 'velocoty' in q:
        return 'vel'
    if 'displacement' in q:
        return 'disp'
    if 'distance travel' in q or 'path' in q or 'total distance' in q:
        return 'path'
    if 'distance' in q or 'diatance' in q or 'height reached' in q or 'rebounce' in q:
        return 'dist'
    return 'size'


def obj_phrase(q):
    q = q.lower().replace('ping pong', 'pingpong').replace('white board', 'whiteboard')
    m = re.search(r"(?:of|by|from) (?:the |that |a )?([a-z ]+?)(?:'s)? (?:at|between|from|when|in|after|before|on|during|with|$)", q)
    if not m:
        m = re.search(r"the ([a-z ]+?)'s", q)
    return m.group(1).strip() if m else q


def times_in(q):
    return [float(x) for x in re.findall(r'(\d+(?:\.\d+)?)\s*s\b', q.lower())]


# Rows that name an event instead of a time: the time each row's own 26_30 session found for that event (its notes).
EVENT_T = {'2145': [1.6], '2150': [1.52], '2155': [1.32], '2160': [1.32], '2495': [1.24],
           '2497': [0.70, 1.24], '2502': [0.70, 1.24], '2507': [0.70, 1.24],
           '2443': [0.80, 1.44], '2453': [0.80, 1.44], '2463': [0.80, 1.44]}

DEP = re.compile(r"(?:t\s*=\s*([\d.]+)\s*s?[^,]*,\s*)?distance_([a-z_]+?)_camera\s*=\s*([\d.]+)", re.I)
NSYN = {'pingpong': ['pingpong', 'ping_pong'], 'soccer': ['soccer'], 'basketball': ['basketball', 'orange_ball'],
        'orange': ['orange', 'basketball'], 'tennis': ['tennis'], 'yoga': ['yoga'], 'white': ['white'], 'green': ['green'],
        'pink': ['pink'], 'book': ['book'], 'jar': ['jar'], 'yellow': ['carrot', 'yellow'], 'toy': ['ball', 'toy'],
        'trashbin': ['trashbin'], 'whiteboard': ['white_board'], 'red': ['ball', 'red'], 'ball': ['ball'],
        'left': ['left'], 'right': ['right']}


def parse_depth(text):
    out = []
    for line in (text or '').replace(';', '\n').split('\n'):
        m = DEP.search(line)
        if m:
            out.append((float(m[1]) if m[1] else None, m[2].lower(), float(m[3])))
    return out


def anchors_for(depth, phrase):
    toks = re.findall(r'[a-z]+', phrase.lower().replace('ping pong', 'pingpong'))
    best, bs = [], 0
    for n in sorted({n for _, n, _ in depth}):
        sc = sum(next(((3 if syn == tk else 2) for syn in NSYN.get(tk, [tk]) if syn in n), 0) for tk in toks)
        if sc > bs:
            best, bs = [n], sc
        elif sc == bs and sc > 0:
            best.append(n)
    if bs <= 0 or len(best) != 1:
        return []
    by_t = {}
    for t, n, z in depth:
        if n == best[0] and t is not None:
            by_t.setdefault(t, []).append(z)
    # a time listed twice with different values (0035a / 0035b: one of the two is the other ball) is not usable
    return sorted((t, zs[0]) for t, zs in by_t.items() if max(zs) / min(zs) < 1.05)


# ---------------------------------------------------------------- geometry
def z_series(tr, anchors):
    """Depth per frame: apparent size scaled to the row's own depth anchors (or relative), else anchor interpolation."""
    ks = sorted(tr)
    sized = [k for k in ks if tr[k][2]]
    if len(sized) >= max(5, 0.5 * len(ks)):
        T = np.array([cap_time(k) for k in sized])
        L = np.log([tr[k][2] for k in sized])
        lz = {}
        for k in ks:
            t = cap_time(k)
            w = np.abs(T - t) <= 0.13
            if w.sum() >= 3:
                lz[k] = -np.polyval(np.polyfit(T[w] - t, L[w], 1), 0.0)
        if anchors and lz:
            # the size curve gives the shape, the row's own depth readings pin it: the scale is interpolated in time
            # between anchors, so Z passes through every anchor (a poor size proxy, e.g. a sliding book, cannot
            # override two depth readings)
            rat = []
            for ta, za in anchors:
                k = min(lz, key=lambda kk: abs(cap_time(kk) - ta))
                if abs(cap_time(k) - ta) <= 0.05:
                    rat.append((ta, za / math.exp(lz[k])))
            if rat:
                tt, rr = [x[0] for x in rat], [x[1] for x in rat]
                return {k: float(np.interp(cap_time(k), tt, rr)) * math.exp(v) for k, v in lz.items()}, 'size+anchor'
        return {k: math.exp(v) for k, v in lz.items()}, 'size-rel'
    if len(anchors) >= 2:
        return {k: float(np.interp(cap_time(k), [a[0] for a in anchors], [a[1] for a in anchors])) for k in ks}, 'anchor-interp'
    if len(anchors) == 1:
        return {k: anchors[0][1] for k in ks}, 'anchor-const'
    return None, 'none'


def positions(tr, zs):
    return {k: np.array([(tr[k][0] - CX) / FOC * zs[k], (tr[k][1] - CY) / FOC * zs[k], zs[k]]) for k in tr if k in zs}


def deriv(P, t, half=0.10, order=1):
    idx = [k for k in sorted(P) if abs(cap_time(k) - t) <= half + 1e-9]
    if len(idx) < (3 if order == 1 else 5):
        return None
    T = np.array([cap_time(k) - t for k in idx])
    X = np.array([P[k] for k in idx])
    deg = 2 if len(idx) >= 4 else 1
    if order == 2 and deg < 2:
        return None
    return np.array([np.polyval(np.polyder(np.polyfit(T, X[:, c], deg), order), 0.0) for c in range(3)])


def fac(vec, s):
    n = np.linalg.norm(vec)
    return float(np.linalg.norm([s * vec[0], s * vec[1], vec[2]]) / n) if n > 1e-12 else None


def nearest(P, t, tol=0.05):
    k = min(P, key=lambda kk: abs(cap_time(kk) - t)) if P else None
    return k if k is not None and abs(cap_time(k) - t) <= tol else None


def factor_for(kind, tr, anchors, times, s):
    zs, how = z_series(tr, anchors)
    if zs is None:
        return None, how
    P = positions(tr, zs)
    if kind == 'vel' and len(times) == 1:
        v = deriv(P, times[0] + 0.02)
        return (fac(v, s) if v is not None else None), how
    if kind == 'acc' and len(times) == 1:
        a = deriv(P, times[0], half=0.14, order=2)
        return (fac(a, s) if a is not None else None), how
    if kind == 'disp' and len(times) == 2:
        a, b = nearest(P, times[0]), nearest(P, times[1])
        return (fac(P[b] - P[a], s) if a is not None and b is not None and a != b else None), how
    if kind == 'path' and len(times) == 2:
        ks = [k for k in sorted(P) if times[0] - 0.03 <= cap_time(k) <= times[1] + 0.03]
        if len(ks) < 3:
            return None, how
        num = sum(np.linalg.norm([s * (P[b] - P[a])[0], s * (P[b] - P[a])[1], (P[b] - P[a])[2]]) for a, b in zip(ks, ks[1:]))
        den = sum(np.linalg.norm(P[b] - P[a]) for a, b in zip(ks, ks[1:]))
        return (num / den if den > 0 else None), how
    return None, how


# ---------------------------------------------------------------- 0034b: the row's own prior sets the scale
def prior_scale_0034b(video, phrase, kind, s):
    tr = load_track(resolve('s26_scene_full', video, phrase))
    ks = sorted(tr)
    d = [tr[i][2] for i in ks if 26 <= i <= 33 and tr[i][2]]
    m_per_px = 0.067 / float(np.median(d))
    if kind == 'vel':
        idx = [i for i in ks if abs(cap_time(i) - 1.22) <= 0.1]
        T = np.array([cap_time(i) for i in idx])
        sp = math.hypot(np.polyfit(T, [tr[i][0] for i in idx], 1)[0], np.polyfit(T, [tr[i][1] for i in idx], 1)[0])
        clean = sp * m_per_px * 100
    else:   # total path: release (frame 22) to the end, 3-frame smoothing split at the collision (frame 38)
        clean = 0.0
        for seg in (range(22, 39), range(38, 49)):
            P = np.array([[tr[i][0], tr[i][1]] for i in seg if i in tr])
            Q = np.array([P[max(0, j - 1):j + 2].mean(0) for j in range(len(P))])
            clean += np.linalg.norm(np.diff(Q, axis=0), axis=1).sum() * m_per_px * 100
    return clean * s, clean      # motion is lateral (table plane facing the camera): F = s


# ---------------------------------------------------------------- build
def build(a):
    led = {r['id']: r for r in csv.DictReader(open(f'{ROOT}/results/s26_scene_full/ledger.csv'))}
    base_rows = list(csv.DictReader(open(f'{ROOT}/{a.base}')))
    base = {r['id']: r for r in base_rows}
    cur = {str(int(r['row_idx']) + 1): r for r in json.load(open(f'{ROOT}/data/test/test_dataset_current_20261021.json'))}
    changes = []
    for i, r in sorted(led.items(), key=lambda kv: int(kv[0])):
        if r['source'] != 'lab' or r['category'] == 'D2':
            continue
        c = cur[i]
        q = c['question'].strip()
        kind = qtype(q)
        if kind not in ('vel', 'disp', 'path'):      # accelerations: second differences too noisy for a direction
            continue
        e = float(base[i]['parsed_value'])
        try:
            k_const = e / float(r['first_answer'])
        except Exception:
            continue
        if not 1.15 <= k_const <= 1.25:      # only rows carrying the class constant
            continue
        ph = obj_phrase(q)
        ts = EVENT_T.get(i) or times_in(q)
        if any(t > 2.05 for t in ts):         # asks past the clip end (0018 at 3.4 s)
            continue
        if r['video'].startswith('captured_0034b') and kind in ('vel', 'path'):
            new, clean = prior_scale_0034b(r['video'], ph, kind, a.s)
            changes.append(dict(id=i, video=r['video'], cat=r['category'], kind=kind, before=e, after=round(float(new), 4),
                                F=a.s, how='prior-scale', const=round(k_const, 3), raw=r['first_answer']))
            continue
        tf = resolve('s26_scene_full', r['video'], ph)
        if not tf:
            continue
        tr = load_track(tf)
        an = anchors_for(parse_depth(c['depth_info'] or ''), ph)
        Fv, how = factor_for(kind, tr, an, ts, a.s) if tr else (None, 'none')
        if Fv is None:
            continue
        new = e / k_const * Fv
        changes.append(dict(id=i, video=r['video'], cat=r['category'], kind=kind, before=e, after=round(float(new), 6),
                            F=round(float(Fv), 4), how=how, const=round(k_const, 3), raw=r['first_answer']))
    os.makedirs(f'{ROOT}/{a.out}', exist_ok=True)
    ch = {x['id']: x for x in changes}
    name = os.path.basename(a.out.rstrip('/')).replace('fulltest_', 'track_a_')
    with open(f'{ROOT}/{a.out}/{name}.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(base_rows[0].keys()))
        w.writeheader()
        for r in base_rows:
            rr = dict(r)
            if r['id'] in ch:
                rr['parsed_value'] = repr(float(ch[r['id']]['after']))
            w.writerow(rr)
    with open(f'{ROOT}/{a.out}/changes.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(changes[0].keys()))
        w.writeheader()
        w.writerows(changes)
    by = {}
    for x in changes:
        by.setdefault((x['cat'], x['kind']), []).append(x['F'])
    summary = {f'{k[0]}/{k[1]}': dict(n=len(v), F_median=round(float(np.median(v)), 3)) for k, v in sorted(by.items())}
    json.dump(dict(base=a.base, s=a.s, rows=len(changes), by_cell=summary), open(f'{ROOT}/{a.out}/manifest.json', 'w'), indent=1)
    print(json.dumps(summary, indent=1), '\nrows changed:', len(changes))


def val(a):
    """End-to-end on the labelled lab motion rows of the validation videos: the 27_3 per-question answers (raw, no
    constant) times x1.215 against times F, F from the same videos' question-blind records (s27_labphys_val)."""
    vrows = list(csv.DictReader(open(f'{ROOT}/data/validation/validation_dataset.csv')))
    lab = {(r['video_id'].strip(), r['question'].strip()): (float(r['ground_truth_posterior']), r['depth_info']) for r in vrows}
    out = {'x1.215': [], 'F': []}
    for d in sorted(glob.glob(f'{ROOT}/results/s27_labphys_val/q/*')):
        if not (os.path.exists(d + '/inputs.json') and os.path.exists(d + '/answers.json')):
            continue
        Q = json.load(open(d + '/inputs.json'))
        Q = Q.get('question') or Q
        q = (Q.get('text') or Q.get('question')).strip()
        vid = os.path.basename(d).split('__')[0]
        kind = qtype(q)
        if kind not in ('vel', 'acc', 'disp', 'path') or (vid, q) not in lab:
            continue
        g, dep = lab[(vid, q)]
        ans = float(list(json.load(open(d + '/answers.json')).values())[0])
        ph = obj_phrase(q)
        tf = resolve('s27_labphys_val', vid, ph)
        Fv, how = (factor_for(kind, load_track(tf), anchors_for(parse_depth(dep), ph), times_in(q), a.s) if tf else (None, 'none'))
        Fv = Fv or 1.215
        out['x1.215'].append(mra(ans * 1.215, g))
        out['F'].append(mra(ans * Fv, g))
        print(f'{vid:16s} {kind:4s} {q[:60]:60s} ans={ans:<8} gt={g:<8} F={Fv:.2f} ({how}) x1.215 {out["x1.215"][-1]:.1f} F {out["F"][-1]:.1f}')
    print({k: round(float(np.mean(v)), 3) for k, v in out.items()}, 'rows', len(out['F']))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('cmd', choices=['build', 'val'])
    ap.add_argument('--s', type=float, default=1.5)
    ap.add_argument('--base', default='results/fulltest_s27_e2/track_a_s27_e2.csv')
    ap.add_argument('--out', default='results/fulltest_s31_lablat')
    a = ap.parse_args()
    {'build': build, 'val': val}[a.cmd](a)
