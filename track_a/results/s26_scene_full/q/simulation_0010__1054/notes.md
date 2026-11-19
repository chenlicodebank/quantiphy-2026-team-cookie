# q_1054 – height of the house's door (m)

Prior: bird length 1.19 m; bird distance 34.584 m (t=0), 33.999 m (t=1 s → frame 24 at question_fps 24);
house distance 55.083 m; cart distance 30.374 m. File fps 22.892 (frame-indexed; question_fps 24 used for t→frame).
Camera static (scene/ record). Principal point assumed at the image centre (960, 977).

## Focal length (from the bird)
birdlen.py: median-background difference mask (threshold 15 and 25) for frames 0–39, horizontal extent of the bird
(tip of beak/head to tail). The bird flies almost across the view (its distance changes only ~0.3 m in Z over 1 s while it
moves ~3.7 m sideways), so its length is seen nearly fronto-parallel.
- frames 0–4: ~168–173 px, Z ≈ 34.2 m → f ≈ 4890 px
- frames 18–20: ~158–167 px, Z ≈ 34.0 m → f ≈ 4600 px
- frames 27–29: ~161–176 px, Z ≈ 33.9 m → f ≈ 4730 px
f ≈ 4740 px (±4 %), hFOV ≈ 23°. (Z = distance / sqrt(1+((u-cx)/f)^2+((v-cy)/f)^2).)

## Door pixel height
prof.py row profiles at frame 0: door leaf (planked door, x 395–500) and the open doorway (x 509–622) both run from
y ≈ 880 (under the header beam) to y ≈ 1157 (threshold) → 277 px. Both readings agree.

## Door depth
House origin (presumably base centre, u ≈ 560): Z ≈ 55.083/1.0045 ≈ 54.84 m. The door is on the front wall, closer than
the origin by half the house depth. The house is ~7.7 m wide (700 px × 52/4740); its side walls are not visible
(near-fronto-parallel facade), so the depth cannot be measured; assumed roughly square plan → half-depth ≈ 3.5 m,
Z_door ≈ 51.3 m. (Ground-plane check with the cart was too sensitive to the unknown horizon to constrain this:
horizon 1025–1075 gives front-wall Z 47–55 m.)

## Result
height = 277 × 51.3 / 4740 ≈ 3.00 m.
Sensitivity: door at the origin depth → 3.20 m; half-depth 5 m → 2.91 m.
Sanity: barrels 113 px → ~1.25 m, house wall height to eaves ~4.2 m – consistent with a scene ~1.3–1.4× real scale
(door 3.0/1.35 ≈ 2.2 m real-world equivalent).

Confidence: moderate (±7 %); main uncertainties are the bird pixel length (wing pose) and the door's depth offset
from the house origin.
