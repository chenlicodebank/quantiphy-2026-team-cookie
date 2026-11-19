# Q2839 – velocity of the green ball at 1.5 s (captured_0054a, lab, 24 fps; file fps = question fps = 24)

**Answer: 3.6 m/s.** Confidence is low to medium. The value depends heavily on the reference's smoothing convention, as explained below.

## Identification
- Green ball = the yellow-green tennis ball thrown by the standing person (`scene/tracks/yellow_ball.csv`). Its depth at t=1.0 (f24),
  3.039 m, fits the throw position at the back wall. The "white ball" (3.07 m) is the pale ball thrown with it.
- t = 1.5 s means frame 36. At f36 the ball is a vertical blur streak just before it hits the floor. The contact falls between f36 and f37, so f37 is already the bounce.

## Key observations
- **Frames are dropped:** the step from f35 to f36 is 2.5x the expected step for both thrown balls (yellow 47 → 132 px, then 46).
  The basketball has the same kind of jump at f11→12 (16 → 33 px), which I checked by eye on zoomed crops (`frames/bb.png`).
  The container timestamps are uniform, so the frames were lost at capture.
- The prior (orange ball 2.21 m/s at f12) can only be reproduced if this jump is kept as it is with frames spaced 1/24 s apart.
  Without the jump, the physical basketball speed is about 1.65–1.9 m/s. So the reference uses frame indices and does not correct for dropped frames.

## Method
1. `floor.py`: the basketball rolls on the floor. I back-projected its centre at f12 (2.3557 m) and f24 (1.8100 m) to get the floor plane:
   pitch 2.9°, camera about 0.90 m above the floor. Then I computed basketball depths per frame on that plane and checked the prior under several conventions.
2. `fit_bounce.py`: 3D ballistic fit of the green ball with gravity 9.81 along the floor normal. Inputs: range fixed to 3.039 m at f24,
   a free time-gap parameter at f35→36, and a floor bounce on the calibrated plane (ball radius 3.3 cm) with a free velocity after the bounce.
   Frames 23–44, with streak centres re-measured by `streak.py`. Result: RMS 3.6 px, gap 0.64 frame, physical speed 4.88 m/s at f36 (5.1 m/s at contact).
3. `conventions.py` / `conventions2.py`: observed pixel centres back-projected with the fitted ranges, then the paper's velocity under the
   smoothing conventions that reproduce the basketball prior within about 7%:
   - smoothing the velocity vector or the positions (MA5, SG5, SG7, Gaussian): 2.75–3.6 m/s, about 3.45 m/s for the centred 4-frame vector difference.
     These are lower because the bounce reverses the vertical velocity inside the window.
   - smoothing the scalar speed (MA5 = 4.37, SG5 = 4.81 m/s). These are higher because the dropped-frame jump inflates them.
   - for the basketball, |P14−P10|/4 gives −1%, SG5 gives +3%, MA5 gives −6.5%. The prior cannot tell these conventions apart.
4. Second route: depth from the ball's apparent width (constant fitted on f23–32, which implies 3.05 m at f24, consistent with the given 3.039 m). It is too noisy near the bounce (scatter ±10%) to settle the value.

## Choice
I chose 3.6 m/s, near the middle of the plausible spread (2.75–4.9). It matches SG5-smoothed velocity (3.59) and the 4-frame central
difference (3.45), and is about 25% below the physical speed before the bounce (4.88 m/s).
