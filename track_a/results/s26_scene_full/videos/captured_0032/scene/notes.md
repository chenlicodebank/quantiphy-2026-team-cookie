# captured_0032 — measurement record (pixels / seconds only)

Lab video, 3D scene, 1280x720, 24 fps, 49 frames (t = frame/24, 0 … 2.000 s). Lab convention: fx = fy ≈ 763 px,
principal point ≈ (640, 360). No metric scale was assumed anywhere.

## Scene
A person sits behind a wooden table (their face and body are pixelated) with both hands resting on the far edge.
Two balls sit on the back of the tabletop:
- **yellow_ball**: a yellow-green tennis ball, the larger ball, at the right-back, centre (775, 411), about 28–30 px across.
- **white_ball**: a small white ball, at the left-back, centre (646.5, 413.3), about 15 px across.

What happens:
- The right hand pushes the yellow ball at **frame 22** (t = 0.917 s). It rolls left and toward the camera along the
  back half of the table.
- The left hand pushes the white ball to the right at **frame 29** (t = 1.208 s; clearly moving by frame 30). It rolls
  right and toward the camera.
- In frames 30–32 the yellow ball passes **in front of** the white ball. The white ball is fully hidden at frame 31 and
  partly hidden at frame 32. Nothing shows that they touched: they move in opposite directions and the white ball was
  already moving.
- The yellow ball reaches the left side edge of the table at about **frame 41** (t = 1.708 s). It falls from frame 42
  (its downward image motion starts between frames 41 and 42), shows heavy motion blur in frames 43–46, is cut off by
  the bottom image edge at frame 47, and is gone at frame 48.
- The white ball is still rolling when the clip ends (frame 48).
- **There is a dropped frame between frames 35 and 36.** Both balls jump about twice their normal step there (yellow
  −31 px against about −15 px; white +13.6 px against about +6 px). Anyone differencing across 35→36 should treat it
  as about 2 frame intervals.

## Files
- `scene.json`: inventory (moving and static objects, pixel extents), events, camera and perspective cues.
- `tracks/yellow_ball.csv`, `tracks/white_ball.csv`: one row per frame with these columns:
  - frame, t
  - cx, cy: mask centroid, which is the visible centre and the reference point
  - x0, y0, x1, y1: bounding box, inclusive pixels
  - bb_w, bb_h
  - len_major, len_minor: mask extent along and across its principal axis
  - eq_diam: diameter of a circle with the mask's area
  - area
  - occluded: 0 = clear, 1 = partly hidden or clipped, 2 = fully hidden and interpolated
  - note
- `scripts/`:
  - `track.py`: HSV colour masks and connected components. Yellow: H 23–42, S > 140, V > 100. White: S < 60, V > 185,
    inside the tabletop region. It writes `frames/raw_tracks.json` and overlay images.
  - `write_record.py`: builds the CSVs and scene.json.
  - `table.py`: tabletop extents.
  - `camera_check.py`: background shift.
  - `montage.py`, `probe_hsv.py`: checking aids.

## How it was checked and how reliable it is
- **Camera**: static. Phase correlation of the top background band against frame 0 gives shifts under 0.02 px in every
  frame.
- **Checks**: overlays of masks and boxes at frames 0–48 were inspected. Both tracks sit on the correct ball.
  - The yellow mask covers the whole ball. It leaves out the faint, desaturated blur halo, so in falling frames 43–46
    the centroid is the bright core of the blur streak (good to about 3 px), and the box undersizes the streak.
  - The white mask covers the ball, possibly with a thin bright reflection.
- **Centroid accuracy**: about ±0.5 px for static balls, ±1–2 px while rolling.
- **Partial occlusion**:
  - Yellow ball, frames 0–21: the right hand's fingertips touch its back-right. bb_h of 26 px is a little small; the
    unoccluded diameter there is about 29–30 px.
  - White ball, frames 0–28: fingertips hide its lower-left part, so bb 16x13 and eq_diam 15 slightly undersize it.
- **Pixel diameter**: horizontal motion blur stretches bb_w and len_major. While rolling, bb_h (the vertical extent) is
  the better measure; while falling, bb_w is.
- **Apparent size over time** (both balls approach the camera, so their depth changes):
  - yellow: about 28–30 px at frames 0–21 → 30 px at frame 30 → 38–40 px at frame 36 → 42–44 px at frame 41. When
    falling it is about 45 px and the blur inflates it.
  - white: about 15 px at frames 0–28 → about 18 px at frame 34 → 21.6 px at frame 40 → 26 px at frame 48.
- **White ball, frame 31**: fully hidden; the row is interpolated (occluded = 2). Frame 32 is partly hidden and its
  centroid is biased right by a few px.
- **Static objects**: positions are good to about ±4 px.
  - Table corners: far-left (560, 428), far-right (850, 428), near-left top (464, 485), near-right top (963, 497).
  - Front face of the table: 20–22 px thick.
  - Edge lengths: near edge 499 px, far edge 290 px.
  - The table's side edges converge to a vanishing point at about (707, 341), so the horizon is at about y ≈ 341
    (above the image centre, so the camera looks slightly down).
  - Other static objects: the camera tripod with a small camera at (672–710, 65–97), a light-stand leg at the left
    edge, the TV at the top right, the grey wall panels with the room corner at x ≈ 820, and cables on the carpet.
    Extents are in scene.json.
- **Events**:
  - Motion starts are good to ±1 frame.
  - "Leaves table" is frame 41–42.
  - The fall is short (frames 42–47, cut off at the image edge) and blurred, so fitting gravity to it is rough.
- **Ambiguities**:
  - The ball's shadow and reflection on the varnished table are excluded by the saturation threshold.
  - There is a small light highlight on top of the yellow ball in frames 28–29.
  - A "Modified with Segment Anything 2 Demo" watermark sits at the bottom right.
