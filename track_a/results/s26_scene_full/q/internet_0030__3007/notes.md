# Q3007 — average acceleration of the boat, 0.5 s to 1.37 s

Prior: speedboat length = 3.2 m. 2D internet clip; one scale from the prior, following the annotators' convention.

## Time base
The file runs at 29.15 fps and question_fps is 30. I used 30 fps, so the interval is frames 15 to 41. A speed of about
15 px/frame works out to about 7.3 m/s (about 26 km/h), which is plausible at either rate. With 29.15 fps (frames 15
to 40) the pixel acceleration comes out about 10% smaller.

## Scale
Bow tip to stern (the rear edge of the orange object on the transom): 199 px at frame 15. It falls to 190 px by
frame 41 because the boat yaws slightly; the mean over the interval is 195 px. I used 198 px, which gives
0.01616 m/px.

## Motion (background-stabilised x; the camera pans about -0.75 px/frame)
- My own phase correlation of the background agrees with the record (-30.6 px against -30.7 px at frame 41).
- Route 1: the record's bow and stern template tracks (track.py, analyze.py, fit.py). A quadratic fit over frames
  15-41 gives -30.8 px/s² (bow) and -20.4 px/s² (stern).
- Route 2: my own templates of the whole boat body and of the cabin and canopy, each taken from frames 15, 28 and 40.
  Quadratic fits give between -11.7 and -33.6 px/s², with a mean of about -25.
- Velocity at the ends: about 14.9 px/frame around frame 16.5 and about 14.2 px/frame around frame 38.5. That is
  -0.70 px/frame over 22 frames, or about -28.6 px/s².
- Taken together: about -27 px/s² × 0.01616 m/px ≈ -0.44 m/s². The boat is slowing down slightly, so I report the
  magnitude, 0.44.

## Confidence
Low to moderate. The acceleration is small (Δv is about 5% of v), so tracking noise and the slight yaw (perspective)
matter. The spread between methods is about ±30%.
