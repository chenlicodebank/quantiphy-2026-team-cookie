# q_3205 – wallet displacement 2.20 s → 2.50 s

- 2D internet clip with 30 fps (the file's rate and question_fps are the same). The footage is rotated, so gravity points along image +x. The camera is static.
- The "wallet" is the black pouch. It is released at frame 66 (t = 2.20 s) and falls freely until frame 80, then hits the baseboard at frame 81.
- Scale comes from the prior g = 9.8 m/s². The pixel acceleration is a parabola fitted to the centroid x over frames 67/68–80:
  - 11.77 px/frame², which is 10590 px/s²
  - scale = 9.25e-4 m/px
  - The mean of the raw second differences is about 11.8–12.0. The last one (14.6, frame 80) is inflated by blur near the baseboard.
- Frames: t = 2.20 s is frame 66 and t = 2.50 s is frame 75 (round(t × 30)).
- Centroid x (scene track): 158.5 → 628.9, so Δ = 470.4 px (y changes by only 2 px). My own re-segmentation gives 154.8 → 628.9. At frame 66 the hand touches the pouch, which shifts the centroid a few px.
- Displacement = 470.4 × 9.25e-4 = **0.435 m**.
- Checks:
  - The fitted parabola gives 0.433 m.
  - My independent segmentation gives 0.439–0.442 m.
  - Physics check: falling from rest for 0.3 s gives ½·9.8·0.09 = 0.441 m. That agrees, since the release happens near frame 66.
- Confidence: high, about ±3%. The main uncertainty is the exact pixel acceleration the annotator used (11.8 vs 12.0 px/frame²).
