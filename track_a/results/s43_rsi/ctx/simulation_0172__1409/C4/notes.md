Scale from the prior+given depth: the astronaut moves parallel to the image plane (SAM helmet area 2763 px at f24 vs 2715 px at f42, <1% linear), so m/px = 2.2/h_stand_px with h_stand_px = 420 px (max body extent over the clip, confirmed by SAM vert_px=417 at f44 and a segment sum of 422) -> 5.238 mm/px. Speed at frame 24 from sub-pixel template matching of three rigid patches (helmet, chest, hip) between frames 23 and 24: (30.5, -14.9) px/frame = 33.9 px/frame = 814 px/s (the scene/ pelvis point was biased by the growing bbox height). 814 px/s x 5.238 mm/px = 4.26 m/s; per-patch range 4.20-4.36, answer 4.25 m/s.

Final message:
**Answer: 4.25 m/s** (question 1409).

Method summary:
- **Scale**: the astronaut moves parallel to the image plane (SAM helmet mask area 2763 px at f24 vs 2715 px at f42 → <1 % linear change), so the depth is constant and the local scale is `2.2 m / h_stand_px`. The standing height in pixels is 420 px (max body extent over the clip, cross-checked by SAM `vert_px`=417 at f44 and a joint-segment sum of 422) → 5.238 mm/px (implied f = 3464 px, hfov 37°, plausible).
- **Speed at t = 1 s (frame 24)**: the scene record's pelvis point was biased by the rapidly growing bbox height (dy = −7.2 px/frame). Sub-pixel template matching of three rigid patches (helmet, chest, hip) between frames 23 and 24 gives (30.5, −14.9) px/frame = 33.9 px/frame = 814 px/s, confirmed by the helmet-top row moving −15.25 px/frame.
- 814 px/s × 5.238 mm/px = **4.26 m/s** (per-patch range 4.20–4.36).
