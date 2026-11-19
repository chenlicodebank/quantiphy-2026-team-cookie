# Q1014 – length of the fish (m); prior: fish speed 0.67 m/s; no depth_info; question_fps 24 (= file fps)

Top-down 2D Blender scene with a static camera. One shark swims right to left. Its black shadow lies ahead of it in
frames 0-30 and behind it from about frame 54 on.

## Task this round
Round 1 proposed a switch from the blend 0.855 to C1's 0.775. Its claimed fault: the DeepSeek runs measured the
length from the grey wedge of the *shadow* (845 px at frames 6-8) and used low centroid speeds. My job was to verify
this.

## Crux
The pixel length of the fish. C1 and round 1 measured snout to tail at about 640-675 px. C2 and C3 measured 835-845
px at frames 6-8, starting at the grey wedge ahead of the black shadow.

## Own measurements
- **Which object the wedge belongs to** (`check_track.py`, using the record's template ref point on the head and its
  manual keypoints):
  - In frames 34-70 the fish's grey snout wedge sits at ref −172 to −178 px, constant.
  - In frames 10-26 the pale head front sits at ref −187 to −202 px.
  - At frame 8 (crop `frames/f8.png`) the grey wedge tip is at x ≈ 1703, while ref is ≈ 2075. That puts it ≈ 370 px
    ahead, and ≈ 360 px ahead of the pectoral-fin tips (2065-2085). In late frames the snout is only 208-222 px ahead
    of the fins.
  - A rigid fish cannot move its snout 150-190 px forward. The early wedge therefore belongs to the shadow, which also
    sits ≈ 215 px ahead (its black pectoral fins are at ≈ 1850 against the pale fins at ≈ 2070). **Round 1's fault is
    reproduced.**
- **Pixel length** (`tips.py`, 3x gridded crops of the snout and the tail tip; my own readings):

  | frame | snout x | tail tip x | length (px) |
  |---|---|---|---|
  | 46 | 1001 | 1636 | 636 (638 along the axis) |
  | 54 | 812 | 1458 | 646 |
  | 62 | 623 | ~1275 | ~652 |

  The record's manual late values are 624-652. The early lengths (snout = fin − 212) are 651-674 px; the fish appears
  ~2-3% larger early on.
- **Pixel speed**, two routes:
  - Record template track: mean step 23.65 px/frame; chord over frames 10-70: 23.64.
  - My snout readings: (1001 − 623) / 16 = 23.6 px/frame.
  - The record's manual tail tips (independent of the template) give 23.7.
  - The DeepSeek centroid speeds (500-541 px/s = 20.8-22.5 px/frame) are too low.
- **Scale and length:**
  - Scale = 0.67 / (23.64 × 24) = 1.181e-3 m/px.
  - Late mean length 645 px → 0.762 m; early 665 px at 23.9 px/frame → 0.777 m.
  - The range is 0.76-0.79 m. C1's 0.775 sits within ≈1.5% of my values.

## Rechecks
- a. **Closure.** The scale is taken from the prior. Three independent pixel-speed routes agree (23.6-23.7 px/frame),
  so the prior is reproduced within ≈0.5%. closure ≈ 0.3%.
- b. **Plausibility.** There is no standard object in view. A 0.77 m shark at 0.67 m/s swims ≈ 0.9 body lengths per
  second, which is plausible.
- c. **Units and time base.** The answer is in metres. question_fps = file fps = 24, and frame indices are used
  directly.
- d. **Fault proof for C2 and C3.**
  - Their 835-845 px length starts at the shadow's wedge: ≈ 370 px ahead of the head ref point against a rigid
    172-202 px.
  - Their speeds come from silhouette centroids that the shadow contaminates (20.8-22.5 against 23.65 px/frame).
  - Both errors inflate the answer. The DeepSeek median 1.075 is faulty, and so is the 0.855 blend built on it.

## Decision
I switch to C1's 0.775. This verifies round 1's proposal: the fault is reproduced, and my own value of 0.76-0.78
agrees with it within about 2%.
