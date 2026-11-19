# q_1653 — height of the pedestal (square base) under the central sculpture

File fps 33 = question_fps 33, so the frame numbers in scene/ map directly to times.

## Camera (solve.py)
- Person pelvis track from scene/tracks/person.csv (pelvis_x_smooth, pelvis_y_est). Frame 0: u≈-1.5; frame 33: u=252; v≈543.
- Camera level, principal point (540,540), person at constant depth Z. From D0=5.424 and D1=4.886:
  D² = Z²(1+r²/f²) gives f ≈ 907 px and Z ≈ 4.657 m. Changing u0 by ±5 px gives f 894-920.
- Speed route: 1.3 m/s over the mean 252.3 px/s gives 0.005152 m/px at the person's depth. Combined with each given
  distance this gives Z = 4.651-4.667 and f = 903-906. Adopted f = 903, Z_person = 4.655 (HFOV ≈ 62°).
- Level-camera check: the bench floor plate is a rectangle on the floor (front edge y950 is 804 px wide, back edge y862
  is about 630 px wide). That puts the horizon at v ≈ 543, close to cy = 540.

## Camera height
- In frames 2-15 the planted sole is visible left of the bench at y = 731 (bbox_y1, checked on a zoomed crop).
- h_cam = (731-540) × 4.655/903 = 0.985 m.
- Sanity check: the pelvis is at v≈543, so its height is about 0.97 m, for a person 364 px = 1.88 m tall.

## Pedestal (ped_profile.py, final.py)
- The plinth has a light frustum top tier (y 548.5 to ≈600) on a dark square block (x 405-654, y 601 to below the bench top).
- The bottom is hidden by the bench: the 1-px white line at y≈696-698 is a segmentation seam, and the dark continues
  to y 701 at x=528. The predicted floor line at the front face is y≈710, consistent with being hidden.
- So height = camera height − drop of the top below the optical axis.
  - The top silhouette is at v = 548.5 at depth Z_c ≈ 5.94 (from the 5.963 m distance).
  - The drop is 8.5 × 5.94/903 = 0.055 m, and is insensitive to Z: 0.924-0.930 for Z 5.84-6.44.
- **Full pedestal (both tiers) H ≈ 0.929 m**: this is the answer.
- Alternative reading, dark square block only: top front edge at v≈601, front depth ≈5.22 m, giving about 0.63 m.
  I chose the full plinth because the asked object is "the pedestal", and "square base" describes the plinth as a whole.

## Confidence
- The main uncertainty is the camera height: about ±2%, because the planted foot may be nearer or farther than the
  pelvis by about 0.1 m. The camera-tilt check is good to a few px.
- There is also the which-part ambiguity above.
