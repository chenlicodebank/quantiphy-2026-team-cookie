# q3039: acceleration of the swimming woman, 0 s to 5.20 s

**Answer: 0.014 m/s²** (magnitude; low confidence)

## Setup
- Overhead drone shot with a nearly static camera. I subtracted the drift with the `*_camcomp` columns in scene/.
- Time base: question_fps is 24, so 5.20 s is frame 125. The file runs at 22.52 fps.
- Scale: the woman's height of 1.63 m corresponds to her head-to-toe length in a stretched glide frame. I checked this on f123 (frames/f123.png): toes at x≈1720, top of head at x≈2445, so about 720 px. This agrees with C1's 715 px. Scale = 1.63/715 to 1.63/720 ≈ 0.00227 m/px.

## Where the candidates part ways
- C1 (0.012) took the difference between the hip velocities at f0 and f125, divided by 5.2 s, and got a positive value.
- C2 (0.017) fitted a quadratic to the SAM whole-body track over f0–125 and got a deceleration.
- The physical cycle-averaged speed is constant at about 7.3 px/frame (about 0.4 m/s). The true average acceleration is therefore close to zero, and any answer is a small, noisy number.

## My measurement (routes.py, scene tracks, f0–125, 24 fps)
**Velocity difference, v(125) − v(0):** this depends strongly on the reference point and the window. It ranges from −0.14 to +0.04 m/s², so it is dominated by noise and stroke phase.

**Quadratic fit of x(t) over f0–125:** this is more stable.

| Reference point | Fitted acceleration |
|---|---|
| visible-mask centroid | −0.0156 m/s² |
| head (hair) | −0.0116 m/s² |
| trunk | +0.004 m/s² |
| C2's SAM track | −0.016 m/s² |
| C1's hip velocity difference | +0.012 m/s² |

## Choice
- Most routes give a magnitude of about 0.012–0.016 m/s².
- I report 0.014 m/s². Both candidates' scale and time base agree with mine; the remaining spread comes only from the reference point and the noise.
- Confidence is low (roughly ±50%), because the true value is close to zero.
