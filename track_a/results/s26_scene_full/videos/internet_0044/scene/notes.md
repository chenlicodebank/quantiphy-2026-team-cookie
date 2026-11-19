# internet_0044 – measurement record (pixels, seconds)

Video: 1920x1080, 30 fps, 217 frames (t = frame/30). Internet footage, labelled 2D.
The shot shows a desk with (left to right) a white wavy bowl, a juice bottle with a yellow cap, a tall green
glass bottle, a short white ridged cylinder, a red Tefal kettle, a black desk lamp, dark red flowers and a black speaker,
with a black monitor behind. A hand at the lower right holds a white ping-pong ball, swings up and throws it
left at about frame 40. The ball bounces 12 times on the desk, passing in front of every object, and leaves
through the left edge (partly visible 140-147, gone from 148). Nothing else moves.

## Files
- `scene.json`: inventory (names, aliases, distinguishing features, static pixel extents at frame 0),
  events (release, bounces with sub-frame times, apexes, exit), camera summary, perspective notes,
  ball apparent diameter.
- `tracks/ball.csv`: one row per frame (0-216). Columns: `cx_f0, cy_f0` = ball centre in stabilised
  frame-0 coordinates (USE THESE for motion); `cx_raw, cy_raw` = same point in that frame's own image;
  `bbox_*_f0`, `bbox_w`, `bbox_h` = bounding box of the segmented ball blob; `mask_major_px / mask_minor_px` = minAreaRect
  of the blob (major = motion-blur direction, minor ~ diameter across the blur); `state` (held_in_hand,
  in_hand_throwing, flight, bounce_on_table, out_of_frame_left); `occluded`, `truncated_by_edge`,
  `pos_unc_px` (estimated 1-sigma centre error), `source`, `note`.
- `tracks/hand.csv`: rough skin-colour bbox/centroid of the hand (x>1450). Frames 0-36 bbox includes
  the ball; ~46-62 it is mostly the hand's shadow on the desk; after that only a fingertip at the right edge.
- `tracks/camera_similarity.csv`: per-frame similarity transform vs frame 0 (ORB + RANSAC, x<1650):
  p_i = s·R(θ)·p_0 + (tx, ty). `tracks/camera_shift.csv`: phase-correlation shift check (agrees).
- `track_overlay.jpg`: full ball path drawn on frame 0 (red = measured, blue = arc-fit fill, green = in hand).
- `scripts/`: all scripts (camera.py, camera_sim.py, cands.py, link.py, hand_ball.py, build_track.py,
  static.py, hand.py, overlay.py, check.py and helpers for viewing). Intermediate JSONs in scripts/.

## Methods
- Camera: slow drift, no zoom. Translation vs frame 0 reaches ~(+9.5, -10) px by frame 147 and
  ~(+11, -18) px by frame 216; rotation < 0.25 deg; scale within 0.15%. Every frame was warped into frame-0
  coordinates before the ball was segmented, so `_f0` positions are background-referenced.
- Ball (frames 41-147): background = median of warped frames 160-216 (ball absent); ball = pixels that are
  white (S<90, V>140) and differ from background (>30); blob linked frame to frame; centre = blob centroid.
  Checked on zoomed crops for every frame (frames/ PNGs not kept). In 10 frames where the ball is against
  the white cylinder (60-62) or the white bowl (107, 115-118, 123, 125), plus 3 outliers (102, 106, 110),
  segmentation failed. Those rows are filled from a fit (x linear, y quadratic) of the other frames of the
  same arc between bounces (`source=arcfit_fill`). I checked them visually: they sit on the ball within a few px.
- Ball in hand (0-36): HoughCircles, r≈35 (the true radius is ≈38-39). Fingers cover the right part of the ball, so the centre
  is approximate (±4 px, probably 2-3 px up-left of true). Frames 37-40 were read by eye on zoomed
  grids (heavy blur, merged with the hand, ±10 px).
- Bounce sub-frame times = intersection of the y-parabolas of consecutive arcs. The clean arcs all have a
  vertical image acceleration of 19.5-20.0 px/frame² (consistent with gravity at one scale). This is given only as a
  consistency check, not as a measurement for answers.
- Static objects: colour segmentation plus reading by eye on 20-px grids at frame 0 (±3 px). Kettle width 355 px
  including the handle (body without handle ~255 px), height 288. Bowl 383x164, juice bottle 122x386, green
  bottle 137x513, white cylinder 116x196. Lamp, monitor, speaker and flowers boxes are approximate (±10 px).
  Monitor and speaker are cut by the image border.

## Ball size (likely prior object)
Apparent diameter ≈ 76 px (range 73-80). Best measured as the vertical extent / minor axis at arc apexes,
where blur is smallest: 73-75 px for frames 55-86, 75-78 px for 95-112, 79-82 px for 120-135, and ~78 px in the hand at
frame 0. Horizontal width is inflated by horizontal motion blur and height by vertical blur near bounces
(blob up to ~114 px tall at frame 49). If a question gives the ball diameter (40 mm table-tennis ball) as prior, a
single planar scale is 40 mm / ~76 px. Use the size measured near the frames in question if more precision is wanted.

## Reliability
- Clean flight frames: centre ±2 px. Bowl region (100-131) and bounce frames: ±5 px (blur, white-on-white).
  Arc-fill rows: ±4 px. Edge-truncated frames 140-147: centroid biased to the right by up to ~half the cut part,
  ±8 px. In-hand: ±4 px; throw frames 37-40: ±10 px.
- Bounce frames: ±0.3 frame for bounces 1-11; bounce 12 (frame 145) is uncertain because the ball is cut by the edge.
- Release ≈ frame 40 (±1). The ball is still in the hand at 39 and clearly free at 41.

## Ambiguities
- The ball moves slightly toward the camera as it travels left: the image y of its centre at table contact goes from ~790
  to ~810-819, and its apparent size grows ~6%. The planar single-scale convention ignores this.
- Motion blur is strong (vertical near bounces, horizontal during the throw). Centroids are mid-exposure positions.
- The hand's shadow on the desk (frames ~40-62) and the lamp-shade highlight change at the top right are not objects.
- "White object" could mean the bowl, the white cylinder or the ball. The kettle is the only red object, and the bottles are
  distinguished by colour: green glass vs a plastic bottle with a yellow cap.
