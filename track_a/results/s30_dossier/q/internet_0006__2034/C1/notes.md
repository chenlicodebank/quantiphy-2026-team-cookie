# q_2034 – length of the motorcycle (prior: lane width = 3.66 m)

The scene record calls it a "cyclist", but the zoomed crops show a motorcycle with its rider. It is in the right
lane and rides down the image. The camera is a static nadir drone shot, so one planar scale applies (annotator
convention). No timing is involved, so fps does not matter.

## Lane width (measure.py)
- I took the per-pixel median background of the road strip. For each 100-row band I found the asphalt edges from
  the gradient and the centre line from the dash brightness, with a sub-pixel centroid.
- Left lane (edge to centre line): median 36.2 px. Right lane: median 38.1 px. Whole asphalt road: 74.5 px, so half
  of it is 37.3 px.
- Near the motorcycle's path (y 600–1500), the right lane (its own lane) is 37–39.6 px and the left lane is 34–37 px.
- Lane width used: about 37.5 px, giving a scale of 3.66 / 37.5 = 0.0976 m/px.

## Motorcycle length (crop.py, measure.py)
- I took the background difference over a ±30 px window around the tracked centre and counted the rows where the
  difference exceeds about 50. This gives 30–31 px at frames 0 and 72 (the clean frames), from the tail light to
  the front wheel.
- The mask length at threshold 35 over frames 0–115 has a median of 31 px (10th–90th percentile 29–33). The
  record's bbox_h is 29–33 px, median 30.
- Motorcycle length used: 30.5 px.

## Result
30.5 px × 0.0976 m/px = **2.98 m**. The range depends on which lane is the reference: 2.91 m for the right lane
(38.3 px) and 3.09 m for the left lane (36.2 px). Answer: 2.95 m.

## Check
The white car measures 78 px, which converts to 7.6 m with the same scale. So the stated lane width makes every
object look large: the real road is narrower than 2 × 3.66 m. I still follow the convention of a single scale
taken from the prior.

Confidence: moderate. The main uncertainty is which pixel span the annotator used for "lane width" (±5 %) and
the motion blur at the motorcycle's ends (±1 px).
