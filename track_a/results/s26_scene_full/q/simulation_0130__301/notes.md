# q_301 – length of the car (simulation_0130)

**Object.** The only car-like vehicle is the small dark vehicle towing the airliner up stand 01 (x ≈ 475). Seen from above, it looks like a forklift or tug:
- dark roof/guard with a beacon dot;
- yellow-orange trim;
- a grey rounded counterweight at the rear (toward the plane);
- two orange forks/prongs sticking out in front (x ≈ 470 and 481).

The white two-rail towbar runs from its rear to the plane nose. The forks are attached only to the vehicle and end freely in front of it, so I count them as part of the car's model.

**2D scene, scale from the prior.** The view is straight down with no perspective and a static camera.
- The car moves at a constant speed. Over frames 1–71: 5.2463 px/frame (tug track) and 5.2466 (plane track). The first and second halves agree to 0.005 px. My own check of the body front edge gives 774.5 → 407.5 over 70 frames, i.e. 5.243 px/frame. Frames 0 and 1 are identical.
- Pixel speed = 5.2465 × 24 = 125.92 px/s.
- Scale = 11.155 / 125.92 = **0.08859 m/px**.
- Sanity check: plane length 423 px × 0.08859 = 37.5 m, close to an A320 (37.57 m). The scale is realistic.

**Pixel length** (`measure_tug.py`, `measure_prongs.py`): difference from a background frame, and orangeness R−B along the prong columns.

| frame | prong tip y | body front y | body rear y | body length | with forks |
|---|---|---|---|---|---|
| 0 | 751.5 | 774.5 | 824.5 | 50 px | 73 px |
| 20 | ≈651.5 | 675 | 725 | 50 px | 73.5 px |
| 30 | – | 622.5 | 672 | 49.5 px | – |
| 60 | – | 465 | 515.5 | – | – |
| 71 | – | 407.5 | 457 | 49.5 px | – |

The video was rendered at half resolution: rows and columns come in duplicated pairs. Each edge is therefore uncertain by about ±1 px.

**Results**
- Including the forks (the reading I chose, the full bounding box): 73 px × 0.08859 = **6.47 m**.
- Body only, without the forks: 49.8 px × 0.08859 = 4.41 m.
- Width: 25 px ≈ 2.2 m.

**Second route.** The length was measured on independent frames (0, 20, 71). Body and total lengths agree to within 0.5–1 px. The scale also gives a realistic airliner length.

**Confidence.** The scale is reliable to about 1%. The main uncertainty is whether the reference bounding box includes the forks (about 60–65% likely, I think). If it does not, the answer would be 4.41 m.
