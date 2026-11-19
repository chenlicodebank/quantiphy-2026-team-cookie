# internet_0030 — measurement record (pixels, seconds)

Video: 1920x1080, 42 frames, 29.1532 fps (t = frame / fps; frame 41 = 1.4064 s). Internet footage, 2D scene.
Content: a single dark-hulled motorboat with a white bimini top crosses a river from left to right, roughly
parallel to the image plane, with a far bank of trees and a grassy hill behind it. It is fully in frame in all 42 frames.
The camera pans slowly to the right.

## Files
- `scene.json`: inventory (boat, occupants, orange stern object, wake/spray, river, far shoreline, trees/hill),
  summary of the boat's pixel extents, camera summary and events.
- `tracks/boat.csv`: one row per frame (0–41). Columns:
  - `ref_x, ref_y`: visible centre = centre of the box from stern to bow and from canopy top to hull bottom (`bbox_*`).
    `ref_y` uses the raw hull bottom, which is noisy (see below). For horizontal motion use `ref_x`, `bow_x` or `stern_x`.
  - `bow_x, bow_y`: bow tip (front point of the white gunwale stripe), sub-pixel.
  - `stern_x, stern_y`: rear edge of the orange object on the transom (the rearmost visible point of the boat).
  - `length_px = bow_x − stern_x`: bow-to-stern length along the motion direction (horizontal).
  - `bbox_y0` / `canopy_top_y`: top of the bimini canopy. `bbox_y1`: raw hull bottom. `height_px` = canopy top to raw hull bottom.
    `hull_bottom_y_smooth`, `height_px_smooth`: the same after a 9-frame median filter.
  - `canopy_x0, canopy_x1, canopy_len_px(_smooth)`: horizontal extent of the bimini top (about 67 px, constant).
  - `bg_shift_x, bg_shift_y`: background shift relative to frame 0. `*_stab` columns hold the position in frame-0
    background coordinates (x − bg_shift_x), which is the motion relative to the river bank.
  - `score_bow, score_stern`: template-match scores (0.71–1.0). `occluded`: occlusion notes (see below).
- `tracks/camera.csv`: per-frame background shift, measured on the hill (y < 420) and on a right-bank region (x > 1300).
- `scripts/`: s1 (camera phase correlation and coarse template), s2 (pan-compensated median background; its scratch
  .npy files were deleted, so re-run s2 before s4), s4 (foreground mask, orange stern marker, canopy), s5 (zoom
  viewer), s6/s7 (template tracking of bow and stern, final CSV), s8 (smoothing, zoom/rotation check), s9 (scene.json).
  `bow_tips_manual.json` / `stern_manual.json` hold the points read by eye from 10x zooms at frames 5, 20 and 36,
  which seed the templates. `out_*.json` hold intermediate results.

## Method and reliability
- **Camera:** phase correlation of the tree/hill background against frame 0. It pans steadily: background x shift
  −0.75 px/frame (−30.7 px by frame 41) and y shift +0.11 px/frame (+4.4 px by frame 41). Left, middle and right
  regions agree in x to within 1 px, so there is no zoom. Rotation is negligible (about 0.1°). Accuracy is about ±0.3 px.
  Because the camera moves, measure boat motion with the `_stab` columns (relative to the background), in line with
  the annotators' rule. Because the camera follows the boat, the raw image displacement is about 5% smaller than the
  stabilised one: the boat moves about 14.4 px/frame in the image plus 0.75 px/frame of pan, so about 15.1 px/frame
  relative to the background. For example, bow x is 607.5 → 1179.3 in raw image coordinates and 607.5 → 1210.0 stabilised.
- **Bow and stern:** normalised cross-correlation templates taken from frames 5, 20 and 36, using the template nearest
  in time, with sub-pixel peak fitting. Crop montages confirm that the bow crosshair sits on the tip in every frame.
  Per-frame steps are smooth (bow ±0.5 px). The stern is a little noisier (±1 px) because the wake spray changes
  around the orange object; its scores are lowest (0.71–0.76) in frames 13–15.
- **Length:** the bow-to-stern length is not constant. It is about 208 px at frames 0–4, 197.5 px at frame 20 and
  189.6 px at frame 41 (mean 197.8 px), a steady drop of about 9%. Over the same frames the canopy length (67–68 px)
  and the height stay constant, so this is most likely the boat yawing slightly (foreshortening of the long axis), not
  a scale change. A question's "boat length in pixels" depends on the frame chosen; frame-by-frame values are in the CSV.
- **Height:** canopy top (y 444–449) to the waterline where it can be seen (y ≈ 521–523, in frames 0–5 and 20–32) is
  about 77 px. In frames about 6–19 and 33–41, white bow spray hides the lower hull; the detected bottom there (y ≈ 511)
  is too high, and the `occluded` column flags these frames. The bow tip sits about 39 px below the canopy top.
  Measured from frame 0 to frame 41, `ref_y` is distorted by these hull-bottom jumps, so use `bow_y`/`stern_y` for
  vertical position.
- **Vertical motion:** small pitching. Bow tip y is about 486 (frames 0–8), about 481.4 (frames 17–19), about 488
  (frames 29–32) and 485.5 at frame 41. Stern y stays at 500–503.

## Ambiguities
- The orange object at the stern (a flag, light or person's clothing) is taken as the stern. The transom hull itself
  is only 0–4 px in front of it.
- The wake and spray (white water) behind and under the stern are not part of the boat and are excluded from the
  length. The `stern_waterline_spray` flag marks that the lower stern always sits in spray.
- The occupants (1–2 people under the bimini) are dark and partly hidden. They are not tracked separately; they move
  with the boat.
- Motion blur is mild (about 14 px/frame of motion, but edges stay sharp enough for templates). There are no other
  boats, people or animals.
- Events: none besides the steady crossing. There is no start or stop, contact or bounce; only the pitching noted above.
