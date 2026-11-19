# q_2892: soccer ball diameter (cm)

File fps = question_fps = 24, so t = 2.0 s is frame 48.
Depth: soccer ball is 3.254 m from the camera at t = 2.0 s. Focal length f = 0.5959 x 1280 = 763 px (lab method card).

Measurement (`measure.py`): at f48 the soccer ball is a uniform dark-grey disc (interior grey level about 24) on pure
black. It is fully visible and not occluded. I thresholded the grey image, then measured the area-equivalent diameter
and a least-squares circle fit to the contour:
- threshold 6: 45.8 px; threshold 10 (about half the interior level): 45.1 px; thresholds 15-20: 44.2-44.6 px.
- Frames 44-48 at threshold 10 give 48.9, 48.2, 47.5, 46.5, 45.1 px. The diameter shrinks smoothly as the ball moves
  away, so f48 is consistent with the trend; the smoothed value at f48 is about 45.3-45.5 px.
- The scene record's diam_px at f48 is 47.2 (the mean of len and wid, which includes soft edges). Its fit_d is 44.2,
  which agrees with my measurement.

Diameter = 3.254 x 45.4 / 763 = 0.194 m, so **19.4 cm**. The threshold choice gives a range of about 18.9-19.6 cm.
Second route: the area-equivalent diameter and the circle fit agree within 0.2 px. The neighbouring-frame trend gives
the same pixel size.
Sanity check: a real size-5 soccer ball is about 22 cm and a size-4 ball about 20.5 cm. The measured value is a bit
smaller, which may be because the SAM2 mask edge is shrunk or the ball is a smaller size. Confidence: moderate (±5%).
