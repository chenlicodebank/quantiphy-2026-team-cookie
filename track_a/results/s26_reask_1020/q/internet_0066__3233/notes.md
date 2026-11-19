# q_3233 – ball velocity at 2.10 s (frame 63, 30 fps; the file is also 30 fps)

**Scene:** a top-down hand-held view of a gym floor. A basketball rolls from right to left across it between frames 49 and 72.

**Prior:** gravity is 9.8 m/s². That motion is not shown: gravity acts along the camera axis, and the ball's apparent size stays constant (±3%), so it is not falling. The ball's pixel acceleration along the path is about 0 (0.1–0.6 px/frame², which is noise). So the prior gives no usable scale.

**Scale:** taken from the regulation basketball (size 7, diameter 0.24 m), as the task rules direct when the prior's motion is absent.
- Ball diameter: 256 px. This is the median vertical, blur-free extent over frames 53–69 (scene/tracks/ball.csv). I checked it by eye on a zoomed frame 63 (`frames/f63.png`): top edge about 310, bottom edge about 568, so about 258 px.
- Scale = 0.24 / 256 = 9.375e-4 m/px.

**Velocity (fit.py, cx_stab/cy_stab):**
- Forward difference from frame 63 to 64: (−90.5, −1.0) px/frame.
- Central difference: −89.5 px/frame.
- Quadratic fits over windows 53–69, 50–71 and 58–68 give vx at frame 63 from −89.6 to −90.0 px/frame, and vy of about +0.9 px/frame.
- Adopted |v| ≈ 90.2 px/frame = 2706 px/s, which gives **2.54 m/s**.

The motion is uniform, so the different windows and methods agree to within about 1%. The main uncertainty is the scale: the true ball size (a size 6 ball, 0.232 m, would give 2.45 m/s) and the ball being a little closer to the camera than the floor.

Confidence: moderate. The pixel speed is solid; the metric scale comes from the assumed ball size.
