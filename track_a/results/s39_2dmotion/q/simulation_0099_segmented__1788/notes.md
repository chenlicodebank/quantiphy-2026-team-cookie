# q1788 — average speed of the boat (m/s)

The prior is "boat length = 10 m". This is a 2D video at 24 fps; the file rate and question_fps are the same.

## Method (`measure_boat.py`, output in `boat_meas.csv`)
- I segmented the boat in code: in the upper image (y < 740), pixels with min RGB < 238 or saturation > 25, cleaned with a 3x3 opening. I took the horizontal extents in every frame.
- **Boat length:** 857 px (median over frames 0–47, range 855–860, while the whole boat is in frame).
  - Scale = 10 m / 857 px = 0.011669 m/px.
- **Motion:**
  - Frames 0 and 1 are identical.
  - From frame 1 to 72 the stern x is linear: +17.886 px/frame (max residual 1.6 px).
  - Over frames 1–47 the bow fit gives 17.869 and the mask-centroid fit gives 17.95.
- **Speed:** 17.886 × 24 × 0.011669 = **5.01 m/s**. It is constant from frame 2 onward.
  - If the zero backward-difference speed at frame 1 is averaged in (72 per-frame speeds), the mean is 4.94 m/s. That is 1.4 % lower.
  - I answer 5.0, the uniform motion speed.

## SAM 3 check
- I segmented "boat" on frames 10 and 40. The mask covers the hull, wheelhouse and mast (overlay checked).
- **Length:** SAM horiz_px is 854 / 855 against my 857, a 0.3 % difference. SAM trims the thin bow tip and rudder pixels slightly. Both values are well within 3 %.
- **Speed (second route):** the SAM box centre goes from 821.05 at f10 to 1356.2 at f40, which is 17.84 px/frame. That is 0.3 % from my fit.
  - SAM-only route: 17.84 × 24 × 10 / 854.5 = 5.01 m/s.

The scene/ record (857 px, 17.886 px/frame) agrees with my measurements.

Confidence: high. The answer is about 5.0 m/s (±1 %).
