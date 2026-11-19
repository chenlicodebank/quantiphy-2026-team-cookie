# Q12: width of the boat (m). Prior: the person is 1.75 m tall. No depth_info.

**Answer: 3.30 m**

## Where the candidates part ways
- **C3 (5.4 m)** used one 2D scale: 42 px for the person = 1.75 m. That is wrong here. The view is clearly oblique (about 35° off nadir, long focus): the person's height is foreshortened by about sin β (about 0.58), while the deck is compressed only by about cos β (about 0.86). The boat looks like a fishing boat about 10–11 m long, so a 5.4 m beam would also be implausible (L/B ≈ 2).
- **C1 (3.32) and C2 (3.38)** both built a pinhole model with off-nadir ≈ 35°. They reached that angle independently, from different cues: mast lean plus scale change for C1, and cabin-corner lean, motion vanishing point and rectangles for C2. Their 2% gap comes almost entirely from the person's minimum head-to-toe extent (C1 38.8 px, C2 37.3 px), plus small differences in the person model.

## My checks (own scripts)
- `prof.py`: I rotated frame 30 so the boat axis (15.8°) is horizontal and found the white/red near-gunwale boundary per column. It sits at y' ≈ 989.5 under and just aft of the cabin. The far gunwale (white deck against water) is at y' ≈ 893–898 at the bow and aft of the cabin, so about 891 under the cabin. That makes the **maximum width across the axis ≈ 98 px**, which agrees with C1's 98 px. The far-edge points C2 read aft of the cabin also match mine.
- `pext.py`: I measured the person's head-top to lowest-toe extent against a clean background, built from frames in which the person and their shadow were not over the pixel. The per-step minima are at frames 17, 34, 51 and 68: sub-pixel 38.0, 38.7, 38.5 and 37.7 px (integer row counts 41, 39, 40, 41). **E ≈ 38.2 px**, which lies between C1 and C2.
- Affine/pinhole check at off-nadir α0 ≈ 34.5–35.4° (local ray angle about 35.3° at the person and about 31° at the boat):
  - Person model: head ellipsoid with its top at about 1.75 m, giving an extent of 1.65·sinβ + 0.10, plus the toe 0.10–0.17 m ahead of the head times cosβ. This gives **s_person = 32.0–33.6 px/m**.
  - Distance ratio from the boat to the person, with the deck at 0.8 m: 1.058, so s_boat = 33.9–35.6 px/m.
  - Beam foreshortening, projected onto the image perpendicular of the axis: 0.86–0.87.
  - W = 98 / (0.87 · s_boat) = **3.17–3.32 m**. The pinhole rectifications in C1 and C2, rescaled to E = 38.2 px, give about 3.33–3.40 m.
- Plausibility: beam 3.3 m on a gunwale about 10–11 m long gives L/B ≈ 3.1, typical for a small fishing boat. The person's walking speed comes out at about 1.3–1.45 m/s, which is realistic.

## Conclusion
I agree with the C1/C2 geometry and reject C3's single 2D scale. My measurements put the beam at 3.2–3.4 m, and I answer **3.30 m**. The main uncertainties are the camera tilt (±1° changes the result by about ±2.5%) and the toe-offset model for the person (about ±3%). Confidence: about ±6%.

Time base: the file is 24 fps and question_fps is 24. Time does not enter this size question.
