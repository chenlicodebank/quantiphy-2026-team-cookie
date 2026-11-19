# q_2543 — diameter of the white ball (cm)

The question's fps and the file's fps are both 24, so t = 1.5 s is frame 36. Lab camera, f = 0.5959 x 1280 = 762.75 px.
The white ball is the ping-pong ball (depth 1.353 m at t = 1.5 s). The yellow ball is the tennis ball (6.7 cm, depth 1.183 m).

## Measurement (frame 36; scripts measure.py and edges.py; overlays in frames/zoom_36.png and frames/edge_36.png)
- The white ball rolls mostly horizontally (about 8 px/frame in x and about 2 px/frame in y), so motion blur makes it wider but
  barely taller. The SAM mask halo outlines the ball.
- Vertical extent (from the raw pixel profile): the top is at y ≈ 422.5 (the sky/ball boundary) and the bottom halo is at
  y ≈ 444. This gives 21–22 px.
- The horizontal halo extent is x ≈ 709.5–735.5, about 26 px including blur. Removing the blur using the ratio of the x and y
  speeds gives about 20.4 px.
- A circle fit to the halo points (edges.py) gives 23.1 px at f36 and 22.7 px at f37, but blur widens these fits.
- Adopted diameter: 22 ± 1 px. D = 1.353 m x 22 / 762.75 = 3.90 cm (range 3.81–4.08 cm for 21.5–23 px).

## Check against the prior
- Yellow ball at f36: width across the motion is 42.7 px. 1.183 x 42.7 / 762.75 = 6.62 cm, against the prior of 6.7 cm.
  So the method reads about 1.2 % low; correcting for that gives 3.95 cm.
- Second route (white ball at rest at the back, 17–18 px, with ground-plane depth taken from the tennis ball at rest):
  about 3.77 cm. This route is sensitive to the horizon estimate, so it is used only as a rough check.
- Sanity check: a real ping-pong ball is 4.0 cm, which agrees.

Answer: 3.95 cm. Confidence: moderate-high (about ±4 %).
