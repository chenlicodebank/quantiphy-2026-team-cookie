# Q3260 – height of the speedboat (m)

Prior: speed at 1.00 s = 11 m/s. Internet video, side view, so one scale factor (m/px) comes from the prior.
Time base: file 29.97 fps vs question 30 fps (0.1 % difference, so it doesn't matter); t = 1.00 s is frame 30.

## Speed in pixels (measure.py, from scene/tracks/boat.csv)
- The camera pans right slowly. I used the pan-compensated `*_bg` columns, which measure against the background.
- Canopy template track (the smoothest reference point): 15.70 px/frame forward difference at f30→31, and
  15.82 px/frame averaged over f27–33. Bow tip: 16.3 / 15.9. Raw track without pan compensation: 15.2–15.4.
- Value used: 15.82 px/frame × 29.97 = 474 px/s, so the scale is 11 / 474 = 0.0232 m/px.

## Height in pixels
- From the canopy (bimini) top to the hull bottom at the waterline. I checked it on a 4× zoom of f30
  (frames/f30.png): top ≈ 443–445, hull bottom ≈ 503–504.
- Mean over f25–35 is 61.1 px; the mean over the whole clip is 59.6 px.

## Result
61.1 px × 0.0232 = **1.42 m**.

## Checks
- Using the whole-clip height gives 1.38 m. Using the raw speed with no pan compensation (15.4 px/frame) gives 1.45 m.
  These cases span roughly ±3 %.
- As a sanity check, the bow-to-stern length at f30 is 218.7 px, which works out to 5.1 m. That is a plausible
  length for a bowrider.

Confidence: moderate-high. The main uncertainty is the hull bottom, which blends into spray (±3 px, about 5 %).
