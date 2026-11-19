# q3279: height of the package between the red parcel and the blue bag (internet_0073)

**Object:** the package between the red parcel and the blue bag is the flat beige cardboard box (`cardboard_box`
in scene/). At frame 0 its bbox is x 490-594 and y ~367-402.

**Prior:** the conveyor belt moves at 0.3 m/s. I took one planar scale from the belt's pixel speed, following the
annotators' convention.

## Measurements
- **Belt pixel speed.** From the scene tracks (camera drift removed, linear fit of cx_bg over frames 0-137):
  - cardboard_box: 1.967 px/frame
  - red_parcel: 1.961 px/frame
  - white_box, white pouches: 2.00 px/frame
  - blue_bag: 1.93 px/frame

  I used **1.97 px/frame**. `speed.py` gives these numbers.
- **Frame timing.** `steps.py` measures the per-frame shift of the belt band with phase correlation. The steps are
  uniform, with no 1/2-frame alternation, so frames were not dropped or duplicated to change the rate. There is one
  double step at frame 54, which is a single dropped frame. It changes the speed by less than 1%.
- **Box pixel height.** `profile.py` takes vertical intensity profiles at 6 columns across the box at frames 0, 70
  and 130. The top edge (dark-to-bright) is at about y 366.5 / 367.5 / 364.5. The bottom edge, where the box meets
  the dark contact line above the belt, is at about y 402.5 / 403 / 400.5. The visible vertical extent is
  **35.5-36 px** at all three frames. The front face alone (below the bright top-face sliver, about y 378) is about
  24 px.

## Time base
The file runs at 25.11 fps and the question states 30 fps. The frames are consecutive original frames, so a re-timed
clip would keep the same px/frame but change the real time per frame. Both rates give plausible parcel sizes, so the
scene cannot decide between them. I used the question's 30 fps, since the annotators state it with the question:
- 30 fps: 59.1 px/s, scale = 0.3 / 59.1 = **0.00508 m/px**
- 25.11 fps (the file's rate): 0.00605 m/px

## Result
Height = 36 px × 0.00508 m/px ≈ **0.18 m** (0.182 m). At this scale the box length (104 px) is 0.53 m, which is a
plausible size for a flat parcel.

Alternatives:
- At the file's 25.11 fps: 0.22 m
- Front face only (24 px) at 30 fps: 0.12 m

## Second-route check
The pixel height is consistent within 0.5 px at frames 0, 70 and 130. The belt speed is consistent within ±2% across
6 parcels.

**Confidence:** moderate. The main uncertainty is the frame rate (the two rates differ by 19%), then the convention
for the height (full visible extent vs. front face only).
