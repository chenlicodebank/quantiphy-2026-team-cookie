# Q2350 – height of the yellow toy (cm)

The file rate and question_fps are both 24 fps. t = 0.60 s is frame 14.
The yellow toy is the object scene/ calls `yellow_fruit`, which the right/far person throws. It is the "carrot" in
depth_info: at t = 0.6 s it is just out of the far person's hand, at d = 2.63 m. The "jar" at 1.97 m is the white object
near the near person. The toy is a yellow body shaped like a mango or pear, with a green leafy cap at the stem end.
In frames 20-23 its outline is curved like a kidney, which motion blur alone cannot produce.
I take "height" to be the toy's long (stem-to-blossom) dimension, including the stem and cap.

Camera: f = 0.5959*1280 = 762.8 px, principal point (640, 360).

## Measurements (scripts in this folder)
- profile.py, frame 14 (d = 2.63 m given; Z = 2.476 m): the dark blossom and stem spots are 42.4 px apart.
  Along that axis the body is above half-maximum over about 37 px, and the olive stem/cap continues to about 44 px in
  total. 44 px x 2.63/762.8 = 15.2 cm (method card, distance); x Z = 14.3 cm. The axis may be foreshortened in this frame.
- traj.py: a fit of free flight (frames 12-24) with gravity 9.8 m/s^2, anchored at d(14) = 2.63, gives
  vz = -0.97 m/s with 6.6 mm rms residual. The depth is about 2.65 m at frame 13, 2.58 m at frame 16 and 2.40 m at
  frame 21. Extrapolated to frame 0 it gives Z 3.04 m (d about 3.17 m), consistent with the toy held at the far
  person's side (pelvis Z about 3.0).
- feret_all.py: maximum Feret length of the yellow+olive mask in every flight frame. I subtracted motion blur as
  0.3 x the frame displacement x the cosine to the motion direction; 0.3 comes from the elongation of the dark spots
  in frame 14.
  The size from distance d is 17.3-18.8 cm for frames 16, 17 and 20-22, and the size from Z is 15.8-17.3 cm.
  Frame 13 gives 13.7 cm (foreshortened); frames 15 and 23 give 20-22 cm (blur or a hand mixed into the mask).
- profile0.py, frames 0-1 (held, sharp): blossom tip to cap end is about 42 px. At d about 3.17 m that is 17.4 cm,
  or 16.8 cm with Z.

## Answer
The routes give 15 cm (frame 14 at the given depth, probably foreshortened) and 16-18 cm (the other flight frames
and the held frames 0-1). Answer: 16.5 cm.
Confidence is moderate, about ±10%. The main uncertainties are the blur correction, the toy's tumbling (foreshortening)
and whether the ruler "height" includes the leafy cap. Without the cap the body alone would be about 13-15 cm.
