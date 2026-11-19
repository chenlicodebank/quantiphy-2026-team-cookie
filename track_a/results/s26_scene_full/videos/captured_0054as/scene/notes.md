# captured_0054as: measurement record

**Video:** lab capture, 3D scene, 24 fps, 49 frames (0–48, t = frame/24, 0–2.0 s), 1280×720.
The background has been replaced (segmentation-style): a static blue-white gradient with fixed noise, plus a
"Modified with Segment Anything 2 Demo" watermark at x 1030–1280, y 690–720. There is no visible floor,
furniture or marking. All values are in pixels and seconds. No metric scale is assumed.

## Scene
Two people and four balls.
- **person_crouching** (lower left, black clothes, long hair). At t = 0 their right hand rests on the
  **basketball** (orange, centre (240,573)) and their left hand on the **soccer_ball** (white with black
  pentagons, centre (158,610)).
- **person_standing** (centre-right, blue-grey hoodie, black trousers, feet at y = 542). They hold the
  **tennis_ball_yellow** in their right hand (image right, ~(700,392)) and a small **grey_ball** in their left
  hand (~(628,383), almost entirely hidden by the hand).

What happens:
- The crouching person pushes the basketball from frame 5. It rolls down-right toward the camera and leaves
  through the bottom edge (last visible frame 32).
- The crouching person releases the soccer ball at about frame 21–23. It rolls down-left toward the camera and
  leaves at the bottom-left (last visible frame 40).
- The standing person brings both hands together (frames 15–22) and tosses both small balls underhand toward
  the crouching person: the grey ball leaves the hand at frame 23, the yellow ball at frame 25.
- Both balls arc (image apex: yellow at frame 26, grey at 27), bounce once on the floor in front of the crouching
  person (lowest image point: yellow at frame 37, grey at 38), and are caught at about frame 42. The crouching
  person then holds them up near their face (42–48).

## Files
- `scene.json`: inventory (how to tell objects apart, visible frames, pixel sizes), events, camera.
- `tracks/<object>.csv`: one row per frame the object is visible. Columns:
  - `cx,cy`: mask centroid, the reference point (the "visible centre").
  - `bcx,bcy`: bbox centre.
  - `bx0,by0,bx1,by1,bw,bh`: bbox, inclusive pixels.
  - `area`, `eq_diam` = 2·sqrt(area/π).
  - `len_major,wid_minor`: mask extent along and across its principal axis; `angle_deg` is that axis
    (0 = +x, image y points down).
  - `at_border`: the mask touches the image edge.
  - `touch_person`: the mask, dilated by 7 px, touches a person mask.
  - `occluded`: 1 if partly hidden or cut off by the edge.
  - `note`: why.

  Objects: basketball (0–32), soccer_ball (0–40), tennis_ball_yellow (0–48), grey_ball (23–46),
  person_crouching (0–48), person_standing (0–48).
- `scripts/`: `run_all.py` rebuilds everything (`bg.py` → `cleanbg.py` → `track.py` → `postprocess.py`).
  - Viewers: `view.py`, `zoomsheet.py`, `checkzoom.py`, `diffview.py`.
  - Diagnostics: `comps.py`, `events.py`, `summary.py`.
  - Background images and check sheets are written to `../frames/` (scratch, not part of the record).

## How it was measured
- **Foreground:** |frame − clean background| summed over RGB > 60 (background noise has a 99.5th percentile
  of 40), followed by a 3×3 opening.
- **Basketball:** orange colour test (R > 50, G < 0.66R, B < 0.5R), holes filled. Once the ball is free of
  the person, the whole foreground blob is used, so the darker shaded bottom is included.
- **Soccer ball:**
  - Light, low-saturation, non-skin pixels near the previous position; their convex hull (which takes in the
    black patches) intersected with the foreground.
  - In frames 26–34, the crouching person's light-grey left shoe (mask taken from frame 44) is excluded.
- **Small balls in flight (23–41):** isolated small foreground blobs. When there are two, the yellower one
  (mean G − B) is the tennis ball. When they have merged, they are split per pixel by yellowness.
- **Small balls in hand:** colour (yellow ball), or grey pixels next to the hand (grey ball after the catch).
- **Persons:** the remaining large foreground components, with the ball masks subtracted.
- **Checks:** every object was overlaid on frames and zoomed check sheets were inspected. The masks cover the
  full visible object.

## Camera
- **Static:** the background is bit-identical between frames except for compression noise, and the feet stay
  fixed. The per-frame background shift is 0.
- **Intrinsics:** use the lab convention (f ≈ 763 px, principal point ≈ (640,360)).
- **Perspective cues:** there is no ground plane or horizon to see. Depth ordering: the standing person (feet
  y = 542) is behind the crouching person (feet y ≈ 600–615). The basketball rolls toward the camera, and its
  apparent width grows from 68–70 px (rest) to 80 px (frame 22) and 84 px (frame 24). The soccer ball also
  approaches the camera (65–70 px at rest, about 85–90 px near the exit, partly blur). The thrown balls grow
  from about 18–22 px to about 30 px.

## Reliability and ambiguities
- **Persons' tracks:** only bboxes and centroids are recorded, and they include arm motion.
  - The standing person's head-to-feet bbox height is 336 px (frames 0–16) or 342 px (frames 25–48),
    depending on posture and hair.
  - The crouching person's bbox height is about 207 px while crouched with the arms up, and up to 254 px when
    a hand reaches the floor (frames 36–48).
- **Basketball:** about 1 px accuracy while free.
  - Frames 0–5: the hand covers its top-right.
  - Frames 23–32: it is cut by the bottom edge. The centroid and bbox describe only the visible part, so the
    true centre is lower; use the bbox width and the top edge `by0` with the free diameter instead.
- **Soccer ball:**
  - Frames 0–22: fingers cover the top, so `by0` is the fingers. The horizontal width (65–70 px) is the
    reliable diameter.
  - Frames 24–36: strong motion blur, so the length along the motion is inflated. Use `wid_minor` for size.
  - Frame 25: the bbox may include the edge of the shoe.
  - Frames 35–40: cut by the border.
- **Small balls:** the blur streaks from frame 33 onward make `len_major` up to about 3× the diameter
  (frames 36–37); the centroid is the middle of the streak. Before frame 23 the grey ball is hidden in the hand
  and not tracked. Grey-ball frames 47–48 were dropped (the mask hit the hand or the grey face patch). In
  frames 42–48 the yellow ball is partly hidden by the hands.
- **The two small balls look alike in size.** The grey ball leaves the hand first and stays above-right of the
  yellow ball until the bounce. After the bounce (frames 38–41) the yellow ball is above-left.
- **Timing anomalies (likely dropped capture frames):**
  - The basketball moves 32.8 px from frame 11 to 12, against 15–18 px in neighbouring frames.
  - Both small balls jump 120–135 px from frame 35 to 36, against about 45–53 px before. This is also near
    the bounce and in heavy blur.

  Frame indices are kept as-is (t = frame/24); answering sessions should be aware of these gaps when they
  difference positions.
- **Faces** are anonymised with grey patches, which can be mistaken for the grey ball near the face.
- **No shadows** are present, because the background was replaced.
