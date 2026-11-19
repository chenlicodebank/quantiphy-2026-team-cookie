# q_1998: speed of the soccer ball at t = 1 s (m/s)

Prior: the ball's diameter is 0.344 m. This is a 2D scene, so I used a single metres-per-pixel scale. The file and the question both give 24 fps, so t = 1 s is frame 24, and the speed is the backward step from frame 23 to frame 24, multiplied by 24.

## Measurements (scripts in this folder)
- `measure.py`: tracks the ball in every frame using three thresholds (250, 245 and 240), recording the bbox midpoint
  and the darkness-weighted centroid, and saves the results to `track.npy`. Motion is horizontal, with y ≈ 556 px.
- `diam.py`: measures the diameter to subpixel precision from the half-level crossings of row and column profiles taken through the centre
  (frames 3–50). Median width is 49.3 px and median height is 47.8 px. Near frame 24 the values are about 47–49 px.
  Area-equivalent diameters near frame 24 are 49.3 at threshold 250 and 48.0 at threshold 245. I chose **D = 48.5 px (±1)**.
  Scale = 0.344 / 48.5 = 0.007093 m/px.
- `speed.py`: step from frame 23 to frame 24, using polynomial fits to x(frame):
  - quadratic, frames 3–49: 29.65 px/frame
  - cubic: 29.68
  - quadratic, frames 14–34: 29.67
  - the bbox-midpoint tracks give the same results (29.63–29.67)
  - raw single steps are 29.0–29.5
  - the mean step over frames 21–27 is 29.7–29.9

  I took **29.65 px/frame = 711.6 px/s**.

## Answer
711.6 × 0.007093 = **5.04 m/s**. The second route (bbox-midpoint track instead of the weighted centroid) agrees to within 0.1%.
The main uncertainty is the pixel diameter: ±1 px gives ±2%. Confidence: good (about ±3%).
