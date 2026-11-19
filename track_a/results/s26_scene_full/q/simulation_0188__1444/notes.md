# Q1444 – width of the truck (simulation_0188)

Prior: the truck's acceleration is 10.757 m/s². Depth info: the distance from the camera to the truck centre is 22.532 m at t=0.5 s (frame 15) and 19.525 m at t=1.0 s (frame 30).
The file and the question both use 30 fps, so frame = round(t·30).

## Geometry (scripts here: kin.py, model.py, frontvp.py, sidevp.py, tri.py, proj.py, rightedge*.py, boxrear*.py, cabside.py, boxfrontleft.py, boxright*.py)
- The camera is static and level. Side edges of the box (top and bottom, fitted sub-pixel on frames 34–43) are fixed image lines that meet at VP_L = (−3165, 539). That gives the horizon at y = 539. Because the edges stay fixed, the truck moves exactly along its own axis.
- Front-face horizontal edges (grille top and bottom, frames 30–43) meet each other on the horizon (y = 539.3) at VP_R ≈ (2670, 539).
  So f = sqrt((960 − VP_L)(VP_R − 960)) ≈ 2656 px, an HFOV of about 40°.
- The front-hub track (frames 0–46) lies on a horizontal line Yp below the camera, with Z = f·Yp/(y−539). Its path is s(t) = ½·a·t², starting from rest at t = 0, with a 0.4 cm rms fit.
  Setting a = 10.757 gives Yp = 1.938 m. Every metric value then follows from this, with only a weak dependence on f.
- Check of the scale against depth_info: with the origin at the truck's bbox centre, the predicted camera distances need a scale factor k = 1.011 (t=0.5 s) and k = 1.013 (t=1.0 s). So the depths and the acceleration prior agree to about 1%.
- Lateral positions (along the horizontal normal to the truck axis) come from triangulating rigid points with the known metric motion s(t)·d:
  - Box left side: 12.58 from the rear top light (0.3 px rms) and 12.59 from the box rear-left silhouette.
  - Cab left side lamp: 12.72. Front hub: 12.69.
  - Cab right silhouette: 14.64 (0.14 px rms, several heights).
  - Box right-front edge: about 14.63. This is the light-to-dark edge on frames 2–10 and about x≈742 on frame 30, using the box front plane at along −0.52 m from the box front-left crease triangulation.
  - Right mirror outer silhouette: 14.96 (three rows, ≤1 px rms).

## Widths under each reading
- Body (box and cab, no mirrors): 14.63 − 12.59 ≈ 2.04 m. The cab is about 1.92–2.0 m.
- Full AABB including the side mirrors: the right mirror sits 0.33 m outside the body side. Assuming a symmetric left mirror (truck centre at 13.61–13.68), the span is 2·(14.96 − c) ≈ 2.56–2.70 m, centre value ≈ 2.63 m.
- Rail/platform extents measured on the right (14.32, about 14.85) are inside the mirror line.

## Answer
The reference sizes are the world-space AABB of the object, which includes the mirrors attached to the cab. Answer: **2.6 m**. If the mirrors were excluded, the body width would be about 2.05 m.
Confidence: medium. Scale and focal length are good to about 2%. The main uncertainty is whether the mirrors count, and the left mirror is assumed symmetric rather than measured.
