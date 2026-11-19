# q949 - phoenix body length (m)

Prior: acceleration at 2.0 s (frame 48) = 2 m/s^2. 2D Blender render, 24 fps (file and question rates agree). No depth_info.

## Acceleration in pixels
- track_head.py: sub-pixel template matching of the head and body region (chroma image) from frame to frame -> x track (dx_head.npy).
- fit_acc.py: the speed rises in steps (~5 -> ~16 -> ~26 px/frame), in phase with the 25-frame flap cycle. The position fits
  x = x0 + v0 t + a t^2/2 + A sin(2 pi t/P + phi) with rms about 1 px (a pure quadratic leaves 7-12 px rms), giving P = 25.0 frames
  and a = 0.413-0.418 px/frame^2 in every window tried (1-71, 12-62, 5-55, 20-70). The template track and the beak track
  from scene/ agree.
  So the origin is uniformly accelerated, and the flap adds a fore-aft surge of 11-18 px. A round prior of 2 m/s^2 fits a constant.
- a = 0.4155 px/f^2 = 239.3 px/s^2  ->  scale = 2/239.3 = 0.008357 m/px.
- Alternative reading, not used: the local surge acceleration at frame 48 is about 1.2-1.4 px/f^2, which would give about 1.1-1.3 m.

## Body length in pixels
- From beak tip to the tip of the central tail spike, along the flight (x) direction.
  - The scene record gives a colour-mask median of 438 px (range 396-450), but that mask misses the faint grey spike tip.
  - A background-subtracted run (length.py) gives 430-457 px on clean frames.
  - At frame 48 a zoomed crop (frames/tail48.png) shows the beak at x = 1004 and the spike tip at about 1440, i.e. 436 px.
  - Used 440 px (about ±10 px).
- Length = 440 x 0.008357 = 3.68 m (range 3.59-3.76).

## Check
The beak track and the head-template track give the same acceleration to within 1%.
Confidence: moderate. The main risk is whether the reference treats the motion as uniform acceleration (used here) or uses the local surge.
