# q_2491: maximum height of the ping pong ball (cm)

The file rate and question_fps are both 24. depth_info gives 1.557 m at t=1.1 (frame 26, the first bounce on the table) and 1.4115 m at t=1.3 (frame 31, the apex). I read "max height" as the rebound apex above the table bounce point, measured centre to centre.

## Method (measure.py, fit.py)
- I re-segmented the ball in frames 20–36 with a mask of white, low-saturation pixels. The overlays are in frames/c*.png. The scene/ track is consistent with my results.
- The descent arc (frames 22–25, centroid at mid-exposure) and the ascent arc (frames 27–35) are each fitted with a parabola in v.
  - Bounce at frame 26.21 with the centre at v = 421.1. This is consistent with the frame-26 streak bottom at 429 minus the ball radius of about 11 px, which gives about 418.
  - Apex at frame 31.87, v = 301.6.
  - The rise is 119.5 px.
- I back-projected each point with f = 763 and principal point (640, 360), using the given depths: the bounce point at 1.557 m and the apex at 1.4115 m.
  - Fitted centres: dY = 22.99 cm, dZ = 14.6 cm, 3D distance 27.3 cm.
  - Contact centre (738, 418) and the frame-31 centroid: dY = 21.8 cm. With the frame-32 centroid: 22.5 cm.
- Camera pitch from the table trapezoid: the back edge is 283 px wide and the front edge 500 px. This gives a pitch of about 1.5° downward, so the world vertical is close to the camera Y axis (+0.4 cm correction).

## Checks
- Pixel route with a single depth for both points: 22.1 cm (1.4115 m) and 24.4 cm (1.557 m).
- Ball size: the ball is about 22–23 px wide at the apex, which gives a depth of about 1.35 m. That is consistent with the given 1.41 m and would give about 21 cm.
- Physics: the rise time of 0.236 s gives g·t²/2 = 27 cm. The pixel acceleration likewise implies a larger scale. The depth data contradict this, so I did not use it. I answer with the depth_info-based vertical rise.

Answer: **23 cm**. Confidence is moderate: the readings range from 22 cm (vertical, depth-based) to 27 cm (3D distance or physics).
