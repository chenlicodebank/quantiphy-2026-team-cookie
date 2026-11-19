# q_2785: length of the shoe (cm), captured_0052

The file and question are both 24 fps. The shoe is static (white sneaker, lower left of the image, frames 0-48).
Camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360).

## Pixel measurements (frame 24, t = 1.0 s)
- `zoom.py`: an 8x crop with a 5 px grid. The toe tip at sole level is at about (251, 680) px. The heel
  back at sole level is at about (317.5, 651) px. The toe-to-heel pixel distance is about 72.5 px (±2 px).
- `measure_shoe.py`: a white-pixel mask. It misses the grey sole/toe and gives 71-77 px depending on the
  threshold. The record's value of 71 px is in this range.
- `grabcut_shoe.py`: a GrabCut mask. Its Feret diameter is 90.6 px, but that runs from the toe bottom to the heel-collar
  top, so it includes the shoe's height and the shadow. It is not the length.

## Foreshortening: the shoe points away from the camera
The toe is lower in the image, so it is nearer than the heel. A single-depth conversion
(72.5 px x 2.231 / 763) gives 21.2 cm, which underestimates the length.

## Floor-plane route (`floor3d.py`)
I fitted a floor plane (normal plus camera height) to the 3D centres back-projected with the given depths, each at its
known height above the floor:
- yoga ball (R = 0.251 m from its apparent size at 2.612 m), at frames 19-31; its depth is scaled by apparent size
- basketball (R = 0.117 m)
- bin (half of its 0.42 m height)
- shoe centre (about 4.5 cm)

The fit gives a nearly level camera (tilt about 3-4 deg) at 0.71 m height. Residuals are a few cm. The shoe centre
depth it predicts is 2.252 m (2.231 m given), so the fit is consistent with the given depth.
Intersecting the toe and heel rays with the plane gives a toe depth of 2.24 m and a heel depth of 2.41 m. The length is
23.4-23.7 cm (sole points 0-1 cm above the floor). Moving each end point 1.5 px outward gives 24.4-24.7 cm.

## Checks (`variants.py`)
- Dropping the bin: 23.5-23.9 cm.
- Shoe-centre height 3 cm or 6 cm: 23.3-23.9 cm.
- Dropping the shoe and bin: 22.5 cm, but that plane predicts a shoe depth of 2.45 m against the given 2.23 m, so I
  rejected it.

## Answer
24.0 cm. This is the floor-plane 3D length, nudged up slightly because blur shrinks the endpoint extents.
Confidence is moderate (about ±6%). The main uncertainty is the endpoint pixel positions; the floor tilt matters less.
The plain lab method card, with no foreshortening correction, would give about 21 cm.
