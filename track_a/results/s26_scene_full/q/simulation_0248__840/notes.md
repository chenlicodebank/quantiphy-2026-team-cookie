# Q840: length of the rabbit (m)

Prior: speed of the horse at the back = 0.874 m/s. Everything moves to the right (+x), so the horse "at the back" is the
trailing chestnut horse (horse_red, on the left). fps = question_fps = 24, so no re-timing. 2D side view with a static camera.

## Scale (measure.py, scene/tracks/horse_red.csv, frames 0-48; frame 49 is an animation-loop reset and is excluded)
- Torso-centroid x: mean per-frame speed 77.2 px/s. A linear fit gives 77.4 px/s. Mask x_min and x_max fits give 75.6 and 76.8 px/s. Mask centroid gives 75.7 px/s.
- I used 77.3 px/s, which gives 0.874 / 77.3 = 0.01131 m/px.

## Rabbit length
- The rabbit mask x-extent over 50 frames has a median of 44 px, a mean of 44.9 px and a range of 42-53 (it changes with the hopping gait).
- I checked it on a zoomed crop at frame 24: the body spans about 1158-1202 px.
- 44.5 px x 0.01131 = 0.503 m. Answer: **0.50 m**.

## Check
- With the same scale, the red horse's median length of 194 px is 2.19 m, which is plausible for a horse. So the scale is
  physically sensible. (The other horse would give a scale of 0.0061 m/px, which would make the red horse only 1.2 m long.)
- The rabbit stands on floor row ~637 and the red horse on ~630, so the rabbit is a little closer to the camera. Perspective could
  make the rabbit look up to a few percent larger than it would at the horse's depth. I applied no correction, following the 2D convention.

Confidence: moderate-high. The main uncertainty is gait-dependent length (±5%) and the slight depth difference.
