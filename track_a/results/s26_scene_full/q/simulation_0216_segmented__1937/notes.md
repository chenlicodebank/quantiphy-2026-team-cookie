# q_1937 — length of the TV stand (m)

The video is a 2D side view with a static camera, running at 24 fps. question_fps is also 24, so there is no timing ambiguity.
The prior is the black cat's speed, 0.94 m/s. The cat walks steadily with no starts or stops.

## Cat speed in pixels
- From the record's `tracks/cat.csv`, the linear-fit slope is 17.65 px/frame for `cx`, 17.80 for `dark_cx` and 17.56 for `bbox_cx`.
  Mean per-frame steps fall between 17.5 and 17.8.
- Independent check (`check.py`): I took the centroid of the black fur in the body band y = 820–905, which keeps clear of the
  console's black base, and measured it against the per-pixel-maximum background. Its mean step is 17.63 px/frame and its fit slope is 17.82.
- Adopted value: 17.7 px/frame, which is 424.8 px/s.
- Scale: 0.94 / 424.8 = 2.213e-3 m/px.

## TV stand width in pixels
- The record's bounding box runs from x = 651 to 1422, which is 772 px. My max-image row scans give 659–1413 at the top
  (y = 790) and 657–1422 at y = 850. I used the full axis-aligned extent of 772 px.

## Answer
Length = 772 × 2.213e-3 = **1.71 m**. That is a plausible size for a TV console.

## Confidence
Moderate to high. The speed has about ±1% uncertainty and the width about ±1%. The main risk is perspective: the cat walks about 30 px
lower in the image than the furniture feet, so it may be slightly nearer the camera. If so, its pixel speed would be slightly
inflated and the true length a little larger. Following the 2D convention, I applied one scale to both.
