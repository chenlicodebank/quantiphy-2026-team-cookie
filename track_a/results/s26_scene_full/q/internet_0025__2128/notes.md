# Q2128 — average speed of the canoe (m/s); prior: boatman height = 1.75 m

## Time base
File runs at 29.97 fps and the question gives 30 fps. The 0.1 % difference doesn't matter, so I used the file's rate.
The boat is moving through the whole clip, frames 0–472 (15.75 s).

## Scale (planar, one factor from the prior)
- The boatman stands at the stern. His feet are hidden by the hull in every frame.
- I read the pixel height at 8× zoom (`crops2.py` → `crops2.png`) from the head top (the pixelated head block or
  hat) to the lowest visible point of the legs, where they disappear behind the hull:
  - frame 0: 600 → 661 (61 px)
  - frame 100: 593 → 655 (62 px)
  - frame 280: 594 → 656 (62 px)
- **H ≈ 62 px**, so the scale is 1.75 / 62 = 0.0282 m/px.
- Sanity check: the boat is about 352 px long, which gives about 9.9 m. That is plausible for a traditional
  Hallstatt boat.
- Ambiguity: if the hidden feet are extrapolated (from the knee position, the feet are probably about 10 px lower,
  H ≈ 72–75 px), the speed would be about 0.64 m/s. I followed the annotators' pixel convention, which measures the
  visible extent.
- My automatic detector (`man_height.py`) was unreliable: it missed the grey pixelated head. I used the manual reads.

## Motion
- The camera pans right by about 44 px at the boat's height, with a slight tilt and roll. I used the record's
  background-stabilised boat centre (`x_stab`).
- Independent check (`disp.py`): I template-matched background patches myself. Raw boat displacement plus the
  background shift gives 427–431 px over frames 0→472, against the record's 428.3 px.
- Net displacement is 428.3 px over 472 frames, which is **27.19 px/s**. The motion is monotonic and almost purely
  horizontal.
- Mean per-frame speed (`speed.py`):
  - smoothed over 5, 9 and 15 frames: 27.33, 27.14 and 27.01 px/s, consistent with the net value
  - unsmoothed: 32.6 px/s, inflated by mask-quantisation noise, so not used
- Second route: the boatman's torso, stabilised, gives 28.5 px/s (+5 %). The difference comes from his sway, and the
  stern moving slightly more than the bow as the boat recedes or yaws slightly.

## Answer
v = 27.19 px/s × 0.02823 m/px = **0.768 m/s**

Confidence is moderate. The main uncertainty is the boatman's pixel height, because his feet are hidden:
- ±1–2 px on the visible height changes the answer by about ±3 %
- the full-height reading would make the answer about 17 % lower
