"""Series 37: a Track B file that takes each category from one of two audited builds (session 05e6b3c8, 2026-10-24).

Track A's #212 U1 read (run channel #226) found the lab direction model winning S3 (+.0030) and losing D3 (-.0047) on
Track A's answers, so the next Track B candidate may take S2 / D2 / S3 from the lat build and D3 from the const build.
Both inputs are s37_final_b.py builds on the same runs (each passed s37_audit.py); this copies every row of a category
from the build named for it and checks that the two builds agree outside the lab motion rows of the switched
categories (the only rows the lab model touches), then writes the file, a manifest and the per-row source.

    python scripts/s37_mix.py --lat results/fulltest_s37_b9lat --const results/fulltest_s37_b9const \
        --const-cats D3 --out results/fulltest_s37_b9mix
"""
import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import s37_eval as E  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lat", required=True)
    ap.add_argument("--const", required=True)
    ap.add_argument("--const-cats", default="D3", help="categories taken from the const build, comma-separated")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    out = ROOT / a.out
    if out.exists():
        raise SystemExit("use a new directory")
    ml = json.loads((ROOT / a.lat / "manifest.json").read_text())
    mc = json.loads((ROOT / a.const / "manifest.json").read_text())
    if ml["runs"] != mc["runs"] or ml.get("physcheck") != mc.get("physcheck"):
        raise SystemExit("the two builds read different runs")
    fl = pd.read_csv(ROOT / a.lat / ml["file"])
    fc = pd.read_csv(ROOT / a.const / mc["file"]).set_index("id")
    ds, _, _ = E.tables()
    cc = set(a.const_cats.split(","))
    take = fl.id.map(ds.cat).isin(cc).values
    mixed = fl.copy()
    mixed.loc[take, "parsed_value"] = fc.loc[fl.id[take], "parsed_value"].values
    chl = pd.read_csv(ROOT / a.lat / "changes.csv").set_index("id").reason
    lab_motion = {i for i, r in chl.items() if "_xF" in r or "_x1.25" in r or "_x1.5" in r}
    vl, vc = fl.set_index("id").parsed_value.astype(float), fc.parsed_value.astype(float)
    diff = [i for i in fl.id[take] if not np.isclose(vl[i], vc[i], rtol=1e-12) and i not in lab_motion]
    if diff:
        raise SystemExit(f"{len(diff)} rows of the switched categories differ outside the lab motion rows, e.g. {diff[:5]}")
    out.mkdir(parents=True)
    name = f"track_b_s37_{out.name.split('_')[-1]}.csv"
    mixed.to_csv(out / name, index=False)
    src = pd.DataFrame({"id": fl.id, "cat": fl.id.map(ds.cat), "from": np.where(take, a.const, a.lat)})
    src.to_csv(out / "row_source.csv", index=False)
    man = {"series": "37", "track": "B", "file": name, "lat_build": a.lat, "const_build": a.const,
           "const_cats": sorted(cc), "rows_from_const": int(take.sum()),
           "rows_differing_from_lat": int(sum(1 for i in fl.id[take] if not np.isclose(vl[i], vc[i], rtol=1e-12))),
           "note": "every row is a row of one of two audited s37_final_b.py builds on the same runs; the lab model per "
                   "category follows Track A's #212 U1 read (S3 +.0030 lat, D3 -.0047 lat) - a board-informed method choice, disclosed"}
    (out / "manifest.json").write_text(json.dumps(man, indent=1) + "\n")
    print(json.dumps(man, indent=1))


if __name__ == "__main__":
    main()
