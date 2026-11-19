# q_1559 – length of the typewriter (simulation_0202)

Question fps = file fps = 24. 3D Blender render with a static camera. Principal point is taken as the image centre (1062, 540).

## Camera from the prior (fit_cam.py)
- I used the magnifying glass track from scene/ (bbox centre, frames 0-9, all before the impact at f11). The glass is
  placed at depth 4.2401 m at t=0 and falls from rest under g = 9.8 m/s² along the world-down direction. I fitted the
  focal length f, the camera pitch, the roll and the release time.
- Result: f = 2644 px, pitch = 14.0° down, roll ≈ 0, t0 ≈ 0. RMS error 0.23 px over 20 coordinates.
- Checks:
  - The model predicts the glass at depth 4.415 m at f11, on the desk. The given value is 4.4097 m at t=0.5 (f12).
  - Back-projecting the resting glass with depth 4.4097 gives a purely vertical drop of 1.06-1.07 m from the start
    point (horizontal residual 1 cm).
  - Desk plane: the given near-corner distance (3.593 m at pixel (700,885)) places the desk top 2 cm below the
    glass's resting origin, which is consistent.
  - The far-right desk corner comes out at about 4.93 m on that plane versus the given 5.009 m. The corner pixel is
    poorly defined in the dark.
  - The desk-top corner comes out at 91°.

## Typewriter (typewriter.py, tw2.py, linedir.py, frame 29)
- I located the base corners on 2.5-4x brightened crops and intersected them with the desk plane: front-left bottom
  (1004,752), front-right (1158,~707), rear-left (864,712).
- In its own axes the typewriter measures about 0.345 m left-right and about 0.31-0.32 m deep. The corners come out
  at 91-94°. The carriage knob adds at most about 1 cm.
- Rotation: the vanishing directions of three key rows, which are horizontal and left-right, show the typewriter
  turned 17.5-19° from the desk's front edge. The footprint corners give 16°, which agrees.
- World AABB, assuming the world axes follow the desk edges: 0.41-0.44 m along the desk's long axis (rear-left corner
  to front-right corner, with corner-pixel uncertainty) and about 0.40 m across it. The rectangle model gives
  0.35·cos17° + 0.32·sin17° = 0.43 m.

## Answer
- The reference convention is the world-space AABB, which gives about 0.43 m if the desk is axis-aligned. The
  typewriter's own left-right width is about 0.35 m.
- Whether the desk is aligned with the world axes cannot be verified: the wall/floor seam is blurred and
  inconclusive. I therefore answer 0.41 m, weighted toward the AABB reading.
- Readings: own-axis length about 0.35 m; AABB length about 0.43 m.
- Scale sanity: the magnifying glass comes out at about 0.29 m long, the typewriter at 0.35 x 0.32 m (a portable),
  the desk at 2.4 x 1.0 m (large). The scene appears to be at real scale.
- Confidence: medium. The geometry is solid (about 3%); the uncertainty is in the AABB convention and the world
  orientation.
