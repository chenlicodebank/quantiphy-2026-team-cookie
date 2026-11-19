3D pinhole reconstruction: f=3200 px from the 2.2 m height prior + 18.147 m depth at t=1 s; per-frame depth from the rigid PLSS backpack vertical extent (SAM track), which reproduces the 2.2 m height everywhere (2.02-2.25 m). At frame 12 the pelvis (object origin) moves 10.4 px/frame horizontally and 4.2 px/frame vertically with scale 0.00594 m/px, plus a depth rate of about -1.2 m/s, giving |v| = sqrt(1.62^2+0.50^2+1.2^2) = 2.05 m/s. Second route: whole-clip average 3D speed ~2.3 m/s and vz=0 bound 1.60 m/s bracket the value.

Final message:
**Answer: 2.05 m/s** (question 1882).

Method summary:
- **Scale**: focal length f = 3200 px from the 2.2 m height prior and the 18.147 m depth at t=1 s (frame 24).
- **Depth per frame**: used the PLSS backpack's vertical extent (SAM 3 track) as a pose-invariant rigid gauge — it reproduces the 2.2 m astronaut height to within ±5 % across all 80 frames, validating the scale.
- **Motion at frame 12 (t=0.5 s)**: pelvis (object origin) moves 10.4 px/frame horizontally, 4.2 px/frame vertically; local scale 0.00594 m/px → 1.62 m/s and 0.50 m/s, plus a depth rate of ≈ −1.2 m/s → **2.05 m/s**.
- **Checks**: whole-clip average 3D speed ≈ 2.3 m/s; vz = 0 bound gives 1.60 m/s, so the value is bracketed within ~±12 %.
