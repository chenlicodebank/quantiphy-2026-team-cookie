# q2832 – soccer ball displacement between 1.0 s (f24) and 1.4 s (f34) — answer 0.49 m

File fps = question_fps = 24, so 1.0 s → f24 and 1.4 s → f34.

## Problem
depth_info gives no depth for the soccer ball. It gives depths for the orange basketball (2.3557 m at f12, 1.8100 m at f24),
and for the "white" (3.07 m) and "green" (3.04 m) balls at f24. Those two are the pale ball and the tennis ball held by the
standing person at the back wall, not the soccer ball, which is on the floor beside the seated person at about 2.6 m.
So I placed the soccer ball using the floor plane.

## Method (lab camera f = 0.5959·1280 = 762.8 px, principal point (640, 360))
1. Floor normal from the vertical vanishing point of wall panel seams and the room corner (Hough lines, `vvp.py`):
   tilt 0.8°, roll −0.6°. Check: the basketball's motion between its two given 3D centres lies 0.6° off this plane.
2. Plane height: the basketball centres at f12 and f24 (given depth × pixel ray) are 0.715 m and 0.724 m from the camera
   along the normal. Mean 0.72 m, plus the ball radius about 0.115 m, gives a camera height of about 0.835 m above the floor.
   Re-projecting the basketball onto this plane gives 2.371 / 1.799 m (given: 2.3557 / 1.8100).
3. Soccer ball: the record's centres are biased. In frames 0–23 its cy of about 613 includes the shadow; the true visual
   centre is about 604. So I measured the floor-contact shadow directly below the ball (darkest point of a vertical
   intensity profile, `contact.py`), with x taken as the middle of the blurred left/right edges:
   - f24: (152, 639)
   - f34: (67, 721.5). The shadow there is cut by the image border, so I extrapolated it from f27–33 (quadratic 722,
     linear 718.6) and checked it against top edge 646 + the ball's ~75 px apparent height.
   A rolling ball's contact-point displacement equals its centre displacement, so the soccer ball's size is not needed.
4. Back-projecting both contact points onto the floor plane gives distances of 2.64 m (f24) and 2.20 m (f34), and a
   **displacement of 0.491 m** (`final2.py`).

## Checks / alternatives
- Centre-based route (`final.py`), with visual centres f24 (152, 606.5) and f34 (67, 682) on the plane of ball centres:
  0.495 m. With 5-frame smoothed centres: 0.471 m. With the record's (biased) centres: 0.42 m.
- Sensitivity:
  - ±0.5° tilt or roll: 0.474–0.510 m.
  - ±3 px in contact v: ±0.01 m.
  - Basketball radius 0.11–0.12 m: 0.488–0.494 m.
  - If the given depths are to the ball surface rather than the centre: 0.51 m.
- Prior check: on this plane the basketball's speed around f12, averaged over 5 frames, is 2.14–2.27 m/s
  (prior 2.21 m/s; the steady speed later is about 1.65–1.7 m/s).

## Confidence
Moderate. The likely range is 0.47–0.52 m. The main uncertainty is the soccer ball's depth: no depth was given for it,
so it comes from the floor plane, and at f24 one pixel of vertical position changes the depth by about 1 cm.
