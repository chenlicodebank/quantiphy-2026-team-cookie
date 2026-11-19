# Q866: speed of the tennis ball at t = 1.75 s

- 2D simulation at 24 fps; question_fps is also 24, so no re-timing. t = 1.75 s is frame 42.
- Prior: ball diameter = 0.17 m. One metres-per-pixel scale for the whole clip.

## Pixel speed
- The ball centres come from scene/tracks/ball.csv (HSV mask centroid). I checked them on zoomed frames.
- Backward step 41→42 = (44.13, 43.04) px, so |step| = 61.64 px/frame.
- Second route: a linear fit of the per-frame steps over frames 21-47 gives 61.52 at frame 42 (residual 0.7 px). A quadratic fit of the arc length gives 61.77 at frame 41.5. All three agree within 0.4%.

## Pixel diameter (this sets the answer's error)
- Saturation soft-alpha, half-max mask and radial 0.5 crossings (measure.py) give 22.4 px on the ramp and 22.7 px on the floor. This is probably a little low: chroma is subsampled 4:2:0 and the dark rim is under-weighted.
- The RGB-distance mask (measure2.py) gives 24.8 px. This is too high because it takes in the cast shadow.
- The overlay (overlay.py, frames/ov.png) puts the edge between the 22.4 px and 24 px circles, at about 23.2-23.5 px. scene/notes.md gives 23.5.
- Gravity check: the free-flight hop on frames 49-54 has a parabola fit of 2.34 px/frame² (residual 0.09 px). Requiring g = 9.81 m/s² gives D = 2.34·576·0.17/9.81 = 23.36 px. This is independent of the edge measurements and agrees with them.
- I used D = 23.35 px, so the scale is 0.17/23.35 = 0.007281 m/px.

## Answer
v = 61.64 px/frame × 24 × 0.007281 = **10.77 m/s**

The ramp acceleration of 1.227 px/frame² converts to 5.15 m/s², or 0.52 g on a 44° slope. That fits a ball rolling down the ramp, which is physically plausible.
Confidence: good, about ±3%. Nearly all the uncertainty comes from the scale.
