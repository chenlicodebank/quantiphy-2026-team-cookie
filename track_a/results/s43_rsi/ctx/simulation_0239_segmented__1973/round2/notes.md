# q1973 round 2: width of the house (m). Prior: brown horse speed 0.874 m/s. No depth_info. File fps = question_fps = 24.

## Task
Round 1 proposed switching from the submitted 8.94 (a 0.7/0.3 log blend of C1 8.2 and DeepSeek 10.93) to 8.1. I verified that
proposal with my own code (my_measure.py, my_measure.json, frames/my_overlay.png).

## Crux
Which pixel extent is the width. C2 and C3 used the 805 px full horizontal extent of the cross-gable band. That band is
ridge-level and lies along the longer side. C1 and round 1 used the 618-620 px eave-level y extent, which is the shorter side.

## Measurements (my code, different routes from round 1)
- House mask: median of 5 frames (0, 12, 24, 36, 48).
  - Main eave columns x 662 / 1361, so the x extent is 699 px.
  - Eave corner rows read directly at the eave columns: 96 / 714, so the y extent is 618.0 px. The rake-line fit gives
    618.1 px.
  - Ridge apexes at y 22.3 / 744.2, so the ridge/eave ratio is 1.168 and the nadir is at row 538.4. That is a top-down
    camera, the same as round 1 found.
  - The cross-gable band spans 805 px (x 618-1423) at its ridge row y=380. At y=270 and y=520 its edges are flush with the
    main eaves (661/1362). So the 805 px is the radially pushed-out ridge level, not the footprint.
- Brown horse pixel speed, frames 0-48 (frame 49 is a reset):
  - Texture template matching over one gait cycle (20-frame spans, body-only template): median 2.657 px/frame. This is a
    new route.
  - Mask centroid linear fit: 2.665. Nose-edge fit: 2.636.
  - Adopted 2.65 px/frame = 63.6 px/s, so the scale is 0.013742 m/px at the horse's body level.
- Uncorrected width: 618 × 0.013742 = 8.49 m.
- Depth correction: the eaves sit higher than the horse's silhouette, by about 1.5 m for a single-storey eave. The roof pitch
  satisfies tan = f/2431 px. A pitch of 35/40/45° gives f = 1700/2040/2430 and a horse depth of 23.4/28.0/33.4 m, so
  k = 0.936/0.946/0.955 and W = 7.95/8.03/8.11. Central value: **8.05 m**.
  - If the house were two-storey (eave about 5.5 m), W would be about 7.0-7.5. There is no evidence for that, and C1 and round 1
    assumed a single storey too. This is the main remaining unknown.

## Rechecks
a. Closure: the three independent speed routes (template 2.657, centroid 2.665, nose 2.636) give 0.876 / 0.879 / 0.869 m/s
   at the adopted scale, within 0.6% of 0.874.
b. Plausibility:
   - Brown horse: 148 px long gives 2.03 m, and about 40 px wide gives 0.55 m. Both are realistic.
   - Cream animal: 176 px gives 2.4 m (a cow-sized animal).
   - House footprint: about 8.0 × 9.0 m, with a ridge 3-5 m above the eaves. Plausible.
c. Units: metres. Frames are counted at 24 fps, which equals the file rate.
d. Fault proof:
   - C2 and C3 (10.96 / 10.9) take 800-805 px = x 618-1423. I measured that extent only at the cross-gable ridge row y=380.
     At eave level the same band is 661-1362 = 699-701 px. So their pixel extent is inflated about 1.15× by ridge height,
     and it is also the longer side, which is the length by convention (read as length it would be about 9.0-9.2 m).
   - The submitted 8.94 carries 30% weight from that faulty value.
   - C1 (8.2) and round 1 (8.1) agree with my value within 2%.

## Decision
Switch, verified: the round-1 fault is reproduced, and my own value of 8.05 agrees with round 1's 8.1 within 1% (C1's route).
Other reading: if "width" were the x extent, the answer would be about 9.0-9.2. By convention width is the shorter
horizontal side, so the answer is 8.05. Confidence: medium. The eave height and focal length cannot be measured, which
leaves about ±2-3% (more if the house is two-storey).
