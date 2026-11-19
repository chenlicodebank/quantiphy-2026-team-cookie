# Q519: vertical height of the "SKYNOVA" lettering (m)

Treated as a 2D video: I used one metres-per-pixel scale, taken from the droplet's acceleration prior (9.7 m/s²). The time base is 60 fps (the file and the question agree).

## Scale
- The droplet centroid track (scene/tracks/droplet.csv, which I checked) has vertical second differences over frames 0–10 of
  31.2, 32.7, 30.5, 33.7, 30.8, 31.0, 29.6, 33.2, 31.2 px/frame². Their mean is 31.54.
  The speed differences (backward-difference convention) are the same.
- A quadratic fit to cy over frames 2–10 gives 31.33 px/frame². With the bbox centre it gives 31.70.
- I used 31.45 px/frame², which is 113,200 px/s². The scale is therefore 9.7 / 113,200 = 8.57e-5 m/px.

## Lettering
- "SKYNOVA" runs vertically (rotated) on the bottle's front, at x ≈ 1780–1830.
- measure_letters.py looks at frame 12 and marks pale pixels (R−B < 60) on the orange label, row by row.
  The letters span from y ≈ 812.5 to y ≈ 1142.5, which is about 330 px (±3 px).
- I confirmed this by eye on a zoomed, gridded crop (frames/sky.png): the letters run from about 812 to 1137 plus the edge blur.

## Answer
330 px × 8.57e-5 m/px = 0.0283 m.

## Sanity check and confidence
- The bottle body is 427 px wide, which is 3.7 cm at this scale. That is plausible for a 30 ml dropper bottle.
- The main uncertainty is a possible depth difference between the droplet's plane and the bottle front. The 2D convention ignores it.
- Confidence is moderate to high: about 3% from the measurement itself, with the plane assumption on top of that.
