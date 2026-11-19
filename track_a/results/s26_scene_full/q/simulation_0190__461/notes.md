# Q461: height of the truck at t = 0 s (prior: box width = 1.33 m)

## Scale (2D, one scale from the prior)
- Cardboard box width at frame 0: 281.5 px (scene record, x 806.0-1087.5; checked on frame 0).
- Scale: 1.33 / 281.5 = 0.004725 m/px.
- The box rises less than the body (ratio 0.96 → 0.90 → 0.73 over the clip). That is its own animation, not a fixed
  depth ratio, so it gives no reliable depth offset. Following the 2D rule, I used a single scale.

## Truck extent in pixels (frame 0)
- Top: the cargo-body roof edge at y = 338.1. The camera is below the roof, so this is the highest point.
- The ground under the truck is not visible: below the bumper (y 1040-1080) there is only shadowed floor, and the
  wheels are hidden. Evidence for where the ground is:
  - Red horizontal discs under the bumper (support-leg feet) are ellipses about 40 x 10 px (`discs.py`). That gives
    f ≈ 1870 px. The camera is level (vertical lines are vertical), so the horizon is at y ≈ 540.
  - Treating those feet as touching the ground puts the ground at y ≈ 1044. The underride bar (bottom at y ≈ 1035)
    would then be only about 4 cm off the ground, which is not plausible. The black, shadowed floor under the bumper
    also fits seeing *under* the truck.
  - Truck proportions give the ground instead: the bar is 0.45-0.5 m above the ground, the body floor 1.25-1.35 m
    (the chassis band 858-1035 px is 0.84 m), and overall height / body width is about 1.4-1.5 (body 570 px wide).
    Together these put the ground at y ≈ 1140 ± 15.
- Height ≈ 1140 − 338 = 802 px, so 802 × 0.004725 = 3.79 m.
- Check: camera height ≈ (1140 − 540) × s = 2.8 m. With f = 1870 the rear face is about 8.8 m from the camera, and the
  floor at the bottom image row is about 9.9 m away, which is under the truck. That matches the dark shadowed floor
  seen there.

## Other readings
- "Truck" = only the moving part (cargo body plus the under-panel with the chevron bar, roof 338 to about 980 px,
  found in `movparts.py`): about 642 px = 3.03 m.
- Body rear face alone: 520.4 px = 2.46 m.
- Answer: the whole truck from ground to roof, 3.79 m. The phrase "at time 0s" suggests a vehicle rig whose bounding
  box changes as the body lifts.

## Confidence
Low to moderate. The ground line is inferred, not seen (about ±5%). It is also unclear which object the reference
calls "truck", and the box may sit deeper than the rear face; if so, the answer would be up to about 10% smaller.
