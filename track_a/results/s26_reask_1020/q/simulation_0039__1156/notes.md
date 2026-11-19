# q1156 – width (beam) of the boat, simulation_0039

Answer: **3.15 m** (beam, gunwale to gunwale across the hull).

## Time base
File: 25 fps, 75 frames; question_fps = 24. Frames 1, 26, 51 duplicate 0, 25, 50, so the file is a 72-frame
24 fps render with 3 duplicated frames. Boat image velocity from template matching (shifts.py, frames 2→68 =
64 render steps): (-193.4, -54.2) px/s, |v| = 200.9 px/s. The boat translates at constant velocity and does not rotate.

## Camera (geom.py)
- Prior: 4 m/s, so the boat moves 4 m in 1 s. Depths 177.2077 m (t=1) and 177.9993 m (t=2). Hull-centroid pixel
  at t=1 is (552, 1364); at t=2 it is that point + v. Solving |d2·ray2(f) − d1·ray1(f)| = 4 gives **f = 9074 px**
  (HFOV 9.7°). Moving the assumed origin pixel by ±60 px changes f by less than 0.1 %.
- Ground normal: assumed zero roll, with the 3D displacement lying in the ground plane. The camera axis is about 35.6°
  from vertical (54° depression).
  Zero roll checked: the mast leans toward the predicted nadir vanishing point (about 6 px over 150 px).
- Plausibility: eagle wingspan ≈ 90 px × 177/9074 ≈ 1.75 m (foreshortened), plausible. Person walking ≈ 1.3 m/s on
  the ground, plausible. The person's depth hardly changes (0.09 m/s) while the body walks toward the camera, so their
  origin is not on the body and was not used.

## Beam measurement (rectify.py, stbd_aft.py, beam.py)
- Image points were back-projected onto a plane parallel to the ground through the boat origin. Axes: a = along the
  motion/bow direction, b = across. Plane height changes the scale by less than 1 %.
- Port edge: the white cap → red hull boundary on the camera-near side, visible along the whole length.
- Starboard edge: the outer silhouette on the foredeck (no rails there). Aft, it is the top of the white cap band
  under the rails, found from colour profiles. The rail tops (about 0.9 m high) were deliberately excluded. Midships,
  the cabin hides the edge.
- Paired widths at the same station: 2.58 m at a = −1.33 (aft of cabin), 2.80 m at a = 2.56 (forward of cabin),
  narrowing to 1.70 m at the stern and 0.8 m near the bow.
- The midline (port+stbd)/2 drifts smoothly toward the bow because the sheer rises; this drift is the same for both
  edges and does not affect the width. Fitting a quadratic or cubic midline and taking 2 × max(port_b − midline) gives
  **3.156 to 3.161 m**, with the maximum at a ≈ 1.1 m (beside the cabin).
- Second route / repeat: the same pipeline on frames 10, 40 and 55 gives 3.159, 3.176 and 3.161 m. Fitting a
  polynomial directly to the paired widths gives 3.08 to 3.28 m.
- Boat length (bow tip a ≈ 5.1 to transom a ≈ −4.6) is ≈ 9.7 m, so L/B ≈ 3.1: a realistic fishing boat.

## Confidence
Moderate. The beam station is hidden by the cabin, so midline interpolation adds about ±4 %. If the world bounding box
is not aligned with the hull, the reference width could be larger; I assumed the boat runs along a world axis.
