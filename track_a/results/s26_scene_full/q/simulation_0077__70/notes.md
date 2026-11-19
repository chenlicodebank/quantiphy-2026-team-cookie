# Q70: speed of the person in the white shirt at 1.0 s (prior: black-shirt person's speed = 1 m/s)

The video is a top-down 2D view with a static camera. Both men walk in straight horizontal lines at the same depth, and their apparent sizes match and stay constant over time. So one m/px scale from the prior applies to both. fps is 24 and question_fps is 24, so t = 1.0 s is frame 24.

Script: `ratio.py`. It reads the torso (shirt-centroid) tracks in scene/tracks. I checked the record's notes and the per-frame steps: walking starts at frame 2, and white's track is clean up to frame 61.

Per-frame torso speeds (px/frame):
- Mean over frames 2–61: black 11.46, white 15.18. Ratio **1.325**.
- Net displacement over frames 1–61: black 11.45, white 15.15. Ratio 1.324.
- Step 23→24 (backward difference at t = 1.0 s): black 11.11, white 14.92. Ratio 1.343.
- Window of frames 21–28: black 11.32, white 14.77. Ratio 1.305.
- Second route, head points (net): black 12.09, white 15.70. Ratio 1.298. The head points are slightly inflated by perspective.

Scale: the prior's "1 m/s" is read as black's walking speed. Black's mean speed is 11.46 px/frame, so 1 m/s corresponds to 11.46 px/frame.

How to read the prior changes the result:
- If the prior is black's mean speed: white at frame 24 is 14.92 / 11.46 = 1.30 m/s.
- If the prior is black's speed at the same frame: white is 1.343 m/s.
- Using the mean ratio: 1.325 m/s.

Answer: **1.32 m/s**. All readings fall within about 2% of this. Confidence is good.
