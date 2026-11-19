Scale from the prior: person mask height 51 px at the given 114.83 m depth gives f = 51*114.83/1.75 = 3346 px. Boat horizontal extent at t=1 s (frame 24) = 250 px (threshold mask and SAM 3 agree), boat depth 103.157 m -> Z=103.04 m, so L = 250*103.04/3346 = 7.70 m; a projected-box fit (boat is slightly yawed/turning, its length shrinks faster than 1/Z while its height follows 1/Z exactly) gives a yaw of ~8-15 deg and L = 7.4 m. Second route at frame 0 (boat near image centre) gives 7.5 m. Answer 7.45 m, ~5% uncertainty.

Final message:
**Answer: 7.45 m** (boat length, question 1688).

Method summary:
- **Scale**: person mask (SAM 3 + threshold) is 51 px tall at the given 114.83 m depth → f = 51·114.83/1.75 = 3346 px (≈16° FOV, within the allowed range).
- **Boat**: horizontal extent 250 px at t=1 s (frame 24), depth 103.157 m → Z = 103.04 m, giving 7.70 m before correction.
- **Correction**: the boat's apparent length shrinks 14.3 % over the clip while its given distance grows only 8.4 %, whereas its vertical extent follows 1/Z exactly (H·Z constant to 1 %) — so the boat is slightly yawed/turning. A projected 3-D box fit plus the visible stern-face width give a yaw of ~8–15°, i.e. L ≈ 7.4 m.
- **Second route**: frame 0 (boat near the image centre, minimal perspective distortion) gives 7.5 m. Agrees.
