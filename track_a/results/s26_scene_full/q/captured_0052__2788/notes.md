# q_2788: distance between basketball and shoe (m)

- The basketball and the shoe are both static. The file and the question are both 24 fps, so t = 1.0 s is frame 24.
- Pixel centres come from the colour masks in scene/static_measure.json, which agree at frames 0, 24 and 47.
  I checked them on zoomed crops (frames/bb.png, frames/shoe.png):
  - basketball (800.6, 667.4); bbox 756-847 x 624-709
  - shoe mask centroid (284.2, 653.5); shoe bbox centre (286.5, 650.0)
- Lab camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
- Depths from depth_info: basketball 1.9365 m, shoe 2.2310 m.
- Back-projection follows the method card, P = ((u-cx)/f, (v-cy)/f, 1) x depth:
  - basketball (0.408, 0.780, 1.937)
  - shoe (-1.041, 0.858, 2.231)
  - distance = **1.480 m** (1.473 m with the shoe bbox centre)
- Other reading: if depth is the Euclidean distance along the ray, the distance is 1.27 m. I rejected it because the
  z-depth reading gives a basketball diameter of 1.9365 x 92 / 763 = 0.234 m, close to a real basketball (0.24 m).
  The Euclidean reading would give about 0.21 m.
- Answer: 1.48 m. Confidence: moderate-high. The depth convention is the main uncertainty.
