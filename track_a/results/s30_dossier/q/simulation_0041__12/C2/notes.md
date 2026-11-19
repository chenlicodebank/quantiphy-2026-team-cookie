# Q12 – width of the boat (m); prior: person height 1.75 m; no depth_info

Answer: **3.38 m** (the boat's beam: its widest gunwale-to-gunwale extent across the hull).

## Why the "2D" label is not enough
The camera is a static, oblique, long-focus view. The person's height is foreshortened by sin(theta), while the deck is
compressed only by cos(theta) along the image vertical. One px/m scale taken from the person's 45 px height
(about 0.039 m/px) would give the wrong width. So I built a pinhole model (principal point at the image centre, roll about 0).

## Camera (all measured in code, frame 30 is the reference)
- `corner_lean.py`: the cabin's vertical aft corner, tracked over 32 frames as the boat crosses the image. Its lean is
  linear in x with slope 1/4123 px, so the vertical vanishing point (nadir) is 4123 px below the boat:
  **f·tanθ ≈ 4523 px**. The residuals are 0.05 px. The mast agrees (by eye).
- `vp_tracks.py` / `vp_fit.py`: ten boat points tracked along straight lines. The vanishing point of the motion puts the
  horizon at y ≈ −9000 (best chi²; −3000 and −15000 are clearly worse), so **θ ≈ 34.5°**.
- Rectangles on the boat (hatch top face, cabin-roof eaves): beam-direction edges at −67.4° to −68.6° with the
  axis/motion at 15.7°. The pinhole model reproduces this for **θ ≈ 33.5–35°** (`pinhole.py`).
- Template scale change (`scale_change3.py`) gives horizon ≈ −7000 to −9000, which is consistent. The boat's image
  speed falls 2.5% over the clip, more than perspective explains, so the boat probably decelerates slightly; I did not
  use speed.
- Adopted: θ = 34.5°, f ≈ 6580 px (HFOV ≈ 9.4°).

## Scale from the person (`person_extent.py`, `beam.py`)
- I measured the head-top to lowest-toe extent with a median background and 50% crossings. The feet are truly planted
  (the toe row stays fixed for 8–10 frames), the gait period is 17 frames and one step is 25.3 px.
- The per-step minimum extent (the swing toe passing the stance toe, around mid-stance) is 37.3 px (36.3–38.3).
- Model: head centre at 1.63 m plus a 0.11 m head radius, stance toe 0.17 m ahead of the head. This gives a ground
  scale of 31.2 px/m at the person and 33.1 px/m at the boat (perspective, deck height 0.8 m).
- Alternative timing (toe 0.10 m ahead) or the max-extent route gives 32.3–33.4 px/m. **This is the main uncertainty
  (about ±4%).**

## Beam (`edges.py`, `beam_local.py`)
- Near gunwale: the outer edge of the white cap over the red hull, found per column. Far gunwale: the bow silhouette
  edge plus the bulwark top behind the cabin (read at ×8).
- Everything is back-projected to the gunwale plane, and widths are measured perpendicular to the heading (taken from
  the motion direction). Chord widths are insensitive to the heading (±4° changes them by <1%) and to sheer.
- Largest visible chord: 3.33 m, just aft of the cabin. Mid-ship under the cabin, using the near edge and a centre
  line interpolated between the nearest chords: maximum about 3.44 m (smoothed; θ = 34.5°, toe offset 0.17 m).
  Gunwale length is about 10.1 m (length/beam ≈ 3, plausible for a fishing boat).

## Result and checks
- Beam = 3.44 m with a scale of 31.2 px/m, or 3.33 m with the alternative 32.3 px/m. Answer: **3.38 m**.
- Sensitivity: θ ±1° gives ±2.5%; the person-scale model ±4%; edge digitisation ±2%.
- Unresolved conflict: θ ≈ 34.5° implies a long step (about 0.95 m) for a 1.75 m person. A normal 0.75–0.8 m step would
  need θ ≈ 27–29°, which would make the width about 3.0–3.1 m. I trust the direct boat and perspective geometry
  (three cues) over the anthropometric prior.
- The naive single-scale 2D reading (1.75/45 m/px) would give 4–5 m, which the geometry above rules out.

Confidence: moderate (about ±8%).
