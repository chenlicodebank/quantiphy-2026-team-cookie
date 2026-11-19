# q_1623: width of each glass window (simulation_0242)

The file rate and question_fps are both 24 fps. I used frame 0 and frame 24 (t = 0 and t = 1 s) for the depth_info.

## Camera geometry (geom.py, pitch.py, final.py)
- **Animals' motion.** All three animals move along the image x axis at a constant image y. The facade is parallel
  to the image x axis, so I modelled the motion as parallel to the camera X axis (constant camera Y and Z).
- **Focal length.**
  - Brown horse: depth 16.288 → 16.112 m plus its speed of 0.874 m/s (straight-line distance over 1 s, with a pixel
    rate of 5.94 px/frame) gives f ≈ 2582 px. The origin sits about 55 px behind the torso centroid (the hip/root).
  - Rabbit: its depth change alone, with the origin at the centroid, gives f ≈ 2560 px.
  - Joint least squares over all depths, the speed and the ground constraint: **f = 2587 px** (HFOV ≈ 41°).
- **Pitch and camera height.** The two horses (same size, so their origins are at the same height) give a pitch of
  about 38°. The joint fit with origins on the ground (hoof rows) gives **pitch 37.3°, camera height 9.72 m**,
  and the rabbit fits the same ground plane (residual < 0.01 m).
- **Pitch check from the window frames.** The vertical edges of the window frames, measured from column profiles,
  converge to a vanishing point at y ≈ 3710 px, so f/tanθ ≈ 3170 px. That gives about 39°, which agrees. The wall
  corners in the scene record suggested a smaller pitch, but those corners are blurred by depth of field, so I did
  not use them.
- **Wall distance.** The wall base (brick-to-grass transition, wallbase.py) is at row ≈ 378.5. Intersecting that
  row with the ground plane puts the wall at a horizontal distance of **D ≈ 14.55 m**, about 2.1 m behind the brown
  horse.

## Window width (winmeas.py, winprof.py)
- I measured the white frame's outer edges (half-maximum) on the mean of 5 frames.
  - Row ≈ 232: left 110.2 px, middle 110.3 px, right 111.3 px.
  - Row ≈ 160: about 112 px.
  - The glass alone (dark interior, or frame centreline to centreline) is about 106-108 px.
- The facade is parallel to the camera X axis, so width = px × D / (f·cosθ − (v − cy)·sinθ).
  - Outer frame: 0.712-0.724 m.
  - Glass only: about 0.69 m.
- **Sensitivity.**
  - Without the speed prior: 0.726 m.
  - Origin row 15 px above the hoof line: 0.70-0.71 m.
  - Wall base ±3 px: ±0.002 m.

## Answer
**0.72 m**, the window object's outer extent including the frame. The scene record listed 115-127 px per window;
that range included the dark reveal and the arch shading, so I re-measured it at about 110-112 px.

Confidence: moderate-good, about ±5 %. The main risks are whether the frame is counted and a recessed window depth.
