# q_1466 — width of the red car (left wheel to right wheel), simulation_0301

The file and question both run at 24 fps. t=1 s is frame 24 and t=2 s is frame 48.
Prior: the forklift accelerates at 2 m/s². Depths: forklift 16.7953 / 19.0980 m and car 17.8278 / 23.1989 m at t = 1 / 2 s.

## Camera focal length (two routes agree on f ≈ 3390 px, HFOV ≈ 41°)
1. **Forklift kinematics** (calib.py, early.py, fit_track.py). Phase correlation on frames 0–14 shows motion
   s ∝ (i − 0.29)², so the start is τ ≈ 0.012 s. Frames 0 and 1 are identical.
   The forklift travels D = ½·2·((2−τ)² − (1−τ)²) = 2.976 m between t=1 and t=2.
   Back-projecting the forklift origin (amodal bbox centre) with the given depths reproduces D at f = 3396
   (f = 3330 if τ = 0, 3577 if τ = 1/24). If the origin were the bbox bottom, f would be 3655.
2. **Vanishing-point orthogonality** (vp.py, pairs.py). The car moves straight; its direction h comes from the
   two depth-anchored origins. The car's width direction w comes from two symmetric pairs at frame 24: the two
   mirror heads and the two outer tail lights. Requiring w ⊥ h gives f = 3380 (bbox-centre origin) or 3305
   (bottom origin). A Monte-Carlo test with ±1.5 px on the features gives 3400 ± 250.
   Only the bbox-centre origin agrees with route 1, so I used origin = bbox centre and f = 3390.
   The fitted ground normal gives a camera pitch of about 19° and roll of about 1.4°.

## Car width
- **Symmetric-pair triangulation** (pairs3.py). The pair's 3D separation is parallel to w, and its midpoint lies
  in the car's symmetry plane through the origin. f = 3390, with the f = 3300 / 3500 values in brackets:
  - outer tail lights: 1.56 m at f24, 1.53 m at f71
  - mirror-head centres: 1.88 m at f24, 1.85 m at f71
  - **mirror tip to tip: 2.13 m at f24 and 2.04 m at f71** (2.10–2.20 at f = 3300; 1.97–2.05 at f = 3500).
    Frame 71 views the car more from behind, so its mirror extent is less mixed with the mirror's length.
- **Body width from silhouette tangents** (tangents.py). Vertical planes through the camera touch the right-rear
  of the silhouette at 18 unoccluded frames (21–27, 52–61, 71). Viewing angles run from 55° down to 24°.
  A joint fit for rear overhang and half-width gives a rear overhang of 1.73 m and **body width 1.85 m**
  (assuming the origin sits on the symmetry plane). The rear grey panels are included, but the mirrors are not.
  The left/front tangent does not fit a box: the nose is rounded and hidden by the forklift. I did not use it.
- Sanity check: mirror span / body width = 1.10, the same as a real LaFerrari (about 2.2 / 1.99). Absolute
  sizes come out about 0.9–0.93 of a real LaFerrari, which is acceptable for a rendered scene.

## Answer
The reference is the world-axis-aligned bounding box of the car object, which most likely includes the wing
mirrors: about 2.04–2.13 m. Without mirrors, the body width is about 1.85 m.
**Answer: 2.03 m.** It is weighted toward the mirror-inclusive value from the better-conditioned frame-71 view,
with a slight hedge toward the body-only reading.
The focal length is uncertain by about ±4%, and the mirror-or-body choice adds up to about ±10%.
Confidence: moderate.
