# q_1677 – height of the boat (m)

Prior: boat speed 4 m/s. depth_info: 90.1103 m at t=1 s (frame 24), 90.4360 m at t=2 s (frame 48); question_fps 24 (file is 25 fps, frames indexed by frame number).

Method (scale.py):
- Linear fits of boat pixel position in scene/tracks/boat.csv (frames 3–74): x slope -6.43 px/frame, y slope -0.29..-0.31 px/frame (bbox centre, hull/keel and centroid agree).
- Back-projected the positions at frames 24 and 48 with principal point (480,480) and the given depths, then solved for the focal length that gives 4 m/s (24 fps): f = 3497 px (bbox), 3496 (hull), 3503 (centroid); hfov ≈ 15.6°. The depth change (0.33 m/s) is a small part of the speed, so f is robust.
- Boat height in pixels = bbox height (mast tip to keel): 362–364 px around frames 24–48 (median 363; frames <30 can be cut by ~3 px where the mast tip meets the rock).
- H_img = 363 × 90.3 / 3497 = 9.37 m.
- The camera looks slightly down (deck and roof tops visible; estimated elevation ~10°), so the projected vertical extent is ≈ H·cosθ; correcting gives ≈ 9.5 m.

Check: hull length 396→387 px gives ~10.2 m long, height/length ≈ 0.92, plausible for a small fishing boat with a tall mast. Three tracking points give the same f within 0.2%.

Answer: 9.5 m (range 9.4–9.6 depending on the pitch correction). Confidence: moderate-high.
