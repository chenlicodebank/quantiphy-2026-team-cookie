# q_1145 – average speed of the person (m/s)

Video 1080x1080, 24 fps (same as question_fps), 72 frames. Frames 0 and 1 are identical, so speed(1) = 0.

## Method
- Track: scene/tracks/person.csv (pelvis estimate ref_x/ref_y, mask centroid cx/cy, head/sole rows). I checked it on crops of
  frames 0 and 71 (frames/c0.png, c71.png): the person is on the sand strip, seen in profile, walking right.
- Linear fits (trend.py): ref_x 127.2 -> 202.6 px (1.062 px/frame), cx 127.3 -> 201.8; y drifts down about 6 px
  (soles 745 -> 751, head 705 -> 711). Height in px stays the same or shrinks slightly (41.45 -> 40.72) and the mask area shrinks a little,
  so the person does not come toward the camera. The given depths (139.1030 / 139.1044 m) also stay constant. So the motion is taken as
  in the image plane (across the view).
- Scale: the 1.75 m rest height against about 41.5 px head-to-sole (the walking height is about 41.1 px; the rest height is a bit taller)
  gives 0.0422 m/px (f ≈ 3300 px, hFOV ≈ 18.6°, plausible).
- Image displacement 0 -> 71 is about 75 px in x and 6 px in y, so about 75.3 px over 71 frame steps = 1.061 px/frame = 25.4 px/s.
- Average of the per-frame speeds (including the zero at frame 1) = 25.4 x 0.0422 ≈ 1.07 m/s.

## Check
- Using the measured walking height of 41.1 px gives 1.083 m/s, and using the pelvis-x slope alone (1.062 px/frame, 70 moving steps) gives about 1.08.
  The range is 1.06-1.09. This is a plausible walking speed.
- The eagle gives no independent size check (its real size is unknown).

Answer: 1.075 m/s. Confidence: moderate-high (about ±4%, mostly from pixel quantisation of the 41 px height).
