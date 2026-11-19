# q_3087: height of the plate (cm)

- **Plate** = the white wavy dish/bowl on the left (static; x 156-580, y 544-727 in frame 44). It is the only plate-like object.
- **Prior** = velocity of the rolling cylinder, 107.3 cm/s. Following the internet convention, one planar scale comes from the prior.
- **Time base:** the file runs at 30.013 fps and question_fps is 30. The difference is negligible, so 30 fps is used.

## Cylinder pixel speed (look.py, scene/tracks/cylinder.csv, camera-stabilised centroid)
Fully visible frames are 4-30. The per-frame speed rises from about 1600 to 2100 px/s because the cylinder rolls toward the camera.
- Centroid, net path over frames 4-30: hypot(1585.7, 120) px / 26 frames x 30 = 1834 px/s
- Leading edge bbox_x0, frames 4-30: 1546 px / 26 x 30 = 1784 px/s
- Mean used: about 1810 px/s, so the scale is 107.3 / 1810 = 0.0593 cm/px.

## Plate pixel height (plate.py, frame 44, plus a 3x gridded crop by eye)
- The mask's bbox gives y 544-725, i.e. 182 px.
- By eye on the gridded crop: highest rim lobe at y 544, base at y 727, i.e. 183 px.
- Value used: 183 px.

## Answer
183 px x 0.0593 cm/px = **10.9 cm**.

Second check: with the two velocity routes separately, the height is 183 x 107.3/1834 = 10.7 cm and 183 x 107.3/1784 = 11.0 cm.
Sanity: the cylinder diameter is about 185 px, which gives about 11 cm (paper-towel-roll size). Plausible.
The plate sits further back than the cylinder, so its true height is probably larger. The answer still uses the planar single-scale convention.
**Confidence:** moderate. The main uncertainty is which frame window the annotators used for the velocity (about ±10%).
