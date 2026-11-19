# q_2792 — height of the trashbin (cm)

File and question fps are both 24, so t = 1.0 s is frame 24. f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
depth_info: the bin is 2.977 m from the camera at t = 1.0 s. The prior (yoga ball speed) is not needed for a size.

## Measurement (measure.py, frame 24, bin not occluded)
- Foreground mask (not the white-blue background) gives a silhouette from rows 484.5 to 591, so **107 px tall**.
  The top rim is 95 px wide (x 681–775). The record in scene/ agrees (bbox 681–775 x 485–591).
- Profile down column 728: the dark band at rows 484–497 is the far (back) rim plus the inside of the opening, seen
  from above. The light line at rows 497–498 is the **front top rim**. The front face therefore runs from about
  497.5 to 591, which is **93.5 px**.

## Routes
1. Method card (depth x full pixel extent / f): 2.977 x 107 / 762.8 = **41.8 cm**. This overstates the height,
   because the silhouette includes the opening's ellipse (about 13 px). The line of sight dips about 13° below the optical axis.
2. Front-face geometry: the bin centre is at z = 2.977 / 1.0335 = 2.88 m. The front face is about D/2 = 0.13 m closer
   (D = 0.26 m is consistent with the 13 px opening band), so z ≈ 2.75–2.88 m and H = 93.5 x z / f = **33.8–35.3 cm**.
- Width check: 95 px x 2.88 / 762.8 = 35.9 cm. The bin looks like a standard 28-qt deskside recycling bin
  (about 38 x 36.6 x 26 cm), and the measured width and depth match that size.

## Answer
The routes span 34–42 cm. The answer is **38 cm**: the size consistent with the measured width and depth, and within about 10 % of both
geometric extremes. Confidence: moderate (±10 %).
