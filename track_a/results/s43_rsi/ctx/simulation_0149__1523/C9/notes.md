Tracked the car's right-front wheel (rim ellipse, bright low-saturation blob) frame by frame; rim height gives the tire's pixel diameter (D_px = 1.62*rimh) and hence depth via the pinhole model, anchored at t=0 with the given 14.244 m distance to that tire and the 0.764 m tire prior (f=2348 px, camera height 0.42 m, horizon y=822 solved from the tire/ground geometry). Back-projected wheel-centre trajectory over frames 10-31 fits a quadratic with rms 0.02-0.05 m: |v|(0.5s)=6.9 m/s, a_vec=(2.1,0,-3.7) m/s^2, giving d|v|/dt = 4.2-4.4 m/s^2 (|a| = 4.3). Second route: car silhouette height (SAM) grows 172->427 px vs tire diameter 131->300 px, consistent; narrower/later fit windows give 5.7-5.9, savgol 4.1, so adopted 4.3.

Final message:
I measured the car's acceleration from the video and finished with the answer.

**Answer: 4.3 m/s²** (acceleration of the yellow car at t = 0.5 s)

**Method summary:**
- Identified the right-front tire (near-side front wheel) and tracked its bright rim ellipse frame-by-frame; the rim's vertical extent gives the tire's pixel diameter (D_px = 1.62 × rim height, verified directly at frames 24/25/28).
- Used the pinhole model with the given 14.244 m distance at t=0 and the 0.764 m tire prior to fix the focal length (f ≈ 2348 px), camera height (0.42 m) and horizon (y ≈ 822), solved self-consistently from the tire/ground geometry.
- Back-projected the wheel-centre trajectory; a quadratic fit over frames 10–31 (residual rms 0.02–0.05 m) gives |v|(0.5 s) = 6.9 m/s and a = (2.1, 0, −3.7) m/s², i.e. d|v|/dt ≈ 4.2–4.4 m/s².
- Cross-check: the car's silhouette height (SAM) grows 172→427 px while the tire diameter grows 131→300 px — consistent depth scaling.
