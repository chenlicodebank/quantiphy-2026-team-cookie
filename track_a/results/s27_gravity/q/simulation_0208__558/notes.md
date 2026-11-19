# q558: typewriter speed at t=0.125 s
2D scene, 24 fps (file and question_fps), so t=0.125 s is frame 3. Speed = (y3 - y2) * fps, the one-frame backward difference.
Scale comes from the prior: free-fall acceleration of 9.8 m/s^2 before 0.45 s (frames 0-10 are airborne).
- Pixel acceleration: quadratic fits to the scene track (bbox centre, mask centroid) over frames 0-6/0-7 give 12.0-12.3 px/frame^2.
  The second differences of the mask centroid over frames 1-5 are 11.7, 12.25, 11.7, 12.2, 12.3, about 12.05 px/frame^2.
  From frame 7 on, motion blur inflates the values, so those frames are not used.
- Pixel displacement from frame 2 to 3: 32.0 (bbox centre), 32.17 (centroid), 31 (top edge), 33 (bottom edge), about 32.1 px.
- Scale: 9.8 / (12.05*576) m/px. Speed = 9.8*32.1/(12.05*24) = 1.088 m/s.
- Check: fitted v3 and raw v3 agree to within 1 pct. Across the reference points and fit windows the result spans 1.04-1.10 m/s.
- Also consistent with release near frame -0.15: 2.65 frames * 12.05 = 31.9 px/frame.
- Template matching was tried as a second route but failed: the object rotates, so it is not used.
Answer 1.08 m/s. Confidence: good, about +-4 pct.
