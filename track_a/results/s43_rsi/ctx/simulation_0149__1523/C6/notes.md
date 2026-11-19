3D pinhole reconstruction: f=2194 px and Z0=13.10 m from the given tire diameter 0.764 m and depth 14.244 m at t=0; per-frame depth from the yaw-invariant license-plate height (cross-checked with the front-tire height ratios, agreeing within 3%). Plate centroid 3D trajectory gives speed ~6 m/s at t=0.5 s and a local quadratic fit (frames 8-16) gives A=(6.2,-0.7,-6.8) m/s^2, |A|=9.2 m/s^2; all-frame local fit 10.0, constant-acceleration joint fit 5.4. Adopted 9.0 m/s^2 (uncertainty ~1.5).

Final message:
I measured the car's 3D motion by reconstructing the scene with a pinhole camera model:

- **Scale/focal length**: used the exact prior (tire diameter 0.764 m) and the given depth at t=0 (14.244 m to the front-right tire). The tire's 128 px vertical extent at frame 0 gave f ≈ 2194 px and a depth of 13.10 m, cross-checked against the car's roof-to-ground height (f ≈ 2226 px).
- **Depth per frame**: measured the license-plate vertical extent (yaw-invariant) at frames 0, 4, 8, 12, 16, 20, 24, and independently confirmed the depth ratios with the front-tire vertical extent (agreement within ~3%).
- **Trajectory**: back-projected the plate centroid at each depth; the car approaches from Z≈13.1 m to ≈8.5 m while moving laterally, reaching ~6 m/s at t=0.5 s.
- **Acceleration**: local quadratic fits around frame 12 give |A| ≈ 9.2–10.0 m/s² (constant-acceleration joint fit gives 5.4 m/s² since the acceleration grows through the clip). Adopted **9 m/s²** with ~1.5 m/s² uncertainty.

Notes are saved in `notes.md`.
