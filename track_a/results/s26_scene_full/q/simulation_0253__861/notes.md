# q861 – acceleration of the box at t = 1.5 s (simulation_0253)

Prior: box width (side parallel to slope) = 0.611 m. depth_info: none. fps = question_fps = 24, so no re-timing.
t = 1.5 s is frame 36.

## Findings
- The camera sees the box's side face (rotated view `frames/rot_20_29.png`, made by `rotview.py`). The slope lies
  close to the image plane, but there is clear perspective: the ramp band narrows 49 -> 46 px from upper-left to
  lower-right (`band.py`), and the box shows its downhill end face early and its uphill end face late (`frames/crops.png`).
- The silhouette centroid in scene/ drifts as those end faces appear and disappear. Instead I tracked the light tape
  patch on the front face (template match with sub-pixel peak, `tape.py` -> `tape_track.csv`, overlay `frames/tape.png`).
- Duplicate frames: frame 27 shows the frame-28 position and frame 28 repeats it. I dropped frame 27 and kept 28 at t = 28/24.
- A plain quadratic gives a pixel acceleration that falls with time: 894 px/s² over frames 15–26 and 689 px/s² over
  29–44, with 2.3 px rms over the whole run. That drop comes from perspective, not from the physics.
- Model (`projfit.py`): q = S/(1+kS), S = S0 + V t + A t²/2, with q measured along the path from the frame-29 tape
  position (so S is in pixels at the frame-29 scale). Best k = 5.5e-5 /px. Fit over frames 15–44: A = 925 px/s², rms 0.23 px.
  Other windows: 15–32 gives 934, 26–44 gives 893, 20–40 gives 928.
  Check on k: the model's predicted across-slope scale ratio over the path is 0.93; the ramp band measures 46/49 = 0.94, so they agree.
  With k fixed at 5e-5 (from the band), A = 911.
- Scale (`facelen.py`): front-face length along the slope, from half-max crossings of b* in the rotated view. It is
  smallest (no end face visible) at frames 26–31: 91.6, 91.8, 92.4, 92.1 and 92.2 px, so L(frame 29) = 92.1 ± 0.5 px.
  This face lies in the same plane as the tracked tape point, so the scales are consistent.

## Answer
a = 925 px/s² × 0.611 m / 92.1 px = 6.14 m/s² (constant acceleration, so this is also the value at 1.5 s).
Range across windows and k choices: 6.04–6.22. Sanity check: the image incline is about 44°, and g·sin44° = 6.8, so
the result implies a friction coefficient of about 0.1, which is plausible.
Confidence: good (about ±3%).
