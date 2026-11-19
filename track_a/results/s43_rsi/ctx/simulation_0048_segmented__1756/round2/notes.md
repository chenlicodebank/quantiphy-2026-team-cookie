# q1756: bicycle height (handlebar to ground under the wheel), round 2

The file fps and question_fps are both 33, so t=1 s is frame 33 and t=2 s is frame 66.

**Answer: 0.93 m.** This verifies round 1's proposed switch (0.95) away from the blend (1.193). My own value agrees with round 1's within 2%.

## Crux
The sessions part over the bike's scale:
- **C1-C3:** use the given bike depth of 16.49 m, which gives a 1.55x giant rider and bike.
- **C4/C5 and round 1:** use the common ground with the 1.8 m walker.

Within the common-ground reading, a second, smaller point separates the values: the handlebar's setback behind the front-wheel contact. C4/C5 leave it out (1.01); round 1 includes it (0.95).

## Measurements (my own code)
- **`measure.py`: per-frame masks.** These are the non-white pixels minus the frame-0 kiosk mask.
  - At frame 33 (overlay `frames/overlay33.png`): walker rows 251-450; cyclist head top 328; front-wheel bottom 559.5.
  - Handlebar: grips (bar ends at the hands) at 425.5 and stem at 433, read on a 6x zoom (`frames/cyc_33.png`). These match C1-C5.
- **`solve.py` / `setback.py`: size against contact row.**
  - Walker: h = 0.3788·y1 + 28.1 (frames 0-98).
  - Cyclist, head to wheel: h = 0.3780·y1 + 20.9 (frames 0-59).
  - The two lines are the same, so the rider-plus-bike height on the walker's ground is 1.741 m with an SD of only 0.010 m over 60 frames. This reproduces round 1's 1.74.
- **Given-depth reading:** the factor is 16.49 / 10.6 = 1.556, which makes the rider plus bike 2.71 m tall while seated. This reproduces round 1's fault.
- **Handlebar height on the common ground, by two routes:**
  1. **Image-only route (`setback.py`).** The handlebar's ground foot is the point the front contact passed k/v earlier. The speed v = 3.2 m/s comes from the rider's size change with f = 1181-1205 and motion along the viewing ray (image x stays constant). The px/m scale at that row comes from the walker line; the cyclist line gives the same.
     - Grips at frames 20, 33, 45 and 55 give 1.02 at k=0 and 0.93-0.96 at k=0.2, steady across frames.
     - At frame 33: grips with k = 0.2 / 0.3 / 0.35 give 0.948 / 0.914 / 0.897; the stem with k = 0.2 gives 0.891.
     - Typical bike geometry (head angle about 70°, trail, stem, swept grips) puts k at about 0.2 m for the stem and 0.3 m for the grips, so this route gives about **0.91-0.95**.
  2. **Round 1's 3D route (`h2_handlebar.py`), read and checked.** This route puts the ground descending 6-9° toward the camera, so the bbox height is measured from the lower front contact. That adds k·tan(slope), about +0.04 m, and gives **0.92-0.96**.
     - The whole difference between the routes is whether the ground really slopes. The kiosk and walker evidence on this conflicts (`geom.py`):
       - The walker's feet at its given depths lie on a level plane at a pitch of about 13°.
       - The walker's body-size line and the cyclist's line need a horizon near row -60 instead.
     - So I take the middle of the two routes: **0.93 ± 0.03**.
- **Pure ratio with no setback (C4/C5's method):** 134 px / 133.4 px per m = 1.00-1.02. This overestimates, because the grips sit behind the contact and so appear higher in the image.
- **`geom.py`, level ground fitted to the walker's feet at the given depths:** under it the cyclist's size drifts from 1.65 m to 1.39 m over frames 20-55. So the cyclist does not fit a level plane through the walker's given-depth feet; this is the same inconsistency described above.

## Rechecks
- **a. Closure:**
  - Kiosk camera (f = 1181, pitch 11°) with the walker's given depths and bbox: walker height 1.841 / 1.789 m at t = 1 / 2 s, mean 1.815, which is 0.8% off the prior.
  - Size-derived walker distance against the given distance: 12.2 vs 11.93 m (2.3%) and 10.75 vs 10.82 m (0.6%).
- **b. Plausibility at my scale:**
  - Rider plus bike, seated: 1.74 m. Bike speed: 3.2 m/s. Walker: about 1.1 m/s. Handlebar: 0.93 m. All are realistic.
  - At the given-depth scale: a 2.71 m seated rider (about 3 m standing), a handlebar of 1.42-1.55 m and a wheel about 1 m across. These fail the adult-size hard check by far more than 40%.
- **c. Units and time base:** the answer is in metres. t=1 is frame 33 (question_fps = file fps = 33). The scene/ track frames match.
- **d. Fault proof:**
  - **C1, C2, C3 (1.41 / 1.49 / 1.55):** they applied the given bike distance, which makes a 2.71 m seated rider (my measurement: 1.741 × 1.556).
    - The harness hard check says to take the scale from the standard object in that case.
    - The given depth's ratio (1.383) does match the rider's apparent growth. So the given depth is image-equivalent to a 1.556x scaled copy and cannot be refuted from the pixels alone. It fails only the real-world-scale convention.
  - **C4, C5 (1.01):** they treated the handlebar as directly above the front contact. A setback of k = 0.2-0.3 m lowers the value by 5-10% (table above).
  - **Submitted 1.193:** a fixed-rule blend of the two readings. Under the common-ground reading it is 28% high.

## Decision
I switch to the common-ground reading, confirming round 1, with my own value of **0.93 m**. Confidence is medium. If the Blender scene really holds a 1.556x cyclist on a lower parallel plane, the reference would be about 1.45 m. The image cannot rule that out; only the real-world-scale hard check rules it out.
