# q_3148 – width of the canopy (m)

Prior: average speed of the scooter rider = 4.9 m/s. 2D internet video, 30 fps (file and question rates match).

## Scale (from the prior)
`speed.py` takes the per-frame track in scene/tracks/rider_scooter.csv and averages the per-frame displacements over frames 0–93:
- raw image coordinates: 16.23 px/frame (bbox centre), 16.27 (front axle), 16.29 (torso)
- camera-stabilised: 16.56 / 16.59 / 16.63 px/frame (the camera drifts about +0.34 px/frame)
- I used the average of the two, 16.4 px/frame = 492 px/s, so the scale is 4.9 / 492 = 0.00996 m/px.

## Canopy
"Canopy" = the ivy-covered pergola roof over the four benches. Its width is its horizontal extent across the face, read on frame 0 from zoomed crops (frames/left2.png, frames/right2.png):
- left edge of the ivy is at x ≈ 880 (y 600–650)
- right edge, where the bright ivy meets the reddish shrub and the pale tree, is at x ≈ 2715
- width ≈ 1835 px (±20 px; the right edge blends into background foliage)

Width = 1835 × 0.00996 = **18.3 m**. Using only raw coordinates gives 18.45 m; using only stabilised coordinates gives 18.07 m.

## Checks / caveats
- The pergola is just behind the path, so it is at about the rider's depth and one planar scale is reasonable.
- Cross-check: at this scale a bench (about 275 px) comes out at about 2.7 m and the rider at about 2.8 m tall. Both are too big for the real world, so the prior's 4.9 m/s seems high for the real footage. The convention says to use the prior's scale anyway, so the answer follows it.
- Another reading: if "canopy" meant only the open roof span between the outer ivy pillars (dark interior, x ≈ 1230–2400, about 1170 px), the width would be about 11.7 m. I answer with the full ivy canopy.

Confidence: moderate. The scale is good to about ±2%; the edges of the canopy are good to about ±1–2%.
