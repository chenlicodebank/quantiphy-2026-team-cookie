# q_1471 — length of the plane (simulation_0303)

Question: length of the plane (m). Prior: speed 22.16 m/s. Depths: 102.6664 m at t=1.0 s (frame 25) and
121.8263 m at t=2.0 s (frame 50). question_fps = 25; the file is 24 fps, so all times use the frame index with 25 fps.
Frame 1 duplicates frame 0, so frame 0 is placed at the frame-1 position.

## Geometry (geo.py)
- The plane flies straight at constant speed, so |p50 - p25| = 22.16 m. With the two depths this fixes the angle
  between the two viewing rays at 5.71 deg. Matching that angle to the image positions of the origin gives:
  - f = 3425 px using the bbox centre as the origin (HFOV 41 deg);
  - f = 3472 px using the mask centroid as the origin.
- Check: a straight line at 0.8864 m per frame, projected, matches the tracked image centre within about 2 px over
  all frames 2–71. Direction of motion in camera coordinates: d = (-0.48, -0.29, 0.83). The plane is mostly flying
  away from the camera, up and to the left.

## What the image shows
The view is from the rear and below; the frame-0 view is oblique (41 deg off the tail axis), and by frame 71 the
view is 24 deg off the axis. The wings with wingtip fins are symmetric about the canopy. The long horizontal image
extent (bbox_w, about 575 px at frame 25) is therefore the **wingspan**, not the length, which explains why
"bbox_w × depth / f" drifts from 17.2 to 18.0 m. Corrected for the span direction s (horizontal, perpendicular to d),
the span is about 19–20 m at the bbox and 17.5 m between the fin tips.

## Length measurement (fitpt.py, crops.py, tips.py)
- I modelled the plane as a rigid body heading along d, with body axes d (forward), s (right) and u (up). Each
  sharp feature's image track over frames 0–71 was fitted for its body coordinates (forward, right, up). The forward
  coordinate comes from how its image offset along the vanishing direction shrinks with sin(view angle) and depth.
- Features (tips found in code as silhouette extremes, checked visually on crop sheets frames/crops_*.png):

  | feature | forward (bbox-centre origin) | forward (centroid origin) | rms |
  |---|---|---|---|
  | front tip of left nacelle | +5.74 | +6.81 | 1.5 / 0.5 px |
  | nose gun/probe tip (manual) | +5.09 | +6.16 | 1.5 / 0.8 px |
  | tip of rear ventral fin (centre line) | -8.41 | -7.49 | 1.5 / 0.6 px |
  | wingtip fins | about -1.4 to +1.9 | | |

  - The wingtip fins come out symmetric at right = -8.1…-8.9 and +8.5…+9.0. This supports the assumed heading
    and orientation.
- Fore–aft extent from the nacelle front to the ventral fin tip:
  - 14.15 m with the bbox-centre origin;
  - 14.30 m with the centroid origin, which fits better.
- The origin choice cancels in the difference, and the camera pitch does not affect the forward coordinates.

## Second-route check
- The two origin and focal routes agree within 1 percent.
- The manual nose-probe track gives the same forward geometry: probe 5.1 m against nacelle 5.7 m.
- The span and trajectory fits are consistent with each other.

## Caveats
- A forward or aft point hidden behind the body in this rear view cannot be excluded. The answer may therefore
  slightly underestimate the true length.
- If the plane climbs (about 17 deg when the camera is level), a world-axis-aligned horizontal extent would be about
  13.7–14.9 m.
- If "length" were read as the longer horizontal extent, the wingspan would give about 17.5–20 m. The aircraft
  convention (nose to tail) is used instead.

Answer: 14.3 m. Confidence: moderate (about ±10 percent).
