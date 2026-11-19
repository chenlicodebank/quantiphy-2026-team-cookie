# q 1530 – acceleration of the car at t = 0.5 s (m/s^2)

Prior: tyre diameter 0.764 m. depth_info: left front tyre at 11.38 m (t=0.5 s), B1 sign at 23.44 m.
fps = question_fps = 24, so t = 0.5 s is frame 12, and a(12) = (x12 - 2*x11 + x10) * 24^2 (backward differences).

## What moves at frame 12
- I tracked the front-wheel rim (this is the left front tyre named in depth_info) with subpixel half-level
  edges (`rimw.py`, `rimw.json`). From frame 10 on, the rim centre stays at y = 791.2 ± 0.1 px, so its depth
  is constant. Its width is 122.5–122.8 px at frames 11–13, against 123.0 px side-on, so the wheel faces
  sideways (yaw ≈ 0–1°). The x track over frames 10–27 fits a Blender Bezier ease
  (smoothstep 3s²−2s³, start frame −0.03, length 59.1 frames) with **0.06 px RMS residual**.
- So from frame 10 the car translates straight left with no rotation or depth change. The origin's
  acceleration therefore equals the wheel's. The turn out of the bay finishes before frame 10.
  - The nose silhouette drifts relative to the wheel at frames 10–13, and the sill-edge and warp tests
    hinted at some yaw. Both are lighting/silhouette-sensitive. A real yaw change of ~1°/frame would move
    the wheel's x by ~4 px and break the 0.06 px fit, so I rejected that reading.
- The scene record's `x_wheelmid` for frame 12 is a template-match extrapolation and was not used.
  Rim positions were re-measured here.

## Scale
- The vertical tyre extent is clipped by the floor (bottom radius ~92 px), so I used the horizontal radius
  at axle height (`tyrew.py`). Where the edge borders the body cleanly it measures 100.0–101.2 px: frames
  13–14 both sides 100.7–101.2; frames 20–22 left edge 100.0. So D = 200.5 ± 2 px, and the wheel-plane
  scale is 0.764/200.5 = 0.003810 m/px. The wheel and the car move by the same metres, so this scale
  applies directly.
- Check against depth_info: with D = 200.5 the focal length is f ≈ 2890 px (HFOV ≈ 37°) and the tyre
  depth Z ≈ 11.02 m. Camera height is 1.35 m (from wheel-centre height = tyre radius). That predicts the
  back-wall floor line, at the B1 sign's depth of 23.44 m, at y ≈ 705. Observed: 706–707. Consistent.

## Result (`accel.py`)
Speeds (px/frame) at frames 11, 12, 13: 60.2, 64.5, 68.4. Second differences fall smoothly and linearly
(4.33 at f12 down to ~1.0 at f27).
- direct x12 − 2x11 + x10 = 4.335 px/frame² → 9.51 m/s²
- linear fit of second differences over frames 13–27, extrapolated to 12 → 9.44 m/s²
- smoothstep model fitted to frames 10–27 → 9.55 m/s²

**Answer: 9.5 m/s².** Uncertainty: ±1–2 % from the tyre pixel diameter, < 1 % from the fit.
Confidence: fairly high. The main residual risk is the tyre diameter in pixels: the edges are partly
hidden by the arch and floor, and 2·r_bottom ≈ 184 px would give ~10.3 m/s². The 200 px value is
supported by two clean edges and by the B1-depth wall-line check.
