# simulation_0244 – measurement record (pixels, seconds)

Video: Blender render, **2D scene**, 1080x1920 portrait, 30 fps, 75 frames (t = frame/30, 0 … 2.467 s).
Coordinates: x right, y down, origin at top-left, full-resolution pixels.

## Scene
A forest road leading to a snowy mountain peak, with conifers on the left and right, bushes on both sides, and a wet road with puddles that reflect the animals.
Two animals cross from left to right, parallel to the image plane, for the whole clip:
- **creature**: a large horned deer/ibex-like fantasy animal. It has a brown body, a white chest mane, long ridged horns that curve backwards, and a long tufted tail. It walks steadily from left to right and is visible in every frame (0–74).
- **rabbit**: a small orange-brown hare/rabbit. It hops along the road just in front of and right of the creature at a nearly constant height (centroid y ≈ 1517, feet ≈ 1547). It is fully inside the frame for frames 0–69, starts leaving at the right edge at frame 70 (bbox x1 = 1079 from frame 71), and is mostly out of view by frame 74. In the image, the two animals never overlap.
Both animals move at almost the same image speed, about 6.3–6.6 px/frame (≈ 190–200 px/s). This is given as context only; fit your own motion.

The camera is **static**. Phase correlation between frame 0 and frame 74 (y < 1000) gives a shift below 0.01 px. Their sky difference has a median of 2 grey levels.
Perspective: the road recedes towards about (530, 1400), but the animals move sideways at a fixed depth. The creature's hooves stay at y ≈ 1544–1549 and the rabbit's feet at ≈ 1547, so they are at roughly the same depth. Their apparent sizes stay constant over time; a single metres-per-pixel scale fits both (2D convention).

## Files
- `scene.json`: inventory (moving and static objects), events, camera, and summary statistics.
- `tracks/creature.csv`: one row per frame (0–74). Columns:
  - `cx, cy`: centroid of the foreground mask.
  - `bbox_cx, bbox_cy`, `x0 y0 x1 y1`: bounding box.
  - `length_px` (horizontal bbox extent, which is the main axis) and `height_px` (horn tip to lowest hoof).
  - `area_px`.
  - `torso_band_*`: mask extent and mean x within rows y 1290–1420, roughly the body level including the tail root and upper legs.
  - `touches_right_edge`.
- `tracks/creature_landmarks.csv`: **the best reference points for the creature's position.** Body patches (`hip`, `body_mid`, `shoulder`) are tracked by template matching with sub-pixel peaks, plus a match score (0.75–0.99).
  - Shoulder x moves very steadily: 425.0 → 913.6 px over frames 0–74, median 6.6 px/frame, range 5.8–7.4.
  - Hip x is similar on average (260 → 758) but oscillates with the gait (2.5–10.9 px/frame).
  - The rig origin of a walking animal is probably near the pelvis/body centre. Any rigid body point gives the same mean translation; use `shoulder_x` or `body_mid_x` for smooth speeds, and the hip if a question needs the pelvis.
- `tracks/rabbit.csv`: same columns as the creature track (no torso band), plus `near_creature_leg`. That flag is 1 when other foreground lies next to the rabbit box (frames 46–49, 52–55, 58–60). It is a crude touch indicator; there is no real occlusion. In frames 70–74 the rabbit is cut off by the right edge, so its centroid and bbox there are biased to the left.
- `scripts/`:
  - `bg.py`: builds a clean background plate (frame 0 for x ≥ 540, frame 74 for x < 540, and a median of frames 14–74 in the frame-0 rabbit box). It writes `frames/bg_full.png`, which `track.py` needs.
  - `track.py [thr=16]`: foreground masks, rabbit/creature split, CSVs and overlays.
  - `landmarks.py`: body patch tracking.
  - `check_landmarks.py`, `views.py`: visual checks.
  - `summarize.py`: writes `scene.json`.

## Sizes (pixels)
- **Creature** bbox (includes horns, tail and legs, comparable to a world AABB):
  - Height: median 421 px (p10–p90: 410–426). Top (horn tip) at y ≈ 1122–1139; hooves at y ≈ 1544–1549.
  - Length (tail tip to nose/horn front): median 486 px, varying 389–563 with the tail swing and leg stride. Frame 0 ≈ 401 px (145–546); frame 74 ≈ 493 px (548–1041).
  - Shoulder-to-hip patch separation is about 155–165 px.
  - The mask may miss part of the dark grey muzzle and dark lower legs on the dark road, so x1 can be about 10–20 px short. In frames 46–49, y1 is 1515–1530 (a lower leg is missing), so use about 1547 for the hoof line.
- **Rabbit** (frames 0–69): length median 73 px (p10–p90: 69–79), height median 61.5 px (51–67). Both vary with the hop pose (stretched vs crouched, ears up).

## Static objects (approximate, read by eye from frame 0; ±20 px)
- Road: vanishing near (530, 1400). The white centre line runs from about (640, 1470) to (500, 1920); a yellow line is at the left, around x 420–460, y 1430–1520.
- Puddles / reflection band: y ≈ 1580–1880; small puddle at about (650, 1490).
- Left conifer: x 0–470, top about (120, 370). Right conifer: x 620–1080, top about (1000, 400).
- Mountain peak: about (565, 600); its visible base is at y ≈ 1380, between x 400 and 710.
- Bushes: left at x 0–370, y 1300–1560; right at x 650–1080, y 1280–1530.
- Thin blue pole/trunk: x ≈ 60–90, y ≈ 1000–1370.

## Events
- Both animals are already moving at frame 0 and keep moving to frame 74. No start or stop, contact, bounce or direction change is seen.
- The rabbit reaches the right image edge at frame 70–71 (t ≈ 2.33–2.37 s).

## Reliability and ambiguities
- **Masks:** difference to the background plate (threshold 16), with rows below y 1553 cut off to exclude puddle reflections and shadow streaks. Overlays were checked at 13 frames, and both objects are covered correctly.
- **Creature bbox x0 jumps:** x0 jumps between about 118 and 232 in some frames (e.g. 9–29) because of the swinging tail tip and occasional bush specks. Prefer the landmarks for position.
- **Centroids:** the mask centroid shifts with leg and tail pose (±10 px), while the shoulder track is smooth to about ±0.5 px per frame.
- **Rabbit centroid:** reliable to about ±2 px while the rabbit is fully visible. Its per-frame dx oscillates with the hop cycle (4–11 px/frame).
- **Reflections:** puddle reflections of both animals are visible below y ≈ 1580 and were not tracked.
