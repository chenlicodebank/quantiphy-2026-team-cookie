# q_798 – length of the front horse (simulation_0239)

Question: length of the horse in the front (m). Prior: speed of the horse at the back = 0.874 m/s. No depth_info.
fps = question_fps = 24.

## Identification
Overhead view, both horses walk toward +x. White/cream horse (lower, y≈865) leads by ~240 px -> "front";
brown horse (upper, y≈776) trails -> "back". (The white one is also nearer the image bottom, so both readings agree.)

## Scale (2D, one m/px from the prior)
Brown horse pixel speed, frames 0-48 (frame 49 is an animation loop reset, excluded), by template matching
(`speed.py`): rump 62.8, mid 66.4, front 64.6, whole-body 64.4 px/s (linear fit); net 0->48 = 126.5-127.4 px
(= 63.5 px/s). Record's full-mask cx: 64.5 px/s (net 125 px). The record's eroded torso_cx (118 px net) is an
outlier caused by the erosion shifting with the gait; not used.
Adopted 64 px/s -> scale = 0.874 / 64 = 0.01366 m/px.

## Length of white horse
Difference mask against a frame where the horse is elsewhere (`measure2.py`), tail tip to muzzle:
frame 0: 176-177 px, frame 12: 163-167, frames 47-49: 169-171 (thr 40), frames 1-2: 172-183 (noisy).
Record zoom: 175 px at frame 0. Adopted ≈173 px (gait varies it ±4).
Length = 173 × 0.01366 = 2.36 m (range 2.28-2.42).

## Check
Brown horse length 143 px -> 1.95 m with the same scale; white 2.36 m: both plausible horse sizes and consistent with
the white horse visibly being larger. Speed from two independent routes (template matching, mask centroid) agree within 2%.
Confidence: moderate-high (~±4%).
