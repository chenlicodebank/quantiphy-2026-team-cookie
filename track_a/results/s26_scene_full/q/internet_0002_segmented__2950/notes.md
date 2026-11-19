# q2950 red car length (internet, segmented, top-down, static camera)
Scale (prior lane width 3.66 m): lane-line centre spacing of the red car's own lane (dash rows y~330 and y~437),
measured in code (measure.py) at x bands 200-300, 580-680, 960-1070: 106.2, 105.9, 108.8 px -> mean 107.0 px.
Car pixel length (x extent bumper to bumper, mask columns >=15 px): frames 0..33 give 190,188,181,179,183,183,184;
scene track median over full-view frames f0-f36 = 184 px (range 179-190). Car tilt ~2.5 deg, negligible.
Length = 184 * 3.66 / 107.0 = 6.29 m.
Check: using the mean of all lane spacings (105.6 px) gives 6.38 m; frame-wise range 179-190 px -> 6.1-6.5 m.
fps (24 vs 30) irrelevant for a size. Plausible for a full-size pickup. Confidence: moderate-high (~3%).
