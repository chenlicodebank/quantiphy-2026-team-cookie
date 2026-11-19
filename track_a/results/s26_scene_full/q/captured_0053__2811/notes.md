# q_2811 – height of the trashbin (cm)

**Answer: 37.5 cm**

## Which object
The scene record calls the moving object a "blue toy car". It is actually the **blue decorated trashbin**, lying on
its side and sliding away from the camera toward the upper left. The decoration (white and yellow patches) does not
rotate between frames, so the bin is not rolling. The left end face is plain dark blue, which looks like the bin's
bottom. The long axis of the box (the bin's axis) is therefore its **height**. The cross-section is about 23-25 cm by
25-28 cm. File fps and question_fps are both 24, so t = 0.4 s is frame 10.

## Method
- Lab camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360). The given depth is 2.73 m to the bin centre at
  frame 10.
- Floor plane: fitted from the given depths of the book, cup, basketball and bin (geom.py). Result: pitch about 34
  degrees, camera height about 1.66 m, residuals 0-4 cm.
- Box fit (boxlib.py, fit_near10.py, fit_scaled.py): a 3D box resting on the floor (yaw, L, W, H) is projected
  through the pinhole model and fitted to the bin mask (same mask method as scene/scripts/track_car.py) by
  maximising IoU (about 0.89-0.91). The scale is set so the box centre at frame 10 is exactly 2.73 m from the camera.
  For neighbouring frames, the depth is scaled by the ratio of the bin's cross-axis pixel width.
- Results for frames 7-13 under three floor planes (pitch/roll 34/0, 38/2, 42/5): mean long axis L = 36.8, 36.9 and
  38.1 cm (sd about 1 cm). At frame 10 alone, L stays at 37-39 cm for any floor pitch from 26 to 46 degrees,
  because the given depth fixes the scale.
- Motion blur at frame 10 (about 12 px/frame of image motion, mostly along the bin's axis) probably inflates the mask
  by about 2 px. The rounded corners make an IoU-fitted box slightly too small. I assumed these two errors roughly
  cancel.

## Second route / consistency checks
- Joint rigid fit over frames 10-47 (jointfit.py): one box shared by all frames, the floor pitch and roll left free,
  scale from the frame-10 depth. Result: L = 41.0-41.4 cm, W about 24 cm, H about 25 cm, mean IoU 0.90.
- Single-frame fits at later frames give larger L (41-48 cm), and the fitted L/H ratio drifts from 1.33 to 1.9. A
  rigid object cannot do that, so the box model has a systematic problem at the far, grazing frames. Likely causes:
  sensitivity to pitch and yaw at shallow viewing angles, and the floor plane disagreeing with the bin's apparent
  shrinkage (the bin shrinks only about 1.3x where the plane predicts about 1.43x). Frames near t = 0.4 s have a
  steeper view and the given depth, and their result is robust to the plane, so the answer is based on them. The
  joint fit's 41 cm is an upper-side check.
- Sanity check of the scale: the basketball is 68 px wide at 2.925 m, which gives 26 cm (a real ball is about 24 cm).
  The cup is 27 px wide at 2.516 m, which gives 8.9 cm.
- The prior speed (0.996 m/s at 0.4 s) is consistent: the lateral image motion of about 11-12.6 px/frame at about
  2.67 m depth gives about 0.92-1.06 m/s.

## Other readings
- If the bin were standing upright instead, its height would be the vertical box extent, about 25-28 cm. I think this
  is unlikely: the "top" face carries the same decoration as the sides, and the end face is plain.

## Confidence
Moderate. The likely range is 36-41 cm. The main uncertainty is the box-model inconsistency across frames.
