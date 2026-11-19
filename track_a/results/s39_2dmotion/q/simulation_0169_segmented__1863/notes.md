# Q1863 – acceleration of the astronaut at t = 2 s (m/s^2)

Prior: height of the astronaut = 2.2 m. No depth_info. 2D video. The file and the question both run at 24 fps, so t = 2 s is frame 48.

## Method
- `measure.py`: my own mask (min RGB < 225, largest blob) for every frame, giving the centroid track (`my_track.csv`) and the extents.
  The centroid sits at waist level, which I use as the stand-in for the pelvis origin. The pose is rigid.
- The motion is a near-vertical rise of 275 px. It fits Blender's default Bezier ease-in/ease-out (a smoothstep
  s = s0 + D(3x²-2x³), x = (f-a)/T) very well: a = -0.39, T = 78.6 frames, D = 275.1 px, rms 0.19 px.
  It does not deviate from the path line by more than 1.5 px.
- Acceleration convention: (speed(48) - speed(47)) x fps, computed on the fitted curve: **-31.5 px/s²**, so it is slowing down.
  The raw one-frame differences are too noisy (±0.7 px/frame) to use directly.
- Local quadratic/cubic fits centred on f48 (half-windows of 6, 8, 10 and 12 frames) give -32.6 to -35.0 px/s².
- Height in pixels: at f0 the figure stands almost upright (tilted about 4°). My mask's vertical extent is 90 px (y 477-566),
  and its length along the main axis is 91.5 px. SAM 3 gives vert_px 90 and length_px 91.0, so the two agree within 1%.
  I used 90.5 px, so the scale is 2.2/90.5 = 0.02431 m/px.

## SAM 3 check
- Segment at f0 (score 0.87): its box 1273-1315 x 477-567 matches my mask, and the overlay outline covers the whole figure.
- Tracking gave 67 valid frames. Its centres differ from mine by 0.03 px on average (std 0.4 px).
  A smoothstep fit to the SAM track gives -31.1 px/s² at f48, within 1.5% of my -31.5. No difference above 3% needs resolving.

## Result
Acceleration ≈ -31.3 px/s² x 0.02431 m/px = **-0.76 m/s²** (magnitude 0.76; the astronaut is decelerating).
Using 90 or 91 px for the height gives 0.765 or 0.757.
The 25° rotation could shift the centroid relative to the pelvis by about 1-2 px over the whole clip, which matters less than 1% here.
Confidence: good (about ±5%).
