# captured_0037x – measurement record

Lab video (Orbbec, 24 fps, 49 frames, 1280x720, 3D). The background was removed by Segment Anything 2, so
everything except the table, the objects on it and the ball is black. The camera is static: phase correlation of the table
region against frame 0 gives a shift of 0.1 px or less in every frame. Intrinsics from the task: f ≈ 763 px, principal point ≈ (640, 360).

## Scene
A white ping-pong-type ball rests on the top-right rim of a tall white cup (frames 0–6). At frame 7 it starts to slip
down the outside of the rim. It is launched up and to the left at about frame 11 and then bounces along the table toward the left
and toward the camera. The bounces are at frames 19 (behind the card tent), 28 (behind the tape roll), 36 (by the glass jar)
and 43 (left part of the table). At frame 48 it is still in the air, moving up and to the left. Its apparent diameter roughly doubles over the clip
(about 18 px at rest, about 34 px at frames 45–48), so it moves a long way toward the camera. Static objects: white cup,
glass jar, tape roll, card tent, flat cards, a dark card on the table, and the table with its pedestal leg. None of them move.

## Files
- `scene.json`: inventory, static pixel boxes, camera, events (frame and time).
- `tracks/ball.csv`: one row per frame (0–48). Columns: `cx, cy` (mask centroid = visible centre); bbox; mask area;
  `length_major_px` / `width_minor_px` (ellipse fit: along / across the blur or motion axis); `height_px` (bbox height);
  `equiv_diam_px`; `motion_blur` flag (major/minor > 1.3); `occluded` flag with a note.
- `scripts/`: `track_ball.py` (first pass and camera-shift check), `write_record.py` (final track and overlay),
  `static_extents.py` (static boxes), `montage.py` (viewing crops).

## Method and reliability
- Ball mask: |gray − per-pixel median over all frames| > 40 and gray > 120, followed by a morphological opening; the largest component is kept.
  I checked the overlay (contours and centres on frames) and every frame hits the ball. The centroid is good to about 1 px in clear frames.
- **Motion blur** is strong while the ball flies fast (e.g. frames 17–19, 26–27, 30, 34, 41–43). There the mask is a streak:
  the centroid is the mid-exposure position, but the major axis and height include the blur. **For size, use `width_minor_px`**
  (across the streak) or the frames 0–6 and 44–48 values.
- Occlusion: in frames 19–20 the ball is behind the card tent, and in frame 20 only its top shows, so the centroid there is biased upward.
  In frame 28 it is behind or overlapping the translucent tape roll; in frames 35–36 it overlaps the glass jar. Treat the centroids and sizes
  in these frames as less reliable (several px).
- Bounce frames are the sampled frames where the ball is lowest in the image; true contact can fall between frames (±0.5 frame).
  Frames 7–11 (slip down the rim) are a small motion of about 12 px.
- Static boxes: the cup, tape roll, flat cards, dark card and table come from colour segmentation of the median frame (±2 px). The glass jar
  (transparent) and the card tent were read by eye from zoomed grid views (±3 px).
- Depth is not known here. For 3D quantities, back-project (cx, cy) with f = 763 px and the depth_info given with
  each question. The apparent diameter (∝ 1/depth) gives the relative depth over time: about 18 px at frame 0 versus 34 px at the end.
- Nothing named a "ball" is ambiguous: there is only one moving object. The white cup has a similar colour, but it is static, and the
  median background removes it.
