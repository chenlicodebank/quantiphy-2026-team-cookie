# Context of question 1314 (organised record; every round adds to it)

## Question
- Text: What is the height of the traffic light in meters?
- Its own prior: acceleration of the white car = 4m/s^2
- Its own depth_info: t=0.58s, distance_human_camera = 38.3473m
t=1.58s, distance_human_camera = 38.7220m
t=0.58s, distance_yellow_car_camera = 35.5258m
t=1.58s, distance_yellow_car_camera = 33.0077m
t=0.58s, distance_white_car_camera = 38.1362m
t=1.58s, distance_white_car_camera = 34.0492m
t=0.58s, distance_bike_camera = 33.9976m
t=1.58s, distance_bike_camera = 28.6807m
- question_fps: 24
- Video: simulation_0064.mp4 (simulation, A3MC)

## The answer currently submitted
4.435 - a fixed-rule blend exp(0.7 ln A + 0.3 ln B) of the Claude line's answer A = 4.97 and an earlier DeepSeek median B = 3.4; the rule blends every row of its population where the two differ by less than about 50 pct, so it is no judgement about this question.

## Answers so far (each from a separate session that saw only this question, its video, prior and depth_info)

| name | who | answer | x submitted |
|---|---|---|---|
| C1 | Claude Opus 5.5 (Claude Code agent), 26_30 per-question run | 4.97 | 1.121 |
| C2 | Claude Opus 5.5 (Claude Code agent), 30_x adjudication, 30_12 D3 adjudication, rows left by 30_11 | 5.05 | 1.139 |
| C3 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r1 | 3.4 | 0.767 |
| C4 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r2 | 3.85 | 0.868 |
| C5 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r3 | 2.9 | 0.654 |

DeepSeek median over its 3 runs: 3.4.

Each candidate's notes.md and scripts are in context/<name>/.

## Investigation rounds

### Round 1 (harness v2; files in context/round1/)
- Answer: 4.97 (switch, confidence medium, follows C1)
- Where the answers part: top point (warning-sign apex vs signal-head top) and camera geometry (f/camera height consistent with the poles' vertical vanishing point vs object-size focal guesses)
- Fault proven: DeepSeek input (C3 3.4) uses f=2727 px that makes the van 1.55 m wide and the pedestrian 1.41 m tall, a camera height inconsistent with the vertical vanishing point, and stops at the signal head instead of the sign on top of the same asset; even head-only the correct geometry gives about 4.2 m
- Closure on the prior: 0.3 pct

# Round 1 addendum (q1314, traffic-light height)

## Established
- **Object:** four identical signal assets: pole, 3-lamp head, pedestrian box, and a triangular crossing sign on top. Near-left: base row 571.0, sign apex 65.1, head top ≈150. Near-right: base 565.4, apex ≈64.
- **Vertical VP** from sub-pixel pole-axis fits (rms ≤0.46 px): (1069, 7743).
- **Camera:**
  - f = 2110–2182 px (from the horizon at −121 off the curb VP, and independently from the van paint width at f14 and f38), pitch 16.3–16.9°.
  - Camera height 6.2–6.7 m from the pedestrian pelvis depth (f38) and the cyclist depth (f14). The two agree within 0.1 m.
- **Light height** (base to sign apex): 4.95–5.04 m on both near lights. Over f = 2110–2727, with the VP kept, it stays at 4.95–5.17 m.
- **Closure:** the van's acceleration from width-derived distances (tied to depth_info) is 3.99 m/s² over f2–62, against the prior of 4 (3.77–3.87 in other windows).
- **Plausibility:** pedestrian 1.69–1.74 m, van width 1.94–2.01 m.

## Ruled out
- f ≈ 2700–3000 px (C3, C4, C5): it gives a van 1.55 m wide and a pedestrian 1.41 m tall.
- Camera heights that ignore the vertical VP.
- 3.4 / 2.9 m: even the head-only reading gives 4.16–4.35 m with the correct geometry.

## Decision
Switch to C1, **4.97 m**. The submitted 4.435 is a blend whose second input (3.4) carries the faults above.

## Open
- Reading only: whether the reference AABB includes the sign. It is part of the identical asset on all four corners, so it most likely does. Head-only would give about 4.2 m.
- The right sign's apex row (≈64) has low contrast against the awning, but it agrees with the left apex to within 0.01 m in height.

### Round 3 (harness v3; files in context/round3/)
- Answer: 4.97 (switch, confidence high, follows C1)
- Where the answers part: camera geometry (f/pitch and camera height) plus top point (sign apex vs signal-head top); light height = ratio(horizon, vertical VP) x camera height
- Fault proven: DeepSeek inputs (C3 3.4 in the blend) use f~2727 which with the measured pole VP puts the horizon at y~-477 against the curb VP at -122, and stop at the head top; correct geometry gives 4.99-5.00 (head-only 4.20)
- Closure on the prior: 1.5 pct

# Round 2 addendum (q1314, traffic-light height)

## Established (own code: curbs.py, poles.py, scan.py, checks.py)
- **Horizon:** the street VP from sub-pixel fits of the two long near curb edges is (1084, −122), rms 0.4–0.9 px. This confirms the record's −121.
- **Vertical VP:** yv = 7850 ± 50 (7877 at f0/f14, 7794 at f60). f ≈ 2200 at yh −122; f = 2120–2146 at yh −75 to −90.
- **Light height:** 4.99–5.00 m on both near lights, base to sign apex. The camera height comes from five depth routes (pedestrian f38; cyclist f14 and f38; van f14 and f38): 6.2–6.9 m depending on the horizon. The ratio light/Hc is 0.80–0.75 over yh −75 to −122. The product is stable: 4.99 at yh −75 and −90, 5.00 at −122, about 4.9–5.1 at −60 and −190.
- **Prior-only Hc route (new):** the van's ground track fitted with a = 4 from rest at f1. It agrees with the depth routes at yh ≈ −60 to −90.
- **Closure:** a = 3.94 at yh −75 and 3.84 at −90.
- **Plausibility:** pedestrian 1.68–1.75 m, van paint width 1.91–2.03 m.
- **Head-top-only reading:** 4.20 m.

## Ruled out
- f ≈ 2700+ (DeepSeek runs): with the pole VP it implies a horizon at about −477, which contradicts the curb VP.
- 3.4 / 3.85 / 2.9: wrong geometry and the head-top reading.

## Decision
Round 1's switch to C1 (4.97) is verified; my own value is 4.99–5.00.

## Open
- Only the reading: whether the reference AABB includes the crossing sign on top (5.0) or not (4.2). The sign is part of the identical asset on every corner, so including it is the most likely reading.
