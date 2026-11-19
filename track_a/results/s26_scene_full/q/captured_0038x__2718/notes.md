# Q2718 – distance between the white cup and the pink bottle (cm)

The file and the question both run at 24 fps, and both objects are static. t = 1.4 s → frame 34.
Camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360).

## Pixel centres (measure.py: HSV masks on frame 5, checked against a zoomed crop of frame 34)
- Pink bottle: x 642-688, y 330 (top) to ~480 (base, partly hidden by the standing card) → centre (665, 405).
- White cup: x 724-794 at the top and 732-787 at the base, y 375-497 → centre (759, 436).

## 3D (dist.py)
Back-projected the unit ray times the depth_info distance (0.9998 m for the bottle, 0.8740 m for the cup),
then took the Euclidean distance between the two points: 17.34 cm.
- Moving the centres by ±2-5 px gives 17.23-17.34 cm.
- Most of the distance comes from the depth gap (12.6 cm); the side-to-side offset adds about 11 cm.

## Checks
- The dark card's 102 px bbox at 0.6867 m gives 9.2 cm. It is a loose bbox (it includes the sticker region),
  but it is the right size for the 8.56 cm card, so the f scale is plausible.
- Using the different pixel-centre variants above changes the result by less than 1 %.

Answer: 17.3 cm. Confidence moderate to high. The result depends mostly on the given depths.
