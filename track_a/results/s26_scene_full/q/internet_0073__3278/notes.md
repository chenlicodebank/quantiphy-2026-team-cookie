# q3278: width of the package between the red parcel and the blue bag (internet_0073)

## Object
The package between red_parcel (x 369-462 at frame 0) and blue_bag (x 730-862) is the flat beige taped
**cardboard_box** (scene/ bbox_f0 490-594 x 367-401). I checked this on frame 0 and in zoomed crops.

## Pixel width (horizontal extent along the belt)
- From `edges.py` and `profile.py` (column brightness profiles, sub-pixel threshold crossings, every 10th frame):
  - The bright front face is 84-85 px wide in frames 0-60, steady (e.g. f0 490.4-574.3, f60 601.4-686.5).
  - A darker end face, seen obliquely because the box is slightly yawed, adds about 18-20 px on the right.
- Full horizontal extent ≈ 104 px (f0 490-~595, f60 ~601-~705 on zoomed crops). This matches the scene record.
- The annotators' convention is the object's full pixel length along the motion direction, so I used 104 px.
  Under the front-face-only reading (84.5 px), the answer would be 19% smaller.

## Scale from the prior (belt speed 0.3 m/s)
- In `speed.py`, the background-compensated (`cx_bg`) linear fits over frames 0-137 give 1.93-2.01 px/frame for
  7 parcels. The median slope is **1.967 px/frame**; the cardboard box itself gives 1.967.
- One frame-drop step appears in every track at step 53. File timestamps are uniform at 1/25.1115 s.
- Frame rate: the file is 25.111529 fps, but the question states 30 fps. I could not settle which is right:
  - The cut shows no periodic frame drops, so the clip is either native ~25 fps (a phone in low light) or the
    original 30 fps footage re-timed.
  - Physical checks (parcel sizes, worker head ~29 px at a greater depth) fit both rates.
- Results:
  - 30 fps: 0.3/(1.967·30) = 5.08e-3 m/px → 104 px = **0.529 m** (front face only: 0.43 m)
  - 25.11 fps: 6.07e-3 m/px → 104 px = **0.632 m** (front face only: 0.513 m)

## Answer
I leaned toward the rate stated with the question (30 fps) and the full extent, and hedged a little toward the
file-rate reading: **0.55 m**.

## Second-route check
The red parcel's speed (1.961) and the white boxes' speeds (2.00) give the same scale within ±2%. The box width
measured at frames 0, 30 and 60 is constant within 1 px.

## Confidence
The width in pixels is solid to about ±2%. The main uncertainty is the time base: the two rates differ by 19%.
