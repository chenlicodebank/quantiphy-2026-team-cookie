# q_2982 – average speed of the canoe (prior: boatman height 1.75 m)

The file runs at 29.9706 fps. All times use question_fps = 30, so frame 304 is t = 10.133 s.
Internet/segmentation 2D clip, so one scale (m/px) comes from the boatman's pixel height.

## Boatman pixel height (scale)
- My own measurement, on zoomed crops with the SAM outline drawn (viewp.py / viewp2.py, frames/pz0, pz100, pz240):
  - Frame 0: head top y≈401, feet on the stern deck y≈439.5, so ≈38.5 px.
  - Frame 240: 396 → 434.5, so ≈38.5 px.
  - Frame 100 (slightly bent): 398 → 434.5, so ≈36.5 px.
- SAM 3 "person" masks (person_h.py, every 20 frames): vertical extents 34–40 px, median 37. Frame 0's box spans
  401.3–439.5 (38.2 px). One frame (180) is a failed segmentation at 9 px and is ignored. SAM agrees with my
  measurement to within 3 pct on the upright frames.
- The scene record's "person height above gunwale" of about 30 px is wrong as a full height: it measured down to the
  raised hull further forward, not to the feet. Zoomed crops show the boatman standing on the low stern deck, with
  the whole body visible down to the feet.
- Adopted height: 38 px, giving a scale of 1.75/38 = 0.04605 m/px. Sanity check: the boat (234 px; SAM canoe
  235 px) comes out at ≈10.8 m, a plausible long wooden canoe.

## Canoe motion (measure.py)
- The background is white, so camera motion cannot be checked. The canoe's size stays constant (234 ± 2 px).
- Stern moves 468 → 624 (+156 px), bow 701 → 855 (+154 px), bbox centre +155 px, all over frames 0–304. Vertical
  drift is only a few px.
- Linear-fit slopes: stern 0.525, bow 0.508, centre 0.516 px/frame. Average speed is 155 px / (304/30 s) =
  15.30 px/s, which converts to 0.705 m/s.

## Second route
- The boatman's own horizontal centre moves at 0.517 px/frame, i.e. 15.5 px/s, giving 0.714 m/s.
- Range for the height choice: 37 px gives 0.72 m/s; 39 px gives 0.69 m/s.

**Answer: 0.70 m/s.** Confidence is moderate. The main uncertainty is the boatman's pixel height (±3 pct) and
whether the original footage panned, which cannot be seen against the white background.
