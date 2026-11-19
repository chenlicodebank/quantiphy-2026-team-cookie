# q_2318 – tennis ball diameter (cm)

The tennis ball is scene/ `green_ball`: the yellow-green ball the near (right) person holds at her fingertips and drops at f27.
depth_info has no distance for it, so I estimated its depth from the scene. The file and question_fps are both 24 fps.
Camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360).

## Pixel diameter (measure.py, diam.py)
- Equivalent diameter from the mask area (colour mask and background-difference mask): held f0–3 = 20.6–21.3 px,
  near the apex f43–46 = 19.8–21.6 px. Frames where the hand merges with the mask (f6, 7, 9 and f10–16) are excluded.
- I used **20.8 px**.

## Depth of the ball (camera z)
1. **Ground contact (main route).** Camera height H comes from the far person's shoes (row 577, z = 3.13/1.055 = 2.97 m),
   giving H = 0.844 m. The near person's feet (rows 670–716, z ≈ 1.8–2.1) and the soccer-ball bounce agree.
   - Fitting a parabola before and after the bounce puts contact at centre ≈ 605 px. That matches f36, where the
     ball's bottom is flattened at row ≈616.
   - Bottom ≈ 615.5 gives z = 0.844 x 763 / 255.5 = **2.52 m**.
   - Including the bounce frame this way assumes no dropped frame there. The ball's track fits that.
2. **Gravity prior.** Fitting a parabola to the fall gives a = 2983 px/s² over f30–35, or 2757 px/s² over f31–35.
   Z = g·f/a = **2.51–2.71 m**. (f28–29 are part of the release push, so I left them out.)
   - The same method on the soccer ball gives 2.62 m against its given z = 2.76 m.
   - The rise after the bounce gives 2.9 m. The ball looks slightly smaller near the apex, so it may have moved away
     after the bounce.
3. **Arm-geometry sanity check:** about 2.1–2.45 m, a rough figure.

I chose z ≈ 2.52 m, so the Euclidean distance is ≈ 2.55 m.

## Result
D = 2.52 x 20.8 / 763 = 6.87 cm. Using the Euclidean distance it is 6.95 cm.
Over the range z = 2.5–2.7 m it is 6.8–7.4 cm. A real tennis ball is 6.5–6.9 cm, which fits.

**Answer: 6.9 cm.** Confidence: moderate (about ±8%), because the depth had to be inferred.
