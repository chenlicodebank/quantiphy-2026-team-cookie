# q1486: dragon body length (m), round 2

The file is 24 fps and question_fps is 24, so frame = round(t*24). Depths: 5.2108 m at frame 24 and 6.3261 m at frame 48.
The principal point is (1439.5, 719.5).

## Task this round
Verify round 1's proposed new value of 0.87 m. Its basis was glide-phase structure from known translation, which puts the tail
tip about 0.5 m nearer the camera than the head and gives a head→tail chord of about 0.74 m.

## Crux
The answers part at the 3D orientation of the head→tail axis in the glide (frames 52-71):
- **Along the flight axis w** (C1, C2, about 26° from the line of sight): the depth spread is about 0.9 m, which gives about 1.0 m plus the snout.
- **Tilted about 15° off w** (round 1): the depth spread is about 0.5 m, which gives a chord of about 0.74 m.
- **Planar** (DeepSeek): no depth spread.

## Measurements (my code: geom.py, lk_glide.py, tri.py, lower.py, closure.py, crops.py)
1. **Focal length** (`geom.py`). I fit a constant-velocity line with hard constraints (|V| = 1.29/24 m per frame, |P24| = 5.2108,
   |P48| = 6.3261) and scanned f.
   - The rms minimum is at f ≈ 3500 (2-71), 3500-3700 (8-64, 24-71) and 3500 (48-71, rms 6.9 px).
   - f = 4500 is clearly worse: rms 24 px against 7 px in the glide.
2. **Hand marks of the tail tip** (4x crops): (1373, 569) at frame 52, (1276, 507) at 60, (1232, 478) at 64 and (1158, 436) at 71. They match round 1's marks to within about 4 px.
   - I tracked the head highlight, hip and left foot with my own pyramidal Lucas-Kanade tracker, frame to frame, with forward-backward errors under 0.3 px.
   - The tail and knee points were lost by LK and were not used.
3. **Triangulation from known translation** (`tri.py`), head_spot→tail tip chord:
   - Window 2-71: 0.68 m at f 3300, 0.74 at 3450, 0.78 at 3550, 0.82 at 3650.
   - Window 48-71: 0.76-0.87 m.
   - The tail tip is 0.5 m nearer the camera than the head, and the head→tail vector is 13-15° from -w. **This reproduces round 1**: 0.72-0.74 m, 0.50 m, 15°.
   - **Caveat:** the same method on other LK points is noisy. The hip lands 0.6-0.9 m behind the root line, and horn vs head_spot differ by
     0.8 m (the horn track slid onto the wing root). Per-point depth is good only to a few tenths of a metre.
4. **Perspective-shrink test** (the same data, the decisive quantity made explicit). Rigid translation shrinks a vector between two points at
   equal depth by the root-depth ratio Z52/Z71 = 0.882. Measured ratios, frame 52 to 71:
   - head_spot→foot_L (rigid, roughly equal depth): 135 → 119 px, ratio **0.881**, as predicted.
   - head_spot→tail tip: 273 → 223 px, ratio **0.817**.
   - Predicted for a body along w (depth spread about 0.9 m, C1's 1.04 m chord): 205 px. Predicted for a 0.74 m chord tilted
     15° (depth spread 0.5 m): 221 px. The measured 223 px fits round 1's geometry; the along-axis geometry misses by 18 px,
     far above the ±3 px mark error.
   - Only a monotonic tail motion of about 4 cm during the glide could mimic it. The image direction of the head→tail vector stays at 41-42°, so there is no sign of a swing.
5. **Independent frame, frame 0** (flapping; the axis is 43° from the line of sight, so droop bias is small, about 7%) (`lower.py`).
   - Visible head front (1995, 895) to tail tip (2442, 1219) = 552 px at root depth 4.20 m.
   - With both points at root depth, L ≥ 0.62-0.63 m. With the body along w, L = 0.82-0.83 m; less the droop bias, about 0.77 m.
   - C1's and C2's own frame-0 values (tail 0.58-0.59 + head 0.21-0.25 = 0.80-0.83) agree.
6. **Snout.** It points away from the camera in every frame and is hidden. Back of head to snout tip is about 0.10 ± 0.04 m (round 1's estimate).
   A curved tail's arc is a few pct longer than its chord.

**Result:** head→tail 0.74-0.80 m (glide triangulation and frame 0) + snout about 0.10 = **0.84-0.90 m**. Round 1's 0.87 is inside this
range (within 3 pct), so it is verified.

## Rechecks
- **a. Closure** (`closure.py`). The hip chord between frames 24 and 48, back-projected with the given depths, is 1.294 m at f 3450 and 1.285 m at f 3550,
  against the prior 1.29: 0.0-0.4 pct (smoothed hips 1.281-1.290).
- **b. Plausibility.** There are no standard objects; the dragon is fantasy. The wingspan is about 1.4 m (C1/C2) at this f, so body/wingspan ≈ 0.6, plausible for a
  wyvern. Rigid points (head, foot) shrink exactly at the root-depth rate.
- **c. Units and time base.** Metres. Every frame comes from t × 24 (the file is also 24 fps).
- **d. Fault proof.**
  - **C1 (1.1, the 0.7 weight of the blend).** C1 takes the tail from glide closest-point-on-w offsets (0.73-0.97 m). That geometry predicts a head→tail
    image length of 205 px at frame 71; I measure 223 px. Its own frame-0 values (0.80 + snout) contradict the 1.1.
  - **C2 (1.05).** The same construction, with partly biased tail and head offsets.
  - **DeepSeek C3/C6/C7 (0.57-0.72) and the 0.815 median in the blend.** They use planar or near-planar lengths, but the measured shrink proves a depth spread of about 0.5 m.
  - **C4 (0.91).** It uses f = 4500, which the line fit rejects (rms 24 vs 7 px); its result is near mine by compensation.
  - **C5 (1.08).** It uses f = 3886 and cos θ ≈ 0.5 on a drooped frame-0 length, so it comes out too long.

## Decision
I verify round 1's change and answer **0.87 m** ("new" relative to C1-C7; follows round 1). Confidence is medium. The open points are the hidden snout (±0.04 m) and
whether the reference length is a rest-pose length with a straight tail (perhaps +0.03-0.05).
