# q_1979 – height of the tree behind the deer (m)

The scene is 2D: one static camera, and the deer walks steadily to the right. fps = question_fps = 30, so no re-timing.

## Scale from the prior (deer speed 1.277 m/s)
The deer's pixel speed comes from scene/tracks/animal.csv, checked in measure.py:
- linear fit of torso_cx: 6.55 px/frame
- mean |step| of torso_cx (equal to the net displacement / 74): 6.44 px/frame
- centroid: 6.37 to 6.45 px/frame; muzzle tip fit: 6.51 px/frame

I used ≈6.50 px/frame, which is 195 px/s. That gives 1.277 / 195 = 0.00655 m/px.

## Tree height
In frame 74, measure.py takes the non-white pixels in the region x < 520. The tree's vertical extent runs from the spire
tip at y = 367 to the bottom of the trunk stub at y = 1367, so it is 1001 px tall. The tree is fully inside the frame
vertically; only its left side is cut off by the image edge.

Height = 1001 × 0.00655 = 6.56 m.

## Check / spread
The spread comes from which deer reference point sets the speed. Using 6.44 px/frame gives 6.62 m, and using
6.55 px/frame gives 6.50 m, so the spread is about ±1%. As a sanity check, the deer's overall height (411 px) comes
out at 2.7 m and its torso at 1.75 m, a plausible scale for a large fantasy deer-like creature.

## Caveat
The tree's base sits about 180 px above the deer's hooves, so the tree may be a more distant background object. The
2D convention uses a single in-plane scale, so I answered with that scale. Confidence is moderate to high under that
convention.
