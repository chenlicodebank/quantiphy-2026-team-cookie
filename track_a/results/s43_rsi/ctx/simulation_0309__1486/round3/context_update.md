# Round 2 addendum (q1486, dragon body length)

## Verified (round 1's proposed 0.87 m holds)
- **Focal length.** My own hard-constrained constant-velocity line fit gives f ≈ 3500-3700, with glide rms 6.9 px. f = 4500 gives rms 24 px and is rejected.
  Closure: the hip chord between frames 24 and 48 is 1.285-1.294 m/s at f 3450-3550, against the prior 1.29.
- **Glide triangulation, reproduced with independent tracking.** I used my own LK tracks and my own 4x tail-tip marks; the tail-tip marks are (1373, 569) at frame 52, (1276, 507) at 60,
  (1232, 478) at 64 and (1158, 436) at 71, within about 4 px of round 1's.
  - head_spot→tail chord: 0.74 at f 3450, 0.78 at 3550, 0.76-0.87 in window 48-71.
  - The tail is 0.5 m nearer the camera than the head, and the head→tail vector is 13-15° from the flight axis.
- **New decisive check: perspective shrink over frames 52→71.**
  - A rigid head→foot pair shrinks by 0.881, equal to the root-depth ratio 0.882.
  - The head→tail vector shrinks 273 → 223 px. The along-flight-axis geometry (C1, about 1.0 m chord) predicts 205 px; the round-1 geometry predicts 221.
  - The tail's image direction is steady at 41-42°, so there is no visible tail swing.
- **Independent frame 0** (axis 43° from the line of sight): visible head front→tail is 552 px at 4.20 m, i.e. 0.82-0.83 m if the body is along the axis and about 0.77 m after droop.
  Both-at-root lower bound: 0.62 m.

## Caveat
Per-point triangulation is noisy: the hip and horn LK points land 0.6-0.9 m off in depth because the tracks slid. Use the end-to-end
shrink ratio rather than single-point depths.

## Answer
**0.87 m** = head→tail 0.74-0.80 + hidden snout about 0.10. Medium confidence.

## Open
- The hidden snout length (±0.04 m).
- Whether the reference used a rest pose with a straight tail (possibly +0.03-0.05). A value above 0.95 m would need both at their maximum.
