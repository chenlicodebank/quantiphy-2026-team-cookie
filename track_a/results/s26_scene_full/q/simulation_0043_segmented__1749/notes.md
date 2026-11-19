# q1749 — height of the boat (prior: boat length = 10 m)

The file and the question both run at 24 fps, so t=1 s is frame 24 and t=2 s is frame 48. This is a 3D Blender render with the background removed.

## Camera model (geom.py, height.py)
- I used a pinhole camera with the principal point at the image centre (540, 540) and **assumed zero camera roll**.
- The boat's image position comes from a linear fit of the mask centroid over all 72 frames. It moves (-3.534, -1.024) px per frame.
- The two depths (173.7093 and 174.5515 m) back-project the two positions into 3D. The difference between them gives the boat's motion direction. The boat moves bow-first along its own axis: the image direction of the motion (16.2°) matches the cabin-roof edge and hull lines along the boat.
- **Focal length:** I chose f so that the bow tip (251, 883.5) and the stern tip (459, 959) at frame 24 are 10 m apart along the boat axis. This gives f = 3781 px (horizontal FOV about 16°).
  - With f = 3781, the camera looks down on the boat at about 61° (the angle of the line of sight below horizontal).
  - Image scale at the boat: about 21.5 px/m along the boat, 19.9 px/m across it, and 10.6 px/m vertically.
- **Checks of the tilt and roll** (these decide the vertical scale):
  - The wheelhouse's vertical aft corner leans with its top to the left. I measured a slope of 0.06 at frame 24, rising from 0.00 to 0.12 as the boat moves left. A zero-roll camera predicts 0.08; a roll of 2.5° would predict about 0.02.
  - Fitting the point where vertical lines converge (nadir.py) over all frames gives an optical-axis depression of about 55.6° and a roll of about 1.4° (sign convention not checked). This is consistent with the model, which puts the axis at about 55°.
  - Four crosswise hatch edges average about 67° in the image. The zero-roll prediction is 67.7°.
  - The proportions are realistic: wheelhouse wall about 2.2 m tall, mast about 5 m above the roof. A shallower camera at 45° would make the wheelhouse wall only about 1.5 m tall.
  - The mast itself leans about 6.7° the other way. I read this as an aft rake built into the model, so I did not use it.

## Height
- The top of the bounding box is the mast top at (337.5, 836.5) on frame 24. It lies on the boat's centreline, 4.5 m aft of the bow tip and 6.7 m above it.
- Going down from the mast top, I found where the near-side hull bottom meets the outline of the mask, at several stations along the boat and for half-widths of 0.6–1.3 m. The deck half-beam is about 1.3–1.4 m, measured from the near and far deck edges.
  - Frame 24: the mast top is 9.1–9.9 m above the lowest visible hull point at midship, and about 9.3 m at the stern stations.
  - Frame 48, as an independent second route: f = 3770, camera at 61.0°, giving 9.2–9.7 m.
- The keel is hidden behind the near side of the hull. I added an estimated 0.3–0.6 m of hull below the lowest visible point (bottom deadrise plus keel).
- **Height ≈ 9.3 + 0.4 ≈ 9.7 m** (range about 9.3–10.2 m).

## Confidence
- This is moderate. The vertical scale depends on the camera angle, which rests on the zero-roll assumption, backed by the wheelhouse-edge and hatch-edge checks.
- With f taken from the scene record's mask_length (3924 px), the result would be about 9.1 m.
- The hidden keel depth is an assumption.
