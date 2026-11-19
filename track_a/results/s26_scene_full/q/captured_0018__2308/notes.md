# q_2308 — distance box ↔ tennis ball at 3.0 s (captured_0018)

**Problem:** the clip is 49 frames long (0–2.04 s at 24 fps; the file rate matches question_fps). 3.0 s would be frame 72,
which is past the end. So I used the end state: by frame 39 the white box has landed. It tips onto its side and
lies still at frames 47–48, centre (423, 593.5) px, 29 px tall and 57 px long. The tennis ball bounces straight up
and down at x≈750 (floor contact at frame 36: bottom y≈615). At 3.0 s it is most likely on or near the floor at that
spot. Frame 48 shows it in the air (centre y 444). That is a worst case and gives 105 cm.

Camera: f = 0.5959·1280 = 763 px, principal point (640, 360). The horizon is at y = 342, so the camera is tilted
down 1.35°.

## Route 1: floor plane (geom.py)
- The soccer ball centre is 2.8 m away (depth_info). At floor contact (frame 39, centre 534.5, 541) its radius is
  2.8·22/763 = 8.1 cm. That puts the camera 0.785 m above the floor.
- Tennis ball on the floor at (750, bottom 615), solved together with its apparent diameter of 24 px: centre
  (0.316, 0.749, 2.171) m, radius 3.6 cm (a real tennis ball has a radius of about 3.3 cm).
- Box lying on its side: centre (−0.638, 0.739, 2.224) m. Size 18 × 9 cm.
- Distance = **95.5 cm**. Using the blurred frame-36 centre gives 95.7 cm.

## Route 2: gravity prior (gfit.py)
- Quadratic fits to the free fall before the probable dropped frame between 35 and 36 give the depth as
  Z = g·f / a_px:
  - tennis ball: 2.26–2.34 m
  - box: 2.36–2.40 m
  - soccer ball: noisy, 3.4–3.6 m, against the given 2.8 m
- Back-projecting the resting pixels at these depths gives a distance of **≈101 cm**.

## Cross-check
The far person's feet, at the floor height from Route 1, come out at 2.85 m. The given 3.13 m is to the body centre,
which suggests the camera may be somewhat higher than 0.785 m. That would make the answer larger, which agrees with
Route 2.

**Answer:** 98 cm, a blend of the two routes (95.5 and 101).

**Confidence:** moderate. The main uncertainties are where the ball is at 3.0 s, since that frame is not in the
video, and the camera height.
