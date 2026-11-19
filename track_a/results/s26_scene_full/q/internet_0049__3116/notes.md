# q3116 — distance between middle brown table and gray table (m)

Internet video, 30 fps (file and question agree). Planar convention: one scale from the prior.

## Scale from the prior (rider average speed = 3.8 m/s)
`speed.py` uses scene/tracks/rider_scooter.csv (torso centroid, background-relative x_bg/y_bg, unflagged rows only):
- endpoint speed, frames 143→259: 941 px/s
- mean of the Savitzky-Golay-smoothed per-frame speeds: 940 px/s
- linear fit 143–255: 949 px/s (the rider speeds up from ~810 to ~1010 px/s)
- independent check: the scooter rear wheel goes from x=82 at f147 to x=2715 at f233 → 30.6 px/frame ≈ 920–930 px/s with camera drift
Used 940 px/s → 0.004043 m/px. Sanity check: scooter 264 px → 1.07 m and rider 420 px → 1.70 m, both plausible.

## Tables (frame 0, zoomed gridded crop, frames/tables.png)
- Gray metal table top: x 297–738 → centre 517.5
- Middle (front-centre) brown table top: x 1707–2406 → centre 2056.5
Both are in the front row (leg bottoms y≈1490–1495), so they are at about the same depth.
- Centre-to-centre: 1539 px → **6.22 m** (answer)
- The alternative reading, the edge-to-edge gap between the tops (738→1707 = 969 px), gives 3.92 m.

Confidence: moderate. The scale is good to about 2%; the main uncertainty is which distance definition the reference used.
