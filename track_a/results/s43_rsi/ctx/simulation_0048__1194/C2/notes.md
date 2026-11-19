# Q1194: height of the moving bicycle (handlebar top to ground), in metres

**Answer: 0.97 m.** Likely range 0.92–1.01 m.

The file and the question both run at 33 fps, so t = 1 s is frame 33 and t = 2 s is frame 66.

## Where the earlier answers part ways
- **C1 (1.49 m)** took the camera from the walker's given depth (f ≈ 1185) and the bike's given depth of 16.49 m at face value. Its own notes record what that implies:
  - the cyclist's ground lies 2.6–2.9 m below the sidewalk;
  - the cyclist is 1.6× the walker's size, so the rider's head would be at about 2.5–2.7 m;
  - the street would have to slope at about 14.5° (the fixed vanishing point at y = −177).

  The frames show a normal curb between the road and the sidewalk, with the rider beside the walker at about the same size. By the realism rules this geometry is wrong.
- **C2 (1.0 m)** used the walker's ground plane, which does not depend on the focal length. Two of its steps are off:
  - its horizon (−165, from its fit) differs from what the scale growth gives (about −93);
  - its curb correction goes the wrong way: a lower road makes the bike larger, not smaller.

  Its value happens to land close to mine.

## My measurements
- **Handlebar top (grip ends) and front-tyre contact**, read on 5–6× gridded crops (`crops.py`, `bar_meas.json`):

  | frame | top (y) | contact (y) | height (px) |
  |---|---|---|---|
  | 0 | 312 | 416.5 | 104.5 |
  | 20 | 374.5 | 492.5 | 118 |
  | 33 | 424 | 560 | 136 |
  | 56 | 552 | 727 | 175 |
  | 60 | 579 | 761 | 182 |

- **Street vanishing point.** It is ill-conditioned from line directions alone, because the paths are almost vertical in the image. I took it from the rider's scale growth instead:
  - template scale of the head and shoulders, relative to frame 33: 0.784 (f0), 1.292 (f60), 1.412 (f66) (`scale_track.py`);
  - for straight-line motion, scale ∝ |p − V|. This gives V ≈ (1777, −93), with a range of −61 to −98 over frame subsets (`vp_from_scale.py`).
- **Camera.**
  - The vertical vanishing point is (958, 8620).
  - I assumed a level ground, so the street vanishing point lies on the horizon. Then f² = (cy − Vy)(VVy − cy), which gives f ≈ 1980 and a pitch of about 13.5°.
  - The camera height comes from the 1.8 m walker's head and foot keyframes: 4.75 m, fit rms 1.4 px (`level.py`).
  - A level street with this vanishing point fits better than the 14.5° slope needed with f = 1185.

## Consistency checks (World B: f ≈ 1980, level ground)
- **Bike depth (independent of the walker).** The predicted distance to the bike origin at t = 1 s is 16.0–16.7 m, against 16.49 m given. The scale from the bike's depth matches the scale from the walker within 0.5–1.2 % (`rider_check.py`).
- **Bike depth ratio.** The rider's scale ratio from t = 1 to t = 2 s is 1.41, against 1.38 from the given depths.
- **Rider.** The head top comes out 1.60–1.69 m above the road, which is plausible for a seated adult.
- **Walker.** Only the walker's given depth (11.93 m, against about 18.3 m in this model) does not fit. Its 1 s change of 1.11 m does match the model's 1.12–1.2 m, so its origin seems offset from the body. That is why C1's f = 1185 is wrong.

## Bike height
The handlebar top sits a distance r_back behind the front contact, on the far side from the camera. I modelled it as a point at height H above the road, r_back further along the street than the front contact (`final.py`).
- **r_back.** Typical bike geometry puts it at 0.3–0.45 m for swept-back grips; I used about 0.35 m. A free fit of r_back is ill-conditioned.
- **Results at V = −93:**
  - H = 0.979 m at r_back = 0.3;
  - H = 0.953 m at r_back = 0.4;
  - H = 0.940 m at r_back = 0.45.
- **Spread.** The frame-to-frame spread is ±2 %.
- **Corrections.**
  - Using the bike-depth scale instead adds 0.5–1 %.
  - Treating the walker's 1.8 m as rest height rather than walking height subtracts up to 2 %.
- **Spread across the vanishing-point range (−110 to −75):** under 1 %.
- **Final:** H ≈ 0.97 m.

## Conclusion
I agree with C2's approach, a real-scale bike on the same ground as the 1.8 m walker, giving about 1.0 m. My value is 0.97. I reject C1's 1.49 m: it implies a 2.5 m rider and a road 2.7 m below the sidewalk.

**Confidence: moderate.** The main uncertainties are r_back (±3 %) and the vanishing point and focal length (±1 %).
