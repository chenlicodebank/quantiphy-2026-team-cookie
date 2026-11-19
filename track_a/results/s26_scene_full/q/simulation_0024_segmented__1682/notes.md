# q_1682 — width of the rock (m)

File fps is 25; question_fps is 24, and every frame↔time conversion uses 24 (t=1 s → frame 24, t=2 s → frame 48).

## Scale from the boat (prior 4 m/s plus depth_info)
- Boat image motion (scene track fits plus my own template match, `fit.py` and `tm.py`): −6.43 px/frame in x and −0.25 to −0.31 px/frame in y. Template scale shrinks by 1.9e-4 per frame.
- Speed per frame = 4/24 = 0.1667 m. Radial component (90.4360 − 90.1103)/24 = 0.0136 m/frame, so the tangential component is 0.1661 m/frame.
  f = 6.445 px / (0.1661/90.27) ≈ **3500 px** (hFOV ≈ 15.6°).
  Check: the template scale change (1.9e-4/frame) implies 0.0175 m/frame of camera-Z motion. The depth_info, after back-projecting the image offsets, gives 0.0162 m/frame. These agree.
- Camera tilt from the boat's upward image drift, assuming the boat moves horizontally: v_Y/v_Z gives θ ≈ 20–23° downward.
  The boat deck visibility suggests a slightly smaller angle, roughly 15–20°.

## Rock
- Static. Image extent is x 326–959 (truncated at the right edge by a few px) and y 24–313, so about 636 px wide and 290 px tall.
- No depth is given for the rock. I placed it on the same ground plane as the boat keel. The camera height (≈36–40 m) comes from the keel row and the tilt.
- I modelled the rock as an ellipsoid resting on that plane (`rock_model.py`) and solved for its centre depth: ≈115–122 m along the camera axis.
- Lateral (image-horizontal) extent: **≈21–22 m**, which is robust across tilt and aspect assumptions. A rock at the boat's depth (90 m) would instead give 16.4 m.
- Front-to-back extent depends on the unknown plan aspect r: r = 0.6 → 12.7 m, r = 0.7 → 15 m, r = 0.8 → 17.2 m, r = 1 → 22 m.

## Answer
The rock looks elongated along the image horizontal. "Width" means the shorter horizontal extent, which here is the front-to-back extent. I took r ≈ 0.75 and allowed for the world bounding box not being aligned with the camera, which pushes the shorter extent up.
Answer **16.8 m**.
- Under the other reading (width = image-horizontal / lateral extent), the value would be ≈ 21.5 m.
- Confidence: low. The rock's depth comes from a ground-plane assumption, and its front-to-back extent is not directly observable.
