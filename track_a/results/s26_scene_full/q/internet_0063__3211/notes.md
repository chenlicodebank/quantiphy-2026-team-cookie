# q_3211: displacement of the water bottle between 1.50 s and 1.70 s

- Time base: the file runs at 30.016 fps and the question at 30 fps. Both give frame 45 for 1.50 s and frame 51 for 1.70 s.
- Scene: the camera is rotated 90°, so the bottle free-falls toward image +x. It is released at frame ~39.5 and hits the skirting board at frame 52–53. Frames 45–51 are clean free fall, and camera drift there (~0.2 px/frame) is negligible.
- Scale from the prior (g = 9.8 m/s²): I re-segmented the blue cap (cap.py). Its x second differences are 11–14 px/frame². Quadratic fits over frames 41–51, 40–52 and 42–50 give 12.3–12.4 px/frame², so a = 12.4 × 900 = 11160 px/s². The scale is 9.8 / 11160 = 8.78e-4 m/px. Sanity check: the 260 px bottle comes out at 0.23 m, which is plausible.
- Displacement in pixels:
  - Bottle centre from the record: (432.1, 566.1) → (1068.7, 549.1), which is 636.8 px.
  - Cap (my own segmentation): (312.6, 555.7) → (956.1, 522.8), which is 644.3 px.
  - I used about 640 px, giving 0.562 m.
- Second route (kinematics): release at frame 39.5 puts the two times at t = 0.183 s and 0.383 s after release. Then d = 0.5 × 9.8 × (0.383² − 0.183²) = 0.555 m. The pixel fit agrees: 0.5 × 12.4 × (11.5² − 5.5²) = 632 px, which is 0.555 m.
- Answer: 0.56 m. Confidence is good, with an uncertainty of about ±4%, mostly from the pixel-acceleration estimate.
