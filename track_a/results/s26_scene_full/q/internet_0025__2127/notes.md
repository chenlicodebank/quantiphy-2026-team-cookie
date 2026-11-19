# q2127 – length of the canoe (m); prior: boatman height = 1.75 m

This is internet footage. I used the planar method with one scale: scale = 1.75 m / the boatman's pixel height. The rate (29.97 vs 30 fps) does not matter for a size question.

## Measurements (crops.py, frames/man_*.png, scene/tracks)
- Boat length, bow tip to stern post (`length_incl_stern_post_px`): 352 px at f0, 348 at f150, 345 at f300 and 341 at f450. I checked the ends at f0 on the zoomed crops.
- Boatman: the hull hides his feet the whole time. The head is pixelated, so its top is uncertain by about 3 px.
  - Visible height (head top to the lowest visible leg pixel): 59 px at f0 (600 to 659), 54 at f150, 53 at f300 and 47 at f450. The median over the clip is 51 px; he bends with each stroke.
  - Estimated full standing height (feet on the boat floor, close to the waterline at y≈670-674 at f0): 70-74 px. A cross-check from body proportions (knee at about 654, so head-to-knee ≈ 0.715 H) gives about 75 px.

## Two readings of the prior's pixel height
- Visible height only (f0: 352/59 × 1.75): 10.4 m (11.9 m with the median visible height).
- Full height including the hidden legs (352/72 × 1.75): 8.5 m (8.2-8.8 m).
- As a sanity check, traditional Austrian lake boats of this type are about 8-10 m long.

## Answer
I cannot tell which pixel height the annotator used. I answer 9.8 m, between the two readings and leaning slightly toward the visible-height one. That is within about 6 % of the f0 visible-height value and about 15 % from the full-height value.
Confidence: moderate-low, because everything depends on how the annotator handled the hidden feet.
