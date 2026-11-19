# simulation_0050 — measurement record (pixels and seconds only)

Video: 1920x766, 33 fps, 99 frames (t = frame/33, frames 0-98, 0-2.97 s), Blender render, 3D street scene.
No metric scale was assumed anywhere. Image coords: x right, y down, origin top-left, full resolution.

## Scene in one paragraph
Static camera (max background shift 0.016 px) looking at a row of facades across a street: from left, a blue
building, a phone booth ("TELEPHONE"), a shop under a yellow "PHOTO LAB'O LAB" sign (blue door with a
Coca-Cola poster, bin), the stoop stairs and brown door of a green clapboard house, a hedge behind an iron
railing, and a grey stone building with an arched wooden door between two stone pillars with ball finials.
Sidewalk in front, road in the foreground (manhole cover lower right). **Two moving objects**, both going
right -> left: a **cyclist** (man in a dark jacket on a dark-blue bicycle with a rear rack, nearest the camera,
riding along the road edge) and a **pedestrian** (man in a white T-shirt and light jeans walking on the
sidewalk). The cyclist overtakes the pedestrian, passing in FRONT of him in frames 5-24 (crossing at about
frame 14). The street recedes to the left (its edges converge to a vanishing point far left of the image,
~(-2200, 600), rough), so moving left means moving away from the camera: both shrink.

## Files
- `scene.json`: metadata, camera, perspective cues, inventory (moving and static objects with pixel extents),
  events, apparent-size-vs-time summary.
- `tracks/cyclist.csv` (frames 0-98), one row per frame:
  - `bbox_x0` = front-wheel leading edge (left), `bbox_x1` = rear wheel / rack trailing edge (right),
    `bbox_y0` = top of the rider's head, `bbox_y1_ground` = wheel ground contact. Floats; they can lie outside
    the image when the bike is cut by an edge (frames 0-4 right edge, 94-98 left edge: `truncated`,
    `visible_fraction`).
  - `center_x, center_y` = box centre; `hub_front_x, hub_rear_x, hub_y` = estimated wheel-centre positions;
    `hub_mid_x` = midpoint between the hubs (a good stand-in for the bike rig root / bike centre in x).
    For the ground point under the bike use (`hub_mid_x`, `bbox_y1_ground`).
  - `length_px` (x1-x0, along the motion), `height_px` (head to ground).
  - `chain_step_scale_x/y`, `match_score`: tracker diagnostics. `anchor`=1 marks the frames whose box was read
    by eye on a zoom (0,15,30,45,60,75,92). `mask_*`: raw background-subtraction box (only frames where the
    cyclist is separate from the pedestrian), for reference only (affected by shadows and lost dark pixels).
  - `occluded` is always 0: nothing ever hides the cyclist.
- `tracks/pedestrian.csv` (frames 0-98):
  - `torso_x` = median x of the white-T-shirt pixels (rows 425-545), measured in every frame including the overlap.
  - `pelvis_x_est` = `torso_x`; `pelvis_y_est` = feet - 0.52 x height (a rough anatomical estimate of the hip).
  - `bbox_*` (y1 = soles of the feet), `bbox_cx`, `height_px` (head top to soles), `width_px` (changes with stride).
  - `occluded`=1 for frames 5-24 (behind the cyclist); `source` tells you whether the box is from the mask or
    is `torso_x_measured+box_interpolated` (frames 4-24: x from the shirt plus offsets interpolated between
    frames 3 and 25; y0/y1 interpolated linearly).
  - `head_top_dropout`=1 (frames 63, 80, 82, 86; also look at 83-85, where y0 is 415-420): head top lost against
    a dark background, so `height_px` is too small there by about 8-16 px.
- `scripts/`: every script used (run in order s1, s9, s11, s12, s14; s2-s8, s10, s13, s15, s16 are helpers or
  diagnostics). Scratch images went to `../frames/` (not part of the record).

## How things were measured
1. Camera: phase correlation of the upper band of every frame against frame 0 (s1). Static.
2. Background: per-pixel median of every 3rd frame (s1). Foreground = |frame - bg| > 14 grey levels, with
   cast-shadow suppression: shadow-like pixels (darker with the same chromaticity) are kept only within 12 px
   of confident foreground (s2 `objmask`). This removes the long shadows the two figures throw to the left
   onto the hedge, steps and sidewalk.
3. Cyclist: chained frame-to-frame masked template matching (s11), starting at frame 30 and running forward to 98
   and backward to 0. Separate x and y scales, because the bike is oblique to the image plane and foreshortens
   as it recedes. Its length shrinks to 0.55x from frame 15 to 92 while its height shrinks to 0.68x. During the
   overlap, pixels in the pedestrian's columns were left out of the template. The chain gives smooth
   frame-to-frame motion but its box edges drifted by about 10-15 px, so each edge was corrected by an offset
   interpolated linearly between 7 visual anchor boxes read on 2-3x zooms (s14). Overlays of the final
   boxes and hub dots on 12 frames were checked by eye: the boxes hug the wheels and head.
4. Pedestrian: mask blob (s9/s14), with shadow pixels near the feet removed. In frames 4-24 the T-shirt
   pixels give the x position (s12); box size is interpolated.
5. Static objects: read on a gridded background image; perspective lines from edge maxima (s13).

## Reliability
- Cyclist per-frame positions: smooth. Frame-to-frame displacement is good to about 0.5 px. Absolute
  edges are good to about +-3 px at anchor frames and about +-5 px between them. The head top is the least
  certain edge (dark hair on dark backgrounds, frames 30-60). The wheel-hub fractions of the box (front 0.19,
  rear 0.80, height 0.815) were read on 4 frames and vary by about +-0.03 of the length in x.
- Image-plane speed of the cyclist decreases from about 32 px/frame (frame 1) to about 12 px/frame (frame 98).
  Most of this is perspective: apparent height falls 321 -> 196 px, a 1.64x increase in depth. Whether it
  also slows down in 3D needs the depth information of the question.
- Pedestrian `torso_x` is good to about 1 px (median of 2000-3000 pixels; integer or half steps) everywhere,
  except frames 13-15, where the cyclist hides most of the shirt (about 600 pixels; +-3 px). It includes the
  swinging arms, so it can differ from the true pelvis by a few px. The mask hip band sits about 10-15 px to
  the left of `torso_x` (rear arm and hand).
- Pedestrian heights oscillate 5-10 px with the gait. Standing-height-like (maximum) values: about 273-276 px
  at frames 0-3, about 266 at frames 25-29, about 256-261 at frames 50-60, about 248 at frames 87-88. In frames
  0-2 the soles were checked after removing the foot shadow.
- Static extents: +-3 px. The vanishing point is rough (+-800 px in x). The horizon is not visible.

## Ambiguities
- "Cyclist" means bike + rider together. If a question needs only the bicycle, its length is
  `length_px` (wheel edge to wheel edge, rack included) and its height is about 0.45-0.5 of `height_px`.
- Shadows of both people fall to the left (onto the hedge, steps and sidewalk). They are not part of the objects.
- In frames 0-4 the cyclist's right end is outside the image. `bbox_x1` there is extrapolated (the frame-15
  correction is carried back), so `length_px` in frames 0-4 (366-344 px) is uncertain by about +-15 px. The trend from frames 15-30
  (about 3.3 px/frame) projects about 350 px at frame 0.
  The visible left edge, head top and ground line are measured.
- In frames 94-98, `bbox_x0` < 0 is extrapolated. The rear edge, head and ground line are measured.
- The pedestrian's box edges sometimes stay fixed for several frames (for example x1 = 1379-1381 in frames
  37-46). That is the planted stance foot, not an error.
- Faces are blurred in the render (grey patches).
