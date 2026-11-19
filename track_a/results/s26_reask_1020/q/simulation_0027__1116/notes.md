# Q1116 – speed of the person, t = 1.0–2.0 s (answer 1.18 m/s)

Time base: question_fps = 24, so t = 1–2 s is frames 24–48. The file itself runs at 25 fps; I used only the frame
column from scene/.

## What the depth_info tells us
The two distances (100.564 m and 100.600 m) change by only 0.036 m in 1 s. Over the same second the body visibly
walks down-right in the image. It walks toward the camera: the person stays upright in the image and there is no
camera roll. So depth_info points to a character origin that barely moves, not to the walking body. I therefore did
not use the distances to time the motion. They do not set the scale either: metres per pixel = 1.75 m / (person's
pixel height), and the depth cancels out. What is left unknown is the camera's depression angle θ: ground motion
toward the camera is foreshortened by sin θ.

## Measurements (scripts in this folder)
- Person height is 61 px (scene record, `height_est_px` median). I used S = 61 / (1.75 cos θ + 0.3 sin θ) px/m, where
  the 0.3 m term is the body and foot depth along the line of sight.
- Image velocity over frames 24–48 (`speed.py`): x ≈ 10.4–10.8 px/s and y ≈ 14.1–16.0 px/s (pelvis, centroid and the
  crisp shoulder-top edge). I used (10.8, 16.0).
- Gait (`speed.py`, from the planted-foot plateaus): one step every 17.5 frames, which is 0.73 s at 24 fps. Each
  step moves (6.7, 11.0) px in the image.
- Water texture anisotropy (`water_aniso.py`): ripples are 0.32–0.44 as tall as they are wide. If the waves were
  isotropic this would mean θ ≈ 16–18° at the person's row. Wave crests that run parallel to the shore would bias
  this low.
- Shadow width (`shadow.py`) and torso width (`width.py`) both point to a fairly low θ (about 10–20°). Both are small
  measurements (4–14 px) that blur probably biases low.
- Apparent size drifts by about −3% over the clip. No θ can produce that geometrically, so I treated it as gait and
  segmentation noise.

## Choosing θ
Speed as a function of θ (from `speed.py`):

| θ | speed | step length |
|---|---|---|
| 18° | 1.53 m/s | 1.04 m |
| 20° | 1.38 m/s | 0.94 m |
| 22° | 1.25 m/s | 0.86 m |
| 24° | 1.15 m/s | 0.79 m |
| 26° | 1.06 m/s | 0.73 m |

The character's origin is static, so the motion comes from the animation's root motion and the steps should be
realistic (about 0.7–0.85 m for a 1.75 m adult). Feet are planted during stance, so there is no foot sliding. That
puts θ at about 22–25°. The water anisotropy suggests a slightly lower θ. I took θ ≈ 23°, giving a speed of about
1.18 m/s and a step of about 0.82 m.

## Second check
Step length × cadence: 0.82 m / 0.73 s ≈ 1.12 m/s for the whole clip. This agrees with the 1.2 m/s from the window's
velocity fit; the window runs slightly fast because 24 frames is not a whole number of steps.

## Confidence
Moderate to low. Everything depends on θ, and plausible θ from 20° to 26° spans 1.06–1.38 m/s, roughly ±12%.
