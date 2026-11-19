# q_1790 — shark length (prior: boat length = 10 m)

2D side-view clip at 24 fps (the file rate matches question_fps). Both objects lie in one plane facing the camera, so a single metres-per-pixel scale applies.

Method: `measure.py` segments the non-white pixels (min RGB < 238 or saturation > 25, 3x3 opening) and splits the image at y = 740 into the boat (above) and the shark (below). It measures each object's horizontal extent in frames 0–44, every 4th frame. In these frames both objects are fully inside the image.
- Boat stern-to-bow: 856–860 px, median **857 px**. Using hull rows only gives the same extent. This matches the scene record.
- Shark snout-to-tail: 276–280 px, median **278 px**. This also matches the record, which includes the pale snout.

Scale: 10 m / 857 px = 0.01167 m/px. Shark length = 278 × 0.01167 = **3.24 m**.

Check: the frame-by-frame ratio stays between 276/860 and 280/856, which gives 3.21–3.27 m. A 3.2 m shark next to a 10 m boat is plausible.

Confidence: high, about ±2%.
