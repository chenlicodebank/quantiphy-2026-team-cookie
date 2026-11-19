# Q442: speed of the box (tool box / crate) at t = 1 s

- The video is 2D at 24 fps; question_fps is also 24, so t = 1 s is frame 24. The only moving object is the tool box, and it slides down the ramp at a constant direction of 28.4° from frame 22 on.
- **Track:** scene/tracks/crate.csv, giving the template-fit centre. I checked it on frame 24 (frames/f24.png), and the centre (775, 649) sits on the box.
- **Scale from the prior:** a = 1.58 m/s² at 1.25 s, which falls inside the steady slide. In fit.py I fitted a quadratic to arc length vs frame over frames 22–44 (rms 0.3 px):
  - a_px = 0.697 px/frame², which is 401 px/s². That gives 1.58 / 401 = 0.00394 m/px.
  - The backward-difference speed from the fit at frame 24 is s(24) − s(23) = 20.42 px/frame, so v = 20.42 × 24 × 0.00394 = **1.93 m/s**.
  - Other fit windows (22–34, 23–38, 28–44, 20–44) give 1.89–2.00 m/s. The raw single-frame step 23→24 is 20.5 px, which gives 1.94 m/s.
- **Second route:** the free-fall phase (frames 0–7) has a constant 4.40 px/frame², which is 2534 px/s². With g = 9.81, the scale is 0.00387 m/px, and v = 20.44 × 24 × 0.00387 = 1.90 m/s. This agrees within 2%, and the two scales agree within 2%, which supports the planar 2D assumption.
- **Answer:** 1.93 m/s. Confidence is high (about ±3%).
