# q 1851: speed of the rocket at t = 1 s (m/s)

The prior is the rocket's length, 2.9 m. This is a 2D video at 24 fps; question_fps is also 24, so t = 1 s is frame 24.
At frame 24 only the tail part of the rocket is in view: the nose left through the top edge at frame 22.

## Scale: rocket length in pixels
- `lencheck.py` measures the extent along the launch axis of the difference mask (|frame - frame 28|), frames 15-20:
  - threshold 25-40: 221.5-229.3 px, median about 226.
- SAM 3 mask at frame 18: length 227.6 px. My th40 mask at frame 18 is also 227.6 px, so the two agree.
- `profile.py` uses half-maximum crossings of an along-axis profile averaged over a core band 9 px wide:
  - 218.6-223.5 px.
  - This is biased short at the pointed nose, because the tip is narrower than the band.
- In a zoomed view (frames/f18nose.png, f18tail.png), the solid nose starts about 7 px behind a faint anti-aliased tip, and the tail ends at a light-blue nozzle.
- I used L = 225.5 px (±2.5), which gives a scale of 2.9 / 225.5 = 0.01286 m/px.
- SAM (227.6) differs from my 225.5 by about 1%, which is under the 3% check limit.

## Speed at frame 24 (backward difference p24 - p23)
- Steps of single frame ends are noisy, about ±3-4 px. The segmentation edges flicker; the measured nose-to-tail length changes 217-226 px from frame to frame. So I fitted smooth trajectories.
- Sub-pixel tail ends (`profile.py`), frames 15-25: the steps are 46.2, 50.1, 49.6, 55.1, 55.6, 60.2, 59.8, 60.0, 57.6, 62.6 px/frame.
  - The rocket accelerates early, then levels off near 60 px/frame.
- Mean tail velocity:
  - frames 22→25: 60.0 px/frame (centred at 23.5, which is exactly the backward-difference time).
  - frames 21→25: 60.0 px/frame.
- Joint polynomial fits (`fit3.py`: nose and tail share one trajectory, each with its own offset) give step 23→24 =
  - quadratic: 61.8-64.0
  - cubic: 60.3-61.4
  - The cubic fits are better (rms 1.0-1.9 vs 2.1-3.3).
- Second route: the SAM masks at frames 23 and 24 put the tail-corner step at 57.3 px (one-frame, noisy). My raw mask tail step is 56.8.
- Whole-rocket template matching (`tmatch.py`) was too noisy to use (rms 3.8), but it gives 57.5-61.4.
- Adopted step: 61 px/frame (range about 60-62).

## Answer
v = 61 px/frame × 24 frames/s × 0.01286 m/px = 18.8 m/s.
- Range from the uncertainties: about 18.3-19.5 m/s.
- Confidence: moderate-good, about ±4%.

## Corrections to scene/
- The record's L = 221.9 px comes from a core-band estimate. It is a little short: the full mask and SAM both give about 226-228.
- In the track, the frame-24 centre (tail + L/2) is fine for direction. Its single-frame step (57.4) is low because of edge noise.
