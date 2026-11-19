# Q1171 – width of the rock (m)

Prior: eagle length = 0.8 m. depth_info: eagle at 175.31 m (t=1 s, frame 24) and 172.99 m (t=2 s, frame 48).
File fps = question_fps = 24. The camera is static and near nadir (3D aerial scene).

## Focal length (from the eagle)
- `bird_length.py`: bird mask extent along the flight direction (the body length; the wings lie across it), frames 1–44
  over the sand. Result: 16.5–17.7 px at the half-max threshold and about 17.5 px at the 0.3 threshold, so I use
  **17.2 px**. The maximum extent across the flight direction is about 40 px, i.e. a 1.86 m wingspan, which is a
  plausible eagle wingspan and confirms that "length" here means the body length.
- Bird depth over these frames is about 175.4 m (linear in time between the two given depths).
- f = 17.2 × 175.4 / 0.8 ≈ **3770 px** (horizontal FOV ≈ 16°).
- Sanity check: the bird moves 10.7 px per frame, which is 0.50 m per frame or about 12 m/s.

## Ground depth (the rock is on the ground, below the bird)
The eagle's cast shadow on the sand is used to find how far the ground is below the bird. With a nadir camera and the
sun as a directional light, the shadow's image positions and sizes across the sun direction scale by
s = D_bird / D_ground.
- `shadow_offset_fit.py`: fits the shadow-minus-bird offset as (s−1)(bird − c) + k(t)·sun_dir.
  Result: s = 0.95–0.97 ± 0.02, so D_g ≈ 182 m.
- `shadow_climb_fit.py`: the same model, but treats the 2.3 m/s depth decrease as the bird climbing.
  Result: height h0 ≈ 14 m, D_g ≈ 191–192 m, s ≈ 0.915, with a residual similar to the free fit.
- `shadow_ratio.py`: thresholded extents across the sun direction, shadow/bird. Result: 0.89 at the 0.5 threshold and
  0.93 at 0.3. Blur shrinks thin wingtips, so these are lower bounds.
- `shadow_moments.py`: second-moment regression. Result: s ≈ 0.77. This is biased because the darkness weights depend
  on chord lengths along the sun direction, so I did not use it.

I adopt D_ground ≈ 190 m. The rock's widest outline sits a few metres above the ground, so I use a depth of about
**187 m** for the rock outline.

## Rock pixel extents (frame 12, zoomed crops in `rock_crops.py` → `frames/rock_*.png`)
- The rock is not cut by the frame edge: its top is at y ≈ 10.5 and its bottom (base fringe) at y ≈ 451.
  **The y extent is ≈ 441 px.**
- Left edge x ≈ 388, right edge x ≈ 886, so the x extent is ≈ 498 px.
- The dark area beyond the right edge belongs to the rock's dark facets; the cast shadow is soft and is not included.
- I assume the world axes line up with the image axes. Then length = the x extent and width = the shorter horizontal
  extent = the y extent, 441 px. The record's PCA width (422 px) would give about 4 % less.

## Answer
width = 441 × 187 / 3770 ≈ **21.9 m**. The x extent gives a length of about 24.7 m.

## Second-route check and confidence
If the outline is taken at the bounds of the ground depth (182–192 m), the width is 21.3–22.4 m.
The main uncertainties are:
- the ground depth (±4 %);
- the bird's pixel length (±3 %);
- the camera yaw relative to the world axes (up to −4 %).

Confidence: moderate, about ±8 %.
