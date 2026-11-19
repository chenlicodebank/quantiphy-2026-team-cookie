# Q1091: width of the pedestal (square base) of the central sculpture

Answer: **1.46 m**

## Setup
- 3D Blender scene. The image is rotated 90° (world up = image −x). The camera is static.
- Time base: t=1 s gives frame 33 at either 33.26 or 33 fps, so the choice of rate does not matter here.
- The pedestal is the dark charcoal box under the sculpture. Its front face spans:
  - y 446.6–747.2, so its horizontal width is **300.6 px**. The edges were measured in code by threshold crossings at every 5 px of x (`box_edges.py`).
  - x ≈ 763 (top) to **896.3** (floor contact line). This was measured at every 20 px of y (`box_edges2.py`).
- The vertical edges of the box are exactly parallel: the y edges change by less than 0.7 px over 120 px.
  - The bottom-edge x is the same (±0.3 px) across the face.
  - So the camera pitch is about 0, and the box face is parallel to the image plane with no yaw.
  - The side edges of the top face converge to roughly the image centre (540, 540), which agrees with zero pitch.

## Focal length (`focal.py`)
- The person walks parallel to the image plane, so their camera-axis depth Z is constant.
- Fitting the given distances 6.84 m (t=0, pelvis at (655.5, 197.7)) and 6.49 m (t=1, pelvis at (657.5, 382.0)) gives **f ≈ 888 px (±20)** and Z_person ≈ 6.34 m.
- Check: 1.87 m × 888 / 6.34 = 262 px, close to the measured standing height of the person in the image (257–261 px). The two references agree.

## Route 1: floor geometry (does not depend on where the pedestal's origin is)
- Camera height:
  - h = (feet x − 540) × Z / f = 243 × 6.34 / 888 ≈ 1.735 m.
  - Independent check from the height ratio: 1.87 × 242 / 260.5 = 1.737 m.
- The pedestal's front face sits on the floor at x = 896.3. Its depth is Zf = h·f / 356.3 ≈ 4.32 m.
- W = 300.6 × Zf / f = 300.6 × h / 356.3 = **1.464 m**.

## Route 2: the given pedestal distance of 5.085 m
- The origin is at the centre of a square base, so its depth is Zc = Zf + W/2. The result depends on the origin's height:
  - Origin at the bounding-box centre of sculpture plus pedestal (image x ≈ 644): Zf = 4.318, W = **1.467 m**.
  - Origin at the centre of the dark box: W = 1.42 m.
  - Origin on the floor: W = 1.395 m.
- The sculpture and the pedestal have the same given distance, which suggests they share one origin.
- The bounding-box-centre case matches Route 1 almost exactly.

## Confidence
- Answer: 1.46 m, uncertain by about ±3%.
- The main sources of error are f (about ±2%) and the person's foot and pixel-height measurements.
- The lighter stone slab on top of the dark box is narrower (about 259 px across its face, and set back). It is not the square base.
