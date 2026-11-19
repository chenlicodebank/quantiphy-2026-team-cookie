# q_615 — height of the table lamp (m)

Prior: black cat speed = 0.94 m/s. No depth_info. fps = question_fps = 24, so no re-timing.

## Scale from the cat
- I checked `scene/tracks/cat.csv` (calc.py). The matched upper-body track gives a mean per-frame speed of 17.737 px/frame,
  which is 425.7 px/s. Two independent checks agree: the torso centroid's net motion is 17.61 px/frame, and the nose,
  read by eye from 529 to 1399 over 49 frames, is 17.76 px/frame. The walk is steady.
- Scale at the cat's depth: 0.94 / 425.7 = 0.002208 m/px.

## Lamp pixel height (legs.py, top.py, frame 0, static camera)
- Top of the shade (apex/finial) is at y ≈ 500 (column profiles at x 1342–1346). The bottom of the copper base is at
  y ≈ 788, where the copper colour stops on the stand top. That makes **288 px** (±3).

## Depth correction (the lamp is behind the cat)
This is a 3D Blender scene. The cat walks on the floor in front of the TV stand, and the lamp stands on the stand top,
so the two are at different depths. The camera looks level: verticals stay vertical, and we see the stand top slightly
from above. I took the horizon at y ≈ 540.
- Cat ground contact: paws at y ≈ 1013–1021, centre about 1017, which is 477 px below the horizon.
- Front-bottom of the stand (foot rail): y ≈ 986, 446 px below the horizon. So Z_standfront / Z_cat = 477/446 = 1.070.
- Stand top face: back edge y 776, front edge y 794. The lamp base sits at y 788, so
  Z_lamp / Z_standfront = 254/248 = 1.024.
- Consistency check: if the back of the stand touches the wall, the wall/floor line should be at y ≈ 954. The observed
  baseboard/junction band is at y 944–962. This agrees, which supports the level-horizon assumption.
- Depth ratio Z_lamp / Z_cat ≈ 1.095. The spread is 1.08–1.12 for a horizon between 500 and 580 and a paw y of
  1013–1021.

## Answer
Height = 288 px × 0.002208 m/px × 1.095 ≈ **0.69 m** (range 0.68–0.71).
With no perspective correction (single 2D scale), it would be 0.636 m. I chose the corrected value because the
geometry clearly puts the lamp about 10 % farther away than the cat.
Sanity check: the cat's body length of 245 px comes out at about 0.54 m, and a 0.69 m table lamp is plausible.
Confidence: moderate. The main uncertainty is the depth ratio (±3 %) and the convention (2D scale vs true 3D).
