# q_2272 — velocity of the toy at 0.6 s (cm/s)

File rate = question_fps = 24 → t = 0.6 s ⇒ frame round(14.4) = 14. No depth_info; prior: g = 9.8 m/s².
Frame 14 is in the throw phase: the toy is still in the hands, moving up fast (release ≈ f15–16).

## Scale (from gravity)
`measure.py`: foreground = |frame − scene/bg.png| > 45, toy component; parabola fits to free flight:
- flight 1 (f17–21): top edge a = 5.43, centroid a = 5.08 px/frame² (rms ≈ 0.1 px)
- flight 2 (f53–58): top 4.96, centroid 5.43 (f52–58: 5.07 / 5.20)
- adopted a = 5.2 px/frame² = 2995 px/s² → 9.8 / 2995 = 0.327 cm/px.
Sanity: person 508 px tall → 1.66 m (plausible); implies toy depth ≈ 2.5 m with f = 763 px.

## Toy position around frame 14 (vertical, y down; checked on 4x zoom crops `crops2.py`)
centre y: f12 291, f13 259, f14 233.5, f15 216.5, f16 199, f17 189, f18 181 (scene record agrees within 1 px).
top edge: f12 ~246, f13 216, f14 191.5, f15 171, f16 152, f17 145.
x drifts ≈ −2 px/frame (452 → 442), small.

## Velocity
Lab convention: forward difference smoothed over 5 frames (window f12–f16 centred on f14):
- centre: mean forward diffs (32, 25.5, 17, 17.5, 10) = 20.4 px/frame
- second route, top edge: (30, 24.5, 20.5, 19, 7) = 20.2 px/frame
- with x component: ≈ 20.4 px/frame → 20.4 × 24 × 0.327 cm = 160 cm/s.
Unsmoothed spread: forward diff alone 17 px/fr (133 cm/s), backward 25.5 (200 cm/s) — hand is decelerating, so the
answer depends on the smoothing; 5-frame smoothing chosen per the method card.

Answer: 160 cm/s. Confidence moderate (±15 %; smoothing convention and g-scale ±4 %).
