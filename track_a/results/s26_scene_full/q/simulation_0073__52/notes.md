# Q52: acceleration of the white car at 1.0 s

- The scene is a top-down 2D view with a static camera, at 24 fps. The question's rate (question_fps) is also 24, so no re-timing applies. Frame 24 (t = 1.0 s) was viewed. The white minivan is behind the cyclist, and both move up the vertical road.
- **Scale:** the prior is the bicycle's speed, 5.33 m/s. A linear fit to the cyclist's centroid (frames 2–71) gives 8.916 px/frame (rms 0.45 px). The bbox top and bottom edges give 8.89 and 8.88 px/frame. That is 213.98 px/s, so the scale is 0.02491 m/px.
- **Car:** the van starts from rest and accelerates uniformly. Quadratic fits to the centroid y give 0.2785 px/frame² over frames 0–71. Other windows give 0.277 (0–47), 0.271 (10–39), 0.282 (24–71) and 0.286 (14–33). The bbox top and bottom edges give 0.277 and 0.274.
- **Result:** a = 0.2785 × 576 × 0.02491 = **4.00 m/s²**. Across the window and edge fits the range is 3.89–4.10.
- **Second route:** the bbox-edge fits and the different frame windows agree to within ±2.5%.
- **Confidence:** high. Script: fit.py.
