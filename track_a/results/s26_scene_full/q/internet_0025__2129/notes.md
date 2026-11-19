# q_2129 — displacement of the canoe in the first 5 s (m)

Prior: boatman height = 1.75 m. Internet video, so I used a planar model with one scale.
Time base: file 29.97 fps vs question 30 fps; either way t = 5 s maps to frame 150 (149.85 rounds to 150), so the choice doesn't matter.

## Scale (boatman)
- `profile_man.py` makes zoomed, gridded crops at frames 0, 30, 60, 75, 90, 120 and 150.
- The head is pixelated. Its top is at y≈600 in frame 0 and y≈593 in frame 150. Legs and feet are visible down to the near gunwale: y≈660–661 in frame 0 and y≈652–653 in frame 150. The feet themselves are just hidden.
- Upright height is about 60 px (59–61 across frames; bent poses are shorter). The scene record's 51–58 px
  stopped at the dark clothes and missed the legs.
- Scale = 1.75 / 60 = 0.02917 m/px. Sanity check: the boat's 352 px works out to about 10.3 m, which is plausible for a traditional lake boat.

## Displacement (frames 0 → 150)
- The camera pans right, so I measured motion against the background.
- Route 1 (`disp.py`, template matching):
  - The background shifts dx ≈ −29.2 px (5 patches, −28.8 to −30.8).
  - Boat patches at the bow, middle and stern shift +106.2, +109.5 and +110.8 px in the image.
  - Relative to the background that is 135.4, 138.6 and 140.0 px. Vertical motion relative to the background is about 0.
- Route 2 (scene record `boat.csv`): the stabilised centre moves from x 876.5 to 1013.5, which is 137.0 px.
- Taken together: about 137.5 px, so 137.5 × 0.02917 = 4.01 m.

Sensitivity: a boatman height of 58–62 px gives 3.9–4.15 m. Without the pan correction (raw image motion of 109 px) the result would be about 3.2 m. I don't think that's what the reference intends, because the instructions say to measure against the background.

Confidence: moderate. The main uncertainty is the boatman's pixel height (head pixelated, feet hidden), about ±4%.
