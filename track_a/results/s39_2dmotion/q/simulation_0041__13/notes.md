# Q13 – speed of the boat at t = 1.0 s (m/s)

Prior: the person's height is 1.75 m. No depth_info. question_fps = file fps = 24, so t = 1.0 s is frame 24 (step 23→24).

**Answer: 4.8 m/s.** The model's best value is 4.87. The plausible range is 4.6–5.0, and I rounded down a little (see Confidence).

## Why a naive 2D scale does not work here
The clip is labelled 2D, but the camera is a tilted perspective camera looking down at the ground. The boat moves across the ground mostly along image x. The prior, the person's height, is vertical and is foreshortened. One metres-per-pixel factor taken from the person's pixel height would therefore be wrong by roughly 1/sin(tilt), about 40 pct. Evidence measured in code:
- **Mast lean** (`mast.py`): the bare mast's dx/dy changes steadily with its image x, from −0.014 at x = 491 to +0.041 at x = 154. So vertical lines converge to a vanishing point about 6070 px below the mast, which is about 6380 px below the image centre.
- **Boat shrinks as it moves up the image** (`boat_scale.py` affine x-scale, plus the boat track's bbox width and mask length): the horizon is 4870 / 6100 / 8700 px above the boat row (best 6100, from the bbox width, which has the smallest residual). The affine shear changes with x by about 1.5e-4 per px, which matches.
- **Pinhole solution** (principal point at the image centre): f² = d_vp · d_h and tan θ = √(d_vp/d_h), where d_vp and d_h are the distances from the image centre to the vertical vanishing point and to the horizon. This gives f ≈ 6045 px (horizontal FOV ≈ 10.2°) and a pitch of ≈ 46.5° from nadir. The vanishing point and the horizon sit almost symmetrically about the image centre, so the tilt is close to 45° unless the lens is shifted by several image heights. A tilt of 30° would need a FOV of 5.6°, which is outside the stated 8–100° range.

## Scale from the prior (`person_vert.py`, `speed.py`)
- **Person height:** the extent from head top to the lowest toe at mid-stance (frames 17, 34, 51 and 68, where the swing foot passes the stance foot) is 40.1, 38.7, 39.5 and 39.5 px, mean **39.45 px**. Edges are sub-pixel half-contrast.
- **SAM 3 check:** SAM "person" masks give rows 390–430, 416–456, 443–479 and 469–506 on the same frames. They agree with my edges within about 1 px (under 3 pct).
- **Correction to scene/:** the scene record's `head_top_y` is about 3 px too low because it misses the dark hair. SAM and my edges agree on this. At heel strike (frame 24) the extent is 49 px because the front foot reaches ahead.
- **Model of the person:** a 1.745 m standing head top (mid-stance) with a head radius of 0.10 m, whose silhouette top is used, and the toe 0.16 m ahead of the point under the head. Solving for the camera height gives 148 m. The horizontal scale is 27.6 px/m at the person and 30.3 px/m at the boat. The boat is lower in the image, so it is closer to the camera.

## Boat motion
- I used the template-track reference point (`scene/tracks/boat.csv` ref_x/ref_y; a rigid boat that does not rotate). Each frame's point is back-projected onto the plane z = 1 m (deck level).
- Speed in m/s:

| Measure | Speed (m/s) |
|---|---|
| Raw step 23→24 | 4.874 |
| Linear fit over frames 14–34 | 4.867 |
| Linear fit over frames 2–62 | 4.868 |
| Mean of per-frame steps | 4.867 |

- The pixel speed is constant at about 5.93 px/frame (per-frame jitter ±0.3 px).
- **SAM 3 check of the boat:** "fishing boat" masks on frames 14, 23, 24 and 34 cover the whole boat (overlay checked). The SAM centroid moves 5.894 px/frame over frames 14–34, against 5.937 for the track (0.7 pct). The single step 23→24 from SAM centroids is 6.79 px, but that is mask jitter on the rigging, so I used the track.

## Sensitivity and second route (`speed.py`)

| Change | Speed (m/s) |
|---|---|
| Horizon from affine x-scale (4870 px) | 5.00 |
| Horizon from mask length (8700 px) | 4.60 |
| Vanishing point at 5500 / 7300 px | 4.72 / 5.00 |
| Roll 0.9° (the mast's zero-lean x is about 437, not 540) | 4.89 |
| Toe offset 0.10 / 0.22 m | 4.73 / 5.01 |
| Person height ±1 px | 4.74–4.99 |
| Boat point height 0–2.5 m | 4.82–4.90 |

Second route: a per-frame calibration of the camera height gives 4.87. Holding the tilt at 40° (FOV 8.2°) gives 4.53.

## Confidence
Medium.
- **Main risk:** the model implies a 1.36 m step and a walking speed of 1.9 m/s for the person, which is long for a human. Tilts of 30–36°, which would give a normal gait, would mean 3.8–4.3 m/s, but they conflict with the measured perspective and the FOV range.
- **Naive alternative:** a single 2D scale from the person's pixel height (40–49 px) would give 5.3–6.2 m/s. I rejected it because the camera is clearly tilted.
- I answer 4.8, slightly below the 4.87 model value, to allow for the gait tension.
