Scale from the 1.75 m person: standing height 58 px at depth 114.83 m gives f=3806 px; boat depth from depth_info (100.22 m at f0, 109.27 m at f74). Boat silhouette horizontal extent 263 px at f0 (229 px at f74). A 3D box model of the yawed boat (bow tip to stern far corner) fitted to all 75 frames gives L=8.52 m, W=2.56 m, yaw 45.6 deg, rms 1.07 px; the fitted yaw matches the boat's path heading (43.4 deg) and the cabin face widths. Second route (perpendicular projection 6.94 m corrected for yaw and stern-corner beam term) gives 8.4-8.6 m.

Final message:
**Answer: 8.5 m** (question 1688, boat length).

Method summary:
- **Scale**: the 1.75 m person (standing, legs-together pose) is 58 px tall at the given depth of 114.83 m → f ≈ 3806 px. Cross-check: the boat's vertical-extent ratio over the clip (0.924) matches its depth ratio (0.917) to 0.7 %.
- **Boat**: silhouette horizontal extent 263 px at f0 (229 px at f74) at depths 100.22 → 109.27 m from `depth_info`.
- **3D fit**: a box model of the yawed boat (bow tip to stern far corner, trajectory from the tracked centroid + given depths) fitted to all 75 frames gives L = 8.52 m, W = 2.56 m, yaw 45.6°, rms 1.07 px. The fitted yaw agrees with the boat's own path heading (43.4°) and with the cabin's face widths.
- Sanity: beam/length 0.30, hull depth 2.0 m, mast top 8.7 m above keel — all plausible for a small fishing boat. Uncertainty ≈ ±0.5 m.
