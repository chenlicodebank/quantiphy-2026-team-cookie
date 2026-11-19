Ball (D=0.21 m) rolls down the lane; f=3829.9 px from the 9.391 m depth at t=0.5 s and the sub-pixel silhouette diameter (85.6 px). The ball centre lies on a plane, so depth z=1/(1.126*v+0.0756) with v=(cy-540)/f (fit rms 0.075 m over frames 6-29, before the pins contaminate the silhouette). Quadratic fit of the 3D positions gives v=3.93 m/s and a=(-0.046,0.014,-0.212) m/s^2 at t=1 s (frame 24); the component along the velocity, i.e. the rate of change of scalar speed, is 0.18 m/s^2 (vector magnitude 0.22). Second route (straight-line + diameter-based depth joint fit) gives a smaller 0.05 m/s^2 but is limited by the +-2% diameter bias; window stability of the plane model gives 0.18-0.24. Adopted 0.20 m/s^2.

Final message:
I measured the ball's motion and answered.

**Method summary:**
- The scene's HSV mask under-measured the ball (80.5 px vs the true ~85.6 px at t=0.5 s), so I re-measured the silhouette with a sub-pixel radial 50 %-crossing circle fit, cross-checked against SAM 3 masks and a horizontal chord measurement.
- Focal length from the prior + depth_info: f = 85.64 × 9.391 / 0.21 = 3829.9 px.
- Since the ball rolls on the lane, its centre lies on a plane, so depth is a function of image row: z = 1/(1.126·v + 0.0756), fitted over frames 6–29 (rms 0.075 m, no systematic trend). Frames 30–40 were excluded because the white pins/pit contaminate the silhouette (diameter residual grows to +4 px).
- Quadratic fit of the reconstructed 3D positions at t = 1 s (frame 24): v = 3.93 m/s, a = (−0.046, 0.014, −0.212) m/s², i.e. a deceleration of ≈0.18–0.22 m/s² along the direction of travel.

**Answer: 0.20 m/s²** (ball decelerating), with a second route (diameter-based joint fit) giving a smaller value and window-stability checks spanning 0.18–0.24.
