# Q218: speed of the left virus at 1.0 s (frame 24)

The video is a 2D render at 24 fps (file fps and question_fps agree). Prior: the right virus moves at 1.7393 m/s. Both viruses move in straight lines at constant speed, and nothing bounces or collides. So one metres-per-pixel scale applies: answer = prior × (left pixel speed / right pixel speed).

## Main route (scene/ tracks, body-sphere circle-fit centres; measure.py)
- Left (small) virus: linear fit over frames 1–30 gives dx = −14.171 and dy = +0.132 px/frame, so the speed is 14.172 px/frame. The single step at frame 24 is 14.17.
- Right (large) virus: dx = +13.728 and dy = −0.718 px/frame, so the speed is 13.747 px/frame. Its centre is still inside the frame at frame 24.
- Scale = 1.7393 / (13.747 × 24) m/px.
- Left speed = 1.7393 × 14.172 / 13.747 = **1.793 m/s**.

## Second route (check.py)
I took the centroid of each full mask (body plus spikes) over frames 3–22, fitted it linearly, and got a pixel-speed ratio of 1.039, which gives 1.807 m/s. That is 0.8% above the main route. The difference comes from the spikes rotating, which moves the full-mask centroid around. The body-sphere centre is the better stand-in for the object's origin, so I used the main route.

Confidence: high, with an error of about 1%.
