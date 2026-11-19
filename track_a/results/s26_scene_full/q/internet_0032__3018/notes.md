# Q3018: average speed of the boat from 4.5 s to 7 s (prior: boat length = 3.5 m)

## Time base
The file runs at 29.85 fps and the question states 30 fps. The two rates give frames 134→209 or 135→210, and the
pixel speed is the same for both (1.607 px/frame). I used the file's rate, 29.85 fps.

## Camera
Static. The background shift is under 0.2 px (scene/tracks/camera_shift.csv).

## Motion
From scene/tracks/boat.csv, one point per frame (forward differences, frames 134-209). Script: `measure.py`.
- Hull-centre x: 1.607 px/frame. The motion is steady leftward with no reversals, so the mean of the per-frame
  speeds equals the net displacement divided by the time.
- Bow tip: 1.667 px/frame. Stern tip: 1.547 px/frame. Their mean is 1.607.
- Pixel speed: 1.607 × 29.85 = 47.96 px/s.
- Check: on zoomed frames 134 and 209 (frames/f45.png and frames/f70.png), the bow is at ~556 and ~431 and the stern
  at ~790 and ~676. These match the track. A separate mask of the hull rows only (520-539) gives the same stern and
  shifts the bow by a constant ~7 px, because those rows miss the thin bow tip.

## Scale
The boat's length, bow to stern, grows from 212 px at frame 0 to 232 px mid-clip, 236 px at frame 134 and
245 px at frame 209, because the boat comes closer to the camera.
- Scale from the frame-0 length (212 px): 0.792 m/s.
- Scale from the clip-median length (232 px): 0.724 m/s.
- Scale from the mean length over the interval (241 px): 0.697 m/s.

## Answer
0.725 m/s, using the median scale (3.5 / 232 m/px). It is within 4% of the interval-matched value and within 9% of
the frame-0 value.

## Confidence
Medium. The pixel speed is solid (±2%). The main uncertainty is which frame the annotators measured the length on
(±9%).
