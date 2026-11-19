# q_2942 – width of the blue shopping bag (cm)

The file and the question are both at 24 fps (t = 1.4 s -> frame 34). The bag is the static "blue_tote_bag" in scene/
(lying flat on the floor, handles on its upper-right long side). Its depth at t = 1.4 s is 3.307 m. Lab camera: f = 0.5959 x 1280 = 763 px, pp (640,360).

## Bag outline (bag.py, refine.py)
- Median of frames 30-48 (the bag is static). Mask = blue body plus logo, handles excluded (frames/bagmask.png).
- Lines fitted to the 4 contour sides, then intersected (frames/refine.png). Corners: (769.9,313.7), (823.2,294.0),
  (898.7,345.6), (843.8,369.8). Long sides (handle/opening side and the opposite one) are 91-93 px, short sides 56-58 px.

## Floor tilt (tilt.py, tilt2.py, joint.py)
The long sides run diagonally on an oblique floor, so they need a foreshortening correction. I estimated the floor plane
normal (pitch, roll) from the moving white board: its edge lengths back-projected onto one plane must stay constant over
frames 20-48, and its corners must be right angles. That gives pitch 37-39 deg and roll about 9 deg. The bag's own corner
angles come out at about 90 deg under the same plane, which confirms it.
Then I back-projected the bag corners onto the plane through the bag centre (depth 3.307 m).
- Long side (across the opening = the bag's width): 41.7 cm (range 40.8-43.0 for pitch 36-41 deg).
- Short side (the bag's height, bottom to opening): 35.5 cm (34-37).
- Conflicts: the prior velocity (1.934 m/s) would fit a pitch of about 26 deg. On the fitted plane the board moves at about
  1.5 m/s. The given depths are not consistent with one floor plane either (the bin would be >1 m above it). So I trust the
  multi-frame rigid geometry over the depth-derived speed. At 26 deg the bag would come out about 53 x 41 cm with
  corners far from 90 deg, which is not plausible.

## Second route
Plain method card: 3.307 m x 92 px / 763 = 39.9 cm for the long side (no tilt correction). This is within 5 % of 41.7.

## Naming
"Width" here is the bag's side-to-side extent across its face and opening, which is the long side: **41.7 cm** (answered).
Under the alternative reading "width = shorter horizontal extent" it would be 35.5 cm.
Confidence: moderate. The tilt uncertainty is about ±3 %, and the reading of "width" is the main risk.
