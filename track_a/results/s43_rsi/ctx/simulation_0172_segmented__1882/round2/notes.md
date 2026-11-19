# Q1882: speed of the astronaut at t = 0.5 s (m/s). Round 2 notes

The file fps and question_fps are both 24, so t = 0.5 s is frame 12 and the speed is |P12 − P11| × 24 (origin = pelvis).
Prior: astronaut height 2.2 m. depth_info: 18.147 m at f24 (Euclidean), which is 18.13 m axial.

## Job
Round 1 proposed a switch from the submitted 2.65 to 1.68 (following C3). My task was to verify that proposal with my own code and routes it did not use. Round 1 used ECC affine registration; C2 used LK; C3 used template scale search. I used SIFT plus RANSAC.

## Crux
The answers part on the depth (approach) rate dZ/dt at frame 11→12. Everyone agrees the in-plane component is about 1.5 m/s. C1 took the depth rate from bbox height, helmet and area, which gives a scale rate of about 6e-3 per frame. The rigid-part routes give about 1.5–2e-3 per frame.

## Measurements (my own scripts)
- **`sift_scale.py`:** SIFT features in rigid upper-body regions, matched over all frame pairs up to 12 frames apart in f0–35. I fitted a RANSAC similarity and a full affine, then solved least squares for log s(i) with s(24) = 1. I used three regions:
  - **Backpack + helmet (0.55w × 0.48h).**
    - s12 = 0.943 (similarity) or 0.937 (vertical scale).
    - Local rate at 11.5 over windows f2–14 to f8–15: similarity 1.48–1.67e-3, vertical 1.80–2.28e-3.
  - **Backpack only (0.35w):** similarity 1.47–1.61e-3, vertical 1.36–1.99e-3.
  - **Wider (0.7w × 0.4h):** s12 = 0.946. Similarity 1.38–1.62e-3, vertical 1.78–2.13e-3.
  - Adopted values: **r = 1.7e-3 per frame** (range 1.45–2.1e-3) and **s12 = 0.943** (range 0.937–0.946), so Z12 = 19.22 m.
  - Round 1 had s12 = 0.954 and r = 1.4e-3. Both differences are small.
- **`hip_motion.py`:** image motion of the hip band from f11 to f12. I used three band definitions and two methods:
  - SIFT similarity: du 9.1–9.9 px, dv 3.5–4.0 px.
  - Sub-pixel template matching: du 10.0–10.6 px, dv 3.0–3.4 px.
  - Adopted: (9.9, 3.5) px, the same as round 1, C3 and C2.
  - The image speed doubles abruptly at f14→15 (du 19–20 px), so the window ends at f14.
- **Focal length.** I normalised bbox_h by s_i. The maximum is 394.5 px (f31) and the mean of the top 5 is 393 px, so I used h24eq = 392 px and f = 392 × 18.147 / 2.2 = 3233 px (HFOV about 39°).
- **`speed.py`:**
  - Central: V = (1.501, 0.449, −0.785) m/s, so **|V| = 1.75 m/s**.
  - Grid over h24eq 382–402, s12, r, du and dv: 10th–90th percentile 1.62–1.91, full range 1.54–2.01.
  - With vz = 0: 1.50.
  - Round 1's parameters reproduce its 1.68.
- **Overlay:** `frames/overlay_f11_f12.png` shows the rigid scale region in blue, the hip band in red and the pelvis point in green.

## Rechecks
a. **Closure.** f = 3233 px with Z24 = 18.13 m gives a maximum normalised height of 394.5 px, which is 2.21 m (+0.6 % against the 2.2 m prior). The f24 bent pose gives 380 px, which is 2.13 m.

b. **Plausibility.** The astronaut is 2.2 m tall, which includes the suit and the backpack. A speed of 1.75 m/s is a normal walk or lope.

c. **Units and time base.** The answer is in m/s. Frame 12 is t = 0.5 s at 24 fps, the same as the file rate, and I used a backward difference.

d. **Fault proof.**
   - **C1 (3.2) and the submitted blend (2.65), which inherits C1's error:** I reproduced the fault. bbox_h goes from 337 to 348 px over f9–14, a rate of about 6.4e-3 per frame, because the legs straighten. My rigid SIFT rate is 1.5–2e-3. Putting r = 6e-3 into my geometry gives 3.29, which reproduces C1. C1's Z12 of 20.0 m (from the bbox ratio 380/343) also disagrees with the rigid-scale value of 19.2 m.
   - **C5 (2.4):** it used a helmet-based depth rate. I did not re-test the helmet alone. My combined helmet + backpack region does not support a rate that high.
   - **C4 and C6 (2.0, 2.05):** they used the clip-mean depth rate, which is dominated by the hop after f15. My scale curve shows the rate is about 5e-3 per frame over f16–24, against 1.7e-3 at f12.
   - **C2 (1.9):** it is inside my grid (90th percentile 1.91). Its r = 2.2e-3 is at the upper edge of my vertical-scale values. I found no hard fault in it.
   - **C3 (1.63) and C7 (1.60):** inside my range. They sit 7 % below my value, mainly because their rate is lower (about 1e-3).

## Decision
- **Verified previous: yes.** The C1 fault (bbox-height depth rate) is real, and my value of 1.75 is within 4 % of round 1's 1.68.
- **Answer: switch from the submitted 2.65 to my measured 1.75 m/s** (the rigid-part method of C3 and round 1). Confidence: medium. The depth rate is still the main uncertainty, about ±8 %.
