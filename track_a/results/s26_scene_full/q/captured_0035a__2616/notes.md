# q_2616 – diameter of the soccer ball (cm)

Lab video, 24 fps (file and question_fps agree), 1280x720, f = 0.5959*1280 = 762.75 px, principal point (640,360).
Prior: basketball diameter 23.2 cm. depth_info: t=0.6 s (frame 14) soccer 2.758 m, basketball 2.270 m;
t=1.6 s (frame 38) two values both labelled "soccer": 3.052 and 2.412 m.

## Which t=1.6 depth is the soccer ball
At frame 38 the soccer ball is higher in the image and smaller (43 px) than at frame 14 (~47 px), so it is farther:
3.052 m is the soccer ball (2.758*47.3/43 = 3.03, consistent). 2.412 m is the basketball (mislabelled): basketball
at frame 38 is 72-74 px -> 2.412*73/762.75 = 23.1 cm, reproducing the 23.2 cm prior (scale check).

## Measurement (scripts: rays.py, chord.py, profile.py, profile2.py, measure.py)
- rays.py: circle fit to sub-pixel rim points (outermost crossing of bg+45 grey level along 45 rays), upper half and
  sides only, to exclude the dark contact crease/shadow at the bottom. Frame 38: D = 43.0 px (rms 0.39 px);
  frames 33-46 give 41.6-44.3, ~43 around frame 38. Threshold bg+35 / bg+55 changes it by about ±0.7 px.
- Hand profile (profile.py) on frame 38, centre row: edges at 477.9 and 520.6 -> 42.7 px. Agrees.
- Main route: D = 3.052 m * 43.0 / 762.75 = 17.2 cm.

## Second route
Frame 14 is motion-blurred. At frames 24-25 the ball is sharp and at nearly the same image position as at frame 14
((552,405) vs (525,408)), so its depth is about the same 2.758 m. There D = 47.3 px -> 2.758*47.3/762.75 = 17.1 cm.
The extent across the motion at blurred frame 14 is ~45.5-47 px -> 16.5-17.0 cm. These agree.

## Basketball scale check
Half-saturation edges at frame 38: 72.5 px horizontal, 74 px vertical -> 22.8-23.4 cm at 2.412 m (prior 23.2).
The record's RANSAC 71.5 px -> 22.6 cm.

Answer: 17.2 cm. Confidence: good (±4%). Off-axis sphere stretch (~2%) is not corrected, matching the method card.
