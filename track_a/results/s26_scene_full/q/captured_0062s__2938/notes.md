# q_2938: height of the trash bin (cm)

The file and the question are both at 24 fps, and the bin does not move (centroid std < 0.5 px). I measured on the
mean of every 4th frame (`bin_crop.py`) and checked it at t = 1.4 s (frame 34). f = 0.5959*1280 = 763 px.
d_bin = 2.303 m.

## Pixel measurements (mask + column profiles, `bin_crop.py`)
- Mask bbox: x 289-378, y 110-209. That is 99-100 px tall, matching the scene record's 100 px.
- The view is oblique from above, so the top opening is visible. Its far rim edge is at y ~111, and the near rim
  edge (a light lip line in the column profiles) is at y ~133-136. So the top surface takes up ~25 px of the
  vertical extent.
- The front side runs from the near rim at y ~136 to the front bottom edge at y ~209, which is 73 px.
- The bin is about 89 px wide at the rim and ~70 px at the bottom, so it tapers by ~9.5 px per side.

## Geometry
- Viewing angle: the top rim is nearly level in the image and close to square, so its foreshortening gives
  sin(alpha) ~ 25/89, i.e. alpha ~ 16 deg below horizontal.
- I tried a floor plane through the other objects' back-projected centres to get a second estimate of alpha.
  It was inconsistent: depending on which 3 objects are used, alpha comes out between 3 and 34 deg, and the full
  4-object fit gives 26 deg.
- Correcting the side for the taper: H*cos(alpha) ~ 73 + 9.5*sin(alpha) ~ 76 px, so H ~ 79 px at alpha = 16
  (86 px at alpha = 26).
- Distance to the front face: 2.303 - (S/2)*cos(alpha) ~ 2.18 m, where S ~ 0.26 m is the rim width.
- Result: H = 79*2.18/763 = 22.6 cm at alpha = 16, or 24.5 cm at alpha = 26.
- The plain method-card reading (full 100 px vertical extent at the centre depth) gives 2.303*100/763 = 30.2 cm.
  That number includes the foreshortened top opening, so it overstates the physical height.

## Answer
23.5 cm, the middle of the 22.6-24.5 cm range from the two viewing angles. Check: the rim width comes out at
~25-27 cm, so the bin is a little narrower in height than in width, which matches how it looks.

Confidence: moderate. The main uncertainty is the viewing angle. If the reference used the naive full extent, it
would be ~30 cm.
