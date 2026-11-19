# q1573: speed of the magnifying glass at t = 0.333 s

question_fps = file fps = 24, so t = 0.333 s is frame 8. The glass is in free fall during frames 0–11 and touches the desk at about frame 12 (t = 0.5 s).

## Method
- Prior: a = 9.8 m/s² before 0.5 s. That means v(t) = v0 + g·t, so the only unknown is v0.
- `fit.py` fits quadratics to the pixel y track (ref_y, mask_cy, bbox_y0) over frames 0–5 and 0–7. The apex/rest time it gives is t_rest ≈ −0.03 to −0.14 frames, so the glass is released from rest at frame 0 (v0 ≈ 0).
  - The first step (6 px) is about a/2 (≈5.4 px), which also points to a start from rest.
  - The pixel acceleration drops later in the fall because of perspective (depth rises from 4.24 m to 4.41 m and the view tilts), so only the early frames are used to find v0.
- Speed by the convention (one-frame backward difference at frame 8): |p8 − p7|·24 = g·(8² − 7²)/(2·24) = 9.8·7.5/24 = **3.06 m/s**.

## Second route (`check3d.py`)
- Pinhole back-projection with the given depths. f ≈ 2250 px (HFOV ≈ 51°), solved roughly from the fall between frames 0 and 12. The vertical position comes from intersecting each ray with the fall line.
- Reconstructed v0 = 0.01 m/s. Speed at frame 8 = 3.58 m/s, but with an acceleration of 11.4 m/s². That f is biased, because contact happens slightly before frame 12.
- The ratio v/a does not depend on scale. Rescaled to g = 9.8 it gives 3.58·9.8/11.4 = 3.07 m/s, which agrees with route 1.

## Confidence
High (about ±2%). The main uncertainty is a release time a fraction of a frame before t = 0 (0.1 frame → +0.04 m/s).
