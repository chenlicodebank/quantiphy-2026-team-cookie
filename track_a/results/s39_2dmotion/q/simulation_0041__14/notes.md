# q14: speed of the person at t = 1.0 s (prior: person height 1.75 m)

Time base: question_fps = file fps = 24, so t = 1.0 s is frame 24. The camera is static (per scene/).

## Pixel motion (speed.py, height.py)
- I tracked the person's upper body in two ways: (a) the centroid of the white shirt pixels, and (b) a sub-pixel template match of head+torso against frame 24.
- Speed in px/frame:

  | window | template | shirt |
  |---|---|---|
  | backward difference at frame 24 | 1.67 | 1.38 (one-frame values are noisy) |
  | frames 22–26 | 1.57 | 1.59 |
  | frames 20–28 | 1.56 | 1.52 |
  | full gait cycle 7–41 | 1.51 | 1.51 |
  | whole clip | 1.53 | 1.53 |

- Adopted pelvis-level speed at frame 24: 1.56 px/frame = 37.4 px/s. This is within 1.5 px/frame of the record's centroid and head-top tracks.

## Scale
- Height in px, from my own background-difference mask (head top to lowest foot) in height.py:
  - It swings 40 to 50 px with the gait. Median 47, maximum 50, about 49 at frame 24, and minimum 40–41 at mid-stance, when the feet are together under the body.
  - The lowest-foot plateaus show one step every ~17 frames, about 25.5 px in the image.
- The view is oblique, not a flat 2D plane facing the camera:
  - The head appears as a hair blob, i.e. seen from above.
  - Ground-forward motion maps to image-down.
  - The step length adds to the apparent height at heel strike, which is why the height swings.
- So I estimated the camera elevation e:
  - Horizontal scale k from widths that are not foreshortened (width.py): shoulders 16.5–17 px, which is ~0.46 m bideltoid; head 5.5–6 px, which is ~0.16 m. This gives k ≈ 35 px/m (±10%).
  - Mid-stance height: 40.5 px = k(1.75 cos e + 0.2 sin e) gives e ≈ 55°.
  - Ground scale along the walking direction: k sin e ≈ 28.8 px/m.
  - Speed = 37.4 / 28.8 = 1.30 m/s. The range for k from 33 to 37 is 1.15–1.40.
- Second route, a naive single 2D scale from the height prior:
  - Using the median height of 47 px: 1.75/47 × 37.4 = 1.39 m/s.
  - Using the full-stride height of 50 px: 1.31 m/s.
- Third check, gait: a 0.88 m step at 1.41 steps/s gives ~1.25 m/s. That is a long stride but a plausible animation.
- Answer: **1.30 m/s**. Confidence is moderate (about ±10%) because the scale depends on the oblique-view correction.

## SAM 3 comparison (measure.py, zoom.py, sam_person.json)
- Text prompt "person" at frame 24:
  - Box y 401.9–451.4 (h 49) vs my 403–451 (h 49).
  - The SAM top is ~1.5 px high; the zoomed overlay (frames/zoom.png) shows SAM's outline runs 1–3 px outside the hair and body.
- Box-prompted SAM masks at frames 14–34 are too generous: heights 45–68, sometimes including shadow or halo. Where the heights differ by more than 3%, my mask is the right one; I checked this on the zoomed frames.
- SAM centroid speed over frames 22–26: 1.46 px/frame vs mine 1.57. SAM's frame-to-frame centroids jitter, so I used the template and shirt tracks.
- The SAM video track was unreliable (anchor IoU 0.42) and was not used.
