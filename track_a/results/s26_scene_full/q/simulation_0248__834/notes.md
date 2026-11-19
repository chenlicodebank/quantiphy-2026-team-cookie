# Q834: height of the horse at the back (m)

- "Horse at the back" = horse_red, the smaller chestnut horse. It trails the group on the left and stands slightly farther back (hooves at y≈630 vs 634 for the other horse). The prior gives its speed: 0.874 m/s. fps = question_fps = 24.
- 2D scale from the prior on the same horse: the horizontal pixel speed over frames 0-48 is 3.20 px/frame. Frame 49 is an animation-loop reset and is excluded. Values by reference point: torso 3.22 (slope and mean |dx|), centroid 3.15-3.22, x_max 3.19, bbox centre 3.03-3.17 (noisier). 3.20 px/frame = 76.8 px/s, so the scale is 0.874/76.8 = 0.01138 m/px.
- Pixel height: the record's mask gives a median of 170 px (range 165-174). I checked it independently (measure.py, check_height.py, zoomed crop). The ear tip is at y≈461-464 on frames 0-48, which matches the record. The hoof bottoms are at y≈628-630 in the zoomed crop. My crude mask's bottom edge (650) was the bright floor band, not the hooves, so I kept the record's 170 px.
- Height = 170 × 0.01138 = 1.93 m.
- Uncertainty: about ±3% from the choice of reference point for speed and ±2% from the pixel height. Confidence is fairly good.
