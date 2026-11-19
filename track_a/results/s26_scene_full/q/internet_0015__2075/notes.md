# Q2075: average vehicle spacing (prior: lane width = 3.66 m)

## Method (lane.py)
The video is a top-down 2D drone view with a static camera. I used one scale from the prior, following the internet-video convention.

**Lane width in pixels.** I took the frame-0 row profiles at five x ranges. The line centres are at:
- upper edge line: y ≈ 521.7
- double centre line: y ≈ 566.3 and 574.4
- lower edge line: y ≈ 620.6

That gives an upper (travel) lane of 44.6 px between line centres and a lower lane of 46.2 px. Using the travel lane:

scale = 3.66 / 44.6 = 0.0821 m/px

**Spacing.** I took the centre-to-centre gaps along x from scene/tracks, which I checked against frame 0.

| pair | gap at frame 0 (px) | mean over all frames (px) |
|---|---|---|
| silver → dark | 407.7 | 415.7 |
| dark → white | 415.6 | 417.3 |
| white → motorcycle | 376.4 | 361.5 |

The fourth road user is a small motorcycle.

**Readings considered.**
- Three cars only: 411.7 px at frame 0, or 416.5 px averaged over all frames.
- Including the motorcycle: 399.9 px at frame 0, or 398 px averaged.

I chose about 410 px (mainly the cars, at frame 0), which gives 410 × 0.0821 = **33.6 m**.

**Other values.**
- Cars only: 33.8 m at frame 0, or 34.2 m averaged.
- Including the motorcycle: 32.8 m.
- With the mean lane width (45.4 px) as the scale: 33.0 m.

## Second check
Car spacings measured at frame 0 and averaged over time agree within 1–2%. The scene's tracks were verified at several frames.

## Confidence
Moderate. The answer is within ±3% under every reading considered. The main uncertainty is how the annotators measured the lane in pixels and whether they counted the motorcycle.
