# Q405 — speed of the astronaut at t = 2 s (m/s)

Prior: astronaut height = 2.2 m. No depth_info. 2D video, 1920x1080, file fps = question_fps = 24, so t = 2 s -> frame 48.
Speed = |p(48) - p(47)| x 24.

## Scale (prior object = the astronaut)
Upright pose at frame 0, vertical extent of the figure (measure.py, own threshold mask):
- gray > 25: 91 px (y 477-567); > 60: 89 px (y 478-566); > 120: 87 px. Edge glow -> take ~89-91.
- SAM 3 text mask, frame 0: vert_px 90, box y 477.5-566.7 (89.2 px), centroid (1295.2, 517.7) vs mine (1295.6, 518.5) -> agree within 1-2 %.
- Height used: 90 px -> 2.2 / 90 = 0.02444 m/px.
Body length stays ~91.5 px through the clip (scene record and SAM length_px 89-92 at frames 44-52) -> constant depth, a single scale holds.

## Pixel speed at frame 48
1. Own threshold-mask centroid (measure.py): raw step into frame 48 = 4.4-4.7 px (pose/mask jitter ~0.3-0.5 px);
   cubic fit of x,y over frames 40-56, derivative at 47.5: 4.96-4.99 px/frame; mean of steps 46-50: 4.98-5.01.
2. ECC (Euclidean) registration of the astronaut patch between consecutive frames (template.py), threshold-free:
   step into frame 48 = 4.978 px (shift +0.37, -4.96), smoothed 4.997; the series is smooth (5.05 at 47, 4.97 at 49) —
   ease-out after a ~5.25 px/frame plateau. Rotation ~0.45 deg/frame, negligible effect on the origin's displacement.
3. SAM 3 text masks frames 44-52 (sam_check_text.py): centroid steps noisy (3.3-5.9 px), cubic fit 4.81 px/frame,
   ~3.5 % below routes 1-2. Its masks vary frame to frame (vert_px 86-90), so its centroid jitter is ~1 px; the
   ECC route (sub-pixel, whole-patch) and my mask agree to <1 % and are taken as right. (Box-prompted SAM masks,
   sam_check.py, were bloated with black background — checked on frames/seg48_zoom.png — and were discarded.)
Adopted: 4.99 px/frame = 119.8 px/s.

## Answer
119.8 px/s x 0.02444 m/px = 2.93 m/s (range 2.89-2.96 for height 89-91 px).
Scene record (scene/) was consistent: same object, centroid steps ~4.7-5.3 around frame 48.
Confidence: high (~3 %), dominated by the pixel height of the figure (glow edges ±1 px).
