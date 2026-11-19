# q1994 — length of the rabbit (m); prior: speed of the brown horse = 0.874 m/s; no depth_info (round 2)

This is a 2D side view of three animals walking right. Left is horse L (red-brown chestnut, the record's "red_horse"), in the middle is horse M (grey-brown with dark legs, the record's "brown_horse"), and on the right is the rabbit (the record's "hamster").
The file rate is 24 fps and question_fps is 24.

## Crux
The crux is which horse is the prior's "brown horse": L (77 px/s, 0.0113 m/px, rabbit about 0.51 m) or M (142.5 px/s, 0.00614 m/px, rabbit about 0.28 m). Round 1 proposed switching to L.
My job was to verify that proposal.

## Own measurements (measure2.py, feet.py, overlay.py)
- Segmentation: min RGB < 235, 8-connected components.
- Horse L, frames 0–48 (frame 49 is a loop reset): the centroid slope is 3.224 px/frame (77.37 px/s) and the torso-band slope is 3.209 (77.02 px/s). I used 77.2 px/s.
  Length median 192 px, height 165 px.
- Horse M: the centroid slope is 5.938 (142.50 px/s) and the torso slope is 5.940 (142.55 px/s). Length median 229 px, height 178 px.
- Rabbit horizontal extent:
  - Bbox median 46 px (mean 46.4, range 42–53). Frames showing 53 px include a touching horse hoof; see frames/rabbit_overlay.png.
  - The soft-coverage extent has a median of 46. The widest single row has a median of 43. Frame 0 is 45 px.
  - I adopted 45.5 ± 1.5 px.
- New route, gait timing:
  - Both horses' hooves stay planted during stance, drifting by 0.1–0.3 px/frame, so there is no foot slip.
  - Horse M: stride period about 17 frames (0.71 s), stride about 95 px. Horse L: stride period about 21 frames (0.9 s), stride about 68 px.
  - Under dynamic similarity, M's period favours the small scale and L's period favours the large scale. The playback rate is evidently matched to each horse's speed, so gait timing carries no usable absolute scale. The route is inconclusive.

## Answer
Scale = 0.874 / 77.2 = 0.011321 m/px (the centroid and torso values give 0.011296–0.011348).
Rabbit length = 45.5 × 0.011321 = **0.515 m**. The range for 44–46 px is 0.498–0.521 m.

## Rechecks
a. Closure: horse L at 77.2 px/s × 0.011321 = 0.874 m/s, which is 0 pct by construction. The two reference points differ by 0.45 pct.
b. Plausibility at this scale:
   - Horse L is 2.17 m long and 1.87 m to the head top. Horse M is 2.59 m long and 2.02 m tall and walks at 1.61 m/s.
   - The rabbit is 0.515 m long and hops at 1.70 m/s: a large rabbit, but plausible.
   - At C1's scale (0.00614 m/px) the horses are 1.18 and 1.41 m long and 1.01 and 1.09 m tall. That is about 45 pct below a real horse, beyond the 40 pct limit, although the prior is a realistic walking speed.
c. Units and time base: the answer is in metres. Both the file and question_fps are 24, so seconds = frame / 24.
d. Fault proof:
   - C1 (0.283): it assigned the prior to horse M. My measurements give 142.5 px/s, matching C1's 142.3, and they reproduce the half-size horses (M 229 px × 0.00614 = 1.41 m, 178 px → 1.09 m tall).
     C1's own notes say "the absolute scale is small for a real horse". Its pixel work is correct; the fault is the scale-object assignment.
   - C2 (0.533): it uses 47 px for the rabbit against my 45.5 (median 46), which is +3.5 pct. Its scale is the same as mine.
   - C3 (0.516): it agrees with my value.

## Verification of round 1
I reproduced round 1's fault with my own code (same px speeds, same horse sizes at each scale). My value of 0.515 agrees with round 1's 0.51 (within 1 pct). The proposed switch stands.

## Decision
I switch to the horse-L reading and follow C3. The answer is 0.515 m.
Confidence is medium. The colour words alone fit horse M slightly better, and the decision rests on the real-scale plausibility rule.
