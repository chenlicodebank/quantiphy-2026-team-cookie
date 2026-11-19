# q139 – speed of the small bird at 0.3 s

- 2D scene with a static camera. The small bird is bird_B (the crow-like bird flying right). The file rate and question_fps are both 24.
- t = 0.3 s gives frame round(7.2) = 7. The bird is fully visible in frames 6–8.
- Scale from the prior (length = 0.94 m):
  - The x extent of the mask (nose to tail) is 107–110 px depending on the threshold (measure.py). At frame 0 it is 109 px at a threshold of 30 and 107 px at 60; at frame 7 it is 108 px.
  - I used 108 px, which gives 0.94 / 108 = 0.008704 m/px.
- Speed, from template-match shifts in measure.py:
  - frame 6→7: 91.64 px/frame
  - frame 7→8: 91.77 px/frame
  - frames 2→7 average: 91.97 px/frame
  - scene record: constant 91.87 px/frame (backward difference at frame 7 = 2206.8 px/s)
  - I used 91.8 px/frame × 24 = 2203 px/s.
- Speed = 2203 × 0.008704 = 19.2 m/s.
- Check: the velocity is constant from frame 2 to frame 8, and every route above agrees to within 0.4 %. The main uncertainty is the pixel length (107–110 px, about ±1.5 %). That gives a range of 18.8–19.4 m/s.
- Confidence: high.
