# q_1715: average speed of the green car (m/s)

## Key fact: the green car is not in this video
- The segmented clip shows only the basketball player and the ball. scan.py checks every frame for green or orange pixels and finds none, and nothing occludes the player or ball between frames 55 and 127.
- So the green car's speed cannot be measured from pixels. It must be inferred from depth_info: 4.3204 m at t=2.5 and 6.9142 m at t=3.
- File fps = question fps = 30.

## Constraints
- **Radial rate:** (6.9142 - 4.3204)/0.5 = 5.19 m/s. This is a hard lower bound on the speed if the car moves at constant speed in a straight line.
- **Constant-speed line:** r^2 = d0^2 + v^2 (t - t0)^2, with t0 = 2.75 - 29.14/v^2. A wide range of v fits, so the depths alone do not settle the speed.

## Orange car (measured, used as an analogue)
- The orange car passes in front of the player and hides the player's legs in frames 42-53. The hidden edge rises from y 770 to 690 and falls back, which is the car's side profile (legs.py, edge.py).
- Its depths are 10.1755 m at t=1.5 and 10.4022 m at t=2.
- Assumptions: the camera axis is perpendicular to its road, and the camera focal length is f ~ 2018 px, taken from a 0.24 m ball that measures 35.1 px at 13.8 m.
- Result: it moves right to left at about 10.5 m/s, with its closest approach (9.9 m) at t ~ 1.70 s.
- Cross-check: 10.5 m/s x 0.42 s of occlusion = 4.4 m, a normal car length.

## Inference for the green car
**Scenario A: parallel lane (favoured).** The green car drives parallel to the orange car, in a nearer lane, at a similar speed (~10-11 m/s).
- Its closest approach is then ~4.3 m at t ~ 2.48. This fits the data on its own terms, because v = 10.8 gives the largest possible d0, exactly 4.32 m at t = 2.5.
- At that distance its roof would sit at about y 909 in the image (scaled from the orange roof at y 690 and 10.5 m), below the player's feet. So the missing occlusion is consistent with this scenario.

**Scenario B: driving away.** The green car drives away from the camera with a sideways offset, at about 5.2-7 m/s.

**Answer:** a hedge weighted toward scenario A, **9.0 m/s**.

## Ball (for the record)
- The ball's image-plane acceleration is only ~150 px/s^2 (x and y). That is inconsistent with 9.8 m/s^2 at 13.8 m for any focal length allowed for these clips (8-100 deg field of view), so the gravity prior gives no usable scale here.

## Confidence
Low. The asked-for object is absent from this clip. Plausible answers range from about 5.2 m/s (driving away) to about 11 m/s (passing in a parallel lane).
