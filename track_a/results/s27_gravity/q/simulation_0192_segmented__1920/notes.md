# Q1920 — height of the box (m)

Prior: box acceleration before 0.6 s = 9.8 m/s² (free fall). 2D clip, 120 fps (file and question rate are the same), no depth_info.
The scale comes from the box's pixel acceleration.

## Acceleration in pixels
- Tracked the box front-face top edge, which lies in a plane parallel to the image. The face width stays 280.8 px for the whole fall, so the box is at constant depth. I used two sources: the scene track `front_top_y` and my own brown-mask edge (`measure.py`).
- The video has frame jitter: duplicated frames (8, 16, 20, 24, 32, 35, 37, 40, 47, 54, 61) and double steps next to them. I confirmed this in my own measurement (frames 31 and 32 are identical). Because the duplicates and skips balance, it is jitter and not a net time change, so long-window fits are valid.
- Fits over frames 5–60, 5–50 and 20–60:
  - Plain least squares: 0.1405–0.1430 px/frame².
  - Free fall from rest with each frame allowed a ±1 frame shift (`fit4.py`, rms 0.3–0.5 px): 0.1395–0.1415 px/frame².
  - Adopted a = 0.141 px/frame² = 2030 px/s². The scale is 9.8 / 2030 = 0.00483 m/px.
- I did not use the bottom edge or the centroid. They give a lower acceleration because the grey underside shrinks as the box falls (a perspective effect).

## Box height in pixels
- Front face at rest (frames 100, 120, 199, `rest.py`): 320.5 → 526.5, so 205.5 px tall (the scene record gives 205.3). Width is 280.8 px.
- The top face is not visible at rest and the underside has disappeared, so the face height is the vertical extent.

## Result
- Height = 205.5 × 0.00483 = **0.99 m**. With a between 0.1400 and 0.1425 px/frame², the height is 0.98–1.00 m.
- Check: the box width is 1.36 m. The truck rear at the same scale is about 2.7 m wide and 2.5 m tall (it is slightly nearer the camera, so its true size is a bit smaller). Both are plausible for a box truck.
- Confidence: good, about ±3%.
