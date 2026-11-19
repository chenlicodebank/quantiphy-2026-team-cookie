# q_1322 – length of the turning yellow car (taxi)

Answer: **4.90 m**

The file and the question both run at 24 fps, so frame = round(t × 24): t=0.58 s is f14 and t=1.58 s is f38.
This is a 3D Blender scene with a static camera, 2160x1080, principal point taken at the image centre.

## Focal length (two independent routes)
1. **Cross-street curbs** (`curbs.py`). I fitted the near-right sidewalk curb (slope -0.0385) and the far curb
   (slope -0.0267) myself on frame 0. Both lines meet the horizon at x≈20800, and they cross each other at y=-203,
   which matches the forward-road horizon at y=-208 from the scene record. If the streets are perpendicular, the
   forward vanishing point (800,-208) and the cross-street one (x≈20800) give f = 2226 px (near curb) and
   2229 px (far curb).
2. **Pedestrian depth_info** (`ped.py`, `zratio.py`). The pedestrian walks sideways, and their distance goes from
   25.357 m to 25.920 m. The change in camera Z comes from the image: for a point at constant height,
   Z ∝ 1/(v − y_horizon), using linear fits of the pelvis, head and feet rows. Matching that gives
   f ≈ 2250 px (2210–2320 for horizon −150…−260).
   The objects that move straight away (van, cyclist) are too sensitive to the horizon position to use here.

I used f = 2235 px (horizontal field of view ≈ 52°). As a sanity check, the pedestrian then comes out about 1.75 m tall.
The van's acceleration hardly depends on f, because its displacement is fixed by the depths. Measured from the
depths and the image track it is 3.4–3.6 m/s², a little under the 4 m/s² prior. So the prior cannot fix f, and
the scale comes from depth_info.

## Distance to the taxi when it is side-on
- Side-on frames f62–70: the bumper-to-bumper pixel extent is **421 px** in every frame. My own background-difference
  mask (`taxiseg.py`, overlay in `frames/taxi65_mask.png`) and the scene track agree on this.
- Road plane taken from the taxi itself (`length2.py`). At f38 I read the near-side tyre contacts at (1302,516) and
  (1490,477). The ground centre is the midpoint of those plus half a track width. Scaling so the origin sits at the
  given 27.0055 m gives the road-plane constant K = H·f/cosθ = 18427. This lies between the van-based value
  (18045) and the pedestrian-based one (18982 without a curb, about 19300 with a 0.15 m curb).
- At f65 the near-side tyre contacts are (1559,469) and (1784,462). This puts the taxi's ground centre at Z = 28.09 m
  (camera distance 29.0 m), heading within 1° of the cross street.

## Length
- I modelled the car as a rounded-rectangle footprint: width 0.37 L, corner radius 0.05 L, ends sampled at bumper
  heights. I solved for the L whose projected horizontal extent is 421 px.
- The camera sees the rear face, which makes up about 40 px of the 421, so the plain formula 421·Z/f (5.29 m)
  overestimates.
- Result: L = 4.886 m if the origin is at ground level and 4.920 m if it is at the body centre. Mean **4.90 m**.
- How much the answer moves: tyre rows ±3 px give ±0.02 m; width ratio 0.33–0.40 gives +0.03/−0.04 m;
  corner radius 0–0.10 L gives −0.13/+0.13 m; f 2227–2250 gives 4.92–4.87 m.
- Earlier routes: a plane through the taxi's bbox-centre points, or a camera height taken from the van, put the taxi
  1–4% nearer or farther. I treated those as noisier because of how the bbox centres and the van's tyre rows are
  defined.

Confidence: moderate. The likely error is about ±4%, mostly from the car-shape model of the extreme points and
from f.
