# q_1957 — spacing between the markings on the pool wall (m)

Prior: black cat speed = 1.041 m/s. depth_info: none. fps = question_fps = 24, so no re-timing.

## The asked feature is not in this clip
This is the segmentation version: the background, including the pool and its wall, has been replaced by white.
`probe.py` checks frames 0, 24 and 49. Every pixel above row 690 is pure white (max deviation 0), and the only
non-white pixels are the chairs, the round item, the cat and the float (rows ≥ 710). No pool-wall markings are
visible anywhere, so their pixel spacing cannot be measured.

## Scale (what can be measured)
- Cat centroid x goes 567.4 → 836.0 px over 49 frames (scene/tracks/cat.csv). That is 5.48 px/frame = 131.6 px/s.
- Scale = 1.041 / 131.6 = 0.0079 m/px at the cat's depth. The view is about 15 m wide at that depth.
- At this scale the front chairs are spaced about 235 px apart (≈1.9 m), and the cat is about 106 px long (≈0.84 m).

## Answer
Because the markings cannot be seen, the answer is a guess, not a measurement. Pool-wall markings (tile or stripe
spacing) are typically about 0.5–2 m apart, which would be roughly 60–250 px at this scale. I picked 1.0 m from the
middle of that range.

Confidence: very low, since there was no measurement and no second route was possible.
