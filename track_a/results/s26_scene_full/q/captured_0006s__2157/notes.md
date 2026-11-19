# Q2157 – width of the toy (cm)

The toy is the yellow toy fruit (the only moving object). The depth_info distances for the "ball" are the distances to this object.
File fps = question_fps = 24, so t=1.0 s is frame 24 and t=1.2 s is frame 29 (round(28.8)).

Method (lab card): f = 0.5959 x 1280 = 762.8 px. Width = depth x minor pixel extent / f.
measure.py builds the mask from the difference to frame 48 (the toy is out of frame there), then takes the largest blob and its min-area rectangle.

- f24 (Z = 1.402 m): minor axis 55 px (bbox 60x56) -> **10.11 cm** (bbox_w reading gives 11.0 cm)
- f29 (Z = 1.065 m): minor axis 73.1 px (the long axis is motion-blurred, 96 px) -> **10.21 cm**
- Second route: the two depths and two frames are independent, and they agree to 1%. The by-eye readings on the zoomed f24 crop (~56-57 px) agree too.
- The prior (g = 9.8 m/s^2) is not needed for this size.

Answer: 10.2 cm (the shorter extent across the elongated toy). Confidence: good, about ±5%. The segmentation rim and the toy's tumbling orientation are the main sources of uncertainty.
