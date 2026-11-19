# q160: car length (prior: car speed = 30 m/s)

This is a 2D side-view clip at 24 fps (the file and the question agree). The scale comes from the car's own pixel speed.

`measure.py` segments the car on every frame by its difference from the background (y > 590, threshold 20).
- **Pixel speed.** Fitting lines to the unclipped frames 11–37 gives 28.40 px/frame for the bbox centre, 28.37 for the centroid, 28.54 for the rear edge and 28.26 for the front edge. Fitting frames 25–37 only gives 28.41 for the centre and 28.39 for the centroid. I used 28.40 px/frame = 681.6 px/s.
- **Scale.** 30 / 681.6 = 0.04401 m/px.
- **Length.** The bbox length is 137–138 px near the left edge, where perspective inflates it. Near the image centre (frames 29–37) it is 130–132 px; the scene record gives 130. I used 130.5 px.
- **Result.** 130.5 × 0.04401 = **5.74 m**. The range across the 130–132 px readings is 5.72–5.81 m.

**Check.** A second route also works: the bbox-centre and centroid speeds agree to 0.1 %, and the slopes from the late window and from the full window agree. The result is also plausible: the Cybertruck-like truck is about 5.7 m long in real life.

**Confidence:** high (about ±2 %).
