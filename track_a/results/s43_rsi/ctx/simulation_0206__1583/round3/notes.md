# Q1583 (round 2): length of the letter (paper slip) under the gun. Answer: 0.139 m (decision: new, verifies round 1)

The file runs at 24 fps and so does the question. The slip is static, so frame 0 is used. 3D Blender scene with a static camera; the principal point is taken at the image centre (1062, 540).

## Task this round
Round 1 proposed 0.139 (new) against the submitted 0.148 (C2). It claimed C2 used a pitch of 11.6° that the verticals contradict. I re-measured that independently: LSD line segments instead of round 1's Hough/edge fits, my own slip-edge fits, and my own fall track and fit.

## Crux
The step where the answers part is the camera pitch, which sets the desk-plane tilt and so the foreshortening of the slip's receding side L–F. With roll 0, the measured vertical vanishing point ties the pitch to f by tan(pitch) = f / (VPy − cy). So once the pitch is right, the remaining uncertainty is f.

## Measurements (all in my scripts)
- **Vertical VP** (`vps.py`, `vcheck.py`): LSD with REFINE_ADV, robust grid fit over 65 near-vertical segments (desk legs, pilasters, chair legs).
  - All segments: VPy = (1066, 11981). Desk legs only: (1064, 12058). RANSAC: (1072, 12100).
  - x ≈ cx, so roll ≈ 0. This matches round 1 (1046, 11967) and C3 (11966).
  - The VPy implied by C2's geometry (f 2770, pitch 11.6°) is at y ≈ 14020. Against my segments it gives a median residual of 0.39°, compared with 0.14° for my fit.
- **Slip edges** (`slipcorners.py`, `slipdraw.py`, `sliprect2.py`; overlay in frames/slipdraw.png): half-level sub-pixel profiles on Lab L*, using the clean parts of each edge (rms 0.09–0.11 px).
  - L–F edge at 21.8°, F–R at 170.7°, back edge L–B at 171.9° in the image.
  - F = (1362.6, 643.1). L, the line intersection, = (1315.8, 624.4). The visible blurred tip is at about 1319.5.
  - R from Lab b* along F–R: half level at x ≈ 1413.5.
  - The F–R edge points beyond x ≈ 1394 bend because they are in the gun's shadow, so I excluded them.
- **f routes**:
  1. **Typewriter fall** (`fall.py`, `closure.py`): I tracked a template of the keys (NCC 0.88–1.0 on frames 1–7) and fitted with g = 9.8 and |P0| = 4.32.
     - Initial velocity free: f = 2690–2700, with the initial velocity at 0.081–0.090 m/s.
     - From rest: f = 2818–2843.
     - The fitted initial velocity matches the semi-implicit-Euler offset of a 60 Hz Bullet step (0.5·g/60 = 0.082 m/s), which favours the free-velocity fit.
     - If the keys sit about 7 cm in front of the origin (d0 = 4.25), each fit drops by about 2.5%.
  2. **Scene bbox-centre track** (`fall2.py`): f = 2640–2680 with v0 = 0.082, or 2750–2780 from rest. This is noisy (rms 2 px).
  3. **Gun origin height above the desk plane** (`heights.py`): 3.3–4.5 cm at f = 2700, 1.4–2.5 cm at f = 2800. A revolver lying flat should be about 2 cm, which favours 2700–2850.
  4. **Desk-rectangle orthogonality** (`deskorth.py`) and **slip rectangularity** (`sliprect2.py`): both are ill-conditioned. The angle peaks at 89–90° over 2700–3000 and never crosses 90°, so I did not use them for f. At f = 2600–2900 with the VPy pitch, the slip's corners come out at 87.8–89.4°. At C2's 11.6° pitch the corner is 84°.
  5. **The 5.009 m "far right corner"** would be at desk-top height only for f ≈ 2550–2620. Its identity is unclear (round 1 suspects a lower slab or bounding-box corner), so I did not use it.
  - Chosen: **f ≈ 2720 (range 2650–2840)**, pitch 13.4°.
- **Length** (`final.py`): back-projection onto the plane normal to VPy.
  - Two plane routes: the near desk corner (698, 880) at 3.593 m, and the gun (1430, 621) at 4.704 m minus 2 cm.
  - f 2650 → 0.147 / 0.144; **2700 → 0.142 / 0.140; 2720 → 0.140 / 0.139; 2750 → 0.138 / 0.137**; 2800 → 0.133 / 0.133; 2840 → 0.130 / 0.131.
  - Tip sensitivity at f 2720: L.x of 1315 / 1316.5 / 1318 gives 0.143 / 0.138 / 0.134.
  - F–R (width) is about 0.109 m, so L–F is the length.

## Rechecks
- **a. Closure** (`closure.py`): at f = 2720 with the VPy pitch, g refitted from the key track is 9.74 (−0.7%) with the initial velocity free. Under the other variants (from rest; keys at 4.25 m) it is −2.3% to +4.1%. All are within 5%.
- **b. Plausibility**:
  - The slip is 0.14 × 0.11 m, the size of a note or card.
  - The revolver is about 154 px across at 4.70 m, which is about 0.27 m (real revolvers are 0.24–0.30 m).
  - The gun origin is about 3 cm above the desk.
  - The typewriter's resting origin is 0.096 m above the desk.
  - Round 1's front sheet came out at 0.19 × 0.31 m (A4-like) at f = 2710.
- **c. Units and time base**: the answer is in metres. The object is static, so frame 0 is used; 24 fps for both the file and the question.
- **d. Fault proof**:
  - **C2 (0.148, submitted):** `length.py` reproduces 0.147 at C2's f = 2770, pitch 11.6° and C2's corners. That pitch puts VPy at y ≈ 14020, which is rejected by the verticals (median residual 0.39° vs 0.14°). It also makes the slip an 84° parallelogram. At C2's own f with the measured VPy pitch, C2's corners give 0.128. The error is C2's premise that the 5.009 m point is the front-right corner at desk-top height, used to solve the pitch.
    - Caveat: at f ≈ 2630 the corrected geometry would give 0.146–0.150. That f is reached only by stacking the low end of every route.
  - **C3 (0.13):** its geometry is the same as mine. It used f = 2750 and the blurred visible tip (1320) instead of the line intersection; at my geometry its corners give about 0.134.
  - **C1 (0.11):** its 3.4° roll is ruled out by VPy x ≈ cx.
  - **C4–C7 (0.20–0.30):** wrong sheet, or no foreshortening.
  - **C8 (0.12):** visible length plus a guess.

## Decision
Round 1's claimed fault is reproduced with my own code, and my own value (0.140 at f = 2720; 0.137–0.142 for f 2700–2750) agrees with its 0.139 to within 1%. So the change stands.

I answer **0.139 m**, decision **new** (it is round 1's value, not that of any C candidate). Confidence is medium: f between 2650 and 2840 spans 0.130–0.147.
