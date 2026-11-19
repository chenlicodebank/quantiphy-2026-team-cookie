# q_1859: acceleration of the astronaut at t = 0.5 s (m/s^2)

Prior: astronaut height = 2.2 m. The scene is 2D, with no depth_info. question_fps = file fps = 24, so t = 0.5 s is frame 12.
Acceleration at frame 12 = (speed(12) - speed(11)) x fps, where speed(i) = |p(i) - p(i-1)| x fps.

## Measurements (own scripts)
- `measure.py`: the astronaut mask (min RGB < 225 on the white background) and a soft-alpha weighted centroid for every frame, saved to `track_own.csv`. My centroids match the scene/ record's to within about 0.2 px.
- `analyze.py` / `analyze2.py`: local polynomial fits centred on frame 11.5. The accelerations are:
  - quadratic or cubic fits with half-widths of 5-14 frames: 0.183-0.202 px/frame^2, most of them 0.19-0.196;
  - global 4th/5th-order fits over frames 0-40: 0.190 and 0.186;
  - Savitzky-Golay filters: 0.19-0.198.
- `fit_bezier.py` (second route, a whole-clip model): a Blender-style Bezier ease between two keyframes. The fit gives keys at f -0.04 and f 78.56 and handles at 0.328 / 0.662, which is the default ease-in/out (essentially smoothstep). The RMS residual is 0.17 px over all 80 frames. This model gives speed(11) = 2.496 and speed(12) = 2.690 px/frame, so the **acceleration is 0.1942 px/frame^2** (peak speed 5.24 px/frame, which matches the observed plateau). It agrees with the local fits; I use 0.194 px/frame^2 = 111.8 px/s^2.
- Note: the scene/ record says the motion starts at f3. The fit shows it starts at about f0 with a smoothstep ease, and the early displacements are sub-pixel.

## Scale
- `height.py`: the vertical extent of the figure over frames 0-14, where it is nearly upright (tilt under about 5 deg). The integer extent is 90-93 px and the sub-pixel coverage gives 90.2-92.4, with a mean of **90.9 px**.
- SAM 3 check (`compare_masks.py`, `frames/cmp_f0.png`, `frames/cmp_f12.png`):
  - Frame 0 ("astronaut"): SAM's vertical extent is 90 px, the same as mine (90).
  - Frame 12 ("person" with a box prompt): SAM gives 93 px against my 90 px (3.3 pct). The zoomed overlay shows that SAM's outline is a 1-2 px halo outside the visible antialiased edge, while my threshold outline follows the edge. Mine is right.
  - SAM's frame-12 centroid (1295.7, 501.5) matches mine (1295.8, 501.3).
  - SAM's video track only starts at frame 13. Over frames 13-30 its centroids follow the same path.
- Scale = 2.2 / 90.9 = 0.02420 m/px.

## Answer
a = 111.8 px/s^2 x 0.02420 m/px = **2.70 m/s^2**.
- The spread of the local fits (0.186-0.202 px/frame^2) gives about +-4 pct.
- A height of 90-91 px gives 2.70-2.73.

Confidence: good (likely within about 5 pct).
