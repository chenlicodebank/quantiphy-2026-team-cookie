# q3180: ball diameter (cm), prior g = 9.8 m/s^2

Time base: file fps = question_fps = 30. Video is 2D internet footage of a basketball thrown across a wall.

Method (single planar scale from the prior, internet convention):
- Pixel gravity: quadratic fit of the ball centre's vertical position cy_bg (camera-drift corrected, scene/tracks/ball.csv)
  against t = frame/30 over the free flight, frames 66-97 (fit.py).
  - Untruncated frames: a = 4956 px/s^2. All frames: 4963. Raw cy without drift correction: 4930-4942.
  - Split fits: ascent (66-76) 5327, descent (81-97) 4747. The ball shrinks slightly (about 128 -> 121 px), so it is
    probably moving away from the camera, and there may be some drag. The whole-arc fit (about 4955) is used, as an
    annotator would.
- Scale: 9.8 / 4956 = 1.977e-3 m/px.
- Ball pixel diameter: 121-122 px (round frames 88-90 are 122x122 bbox; the median minor axis is 122). I checked frame 88 visually:
  it spans y of about 245-365.
- Diameter = 122 x 1.977e-3 = 0.241 m, about **24.1 cm**.

Second-route check: using only the descent-half fit (4747 px/s^2) gives 25.2 cm; the ascent-half fit gives 22.4 cm. The answer
falls between them. A regulation basketball is 23.9-24.3 cm, which is consistent.
Confidence: good (about ±5%).
