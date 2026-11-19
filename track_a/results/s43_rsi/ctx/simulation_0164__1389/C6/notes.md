Ball tracked with SAM 3; scale from prior D=0.21 m and depth_info 9.391 m at t=0.5 s gives f=3850 px (validated by lane-plane vs apparent-size depth agreement, rms 0.23 m). Ball centre moves on a plane parallel to the lane (normal from re-fitted lane edges, VP y=242); 3D positions reconstructed per frame. Quadratic fit over pre-impact frames 6-38 gives v(1s)=3.69 m/s and tangential acceleration -0.27 m/s^2; independent joint fit to image positions + apparent diameters gives -0.24; speed-slope fit gives -0.26. Constant-velocity rejected at ~2 sigma. Answer: deceleration magnitude 0.26 m/s^2.

Final message:
I measured the ball's 3D trajectory and acceleration.

**Method summary:**
- Segmented/tracked the ball with SAM 3 (unique blue object), giving per-frame silhouette diameter and centroid.
- Scale: prior ball diameter 0.21 m + depth_info 9.391 m at t=0.5 s → f = 3850 px, independently confirmed by requiring the lane-plane depth and the apparent-size depth to agree (rms 0.23 m over 45 frames).
- Re-fitted the lane edges myself (far y=−0.07989x+663.66, near y=−0.10131x+776.75, VP y=242) — this also showed the scene record's "lane-unit" scale was wrong (its u is not affine in distance), so I did not use its homography for distances.
- The ball's centre moves on a plane parallel to the lane, so its depth follows from its image position alone; the image track is a straight line through the VP (motion parallel to the lane).
- Quadratic fit over pre-impact frames 6–38: v(1 s) = 3.69 m/s, tangential acceleration −0.27 m/s². Independent joint fit to image positions + apparent diameters: −0.24 m/s²; speed-slope fit: −0.26 m/s². Constant velocity is rejected at ~2σ.

**Answer: 0.26 m/s²** (deceleration of the rolling ball at t = 1 s).
