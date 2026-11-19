# q466 — width of the box (simulation_0191)

Question: "What is the width of the box in meters?"  Prior: box acceleration before 0.6 s = 9.8 m/s² (free fall).
No depth_info. File fps = question fps = 120.

## Reading of "width"
The box's front face (facing the camera) is the long side: 408 px horizontally, 191 px tall. Following the naming rule
(length = longer horizontal extent, width = shorter one across it), width = the box's front-to-back depth (into the
image), which is shorter than the length (see below). Other reading (visible horizontal extent) = 408 px × 0.00496 =
2.02 m (that is the length).

## Scale from the prior (measure.py)
Template-tracked front-face centre cy (scene/tracks/box.csv; I checked it against my own edge crossings, within ~1 px).
Quadratic fit over frames 2–58: a = 0.1372 px/frame² = 1976 px/s², the same to ±0.1% for windows 0–60, 5–59 and 10–55.
→ s_b = 9.8/1976 = 0.00496 m/px at the box's front-face plane. Box length 408 px = 2.02 m, face height 191 px = 0.95 m.

## Box depth/distance ratio (kappa.py, extent.py)
The box is above eye level while it falls, so its underside shows as a strip below the front face. The strip shrinks
linearly as the box falls: strip = kappa·(v0 − y_bottom), with kappa = D/(Zb + D).
- Silhouette bottom (saturation crossing against the background) regressed on the tracked cy, frames 0–52, slope = 1 − kappa:
  kappa = 0.0938 (bands 600–850 give 0.0928–0.0950, rms 0.2–0.35 px), horizon v0 ≈ 520.
  → D/Zb = 0.1035 ± 0.0015.
- Check: total silhouette height against the top edge (frames 30–52) gives kappa 0.089–0.095. The left underside edge
  slants toward a vanishing point near (945, 520).

## Focal length / metric depth: the hard part
D = 0.1035·Zb = 0.1035·f·s_b, so I need f (no depth_info is given).
- The two small dark "jacks" are the far-side twins of the red-footed stabilizer legs: same foot width ×0.87, and they
  sit at mirrored x offsets toward the centre. Depth ratio r = Z_near/Z_far: 0.865 from the x spacing
  ((1241.5−553.5)/(1282.5−487.5)) and 0.8685 from the ground-contact rows ((995.5−520)/(1067.5−520)).
  → leg spread / Z_near = 0.1534.
- At rest the box's front-bottom edge (406.4) sits 3.4 px above the roof edge (409.8), so the box overhangs the truck
  side a little: Zb ≈ 0.97·Z_truck-side. The near feet are about in the truck-side plane, judging by the ground rows
  of the feet and the tyres.
  → D ≈ 0.1035·0.97/0.1534 × leg spread = 0.654 × leg spread.
- Metric anchor (assumption): the truck is real scale (8.6 m long, 3.65 m tall, 0.84 m wheels at this scale). A
  catering truck body is ~2.45–2.5 m wide, and the outboard legs are spread ≈ 2.2–2.3 m. I took a spread of 2.25 m,
  which gives f ≈ 2870 px (hFOV ≈ 37°), Zb ≈ 14.2 m and D ≈ 1.47 m.
- Independent f check: the top of the red pad is a horizontal circle (a ≈ 20.5 px, minor semi-axis ≈ 3.3–4.3 px at
  537 px below the horizon). That gives f ≈ 2550–3400 px, so D ≈ 1.32–1.75 m. It agrees, but is loose because the
  pad's exact shape (flat or conical) is unclear.

## Answer
Width (front-to-back depth) ≈ 1.47 m. The box is 2.02 m long × 1.47 m wide × 0.95 m tall.
Confidence: moderate. The depth/distance ratio (±2%) and the gravity scale (±0.5%) are solid. The focal length relies
on a real-size assumption about the truck's leg spread (±10%), which the pad-ellipse route supports.
