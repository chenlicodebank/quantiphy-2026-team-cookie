# q_2275 — velocity of the toy at 2.6 s (cm/s)

t = 2.6 s -> frame round(2.6*24) = 62 (file fps = question fps = 24). Prior: g = 9.8 m/s^2; no depth_info,
so the metric scale comes from the toy's free-fall acceleration in pixels (planar, toy ~ constant depth).

Frame 62 is just after the 2nd catch (catch f59): the toy is in the hands, moving down and decelerating.

## Scale (flight.py, fit.py)
Background-subtracted mask of the toy in free flight; quadratic fits of the toy's top edge / centroid:
- flight 1 (f17-22): top 145,137,135,138,148,161 -> ~3020-3370 px/s^2; centroid 2925
- flight 2 (f52-58): top 123,112,105,104,109,120,135 -> ~3130-3460 px/s^2; centroid 2990-3350
- record's mask/bbox fits: 2850-3650.
Adopted a = 3130 px/s^2 -> 9.8/3130 = 3.13 mm/px (spread about ±7%).
Sanity: toy 96 px tall -> 30 cm; person 508 px -> 1.59 m. Plausible.

## Velocity at f62 (top.py, view.py)
Toy top edge (x 442-472, mask) f59..65: 161, 207, 240, 273, 291, 308, 320 px.
Record centres f60..64: 252, 277.5, 309.5, 326, 351 (agree with the top-edge motion).
Lab convention = forward difference smoothed over >=5 frames: mean of forward diffs f60->65 = (320-207)/5
= 22.6 px/frame; x drift ~3 px/frame -> 22.8 px/frame = 547 px/s.
Alternatives: central diff 61->63 = 25.5 px/frame (191 cm/s); raw forward diff 62->63 = 18 (135 cm/s);
record centres (352-252)/5 = 20 (150 cm/s).
v = 547 px/s * 3.13 mm/px = 1.71 m/s -> answer 170 cm/s.

Confidence: moderate (±15%): toy in hands during strong deceleration, and the gravity scale from short flights.
