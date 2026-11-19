# q_282 – diameter of the handle (m); prior: puck diameter = 0.074 m

The video is a 2D top-down air-hockey render at 24 fps (question_fps is also 24, so no re-timing). The camera is static and looks straight down: the puck's diameter is a constant 64.2 px everywhere from y = 720 to y = 1650, so the table plane is parallel to the image.

## Measurements (frame 48; the objects don't move)
- **Puck** (`edges.py`): the half-max width of R-B on rows through the centre is 64.1-64.3 px in every frame checked (0-70). The scene record's mask gives 63-64 px. I used **64.2 px** because it is measured the same way (half-level edge) as the knob.
- **Handle knob on the top (moving) mallet** (`knob_radial.py`): I took 720 radial profiles from the knob centre. On each one I found the outer half-level edge of the bright rim that marks the silhouette, then fitted a circle. The diameter is **54.5 px**, with x-extent 54.35 and y-extent 54.9. The overlay is in frames/knob_top_ov.png.
- **Handle knob on the bottom (static) mallet**: the knob is clearly seen in perspective, with its side visible because it sits far off-axis. Its fitted outline is 51.3 px wide in x and 57.3 px along the radial direction. The width across the radial direction, about **51 px**, is its diameter. This mallet is about 6% smaller overall (body 107-108 px against 115 px), so the two handles really do differ by about 7%.
- **Second route** (`measure.py`, raw rows in `knob.py`): the mean radial profile of the top knob has its rim peak at r = 26 and returns to the body level at r ≈ 27.5-28, giving a diameter of about 55 px. Direct row and column cuts give outer edges about 55 px apart. Both agree with 54.5.

## Answer
- The question doesn't say which mallet's handle it means, so I took the mean of the two, **52.9 px**. That is within 4% of either one.
- A small perspective correction of about 1% is applied, because the knob top sits higher above the table than the puck top. I estimated this from the bottom knob's radial stretch of about 6 px at 566 px off-axis.
- Result: about 52.5 px × (0.074 / 64.2) m/px = **0.0605 m**. Using the mask diameter of 63.5 px for the puck would give 0.0617 m.
- I answered **0.061 m**.

Confidence is moderate. The two handles differ by about 7%, so which one is meant is the main uncertainty. The pixel measurements themselves are good to about ±0.5 px.
