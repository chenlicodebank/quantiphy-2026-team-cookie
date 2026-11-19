# Q1512 – distance from the man's foot to the right wall (m)

The file and the question both run at 24 fps.

## Geometry (all floor-plane, f-free in units of camera height h)
- Static camera. Corridor vanishing point (959,539), horizon y≈536, no roll.
- A floor point at image (x,y) is at lateral X/h = u = (x-960)/(y-536) and depth Z = f·h/(y-536).
- Right wall = the line of the right colonnade's inner pillar edges at floor level (pillars 1–5, measured on the median
  background frames/bg.png, crop.py): u = 2.33, 2.25, 2.30, 2.31, 2.28 → **u_wall ≈ 2.30**.
  The space beyond the pillars is open, so the colonnade is the right boundary of the corridor.
- Feet (planted soles from tracks/man.csv; the right foot and left foot alternate): right foot u ≈ -0.55 (frames 0, 24, 48),
  left foot u ≈ -0.66 (frames 12, 36). He walks almost straight, so the lateral distance is nearly constant over the clip.
  Foot to wall: 2.85 h (right foot), 2.96 h (left foot); I used ≈ 2.87 h.

## Metric scale (the hard part)
- Floor steps (sole plateaus every 12 frames = 0.5 s): Δ(1/(y-536)) = 0.000352 per step. With the speed prior
  (step = 0.8465 m), f·h = 2405. With depth_info plus the pelvis over the stance foot, f·h ≈ 2100–2300. The depth and speed
  priors disagree by about 5–15% in this image model.
- Every route gives h ∝ 1/f, so the focal length (or the man's true height) sets the answer:
  - Apparent man height / (sole_y - 536) = 1.385 at all plateau frames, so the man's height H = 1.385 h. That gives
    answer = 2.87/1.385 · H = 2.07 H.
  - The gait looks natural: cadence is 2 steps/s, the stance feet do not slide, and step/H = f·0.000254. A natural step/H
    of 0.40–0.47 gives f ≈ 1600–1850 px (HFOV about 55–62°), and depth_info gives H ≈ 1.6–1.9 m.
  - Alternative: if the floor tiles were square (seams every 0.701 h across and every 0.000246 f·h along), f ≈ 2850,
    which makes the man ~1.05 m tall with 0.85 m steps. That gait is not physically natural, so I rejected it.
    That reading would give ≈ 2.3 m.
- I chose h ≈ 1.32 m. Checks: H = 1.8 m → h = 1.30; f = 1750 with the speed scale → h = 1.37; f = 1750 with the depth scale → 1.26–1.32.

## Answer
2.87 × 1.32 ≈ **3.8 m** (lateral, horizontal distance from the foot to the right colonnade/wall line).
Confidence: low–moderate. The geometry in h units is solid (±3%), but the metric scale depends on the focal length
assumption (natural human size); the square-tile alternative would give ~2.3 m.
