# q_991 – displacement of the whale from 0.5 s to 1.0 s

Time base: file fps = question_fps = 24, so t=0.5 s is frame 12 and t=1.0 s is frame 24. The video is a top-down 2D Blender scene with a static camera. The whale swims straight left (-x), and its vertical drift is under 5 px.

## Scale (from the prior: whale length = 19.17 m)
The whale is horizontal in the image, so its length is the x-extent of the mask bbox (from scene/tracks/whale.csv).
- At rest (frames 0-1) it is 2355 px, which I take as the model's length. Its range is 2125-2405 px, because the tail flukes are foreshortened while they beat.
- That gives 19.17 / 2355 = 0.00814 m/px.
- If the max (2403 px) is used instead, the answer is about 2% lower. If the mean (2274 px) is used, it is about 3.5% higher.

## Displacement in pixels
- From scene/tracks/whale.csv, the nose tip goes from x=1025 at frame 12 to x=921 at frame 24, which is 104 px.
- From a linear fit of the nose over frames 3-71, the speed is 8.567 px/frame, so 12 frames give 102.8 px.
- Checked by eye on zoomed grid crops (frames/n12.png, frames/n24.png):
  - The nose apex moves from about 1029 to about 925, i.e. 104 px.
  - The head outline at y=1050 and at y=1250 moves about 100 px.
- I used about 103 px. The motion is pure translation in x.
- Second route: template matching (match.py) was tried but locked onto the caustic background, so I discarded it. The outline-edge offsets above serve as the second route.

## Result
103 px × 0.00814 m/px = 0.84 m (range 0.82-0.87 m depending on which length in pixels the prior refers to).
Confidence: good (the main uncertainty is the pixel length behind the prior, about ±3%).
