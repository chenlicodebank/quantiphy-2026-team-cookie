# Q2320 – shoe length of the left person (cm)

Left person = the far person (405 px tall vs 615 px) -> depth_info distance_far_person_camera = 3.130 m.
Lab camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360). question_fps = file fps = 24.

## Measurement (shoe.py, crop.py; frames/c12, c24, c40, c48)
- The feet do not move over the clip (row-wise extents identical in f12, f24, f40, f48).
- Shoes (white with black three stripes) seen nearly side-on, toes pointing right. Front (nearer, lower) shoe:
  heel x ≈ 347-348 (y≈564), toe tip x ≈ 399-400 (y≈571) -> extent ≈ 53.5 px (slight downward tilt, ~13 px
  vertical over the length, mostly sole width/perspective). Back shoe: toe at x=420, heel hidden; stripe centre
  at x≈392 implies heel ≈364 -> ≈56 px, consistent.
- Method card: L = 3.13 x 53.5 / 763 = 0.219 m (with 56 px: 0.230 m).

## Second route (ground-plane geometry)
- Pelvis ray (u≈400, v≈375) with Euclidean depth 3.13 -> Z ≈ 2.985 m; shoe bottoms at v≈577 give camera height
  ≈ 0.85 m above the floor (level camera assumed). Person height 405 px -> 1.58-1.66 m (plausible).
- Back-projecting heel (349,571) and toe (399,574) onto the floor: Z 3.07 / 3.03 m, X -1.17 / -0.95 m ->
  length ≈ 0.221 m, yaw ≈ 11° toward the camera. Very sensitive to 1 px in v (≈1.4 cm in Z).

## Answer
Routes give 22-23 cm; a real adult women's shoe is typically 24-26 cm, so I lean slightly up: **23.0 cm**.
Confidence: moderate (±10%); main uncertainties are the blurred heel/toe edges (~±1.5 px) and the shoe's yaw.
