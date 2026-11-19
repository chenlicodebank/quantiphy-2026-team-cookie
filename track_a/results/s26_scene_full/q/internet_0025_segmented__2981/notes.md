# q_2981 – canoe length (prior: boatman height = 1.75 m)

Internet/segmentation clip, side-on 2D view, one scale factor (annotator convention). Time base doesn't matter for a size.

Measurements (person2.py, all 305 frames, output in person_h.csv):
- Canoe length, stern end to bow tip (horizontal extent of the foreground mask): median 234 px (p10–p90: 232–236).
  This agrees with scene/ hull_len_px.
- Boatman: he stands at the stern and his feet are hidden by the hull. From the top of his head:
  - to the hull top under him: median 34 px (31–37)
  - to the top of the stern deck: median 37 px (35–38)
  - visual check at 10x zoom (frames/p0.png, p217.png): about 38 px at frame 0 and 35 px at frame 217.
  - I took 36 px as his pixel height, which is what the annotators would most likely have measured.
  - The scene/ figure of about 30 px was measured above the higher mid-boat gunwale, so it is too short.
- Scale: 1.75 / 36 = 0.0486 m/px. Length = 234 × 0.0486 = 11.4 m.

Second route: using the bounds of the person's height instead gives 234/34 → 12.0 m and 234/38 → 10.8 m, so the
answer is within ±5%. As a sanity check, the length-to-person ratio is about 6.5, which fits a long river pirogue.
Confidence: moderate. The main uncertainty is where the hidden feet are; if an annotator extrapolated the feet
below the gunwale, the answer would be about 9–10 m.
