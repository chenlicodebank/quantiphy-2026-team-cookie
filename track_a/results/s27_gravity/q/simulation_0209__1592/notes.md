# q_1592 – width of the typewriter (m)

The file and the question both run at 24 fps. This is a 3D Blender scene: a typewriter drops onto a desk, rocks and comes to rest from frame 24.

## Scale (camera)
- Fall fit (`fit_fall.py`, `scan_f.py`): a pinhole camera with pitch θ and roll 0. The origin starts at 4.32 m at t=0 and falls at g=9.8
  along world-down. Frames 2-9 are fitted (scene track: centroid and bbox centre). On its own the fit is ill-conditioned: f and θ trade off.
- Constraint 1: the t=0.5 s point (4.501 m, frame 12) must lie vertically below the t=0 point. Horizontal offset is smallest
  near f≈2450-2600.
- Constraint 2 (`desk_check.py`): the desk top must back-project to a rectangle. This needs θ≈13.6°, and the fall fit then
  gives f≈2400 (bbox-centre track) to 2600 (centroid track). The horizon implied by the desk vanishing points (~-45 to -90 px) agrees.
- Result: **f ≈ 2500 px (±4%), θ ≈ 13.6°**. The desk plane is h≈1.25 m along world-down from the camera, taken from the 4.501 m
  depth at the rest location. The result hardly depends on whether the origin is at the base or at the centre (1.247 vs 1.263).

## Typewriter footprint (`footprint2.py`, `yaw_check.py`)
- I read the rest-pose base corners (frame 29) on a 4x contrast-enhanced crop: back-left (1097,662), front-left (1260,694),
  front-right (1365,644). I back-projected them onto the desk plane.
- Front edge (left-right) = **0.375 m**; left side (front-back) = **0.334 m**; corner angle 89.8° (a good rectangle check).
  At f=2400/2600 the side is 0.345/0.322.
- Check on a second frame (frame 9, in the air, depth ≈4.40 m, ~581 px/m): the front edge spans 185 px and the side 106 px
  horizontally. With L=0.375 these give yaw ≈32° and D ≈ 0.345 m, in line with the rest-pose 0.334 (3%). In the air the typewriter is
  lined up with the desk (32° vs the desk's 28° to the camera x-axis). At rest it has turned about 27° relative to the desk.
- Plausibility: about 37 x 33 cm is a normal portable typewriter.

## Answer
Width = the shorter horizontal extent = front-to-back depth ≈ **0.335 m**. The length (left-right) is ≈0.375 m.
Alternative reading: a world-axis AABB taken in the rotated rest pose (world = desk axes) would be about 0.49 x 0.47 m. I did
not use it, because the typewriter's own (initial, axis-aligned) extents are the natural "width".
Confidence: moderate. The main uncertainties are f (±4%), the corner picks (±3%), and whether the paper rest or carriage overhangs the base.
