# Q1105: eagle wingspan (m). Answer: 2.55 m

File is 25 fps; question_fps = 24, so frame = round(t*24): t=1 s is frame 24 and t=2 s is frame 48 (I used the frame numbers from the record).

## Focal length from the prior (solve.py)
- The bird centroid comes from scene/tracks/bird.csv, with a local quadratic fit over the clean frames (excluding frames hidden by the mast, frames where the wings are edge-on, and frames at the image edge).
  It is (470,372.5) at frame 24 and (741,370.4) at frame 48.
- Points are back-projected with the given depths: 116.05 m at frame 24 and 108.28 m at frame 48.
- I solved for the f that makes |P48-P24| = 24 frames x 11.84/24 m = 11.84 m. This gives **f = 3395 px** (hfov 16.1 deg). It is stable within ±0.3 % across fit windows.
- A straight constant-velocity 3D line reproduces the pixel x-track of frames 16-62 with an rms error of 2.5 px.
  The y residual (rms about 9 px) is the centroid bobbing as the wings flap.
- Velocity per frame in camera coordinates is (0.360, 0.008, -0.337) m. So the eagle flies right **and toward the camera**, about 43 deg out of the image plane.
  The depths alone require this: the distance drops 7.77 m in 1 s, out of 11.84 m of travel.
  The appearance agrees: in the wings-up frames 24 and 48 the bird is seen nearly end-on.

## Wingspan (seg.py, span.py)
- Masks come from differencing each frame against the median of frames i±8 and i±12, at thresholds 15, 25 and 40. I checked them on overlays (frames/seg_tiles.png).
- Wings are fully spread and level at frames 42, 60 and 61, with mask widths of 50-54 px. Partly spread frames are 34 and 18.
- The wing axis was modelled as horizontal and perpendicular to the flight direction, at (0.683, 0, 0.730) in camera coordinates. The tips are at P ± S/2·w, using the exact pinhole projection; I solved for S.
  - frame 42: 2.47-2.52 m
  - frame 60: 2.52-2.57 m
  - frame 61: 2.68-2.73 m
  - frame 18: 2.44 m
  - frame 34: 2.25-2.30 m (wings not fully level)
- Answer: 2.55 m, the median of the frames where the wings are clearly fully spread.

## Second-route check and alternatives
- If the motion is treated as in the image plane (span = px x depth / f), the result is 1.60-1.65 m at every peak frame.
  That ignores the measured 43 deg obliquity of the flight, so I rejected it. It would be the answer only if the reference used the plain image-plane extent.
- The true span rises from about 2.3 m to 2.7 m from left to right. This suggests the heading or the flap phase is not perfectly modelled.
- The reference may be the world-axis-aligned bounding box. If the flight direction is not along a world axis, that would differ from the tip-to-tip span.
- Confidence: moderate, about ±10 %.
