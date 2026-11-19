# q1518 – width of the road under the HIMARS truck (simulation_0144)

The file and the question both run at 24 fps (35 frames). The camera is static. The road is the pale pink dirt track under the truck.
It curves toward the camera at the truck. To the right of the truck (x 1560-1880) it runs straight, and both edges are clean there.

## Scale and camera (prior: rocket 2.9 m; depths 43.064 m at t=0 and 41.127 m at t=0.5 / frame 12)
- `focal.py` fits a 3D rocket model. The rocket moves along its own axis; its nose at rest sits at the tube mouth
  (1285,708), possibly recessed by 0-7 px (`restfit.py` fits the rest position from nose frames 4-14). The fit uses the nose at f12,
  the nose and tail at f13/f14, the two given depths and the 2.9 m length.
  Motion-blur correction: the FWHM length (`blur.py`) is about 138-140 px against 145 px from the threshold mask, so about 3.5 px per end.
  Result: **f ≈ 2340 px (range 2300-2600)**, hfov ≈ 45°. Rocket axis in camera coordinates is about (-0.59,-0.62,-0.52), and the
  rest origin is at P0 ≈ (6.6, 3.9, 42.4) m.
- Ground plane (`ground.py`): roll is taken as 0. Pitch and truck yaw come from truck line slopes found with Hough lines (`lines.py`):
  the deck edges and cab-roof side edge run lengthwise (slope -0.13); the cab-roof front edge and pod end edge run across (slope +0.125). Pitch ≈ -1.1° (slightly up), horizon at row ≈ 585.
  **Check:** the truck yaw from these slopes (40.7°) agrees with the horizontal heading of the rocket, measured independently from the
  depths (41-42°), to within about 1°. This confirms f and the pitch: the pod points along the truck.
- Camera height: the point on the ground below P0 is placed on the truck centreline, 1.1 m behind the near-side tyre contact line
  (results are insensitive to this: ±0.2 m gives ±0.3 % width). This gives h ≈ 7.26 m, with P0 about 4.1 m above the ground.

## Road edges and width (`edges2.py`, `width_profile.py`, `final_width.py`)
- Edges come from a road/sand colour score in Lab space, taking the 0.5 crossing in each column. Image thickness is about 36-40 px at
  x 1440-1520 and about 29 px at x 1560-1880.
- Both edges, back-projected onto the ground plane, give these widths (perpendicular distance between fitted edge lines):
  - f=2340: x 1560-1720 → 2.72 m; x 1560-1880 → 2.90 m; x 1700-1880 → 2.98 m.
  - f=2378: 2.68 / 2.86 / 2.94 m; f=2450: 2.61 / 2.79 / 2.86 m; f=2596 (no blur correction): 2.49 / 2.65 / 2.72 m.
- Next to the truck (x<1540) the flat model gives 3.4-3.9 m. This is an artefact of the bend: the near edge already curves there,
  and its matching far-edge points are hidden behind the truck. Both edges bend at x<1540, so this section is not used.
- In the far part the edges diverge by 1-2°, and the image thickness stays constant with distance. This suggests the terrain rises
  away from the camera, which makes far widths overestimates. The nearest straight section is therefore weighted more.

## Answer
Road width ≈ **2.8 m**, the mean of the near straight section (2.72) and the whole straight section (2.90) at f=2340.
Sanity check: the truck's width from the cab face comes out at about 2.2-2.6 m (a real HIMARS is 2.4 m), and the road is slightly
wider than the truck. Confidence: moderate, about ±10 % (focal length, terrain slope, soft road edges).
