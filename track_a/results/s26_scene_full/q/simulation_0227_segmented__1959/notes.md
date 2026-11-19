# q_1959: height of the swimming ring (flamingo float), in metres

Prior: the black cat's speed is 1.041 m/s. There is no depth_info. fps = question_fps = 24, so no re-timing.

## Scale from the cat
- The cat walks steadily to the right at constant depth: its paws stay at y≈919 and its size stays constant.
- Its centroid moves 567.4→836.0 px and its nose edge 619→887 px over 49 frames. That is 5.48 / 5.47 px/frame, or
  131.4 px/s. The first and second halves of the clip agree.
- Scale at the cat's depth: s_cat = 1.041 / 131.4 = 0.00792 m/px.

## Perspective (why the plain 2D scale is not used)
The chairs face the camera, and their seats are seen from above, so this is a 3D scene with a perspective
camera. The float stands lower in the image than the cat, so it is nearer the camera.
- Horizon: I drew ground lines from the front-leg bottoms to the back-leg bottoms of the front-right chair (two
  lines) and the front-left chair (one line), using the median-background mask. The three lines meet near
  (960–970, 525–536), which is close to the image centre. That gives horizon y_h ≈ 531 and a camera that is roughly level.
- Ground plane: distance Z ∝ 1/(y_ground − y_h).
  - Cat: y_ground = 919.
  - Float: the ground point under its centre is the ring's leftmost silhouette point plus the tube radius.
    The leftmost point (tube-centre height) is at y = 988.6, averaged over the frames. The tube radius is 15–20 px,
    from the profile of the ring's tip. That puts the ground point at y ≈ 1005.6.
  - Cross-check: the ring bottom (1009–1015) minus the foreshortened ring radius (about 5–10 px) gives the same value.
- Depth ratio: Z_float / Z_cat = (919 − 531) / (1005.6 − 531) = 0.817.
- World height in pixels at the float's depth: from the neck top (y = 886.3, steady over all frames) down to the ground
  line through the ring centre = 119.3 px. The neck sits on the ring's right side, at about the centre depth.
  The bbox height of about 128 px is larger only because the ring's near edge drops lower in the image.

## Result
H = 119.3 × 0.00792 × 0.817 = 0.772 m, so the answer is **0.77 m**.

Sensitivity:
- Ground point under the float ±3 px → 0.758–0.787 m.
- Horizon ±15 px → 0.767–0.778 m.
- Second route, using the ring's bottom edge instead of its leftmost point: 0.755–0.785 m.

The naive single-scale 2D answer would be 128 px × 0.00792 = 1.01 m. It ignores the fact that the float is about
18% nearer the camera than the cat, so I rejected it.

Confidence: moderate. The main assumption is that the cat and the float stand on the same horizontal ground plane
as the chairs, and the background was removed, so this cannot be checked. Scripts: bgmask.py, floatmeas.py,
ringprof.py, ringprof2.py, compute.py.
