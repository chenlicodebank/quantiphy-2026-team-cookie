# Q3080 – distance between kettle and plate (cm)

- The "plate" is taken to be the white wavy bowl/dish at the far left. The kettle is the red Tefal kettle. The question gives no depth info, so I used one planar scale (internet convention). The time base is 30 fps: the file and the question agree.
- **Scale from the gravity prior** (`gfit.py`): I fitted a quadratic to the ball's image y on each bounce arc, using only measured frames (no arc-fill rows, no bounce frames). Clean arcs give 20.23, 19.80, 18.84, 19.44, 19.12, 19.09 and 20.47 px/frame², mean 19.57. I left out the arc at frames 124-131, which is in front of the white bowl and badly segmented (25.0). 9.8 m/s² = 19.57 × 900 px/s², so the scale is 0.000556 m/px.
  - Check: the ball's diameter of about 76 px comes out at 4.2 cm, close to a real 4.0 cm table-tennis ball, so the scale is plausible.
- **Positions** (`objs.py`, frame 195, colour masks plus a grid check):
  - Kettle bounding box: x 1159-1514, y 508-796. Centre (1336, 652); the mask centroid is (1326, 653).
  - Bowl: x about 117/125 to 500/510, y about 640-805. Centre about (312, 722).
- **Centre-to-centre distance**: about 1026 px, which is 57.1 cm. Using the kettle's mask centroid gives 56.6 cm.
- **Other readings**:
  - Using the centre of the kettle body without the handle gives 54.1 cm.
  - The edge-to-edge gap gives 36.4 cm.
- **Answer**: 57 cm, centre to centre.
- **Confidence**: moderate. The scale is good to within about 3%. The main uncertainty is which reference points the annotators used for "distance".
