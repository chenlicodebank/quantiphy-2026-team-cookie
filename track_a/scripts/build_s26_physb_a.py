#!/usr/bin/env python
"""26_52: the physical scale on self-filmed internet clips whose stated motion prior contradicts the scene.

Evidence before our read: the public VihanAggarwal repo read this on the board twice on its own Claude answers
(research/PROBES.md: PHYSB, 29 D2 rows on 0043 / 0051 / 0053 / 0054, D2 +.009; PHYSB2, 30 D2 rows, D2 +.006): on
these clips the reference answers sit on the scene's physical scale, not the scale the stated speed implies. Their
scale factors came from sibling clips (cross-question, out under the 2026-10-15 rule); ours do not.

Rule, per question, from the video, the question's own prior and world knowledge only: on an internet clip whose
prior is a non-gravity motion (a stated speed or acceleration), take a standard object visible in the clip whose real
size is known to about 5 pct (an adult person 1.65 m cap to soles; a basketball 24.3 cm; a table-tennis ball 4.0 cm)
and compute its size under the prior's scale (its pixel size x stated value / the prior object's pixel motion, all
from the question-blind 26_30 phase-1 scene record, results/s26_scene_full/videos/<clip>/scene/). When that size is
off by more than 15 pct, the clip is on the physical scale: every D2 answer on it (sizes, distances, speeds, all
linear in the spatial scale) is multiplied by k = standard size / size under the prior. Clips whose anchors read
within 15 pct (0049 1.77 m, 0050 1.66 m, 0052 1.58 m, 0056 1.65 m) and clips with no standard object (0028, 0045,
0068, 0069, 0070) are untouched. Fact rows are untouched.

Usage: python scripts/build_s26_physb_a.py --base <csv> --out <dir> --name <file>
"""
import argparse
import hashlib
import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

# clip: (anchor, standard size m, anchor pixel size, prior value SI, prior object's pixel speed px/s, note)
ANCHORS = {
    "internet_0051": ("person (cap to soles)", 1.65, 300.0, 2.07, 17.61 * 30,
                      "scene notes: rider alone ~300 px; cx_bg 1414.5 -> 551.5 over 49 frames, 17.61 px/frame"),
    "internet_0053": ("person (cap to soles)", 1.65, 305.0, 4.46, 18.00 * 30,
                      "scene notes: 315 px at f0, 304 at f40, shrinking; scooter_cx 487.2 -> 1927.0 over 80 frames"),
    "internet_0054": ("person (cap to soles)", 1.65, 286.0, 4.90, 16.6 * 30,
                      "scene notes: 279-292 px, mean 286; front axle stabilised -16.6 px/frame"),
    "internet_0055": ("person (cap to soles)", 1.65, 292.5, 1.95, 8.24 * 30,
                      "scene notes: legs-together bbox_h 272 / 283 / 303 / 312; bbox centre 1220 -> 610 over 74 frames"),
    "internet_0047": ("basketball diameter", 0.243, 225.0, 2.94, 78.0 * 30,
                      "scene notes: diameter 225 px (median f1-21); step median 78.0 px/frame"),
    "internet_0043": ("white ball (table-tennis) diameter", 0.040, 78.0, 0.3338, 45.5 * 30,
                      "egg.csv: 76-79 px both ways; ref_x f29 1257.4 -> f31 1166.3 at t = 1.0 s"),
}
THRESH = 0.15
# 26_54 (after #196 read the six clips above at D2 +.0182 with the time base): two clips whose standard objects are
# known only to about 10 pct, so the 15 pct gate cannot be met cleanly; read as their own probe, never folded unread.
WEAK = {
    "internet_0045": ("500 ml iced-tea PET bottle height", 0.215, 426.0, 1.073, 59.35 * 30.0133,
                      "static_objects.json: tea_bottle_yellow_cap 426 px tall; tracks/cylinder.csv cx_stab_px linear fit "
                      "frames 4-30, -59.35 px/frame at 30.0133 fps"),
    "internet_0069": ("coffee mug height (common mugs 9.5-11 cm)", 0.100, 569.5, 0.32, 1450.1,
                      "tracks/mug.csv: body height median 569.5 px (frames 62-79); leading edge (body_x_right - cam_dx) "
                      "quadratic over frames 60-69 (the prior's 2.00-2.30 s window): 1450.1 px/s^2"),
}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True)
    ap.add_argument("--famprior", default="results/fulltest_s24_famprior/famprior_rows.csv")
    ap.add_argument("--template", default="data/test/template_local.csv")
    ap.add_argument("--out", required=True)
    ap.add_argument("--name", required=True)
    ap.add_argument("--weak", action="store_true", help="also the two clips whose anchors are known only to ~10 pct (26_54)")
    ap.add_argument("--skip-ids", default="", help="comma-separated question ids whose own session already answered on a "
                    "physical scale (e.g. 3151 over the per-question answers: the prior's object is not in internet_0055, so "
                    "that session assumed a physically reasonable scale); they keep the base")
    a = ap.parse_args()

    t = pd.read_csv(ROOT / a.template)
    t["ct"] = t.inference_type.str[0] + t.video_type.str[1]
    base = pd.read_csv(ROOT / a.base)
    assert (base.id.values == t.id.values).all()
    fam = set(pd.read_csv(ROOT / a.famprior).id) | {int(x) for x in a.skip_ids.split(",") if x}
    vals = base.parsed_value.values.copy()
    clips, rows = {}, []
    for clip, (anchor, std, px, prior, pxs, note) in {**ANCHORS, **(WEAK if a.weak else {})}.items():
        size_prior = px * prior / pxs
        k = std / size_prior
        fire = abs(size_prior / std - 1) > THRESH
        clips[clip] = {"anchor": anchor, "standard_m": std, "size_under_prior_m": round(size_prior, 4),
                       "k": round(k, 4), "fires": fire, "note": note}
        if not fire:
            continue
        m = (t.video_id.eq(clip) & t.ct.eq("D2") & ~t.id.isin(fam)).values
        for i in m.nonzero()[0]:
            rows.append({"id": int(t.id[i]), "clip": clip, "k": round(k, 4), "old": vals[i], "new": vals[i] * k,
                         "question": t.question[i]})
            vals[i] = vals[i] * k
    out = base.copy()
    out["parsed_value"] = vals
    dest = ROOT / a.out
    dest.mkdir(parents=True, exist_ok=True)
    out.to_csv(dest / a.name, index=False)
    pd.DataFrame(rows).to_csv(dest / "physb_rows.csv", index=False)
    man = {"run": "26_54" if a.weak else "26_52", "base": a.base, "threshold": THRESH, "weak": a.weak, "skip_ids": a.skip_ids, "clips": clips, "rows_changed": len(rows),
           "sha256": {a.base: sha(ROOT / a.base), f"{a.out}/{a.name}": sha(dest / a.name)}}
    (dest / "manifest_physb.json").write_text(json.dumps(man, indent=1))
    print(json.dumps(man, indent=1))


if __name__ == "__main__":
    main()
