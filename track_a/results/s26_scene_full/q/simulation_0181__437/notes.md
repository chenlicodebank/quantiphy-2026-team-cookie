# q_437 — speed of the box at t = 1 s (m/s)

Prior: acceleration of the box after 0.75 s = 2.338 m/s^2. 2D video, fps = question_fps = 24, so t = 1 s is frame 24
and t = 0.75 s is frame 18. Answer = 2.338 x v_px(24) / a_px. Only the ratio of pixel speed to pixel acceleration
matters, so I don't need a separate pixel scale.

## Measurement
- The scene/ track (mask centroid) is too noisy for an acceleration: per-frame steps jump around by 2–3 px, and
  quadratic fits gave a_px between 1.09 and 1.26 px/frame^2 depending on the window.
- I re-tracked the box myself (track.py) with normalized cross-correlation and sub-pixel peaks. The templates were
  patches of the textured front face, taken from frames 16, 20 and 24. The box keeps a constant 28.6–29° tilt from
  frame 12 on, so it moves without rotating and any point on it moves like its origin. Match scores were 0.8–1.0 for
  frames 12–34; the template fails at frame 35 (occluded), which I excluded.
- fit2.py projects the track onto the slope direction (28.3°) and fits a quadratic (constant acceleration, rms
  residual about 0.1 px):
  - a_px = 1.064 px/frame^2 (window 18–34; 1.058–1.071 over windows 13–34, 14–30, 18–30, 20–34)
  - one-frame backward speed at frame 24 = 31.95 px/frame (raw difference |p24 − p23| = 31.83 px)
- Scale: 2.338 / (1.064 x 576) = 3.815e-3 m/px. Speed = 31.95 x 24 x 3.815e-3 = 2.925 m/s.

## Checks
- Three independent templates and six fit windows give 2.905–2.939 m/s, a spread of about ±0.6%.
- The raw per-frame speed differences average about 1.06 px/frame^2 from frame 15 to 34, which matches a constant
  acceleration starting near frame 15. Taking the raw speed at frame 24 instead of the fitted one would give
  2.914 m/s.

Confidence: high on the ratio (about 1%). The main assumption is that the reference's acceleration was measured on
the same planar track; perspective is slight.
