# q_2777 — yoga ball diameter (cm)

Prior: v(1.0 s) = 2.1464 m/s. depth_info: yoga ball 2.4985 m at t=1.0 s (frame 24); "soccer ball" 1.4972 m at 1.5 s
(there is no soccer ball in the clip, and this depth does not fit the yoga ball at frame 36: the angular sizes give a
1.42x distance ratio, the depths 1.67x, so I ignored it); person 3.83 m. File fps = question fps = 24.

I checked the scene/ ball track (a cone fit to the silhouette, rms ~0.9 px, "good" at frames 18-30) on a zoomed frame 24.
At frame 24 the angular radius is alpha = 5.537 deg (sin = 0.0965), and the off-axis angle is 15.8 deg.

Routes (f = 762.75 px):
1. Sphere geometry, depth taken as the distance to the centre: D = 2 * 2.4985 * sin(alpha) = 48.2 cm.
2. Method card, depth x pixel extent / f, at frame 24: ellipse minor 153.8 px -> 50.4 cm; vertical bbox 157 px
   (y 464-621) -> 51.4 cm; ellipse major 159.9 px -> 52.4 cm. These are inflated by the off-axis stretch.
3. Depth taken as the sensor's front-surface range (d_centre = 2.4985 + R): R = s*d/(1-s), so D = 53.4 cm.
4. Velocity prior (independent of the depth convention, since centre = ray * R / sin(alpha)): fitting the speed per
   unit R around frame 24 over windows 5-13 frames wide gives 7.5-7.9 R/s, so D = 2*2.1464/speed = 54.2-57.1 cm. The
   mean forward difference over frames 22-26 gives 51.6-54.1 cm.
5. Sanity check with the person depth: at frames 0-12 the held ball has alpha 4.42 deg. With D = 48 cm its centre
   would be 3.13 m away, 0.7 m in front of the person at 3.83 m, which is too far for a ball held against the body.
   With D of about 54 cm the centre is about 3.5 m away, so the ball sits against the person, which is plausible.

Routes 3, 4 and 5 agree on a ball of about 53-56 cm (a typical 55 cm ball). Route 1 (48 cm) is the low outlier,
probably because the depth sensor measured the front surface. Answer: 54 cm. Confidence: moderate (about ±8%).
