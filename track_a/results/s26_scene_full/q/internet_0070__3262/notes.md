# q3262 - speedboat displacement 2.00 s to 3.00 s
Prior: speed at 1.00 s = 11 m/s. 2D internet clip, so one scale = 11 m/s / pixel speed at 1 s.
Frames: t*30 gives f30, f60 and f90 (29.97 and 30 fps differ by 0.1 %, which does not matter).
The camera pans right, so all positions are measured against the far bank (background-compensated).

Main route (scene/tracks/boat.csv, canopy_tm_x_bg column, sub-pixel canopy template):
- speed at f30: forward difference 15.70 px/frame; the mean over f26-34 is 15.80. I used 15.75 px/frame = 472.5 px/s.
- displacement f60 to f90: 438.9 px.

Second route (my own measure.py: hull and canopy template plus a median of 6 bank patches):
- f30 to f31: 15.67 px/frame; the local values from f24 to f36 range from 15.5 to 16.1.
- displacement f60 to f90: 438.0 px, compensated. The background shift was -21.1 px here and -21.6 px in the record.
- Without compensation (raw image): speed 15.24 px/frame and displacement 417 px. The ratio barely changes, giving 10.0 m.

Scale: 11 / 472.5 = 0.02328 m/px. Displacement = 438.4 px x 0.02328 = 10.21 m.
The bow track gives about 9.7 m, but it is noisier because of the template drift corrections.
Confidence: good, within about 3 %.
