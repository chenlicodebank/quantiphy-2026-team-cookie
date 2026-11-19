Focal length from prior height 2.2 m and depth 18.147 m at t=1s (apparent height 380 px) gives f≈3170 px, scale 0.00601 m/px at frame 12. Rigid PLSS-backpack height (SAM3 track) grows 170→213 px, i.e. the astronaut approaches: Z(12)=19.05 m, mean depth rate 1.22 m/s. Image speed at frame 12 (central difference, mask centroid, hip-band cross-check) is 10.7-11.2 px/frame → lateral 1.56 m/s; combining with the 1.22 m/s depth rate gives 1.97 m/s (backward-difference route 1.74, central 2.06, hip route 2.02).

Final message:
I measured the astronaut's 3D speed at t = 0.5 s (frame 12) as **2.0 m/s**.

Method summary:
- **Scale**: prior height 2.2 m + depth 18.147 m at t=1 s, with the apparent height (380 px) at that frame → f ≈ 3170 px (cross-checked with h·Z constancy over the clip, ±4%).
- **Depth per frame**: the astronaut approaches the camera — the rigid PLSS backpack height (SAM3 track) grows 170→213 px, and the mask area grows 43%, both giving a ~20% depth decrease over the clip (Z: 19.66 m → 15.71 m, mean rate 1.22 m/s).
- **Motion at frame 12**: image speed 10.7–11.2 px/frame (mask centroid, confirmed with the hip-band reference) → lateral 1.56 m/s; combined with the depth rate → **1.97 m/s** (second routes: 1.74 / 2.06 / 2.02 m/s).

Notes written to `notes.md`.
