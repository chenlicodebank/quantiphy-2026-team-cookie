3D pinhole reconstruction: focal length f=3639 px solved from the 1.29 m/s speed prior plus the two given camera distances (5.2108 m at t=1, 6.3261 m at t=2). SAM-3 body-only masks give the head/horn and tail-tip image points at t=1 and t=2; imposing the rigid-translation constraint (both ends move by the known 3D displacement) yields 3D body lengths 0.585 m and 0.563 m (mean 0.574 m). Checks: L_px*Z is constant (1893 px*m) over frames 0/12/24/48, projected-length ratio 1.205 vs depth ratio 1.214, and the second route L=L_px*Z/(f*sin(alpha)) with sin(alpha)=0.889 gives 0.585 m. Wingspan (width) ~1.22 m, body/wingspan 0.47 as expected for a bird-like flyer.

Final message:
**Answer: 0.57 m** (question id 1486)

Method summary:
- **Scale**: solved the focal length (f = 3639 px, 43° HFOV) from the 1.29 m/s speed prior combined with the two given camera distances (5.2108 m at t=1, 6.3261 m at t=2) and the dragon-origin image displacement.
- **Body axis**: SAM‑3 "dragon body" masks (wings excluded) gave the head/horn and tail‑tip pixel positions at t=1 and t=2. Imposing the rigid‑translation constraint (both ends move by the known 3D displacement vector) recovered the 3D head and tail points → body lengths 0.585 m and 0.563 m.
- **Checks**: L_px·Z is constant at 1893 px·m across frames 0/12/24/48; projected‑length ratio 1.205 vs given depth ratio 1.214; second route L = L_px·Z/(f·sin α) with sin α = 0.889 reproduces 0.585 m. Wingspan (width, not asked) ≈ 1.22 m, giving a normal bird‑like body/wingspan ratio of 0.47.
