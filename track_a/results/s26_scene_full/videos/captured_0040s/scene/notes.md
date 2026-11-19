# captured_0040s – measurement record (pixels, seconds; no metric scale)

Lab clip (3D), 1280x720, 24 fps, 49 frames (t = frame/24, 0 … 2.000 s). Background replaced by uniform green
("Modified with Segment Anything 2 Demo" watermark bottom-right); the person throwing was removed, so the hand is
invisible. Camera is static (table and props pixel-fixed in every frame). Lab intrinsics: fx ≈ 763 px, principal
point ≈ (640, 360).

## Files
- `scene.json` – inventory (ball + static props with frame-0 pixel boxes), table corners, camera/perspective notes, events.
- `tracks/ball.csv` – the only moving object, every frame 0–48: `cx,cy` = mask centroid (visible centre), bbox
  `x0,y0,x1,y1`, `len_major`/`width_minor` (min-area rectangle of the mask), `area_px`, `equiv_diam`, `phase`
  (held_in_hand / flight1 / flight2 / flight3), `occluded`, `note`.
- `scripts/track_ball.py` (median background of every 4th frame, |diff|>40 & low-saturation bright pixels, largest
  component near previous position), `scripts/overlay.py` (checking crops), `scripts/write_record.py` (fixes + JSON).

## Motion summary
- Frames 0–22: white ball held in the (invisible) hand at left, x≈127–169, y≈477–530, jiggled down/up (low at 8 and 20–21).
- Release ≈ frame 23 (t 0.958 s). Flight 1 arc rightwards, image apex y≈331 at frames 28–29.
- Passes in front of the tape roll (frame 32, partly hidden → centre/bbox set by eye) and **bounces on the table at
  frame 33–34** (t≈1.375–1.40 s) near x≈630, in front of the tape roll/left of the card tent.
- Flight 2 just above the white cup rim (apex y≈358, frames 36–37); **second bounce frame 41** (t 1.708 s) at (930, 487).
- Flight 3: apex y≈383 at frame 45, still visible descending at right (1181, 479) at frame 48.
- Apparent size grows (width_minor ~33–40 px early in flight → 46–54 px at the end): the ball travels toward the camera,
  so depth changes; use given depth_info to back-project (X = (cx−640)·Z/763 etc.).

## Reliability
- Centres: ±1–2 px when held and in clear flight; ±3–4 px in strongly blurred frames (blur streak 25–45 px long,
  centroid = mid-exposure position); frame 32 ±5 px (manual), frame 33 ±6 px (faint ghost).
- Ball diameter: held frames major axis ~43 px (minor ~33 is cut by fingers); in flight use `width_minor`
  (across the blur), `len_major` includes motion blur and is NOT the size.
- Static props (frame 0, ±2 px): glass jar 50×83 px, tape roll 78×47, card tent 52×84, flat cards 103×16,
  white cup 74×129 (rim y 377), dark card with yellow note 105×20; table front edge (212,537)–(1140,590) ≈ 930 px,
  edge band ~30 px thick, back corners approx (435,453),(905,465), black pedestal x 630–690.
- Ambiguities: two white objects (ball vs. white cup) – the cup never moves; ball briefly overlaps the cup top at
  frames 36–38 (mask from background difference, so the cup is excluded). Bounce frames are from image-y minima,
  which are only approximate for the true 3D contact because depth changes.
