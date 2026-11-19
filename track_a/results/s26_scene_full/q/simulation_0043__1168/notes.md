# q_1168 — width of the boat (prior: length = 10 m)

The file fps (24) is the same as question_fps (24). t=1 s is frame 24 and t=2 s is frame 48.

## Camera model (camfit.py)
- The camera is static. I assumed no roll: the mast projects close to image-vertical, which supports this.
- The camera is pitched θ from nadir. Ground plane in camera coordinates: Z cosθ + Y sinθ = H.
- Boat origin ≈ the centroid from scene/tracks/boat.csv. I fitted a line over frames 2–71 to remove jitter, then
  used the smoothed positions at frames 24 and 48.
- For any focal length f, the two given depths (173.7093 m and 174.5515 m) fix θ and H.
- f is then set so that the bow-to-stern line (track bow/stern points, back-projected to the plane) is 10 m.
- Result: f ≈ 3810 px (horizontal FOV about 16°), θ ≈ 34.1°, H ≈ 152.7 m. Both depths are reproduced exactly by
  construction. Fitting at frames 2–71 gives f = 3802–3846 and θ = 34.1–34.5°.

## Width (beam.py, centerline.py)
- Edges come from colour segmentation of each image column, and every point is back-projected to the ground plane:
  - Near gunwale: the outer white rubbing strake against the red hull.
  - Far gunwale: the top outline forward of the wheelhouse.
  - Far deck edge aft: picked by hand under the far rail on frame 24 (crop frames/c24aft.png).
- The aft rails are about 0.7 m tall, so I used rail bases and gunwales only, never rail tops.
- The centreline is fitted from the paired far/near edges at the same stations, both forward and aft. It is
  rotated about 3.9° from the motion direction; the bow-to-stern line is about 4.5° off as well.
- Planform: pointed bow, widest at about 1 m forward of the centroid (beside the wheelhouse), narrow stern
  (about 2.3 m at the aft rail).
- The maximum near half-width is 1.63–1.65 m. Forward of the wheelhouse the far half-width matches the near one at
  the same stations (1.45 vs 1.45 at along −2.5 m).
- **Beam = 2 × max half-width:** 3.27 m (frame 24) and 3.28 m (frame 48). Frames 2–60 give 3.27–3.31 m; frame 71
  gives 3.12 m (noisier).
- A simpler route (raw far max fwd minus near min, with no centreline rotation) gives 3.3–3.5 m. It is biased high
  by the 4° axis rotation and by wheelhouse contamination.

## Answer
**3.28 m**

Uncertainty: about ±5%. It is dominated by θ (the depth-ratio fit; ±1–2°), by the gunwale edge choice and by
where the hidden far side is widest. A beam/length of 0.33 is plausible for a 10 m fishing boat.
