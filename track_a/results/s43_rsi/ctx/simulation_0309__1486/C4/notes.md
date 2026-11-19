SAM 3 mask at t=1.0 s (Z=5.2108 m from depth_info): skeleton geodesic from head tip (1510,647) to tail tip (1683,857) = 397 px nose-to-tail body length; wingspan 872 px. Focal length from the speed prior (1.29 m/s) and the depth rate (1.1153 m/s -> lateral 0.648 m/s) via the 3D path length of the undulating, flap-filtered centroid track: f ~ 4500 px (three independent filters 3900-5000 px, instantaneous checks 3300-4000 px). The body is aligned with the flight direction V=(-0.367,-0.339,0.867), 30 deg from the optical axis, so foreshortening = 0.508. L = 397*5.2108/(4500*0.508) = 0.91 m. Second route: body chord at t=2.0 s (228 px at Z=6.3261) gives 1442 px*m vs 1417 px*m at t=1.0 s (1.8% agreement), confirming the depth model and constant orientation; implied wingspan 1.02 m.

Final message:
I've completed the measurement and submitted the answer.

**Summary of the method:**

1. **Object & frames**: The dragon is the only moving object; I used SAM 3 masks at t=1.0 s (frame 24) and t=2.0 s (frame 48), the two times with given depths.

2. **Pixel measurement**: Zhang-Suen skeleton of the frame-24 mask gave the head tip (1510,647) and tail tip (1683,857); the geodesic along the spine is 382 px, +15 px for skeleton tip erosion → **397 px nose-to-tail**. Wingspan (mask major axis) = 872 px.

3. **Focal length** (the only metric anchor is the 1.29 m/s speed prior): depth rate 1.1153 m/s → lateral speed 0.648 m/s. Because the dragon's image path undulates strongly and the silhouette centroid carries a ±110 px wing-flap oscillation, I filtered the track (polynomial, moving average, and instantaneous checks) and matched the 3D path length to 1.29 m/s → **f ≈ 4500 px** (hFOV ≈ 36°).

4. **Foreshortening**: the body is aligned with the flight direction V = (−0.367, −0.339, 0.867), 30° off the optical axis → projection factor 0.508.

5. **Result**: L = 397 × 5.2108 / (4500 × 0.508) = **0.91 m**, with an implied wingspan of 1.02 m (body/wingspan ≈ 0.9, plausible for a long-tailed wyvern). A second route (body chord at t=2.0 s, 228 px at 6.3261 m → 1442 px·m vs 1417 px·m at t=1.0 s, 1.8 % agreement) confirms the depth model and constant body orientation.
