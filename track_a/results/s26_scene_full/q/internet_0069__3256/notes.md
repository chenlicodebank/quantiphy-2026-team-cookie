# q_3256 – displacement of the cup from 2.00 s to 2.10 s (cm)

Prior: acceleration of the cup from 2.00 to 2.30 s = 0.32 m/s^2. Internet video, so I used one planar scale from the prior.

**Time base.** question_fps is 30 and the file runs at 30.013 fps. Both give the same frames: 2.00 s is frame 60, 2.10 s is frame 63 and 2.30 s is frame 69.

**Track.** I checked the record's body edges myself (`edges.py`). I compared each frame with the empty background frame 100, using three separate y bands. All three match the record's edges to within 1-2 px. In frames 60-61 the left edge is cut off by the image border, so the leading (right) body edge is the only point tracked across the whole window. The camera is effectively static (it drifts by about 1 px in this window).

**Pixel acceleration, frames 60-69** (`calc.py`):
- Quadratic fit to the right edge: 1350 px/s^2.
- Mean second difference of the right edge: 1400.
- Velocity change from frame 60 to 69, using forward differences: 1500. Using backward differences: 1400.
- Quadratic fit to the body centre, frames 62-69: 1452. Over frames 62-72: 1435.
- Quadratic fit to the left edge, frames 62-69: 1479.

I adopted about 1420 px/s^2, so the scale is 0.32 / 1420 = 2.25e-4 m/px.

**Displacement from frame 60 to 63.** The right edge moves 589 - 394 = 195 px. Extrapolating the centre gives about 198 px. 195 px × 2.25e-4 m/px gives 4.39 cm.

**Second route.** The different acceleration estimates give answers between 4.16 and 4.62 cm. The fitted centre gives 4.3-4.5 cm. As a sanity check on the scale, the mug body would then be about 420 px × 0.0225 cm/px ≈ 9.5 cm across, which is a plausible size for a mug.

**Answer: 4.4 cm.** The spread of the acceleration estimates puts the uncertainty at about ±6%.
