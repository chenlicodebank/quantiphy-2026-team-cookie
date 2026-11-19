# q_3172: basket-to-floor distance (prior g = 9.8 m/s^2)

Time base: 30 fps. The file rate and question_fps agree, and 30 fps gives a plausible player height (~1.7 m).

## Scale from gravity (fit.py)
I fitted a parabola to the ball centre (scene/tracks/ball.csv) during free flight. The camera drifts only slightly, so
the raw and stabilised tracks give the same acceleration:
- frames 23-42: 2008 px/s^2 raw, 2017 px/s^2 stabilised (rms 0.1-0.2 px)
- frames 23-63: 2000 / 2001; frames 28-56: 2022 / 2025; mean second difference: 1970 / 1976
- adopted value: 2005 px/s^2, giving 9.8 / 2005 = 0.00489 m/px
- Check: the standing player is 344 px, which is 1.68 m. That is plausible, so the scale is right at the player's depth.

## Pixel distance (frame 0, 4x zooms frames/rim.png, frames/floor.png)
- Rim: top edge y ≈ 293, front edge ≈ 305, centre ≈ 297 (the record gives 297).
- Wall-floor junction below the basket: black baseboard at y 790-800, floor starting at ≈ 799.
- Rim to the floor line below it: ≈ 502 px, which is **2.45 m**.
- Second reading: rim to the floor at the player's feet (y ≈ 900): 603 px, which is 2.95 m. The real rim height is
  3.05 m. The basket is farther from the camera than the player, so planar scaling with the ball's scale
  underestimates it.

## Answer
2.6 m. The pixel-literal reading (the annotator convention: rim to the floor directly below it in the image) gives
2.45 m. The feet-level reading gives 2.95 m. I chose a value between them, leaning toward the literal reading, because
I can't tell which one the reference used.
Confidence: moderate. The scale is good to about 2 %; the uncertainty is mainly which floor reference was used.
