# q 2810 – basketball diameter (cm)

File fps = question_fps = 24, so there is no time-base issue. The basketball is static at about (987, 370), by the right wall.

## Method (lab method card)
f = 0.5959 x 1280 = 763 px, principal point (640, 360). depth_info: basketball 2.925 m (t = 0.4 s, frame 10).
`measure_ball.py`: orange HSV mask (h < 25, s > 70/90/110, v > 40) on frames 0, 10, 24 and 47, then
bounding box, equivalent diameter and a least-squares circle fit to the contour. The overlay is in frames/mask_10.png;
the fitted circle follows the ball's edge.

Frame 10 (s > 90): bbox 70 x 66 px, equivalent diameter 66.9 px, circle-fit diameter 66.0 px. Across thresholds and frames
the circle fit is 64-68 px and the vertical extent 62-69 px. Horizontal is slightly wider (motion blur/halo, and the radial
stretch of an off-axis sphere). I use the circle fit and the vertical extent, both about 65-66 px.

D = 2.925 x 65.5 / 763 = 25.1 cm (range 24.5-25.9 for 64-67.5 px).

## Second route / checks
- Off-axis geometry: the ball is at tan(theta) = 0.455 (cos 0.91). If depth_info is a depth-camera Z value (as Orbbec
  gives), the vertical (tangential) extent converts with Z/f directly: 64-66 px gives 24.5-25.3 cm, which is the same as the method card.
  If it were a Euclidean distance to the centre, the perspective-corrected value would be about 22.3 cm. The method card
  (no correction) is used, as instructed.
- A size-7 basketball is 24-24.5 cm across, which is consistent.
- Cup sanity check: 2.516 x 27 / 763 = 8.9 cm, a plausible size.

Answer: 25.0 cm. Confidence: moderate-high (about ±5 %).
