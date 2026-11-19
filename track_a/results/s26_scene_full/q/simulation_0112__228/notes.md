# q_228 - height of the car (prior: speed 6.66 m/s)

Time base: file fps 24.007 and question fps 24.0 differ by 0.03 %, which is negligible. I used the file fps.

Method (2D one-scale convention, measure.py):
- The car moves uniformly left to right in a side view, and the camera is static (from the scene record, which I checked
  on frames 12, 24 and 38).
- Pixel speed is a linear fit over frames 13-36, where the car is fully visible.
  - Near-side wheel hubs: 28.21 px/frame.
  - Car centre plane (the origin depth; parallax-corrected for a far/near depth ratio of about 1.09): 27.00 px/frame.
- Scale = 6.66 / (27.00 x 24.007) = 0.01028 m/px at the car's centre depth.
- Height in pixels: the silhouette runs from roof y about 412-415 to tyre bottom y 539, so 126.5-127.5 px. I used 127 px.
  - The tyre bottom sits at the image-centre row, so the camera is at about deck height. The roof crest lies at the
    car's centre plane, so the centre-plane scale applies to the pixel height.
- Height = 127 x 0.01028 = 1.30 m.

Second route / sanity check:
- Using the near-side hub speed instead gives 1.24-1.25 m. This is the lower bound if all parallax is ignored.
- A Porsche 911 (930) is really about 1.31 m tall, which agrees with the centre-plane result.

Answer: 1.30 m. Confidence: moderate-high (about ±4 %).
