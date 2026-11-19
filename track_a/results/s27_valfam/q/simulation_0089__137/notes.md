# q_137 – wingspan of the big bird (simulation_0089, 2D)

Prior: small bird length = 0.94 m. File fps = question_fps = 24, so no conversion was needed.

Method (`measure_ws.py`): I took the background plate from frame 20 (empty sky), masked pixels where the max-channel |diff| exceeded 10/18/30/50, applied an open, and computed bounding boxes of the connected components for frames 0–8.
- Small bird length (x extent): 107–109 px in every frame and at every threshold (it does not depend on the flap). I used 108 px, which gives a scale of 0.94/108 = 0.00870 m/px.
- Big bird wingspan (y extent):
  - Frames 0–1 (static, identical): 229–230 px.
  - Frames 2–5: 248, 283, 337, 384 px. The wings are still opening when the bird leaves the frame.

Answer: the question does not say min or max, so I took the static initial pose at frame 0, t = 0: 230 px × 0.00870 = **2.00 m** (2.02 m with 107 px). I answered 2.01 m.

Second-route check: the threshold sweep gives 229–230 px and the length reference gives 107–109 px, so the result is within about 1 %.

Confidence: the measurement itself is good to about 1 %. The main risk is the definition. If the reference used the maximum span, the answer would be at least 384 px, about 3.34 m or more (the true maximum was not observed). Medium confidence overall.
