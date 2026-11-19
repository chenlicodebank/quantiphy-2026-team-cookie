# q3104 – height of the wall pads (cm)

Prior: g = 9.8 m/s^2. Time base: 30 fps (file and question agree).

## Scale from gravity (fitg.py)
I fitted a quadratic to the ball's centre y (scene/tracks/ball.csv) during free flight. Frame 35 is the release and
frame 61 is the bounce, so the windows stay inside that range:
- frames 36–60: a = 3729 px/s^2 raw and 3713 px/s^2 camera-compensated, giving 0.002628–0.002639 m/px (rms 0.6 px)
- sub-windows: 38–58 gives 0.00264–0.00265, 36–48 gives 0.00257 and 48–60 gives 0.00262
- adopted: 0.002635 m/px
- check: the ball's diameter is 94 px, which is 24.8 cm. A basketball is 24 cm, so the scale is plausible.

## Pad height in pixels (prof.py, Lab column profiles, frame 0)
The top edge comes from the drop in L from the wall to the pad. The bottom edge is the dark seam where the tan pad
face ends; below it is a shadowed mounting lip with screws, then a grey wall gap, then the black base strip.

| x | top | face bottom (seam) | lip bottom | face height | with lip |
|---|-----|--------------------|------------|-------------|----------|
| 420 | 177.5 | 808.5 | 817.5 | 631 | 640 |
| 1060 | 180.5 | 803 | 813.5 | 622.5 | 633 |
| 1500 | 172.5 | 804.5 | 814 | 632 | 641.5 |

- adopted: about 630 px for the tan face, which is what an annotator would click
- with the lip: about 638 px

## Answer
630 px × 0.002635 m/px = 1.66 m, so the answer is **166 cm**.
- If the lip is included, the height is 168 cm.
- Over the range of gravity-fit windows, the result is 162–167 cm.

Sanity check: the panels are about 216 px wide, which is 0.57 m. Real panels are often 2 ft × 6 ft (0.61 × 1.83 m).
That suggests the wall is about 8 % farther away than the ball's plane. The benchmark convention uses a single
scale, so no depth correction is applied.

Confidence: moderate-high (±3 % on the convention).
