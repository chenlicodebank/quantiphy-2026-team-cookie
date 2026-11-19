# q_340: average speed of the rocket from beginning to end (m/s)

Prior: rocket length = 2.9 m. 2D video, 24 fps (file fps = question_fps = 24), 29 frames. Static camera. The rocket
flies in a straight line at 39.1 deg up and to the left. Its nose appears at the pod mouth at frame 3, and the rocket
leaves the top of the image at frames 22-25.

## Scale (scripts: profile.py, measure.py)
- Own along-axis profile of |frame - frame0| over free frames 13-21:
  - 50% crossing length: median 202 px (200-210).
  - Integral/plateau length (blur-invariant): median 206.9 px.
  - The 50% point at the tapered nose sits slightly inside the tip, so I took L = 204 px (±3).
  - Scale: 2.9 / 204 = 0.01422 m/px.
- SAM 3 masks of "rocket":
  - Frame 15 (box prompt): length 241.8 px. Frame 17: 242.7 px. Frame 21: 257 px.
  - SAM is 18-25% longer than the blur-free length. Its length matches my 10%-level length (237-252 px), so SAM
    includes the motion-blur smear (and a slight boundary dilation).
  - On the zoomed frame 13, the sharp body is about 200 px long. The 50%/integral value is the right one for the
    object's geometric length, and I kept it.
- My d>30 mask centroids (measure.py) agree with scene/tracks/rocket.csv to within 1-2 px in frames 13-22.
- SAM centroids are 5-8 px further toward the tail because they include the blur trail.
- The SAM displacement from frame 15 to 21 is 313.4 px, against 318.0 px from the track (1.5% difference, under 3%).

## Motion (fit.py)
- Along-axis advance per frame: about 17 px at frames 5-6, then 38 (f13), 50 (f17), 58 (f21), and 61-62 (f22-25).
  The rocket accelerates from rest, and its acceleration falls off (eased curve).
- A cubic fit over frames 4-25 has rms 1.7 px. It puts v = 0 near frame 0-2, which fits the launch starting at
  frames 1-2.
- Readings of "from beginning to end", each as the mean of per-frame speeds (= path / time for a straight path):
  - **Whole clip, frames 0-28:**
    - Observed s(24) - s(4) = 846 px.
    - Frames 25-28: about 4 × 62 = 248 px, extrapolated from the plateau.
    - Frames 1-4: about 35 ± 10 px, a ramp from rest.
    - Total about 1129 px, giving 40.3 px/frame, i.e. **13.8 m/s**. The cubic fits give 13.2-14.1 m/s.
  - **Visible flight only, frames 4-25:** 908 px in 21 frames, i.e. **14.75 m/s**. Frames 3-25 give about 14.4.
- The two readings differ by about 7%.
- Answer: **14.1 m/s**. It is within 2.5% of the whole-clip value and within 4.5% of the visible-flight value.
- Second route: the quadratic and cubic fits over different frame windows give 13.2-15.7 m/s across readings. The
  direct observed displacements give 14.4-14.75 m/s for the visible part.

## Confidence
- The scale is good to about ±2%.
- The main uncertainty is which interval the reference averages over (±4%), plus the extrapolation outside the
  image.
