Tracked the right front tire (the near, fully visible wheel) with SAM + a rim-ellipse detector. Rim vertical extent is an exact depth cue (d=f*D_rim/Z); calibrated at t=0 with the given 14.244 m distance to the tire (f~2400 px, Z0=13.27 m, C=Z0*d_rim0=1128). 3D wheel positions from (u,v,Z) give a local speed at frame 12 (t=0.5 s) of 7.15 m/s (raw backward difference 6.94 m/s; range 6.9-7.5 over f=2000-2800). The car moves in a straight line (heading constant ~144 deg), so wheel speed = car speed. Cross-check: displacement 0->12 s and 12->30 s consistent with acceleration from ~2 to ~9 m/s.

Final message:
I measured the car's speed at t = 0.5 s (frame 12) as **7.1 m/s**.

**Method summary:**
- Identified the right front tire as the near, fully visible wheel (white rim) and tracked it across frames.
- Used the rim's vertical extent as an exact depth cue (vertical circle: d = f·D_rim/Z), calibrated at t=0 with the given 14.244 m camera-to-tire distance, giving f ≈ 2400 px and Z₀ ≈ 13.27 m.
- Back-projected the wheel centre each frame to 3D and computed local velocities around frame 12: 7.15 m/s (raw backward difference 6.94 m/s; 6.9–7.5 m/s across plausible focal lengths).
- Verified the car travels in a straight line (heading constant ~144°), so the wheel speed equals the car's speed, and cross-checked the scale against the car's real height and the overall displacement trend.
