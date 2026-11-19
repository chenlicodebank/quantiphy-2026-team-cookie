# q_2014: speed of the blue car at t = 1 s

The blue car is the light-blue cart in scene/. t = 1 s is frame 24, and the file rate and question_fps are both 24 fps.

## Scale
- The car moves rigidly, so the speed of its origin equals the speed of its near-side tyre.
- Speed = (pixel speed of near-side features) × (0.369 m / near-side tyre diameter in px).
- The focal length cancels out. You would get the same result by taking f from the yellow tyre and the 11.38 m depth, then the cart's depth from its tyre size.

**Cart front-tyre diameter** (`tyre_sub.py`, half-level edges at the hub row, frames 33–41)
- Width: 78.5–80.2 px. It is 78.5 px near the image centre and grows slightly off-centre because the sidewall becomes visible.
- Vertical extent from the bottom (y ≈ 819) to the fender is about 76 px, but the fender hides the top of the tyre.
- Hub height of about 778 implies about 80 px.
- **Used: D = 79 px**, giving 0.004671 m/px at the tyre's depth.

**Yellow tyre**, for reference: about 165 px, which gives f ≈ 2460 px and a cart tyre depth of about 11.5 m. This route only checks consistency.

## Pixel speed (`shift.py`, sub-pixel SSD shift of strips between consecutive frames)
**Top strip** (cart roof and rear post, above the car's roof; visible in every frame)
- Frames 20–28: 29.7, 30.7, 29.8, 31.0, **31.6 (frame 24)**, 32.3, 32.2, 32.4, 32.7 px/frame.
- Smoothed at frame 24: about 31.5.

**Near-side wheel/bottom strip** (clean only in frames 33–41)
- It moves about 3.1% faster than the top strip in the same frames.
- Mean ratio over frames 33–41 ≈ 1.03.
- This fits the roof and post sitting about half the cart's width farther from the camera than the near-side tyre.

**Near-side pixel speed at frame 24** ≈ 31.5 × 1.03 = 32.45 px/frame.

## Result
Speed = 32.45 × 24 × 0.369 / 79 = **3.64 m/s**.

## Checks
- **Second route:** the scene/ track cx gives 32.5 px between frames 23 and 24. Its feature diffs give 33 px (post tip) and 32 px (roof tip). That is 3.59–3.70 m/s at the same scale.
- **Sensitivity:**
  - D = 76 → 3.78 m/s; D = 80 → 3.59 m/s.
  - Leaving out the near-side depth correction gives 3.53 m/s.
- **Confidence:** moderate to good, about ±4%.
