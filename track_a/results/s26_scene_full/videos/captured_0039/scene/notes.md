# captured_0039 — measurement record (pixels, seconds)

Lab video (Orbbec Femto Mega, 24 fps, 49 frames, 1280x720, t = frame/24). Background was edited with SAM2
(watermark bottom-right) but the scene is the real room. Benchmark intrinsics: f = 0.5959*1280 = 762.8 px,
principal point ~(640, 360), HFOV 80°. **Camera is static** (no pan/shake; static-region frame differences ≈ 0).

## Scene
A white ping-pong ball sits at the back of a wooden table, steadied by the hand of a person seated behind the
table (fingertip visible left of/behind the ball). It is released, rolls toward the camera and to the left across
the table top, rolls off the front edge and falls in front of the table, leaving the image at the bottom.
The ball is the only moving object (apart from the briefly visible hand).

## Files
- `scene.json` — inventory (moving + static objects with pixel boxes/extents), camera/perspective, events.
- `tracks/ball.csv` — ball, every frame 0-48. Columns: `ref_x, ref_y` = recommended reference point (ball centre);
  `diam_fit` = apparent diameter (px); `cx, cy` = centroid of the (hole-filled) mask; `bbox_*` = mask bbox;
  `area_px`, `equiv_diam`; `len_main_axis`/`width_across`/`main_axis_deg` = mask extents along/across its principal
  axis; `held_by_hand`, `occluded`, `note`. `visible=0` for f45-48 (ball out of the image).
- `scripts/track_ball.py` (tracker + overlay), `scripts/crops.py` (zoomed crops with pixel ruler),
  `scripts/check_dups.py` (frame-difference / camera-motion check), `scripts/probe.py` (pixel profiles),
  `scripts/draw_static.py` (overlay of static boxes, table quad, VP and ball path).

## How the ball was measured / reliability
- Mask = bright (V>150) & low-saturation (S<70) pixels that differ from frame 48 (ball gone), component nearest the
  previous position. The lower part of the ball is shaded and blends into the table, so the mask bottom is cut
  short (bbox_h and cy are biased upward by up to ~5 px during rolling). Therefore `ref_x/ref_y/diam_fit` come from a
  least-squares circle fitted to the upper ~60% of the outline (f0-40). Checked visually on zoomed overlays: the fitted
  circles sit on the ball outline in every frame f0-40. Accuracy ≈ ±1 px centre, ±1-2 px diameter.
- Apparent diameter: 23 px at rest (f0-18) → 29.5 (f25) → 34.5 (f30) → 39.8 (f35) → 48 px (f40). The ball comes
  toward the camera, so its depth roughly halves over the roll (Z ∝ 1/diameter). For metric work, use the given
  depth/size prior with f = 762.8 px (e.g. Z = f·D/diam_px) and back-project (ref_x, ref_y).
- f41-44 (falling off the edge): strong vertical motion blur; ref = bbox centre of the blurred streak and diameter =
  width across the blur (49-54 px). Centre uncertainty ±5-10 px vertically. f44: ball touches the bottom image
  edge (partly out of view), so ref_y (690) is biased upward.
- f10: segmentation artefact — the ball's pixels are greyed out (outline still visible at the same place); since the
  ball is at rest, f9 values were copied (occluded=1).
- f0-18: tiny centre jitter (<1 px) is noise/hand contact, not motion. Mask during this phase includes the dark logo.

## Events (frame / time)
- f0-18 (0-0.75 s): ball at rest, held by hand. Release: motion starts between f18 and f19 (first clear move f19,
  t = 0.792 s).
- f19-40 (0.79-1.67 s): rolling on the table top, image direction down-left (~(-0.7, +0.7)).
- f36: image step f35→36 (~12 px) is about twice the neighbouring steps (~5.5-6.7 px) and the frame difference is
  ~2x larger — probably a dropped/irregular frame in the recording. Treat per-frame differences around f36 with care
  (smooth over ≥5 frames as the reference convention does).
- f40-41 (1.67-1.71 s): reaches the table front edge (edge y ≈ 550 px at x ≈ 470) and rolls off.
- f42-44 (1.75-1.83 s): falling in front of the table's front face. f45 (1.875 s): out of view.

## Static objects (pixel extents at f48, see scene.json)
Table top quad BL(430,452) BR(917,467) FR(1137,586) FL(212,536), front-face thickness 32-36 px; pink bottle
50x149 px (x640-690, y330-479); white cup 71 px top width, 53 px bottom, 123 px tall (x724-795, y375-498);
card tent (front card ~84x21 px, x656-712, y416-500); flat cards (x642-745, y499-515); dark-blue phone/case with
yellow sticker near the front edge (x519-620, y532-552, 101 px long); tripod with blue top light behind the table;
person seated behind the table (legs visible below the table, hand only near the ball); monitor top right;
left light stand; grey wall panels. Tripod/person/monitor/stand boxes are approximate.

## Perspective
Table side edges meet at a depth vanishing point ≈ (698, 349); the horizon is nearly level at y ≈ 349 near the
centre (camera pitched ~1° down, ±10 px uncertain). The ball's image path runs from near the back edge toward the
front-left; it rolls almost straight toward the camera (diameter doubles).

## Ambiguities
Only one ball; no similar moving objects. Ball shading/contact shadow on the table, halo from sharpening (~1-2 px)
and motion blur when falling are the main error sources. The SAM2 edit causes the f10 dropout. No metric scale has
been assumed.
