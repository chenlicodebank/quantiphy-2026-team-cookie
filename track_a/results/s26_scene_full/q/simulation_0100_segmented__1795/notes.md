# q_1795 — height of the shark (m)

The prior is boat length = 10 m. This is a 2D planar scene (constant pixel sizes, static camera), so one m/px scale applies.
fps is 24 and question_fps is 24. Time does not matter for this question.

Measurement (`measure.py`): non-white mask (min channel < 225 or saturation > 40), checked on frames 30, 40, 50 and 57, where the boat is fully in view.
- **Boat length** (hull rows 340–660, stern/rudder to bow tip): 856–858 px. This matches the scene record (856).
- **Shark height** (top of the dorsal fin to the bottom of the pectoral/pelvic fin, the axis-aligned box): 103–104 px, mean 103.5. This matches the record (103).
- **Scale**: 10 / 856 = 0.01168 m/px.
- **Shark height**: 103.5 × 0.01168 = 1.21 m.

Check: the shark length is 278 px, which gives 3.25 m. A 1.2 m fin-to-fin height for a 3.25 m shark is plausible, and so is a 10 m boat. Both sizes are stable across frames to within ±1 px.
Confidence: high. The main uncertainty is about 1% from anti-aliased mask edges.
