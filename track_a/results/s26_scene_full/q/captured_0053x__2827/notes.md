# q_2827: height of the trashbin (cm)

The file rate and question_fps are both 24 fps. The trashbin is the object the scene record calls "blue_box": a soft
blue patterned bin with a white tab underneath. It lies on its side and slides away from the camera, up and to the
left in the image, with no rolling. I read its height as the length along its axis, which is the long axis in the
image. The scene/ track does cover the right object, but I re-measured the masks myself (measure.py, written to
meas.txt).

## Scale
f = 0.5959 x 1280 = 763 px. At t = 0.4 s (frame 10) the distance is 2.73 m, so Z is about 2.65 m (ray factor 1.03).

## Measurements (frame 10)
- Mask PCA axis at 17-19 deg. Extent along the axis is 114.3 px and across it is 92.1 px. The across extent is the
  diameter D: 92.1 x 2.65 / 763 = 0.32 m.
- The along-axis extent 114.3 px gives 0.40 m (the raw method-card value). This includes the end face bulge,
  rounded ends and motion blur along the axis, since the bin moves about 11 px per frame along that axis.
- The straight side edges (silhouette lines along the axis) measured on the 5x zoom: about 100 px on top and about
  104 px at the bottom, so about 0.35 m. Removing about 4 px of blur gives about 0.34 m.

## Second route (recon.py)
I built a 3D track: distance at each frame from the across-axis width (or from sqrt(area)), fixed to 2.73 m at
frame 10. Its speed at frame 10 is about 1.04-1.10 m/s, against the prior's 0.996 m/s (within about 6-10%).
I took the floor plane from the motion direction, then corrected the axis for foreshortening:
L = (Lapp - D sin(phi)) / cos(phi).
- Frames 8-12 give 0.36 m.
- The median over all frames is 0.32 m.
- Late frames read by eye (the top and bottom edges at frame 30) give about 0.34-0.37 m once foreshortening is
  corrected.

## Answer
About 34.5 cm, the middle of the 32-37 cm spread.

Other reading: if the bin were standing upright, the height would be the across-axis extent, about 32 cm.

Confidence is moderate (about ±8%). The camera tilt worked out from the motion (about 41 deg down) disagrees with
how the cup looks (about 15-20 deg down), so the foreshortening correction is uncertain.
