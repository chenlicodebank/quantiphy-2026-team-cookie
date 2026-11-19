# simulation_0197 — measurement record

2D simulation (Blender) close-up, 2560x2560, 30 fps, 50 frames (t = frame/30, 0–1.633 s). Static camera.

## Scene
A white dropper cap with a glass pipette is held tilted (tip lower-left, ~31° below horizontal) above an open,
frosted, amber-filled "NOVA / RADIANCE / VITAMIN B" bottle. The pipette holds amber serum; **one air bubble** inside
the liquid slides down the pipette toward the tip. A teardrop of serum hangs from the tip and never detaches.
The only moving object is the bubble. Light-beige wall with diagonal shadow stripes behind.

## Files
- `scene.json` – inventory, static extents, camera, events (all in pixels / seconds).
- `tracks/bubble.csv` – per frame 0–49: frame, t_s, centroid (cx, cy), bbox, length_px (along the long side of the
  min-area rectangle, ~the pipette axis), width_px, height_px (vertical bbox extent), area_px, occluded flag (always 0).
- `scripts/diff.py` – frame-difference survey (found that only the bubble region changes).
- `scripts/track_bubble.py` – bubble tracking; writes the CSV and `frames/bubble_check.png` (mask overlays).
- `scripts/events.py` – per-frame displacement / projection on the motion axis (used for event frames).
- `scripts/check_global.py` – camera-shift check (phase correlation).
- `scripts/crops.py` – crop viewer.

## How measured / reliability
- Bubble: background = per-pixel median of a ROI (x 300–1100, y 1150–1700) over all 50 frames; mask = |frame−median|
  > 25, close/open, largest component, convex hull. Centroid = hull centroid (≈ bubble centre). Overlays checked at
  frames 0, 7, …, 49: masks hug the bubble well. Centroid noise ≈ ±1 px; motion is along a straight line (perpendicular
  deviation ≤ 5 px; slight bump frames 34–41 when the bubble shifts toward the tube's lower wall).
  Last frames (≥ 42): bubble enters the tapered tip region; the hull includes some glass highlight, so size there is
  ±5 px and centroid ±2 px.
- Bubble size: ~105–110 px along the axis, ~88–100 px across (includes refraction rim); equivalent circle diameter
  ~103 px; roughly constant (2D scene, no depth change).
- Bubble motion: net 410.6 px, path 413.3 px, direction (−0.855, 0.519). Starts from rest ~frame 1–3, accelerates to
  ~12 px/frame by frame ~17, ~steady to ~31, decelerates and nearly stops by frame 47 (≤ 1.7 px/frame for 47–49).
- Static objects were read from 50/100 px grid overlays at frame 0 (±10 px for sharp glass edges, ±20 px for the
  low-contrast white cap). Pipette visible length ~1378 px (tip (205,1700) to cap entry (1380,980)), outer diameter
  ~145 px; hanging drop 225 px tall × 105 px wide; bottle body 1160 px wide, neck 780 px wide; cap ~1070 px long,
  opening ellipse major axis ~730 px.
- Camera: static (shift < 0.01 px). Frames 17–18 show a tiny global intensity change from render noise, not motion.

## Ambiguities
- Only one bubble; the round highlight is the bubble itself (no second bubble). The drop at the tip is static — not
  a falling object. The liquid meniscus (~(920,1330)) does not visibly move.
- Since the scene is 2D, any metric answer should use one m/px scale from the question's prior object (e.g. the
  bubble diameter ~103 px, the pipette, the drop or the bottle widths above).
