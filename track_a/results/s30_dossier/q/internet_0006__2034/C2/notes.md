Motorcycle (rider+bike, right lane) pixel length along motion = 31 px (raw 29-30 px, SAM mask 33 px; track box median 29 px). Scale from prior: visible carriageway width 72 px = 3.66 m -> 0.0508 m/px (applying the prior to a single 36 px lane would make the cars 7.8 m long, ruled out by the sanity check). 31 x 0.0508 = 1.58 m. Second route: SAM mask extent gives 1.68 m; car-based scale (white car 76x30 px as a 4.6x1.8 m sedan) gives ~1.9 m, noted as the alternative reading.

Final message:
I measured the motorcycle's length in the drone footage and finalized the answer.

**Method summary:**
- **Object**: The motorcycle/moped with rider is the only object in the right-hand lane. SAM 3 segmentation at frame 30 gave a clean mask (box [566,1048,581,1080]), and video tracking followed it down the road (276.9 px/s, 1.6 px residual).
- **Pixel length**: Along the motion direction, the object measures ~29–33 px (raw threshold 29–30 px, SAM mask 33 px, track boxes median 29 px); adopted 31 px. Width ~15 px.
- **Scale**: The road is a narrow two-lane carriageway, 72 px wide (centre line at x≈558, lanes ~36 px each). Applying the prior "lane width = 3.66 m" to the visible carriageway gives 0.0508 m/px. Using one lane (36 px) would make the cars 7.8 m long, which the sanity check rules out.
- **Answer**: 31 px × 0.0508 m/px ≈ **1.6 m**.

**Checks**: The motorcycle width (15 px → 0.76 m) matches a realistic handlebar width; the white car comes out at 3.9 × 1.5 m (compact car). The alternative car-based scale would give ~1.9 m, noted in notes.md as the main uncertainty (±18%).
