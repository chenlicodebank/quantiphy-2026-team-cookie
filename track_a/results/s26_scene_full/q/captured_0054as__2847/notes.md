# q_2847: white ball diameter (cm)

**Which ball is it?** depth_info gives white ball 3.0735 m and green ball 3.039 m at t = 1.0 s (frame 24, at
question_fps 24, which matches the file's rate). The green ball is the tennis ball in the standing person's hand.
The "white" ball has to be the small light-grey ball (scene/ calls it `grey_ball`). It was thrown from the
standing person's hand at frame 23, so at frame 24 it is in flight right next to that person, at a depth of
about 3.07 m (see frames/hand_24.png). The soccer ball sits next to the basketball, which is at 2.36 m at
t = 0.5 s, so the soccer ball is about 2.5 m from the camera, not 3.07 m. With 68 px and 3.07 m it would also
come out at 27 cm, larger than the basketball, which is implausible.

**Measurement (measure.py):** I took |frame − median background of frames 0/2/4| in a 50 px crop around the
ball, smoothed it (σ = 0.7), thresholded it, filled holes and measured the principal axes.
- Frame 24: the minor (across-motion) width is 19.4 / 19.5 / 18.5 px at thresholds 40 / 60 / 80, and the bbox
  is 19 × 22 px. The motion blur lengthens the ball along its up-left motion.
- Frames 25–27 (slower near the apex): equivalent diameter 17.9–19.9 px.
- The overlay (frames/mask24.png) follows the visible outline.
- A half-maximum threshold cuts away the lit side of the ball, which looks almost like the background, so I
  rejected it.
- Adopted D ≈ 18.8 px.

**Size:** f = 0.5959 × 1280 = 762.8 px, so D = 3.0735 × 18.8 / 762.8 = 0.0758 m ≈ 7.5 cm. The range from
18–19.5 px is 7.3–7.9 cm.

**Check:** I measured the green tennis ball the same way at 3.039 m. Its across-motion extent in frames 25–27 is
about 17.5 px, which gives about 7.0 cm against 6.7 cm for a real tennis ball. So the pixel scale holds to
within about 5%, and the white ball is slightly larger than the green one in pixels as well.

**Confidence:** moderate to high on which object it is, and about ±5% on the size.
