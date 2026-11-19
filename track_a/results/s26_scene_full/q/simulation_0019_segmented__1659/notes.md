# q_1659: average walking speed of the person (m/s)

The file and the question both run at 33 fps. Prior: height 1.87 m. Depths to the pelvis: 6.84 m at t=0 (frame 0) and 6.49 m at t=1 (frame 33).

## Track
I used scene/tracks/man.csv (masks checked in the record). Linear fits of x against frame:
- pelvis x, frames 0-40: -5.588 px/frame
- head-top x, all visible frames: -5.575 px/frame
- head-top x, frames 78-96: -5.375 px/frame

Pixel speed stays nearly constant over the whole clip and so does the apparent height (median 261 px). He walks parallel to the image plane at a constant camera depth Zc. Pelvis y is about 646.5 px. Principal point is taken as the image centre (540, 540).

## Scale (fit.py)
With Zc constant, the slant distance is D = Zc*sqrt(1+r^2/f^2), where r is the pixel offset from the image centre. Setting the ratio D0/D1 = 6.84/6.49 with u0=877.7 and u1=693.3 (from the fit) gives:
- f = 884.6 px
- Zc = 6.350 m

## Checks
- The height this geometry predicts, f*1.87/Zc, is 260.5 px. The measured walking bbox height is 257-268 px, median 261. The two references (prior height and the two depths) agree to within 1%.
- Second route: back-project the pelvis at t=0 and t=1 using the given depths. The 3D displacement over 1 s is 1.324 m, so 1.324 m/s.
- Third route: whole-clip pixel slope * Zc / f = 1.322 m/s.

## Answer
The forward speed is about 1.323 m/s. The reference answer is the mean of the per-frame speeds of the pelvis. That adds a little for the pelvis's vertical bob and side-to-side sway, which I estimate at about +1-2%. Answer: 1.335 m/s.

Confidence: good, within about 4%.
