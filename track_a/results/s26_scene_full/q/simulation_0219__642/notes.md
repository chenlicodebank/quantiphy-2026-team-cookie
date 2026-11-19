# q642: height of the big robot (blue tracked drill robot), in metres

Prior: big robot speed = 5.924 m/s. Labelled 2D, so I used one m/px scale taken from the robot's own pixel speed. fps = question_fps = 24.

Measurements (measure.py, NCC templates cut from frame 12 and matched in frames 10, 20, 28 and 30):
- main body cylinder: 51.83 to 52.0 px/frame (record: 51.80). Vertical drift 0.
- drill arm (near side, in front): 54.2 to 54.5 px/frame. Wheels/tracks: 50.8 px/frame.
- The origin is the chassis centre, so I took the main-body speed, 51.85 px/frame = 1244 px/s.
- Height: handle top y = 271 and track bottom y = 894 to 895 at frames 12, 20 and 28 (checked on the gridded crop and the mask bottom). That is 623 px, constant over time.

Scale: 5.924 / 1244 = 0.004761 m/px. Height = 623 x 0.004761 = 2.97 m.
Second route: using the spread of part speeds (50.8 to 54.4 px/frame) gives 2.83 to 3.03 m. The near-side track
bottom may sit slightly lower in the image than it would at the origin's depth, so I shaded the answer down a little: about 2.96 m.
Confidence: moderate-high (about ±4%, set by which part stands in for the origin under perspective).
