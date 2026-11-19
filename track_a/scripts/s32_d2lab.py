"""32_3 (session 315f5fc7, 2026-10-22, zero API): the 6 D2 lab velocity rows (captured_0015 / 0015s / 0015x, the toy at
0.6 s and 2.6 s; method_queue 56(c)) at the Series 31 direction factor for in-plane motion, s = 1.5, instead of E2's
class constant x1.19. The prior is gravity (a physical constant, not a clicked label), so each row's 26_30 answer is a
clean speed; a 2D lab clip moves in the image plane, so the direction model gives F = s exactly. A read of these rows in
an otherwise idle D2 seat tests s = 1.5 against a uniform 1.2 on motion that is lateral by construction.

    python scripts/s32_d2lab.py [--s 1.5]
"""
import argparse
import csv
import datetime
import json
import os

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IDS = ('2267', '2270', '2272', '2275', '2277', '2280')
TH = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95])   # the portal's MRA thresholds (evaluator.py C)


def mra(p, g):
    return float(np.mean(abs(p - g) / g < (1 - TH)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--s', type=float, default=1.5)
    ap.add_argument('--base', default='results/fulltest_s27_e2/track_a_s27_e2.csv')
    ap.add_argument('--out', default='results/fulltest_s32_d2lab')
    a = ap.parse_args()
    led = {r['id']: r for r in csv.DictReader(open(f'{ROOT}/results/s26_scene_full/ledger.csv'))}
    rows = list(csv.DictReader(open(f'{ROOT}/{a.base}')))
    ch = {}
    for r in rows:
        if r['id'] in IDS:
            raw = float(led[r['id']]['first_answer'])
            before = float(r['parsed_value'])
            assert abs(before / raw - 1.19) < 1e-3, (r['id'], before, raw)
            ch[r['id']] = dict(id=r['id'], video=r['video_id'], question=r['question'], raw=raw, before=before,
                               after=round(raw * a.s, 3))
    assert len(ch) == 6
    name = os.path.basename(a.out.rstrip('/')).replace('fulltest_', 'track_a_')
    os.makedirs(f'{ROOT}/{a.out}', exist_ok=True)
    with open(f'{ROOT}/{a.out}/{name}.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        for r in rows:
            rr = dict(r)
            if r['id'] in ch:
                rr['parsed_value'] = repr(ch[r['id']]['after'])
            w.writerow(rr)
    with open(f'{ROOT}/{a.out}/changes.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(next(iter(ch.values())).keys()))
        w.writeheader()
        w.writerows(ch.values())
    # prediction: labels = k x raw x lognormal(sigma) under each model; D2 has 1,160 rows on the board's denominator
    rng = np.random.default_rng(0)
    pred = {}
    for model, k in (('direction s=1.5', 1.5), ('uniform 1.2', 1.2), ('uniform 1.19', 1.19)):
        for sig in (0.15, 0.30):
            d = []
            for _ in range(4000):
                tot = 0.0
                for c in ch.values():
                    g = k * c['raw'] * np.exp(rng.normal(0, sig))
                    tot += mra(c['after'], g) - mra(c['before'], g)
                d.append(tot / 1160)
            pred[f'{model}, sigma {sig}'] = [round(float(np.percentile(d, 10)), 4), round(float(np.mean(d)), 4),
                                             round(float(np.percentile(d, 90)), 4)]
    json.dump(dict(written_utc=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), build=f'{a.out}/{name}.csv = E2 + 6 D2 lab velocity rows x{a.s} '
                   '(raw 26_30 answer) instead of x1.19', vs='E2 (D2 .8921 predicted)',
                   D2_delta_p10_mean_p90=pred,
                   scorer='portal (devkit evaluator.py C = 0.1..0.9, 0.95)',
                   reading='On the portal scorer six rows separate the models only weakly: D2 >= 0 leans to s = 1.5 for lateral '
                           'lab motion, D2 <= -.0006 to a uniform ~1.2 (run channel #144). S2 / S3 / D3 untouched.'),
              open(f'{ROOT}/{a.out}/prediction.json', 'w'), indent=1)
    for c in ch.values():
        print(c)
    print(json.dumps(pred, indent=1))


if __name__ == '__main__':
    main()
