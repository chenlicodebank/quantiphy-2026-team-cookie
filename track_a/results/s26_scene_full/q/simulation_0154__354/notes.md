# Q354: displacement of the shark (prior: speed = 7 m/s)

- 2D video, 24 fps (the file's rate and question_fps agree), 48 frames (0–47). Static camera. The shark swims straight left at y ≈ 299 and never stops or turns, so its displacement equals its path length.
- Pixel motion (fit.py, using scene/tracks/shark.csv): snout frames 1–30 move at 58.0 px/frame; the tail tip moves at 60.5 px/frame in frames 15–30 and 56.7 px/frame in frames 31–46. The centre's net move from frame 0 to frame 46 is 2632.6 px over 46 frames, i.e. 57.2 px/frame. The ±5% variation looks like tail-beat or swim-rig wobble plus a slight ease. I treat the motion as steady, with a nominal speed of 7 m/s.
- Scale: 7 m/s ÷ (57.2 px/frame × 24 frames/s) ≈ 0.0051 m/px.
- Displacement from frame 0 to frame 47 (the whole clip, 47 frame intervals): 7 × 47/24 = **13.71 m**.
  - Same answer by the pixel route: 57.2 px/frame × 47 frames × 0.0051 m/px = 13.71 m.
  - Using the full 2.0 s instead gives 14.0 m (+2%).
  - If instead 7 m/s were the peak mid-clip speed (about 60 px/frame), the answer would be about 13.1 m (−5%).
- Confidence: moderate–high.
