# Q1560 – width of the typewriter (simulation_0202)

File fps = question fps = 24. 3D Blender render, static camera.

## Camera (fitcam.py, check.py, check2.py)
- Pinhole camera, principal point at image centre (1062,540). Unknowns f, pitch, roll and initial speed were fitted to the
  falling glass's bbox-centre track, frames 0-10 (free fall before the impact at about frame 10.5), with g = 9.8 m/s²
  and p(0) = 4.2401 m along the frame-0 ray.
  Result: f = 2643 px (HFOV ≈ 44°), pitch 14.0° down, roll ≈ 0, v0 ≈ 0.02 m/s; rms 0.37 px.
- Checks: (1) the glass on the desk at t = 0.5 s (frame 12) comes out at 4.414–4.420 m from the camera; the given
  value is 4.4097 m (0.2 % off). (2) The near desk corner (700,877) at the given 3.593 m lies 1.289 m below the camera,
  the same height as the desk top under the resting glass (1.283 m to the glass centre). (3) The gun at 4.704 m lies at
  1.25–1.27 m, just above the desk top. (4) Everyday objects come out at real size: revolver ≈ 0.27 m,
  magnifying glass ≈ 0.30 m long.
  The far-right corner (2000,656) comes out 5 cm lower. That pixel is probably on the lower edge of the desk-top slab.
- Desk-top plane: 1.293 m below the camera along the world vertical.

## Typewriter (foot.py, model.py, aabb.py)
- I read three corners of the base where it meets the desk on brightened, zoomed crops of frame 29:
  front-left tray corner B (1000,757), front-right tray corner C (1158,705), back-left bottom corner A (864,712).
  I back-projected them onto the desk plane.
- Front edge BC = 0.363 m (side to side across the keyboard). Left side AB = 0.318 m (front to back).
  The angle between them is 88.4°, which supports reading them as the corners of a rectangle.
- The right body edge and the carriage knob fall inside this footprint. The carriage does not overhang noticeably.
- Room direction: the desk front edge (26.4°) is parallel to the floor/wall line (25–27°). The typewriter is turned
  about 17–20° relative to the desk and room.

## Readings of "width"
- Shorter horizontal extent in the typewriter's own axes (front to back): 0.32 m (range 0.30–0.34).
- Side-to-side width across the keyboard: 0.363 m.
- World axis-aligned bounding box, if the world axes follow the room/desk: 0.43 m along the desk and 0.41 m across it,
  so the shorter extent is 0.41 m (range 0.38–0.46). Parts sticking out, such as the levers, would make it larger.
- The world axes can't be determined from the video, so I don't know whether the reference's bounding box is rotated.
  I answer 0.37 m, between the readings: within 3 % of the 0.363 m side-to-side width, about 10 % from the 0.41 m
  rotated-box value and about 14 % from the 0.32 m front-to-back depth.

## Confidence
The camera and scale are solid (several cross-checks agree to within 1 %). The footprint is good to about ±5 %.
The main uncertainty is which definition of "width" the reference used. Taken together I expect the answer to be
within about 15 %.
