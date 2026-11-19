# captured_0020x: measurement record

Lab clip, 3D, 24 fps, 49 frames (t = frame/24, 0 to 2.000 s), 1280x720. The background was replaced by flat green
(Segment Anything 2 demo; watermark box at bottom-right x 1030-1280, y 690-720). The camera is high and looks steeply
down. Benchmark intrinsics hint for this camera: f = 763 px, principal point ~ (640, 360). No metric scale is assumed
anywhere here.

## Scene
Two people play catch with an underarm throw, each throwing one object to the other at the same time:
- **person_near**: long dark-brown hair, dark grey oversized T-shirt, black trousers, white sneakers. Bottom-left of
  the frame and very close to the camera. Cut by the left and bottom edges and appears strongly slanted. Throws the
  **white_ball** and catches the **yellow_fruit**.
- **person_far**: light grey fitted T-shirt, dark cargo trousers, white sneakers, watch on her left wrist. Top-centre,
  facing the camera; her head is cut by the top edge. Throws the **yellow_fruit** and catches the **white_ball**.
- **white_ball**: small white ball (grey shading on its shadow side), ~28-35 px across.
- **yellow_fruit**: pale-yellow elongated fruit with a dark green-brown stem end (banana/mango-like). Its long axis
  is ~40-45 px when held by the far person and ~70-80 px in flight near the near person (blur and rotation included).
- There are no static props, floor markings or furniture. The background is uniform green.

## Files
- `scene.json`: inventory, camera, perspective cues, apparent sizes, events.
- `tracks/white_ball.csv`, `tracks/yellow_fruit.csv`: one row per frame (0-48).
  - Columns:
    - `cx, cy`: centroid of the colour mask, i.e. the visible centre and the reference point.
    - `bbox_*`
    - `len_main_axis, width_across`: PCA extents of the mask.
    - `main_axis_deg`: image angle of the main axis, 0 = +x, y down.
    - `mask_area`
    - `occluded`: 0 = fully visible, 1 = partly hidden or mixed with a hand, 2 = hidden, no values.
    - `state`: held / flight.
- `tracks/person_near.csv`, `tracks/person_far.csv`: one row per frame. Columns: mask centroid, bbox, area,
  `cut_by_frame_edge`, plus:
  - far person: `feet_x`, `feet_y_lowest` (ground contact, constant ~(730, 271)).
  - near person: the rightmost mask point. This is usually the right shoe tip at (389, ~661); in f12-20 it is the
    outstretched arm instead.
- `scripts/`:
  - `track_objects.py` (final object tracker)
  - `persons.py` (people)
  - `build_scene.py` (scene.json)
  - `view.py` / `montage.py` (inspection)
  - `probe.py` / `cands.py` (threshold exploration)
  - `track.py` (first, superseded tracker; it now writes only to frames/)

## Method
- **Objects**: an HSV colour mask (white: S<55, V>195; yellow: H 18-38, S>60, V>110) is taken inside a ±34 px window
  around guide positions. I set the guide positions by hand from inspected keyframes and interpolated between them.
  The component nearest the guide, plus same-colour pieces next to it, gives the mask. In free flight the mask is
  grown into the paler, blurred rim (white: S<80, V>140; yellow: H 19-40, S>30, V>120), so the extents cover the
  whole object.
- **People**: the non-green foreground, split into connected components of at least 3000 px.
- **Checking**: every frame of both object masks was drawn and inspected (frames/chk_*.png), and the people masks
  every 6th frame.

## Events (frame / t s)
- **White ball**
  - f0: in the near person's right hand at hip (306, 512).
  - Back-swing lowest point f4-5 (275, 553), where the direction reverses.
  - Last hand contact f14 (0.583); first free frame f15 (0.625).
  - Image apex f22 (0.917) at y = 36.7.
  - Far person's hand first touches it at f26 (1.083); clasped in both hands at f27 (1.125).
  - The hands carry it down to y ≈ 161 at f35-36, then up to waist level by f48.
- **Yellow fruit**
  - f0: hanging in the far person's hand (649, 133).
  - Swung behind her leg and hidden f4-7.
  - Last finger contact f13 (0.542); first free frame f14 (0.583).
  - Highest image point f18 (0.750), y = 67.6, but f18 is partly covered by the ball; f17 has y = 72.7.
  - Near person's hands first touch it at f24 (1.000); gripped f27 (1.125).
  - Hidden f28-37; visible again in her hands f38-48.
- **Crossing**: the two objects cross in the image at f17-19. The ball is drawn in front of the fruit.

## Camera / perspective
- The camera is static. No background is visible, so this is judged from the people: the far person's feet stay at
  y = 271 ±0 px in every frame, and the near person's shoe tip stays at (389, 661).
- There is no horizon and no floor texture. Ground contacts: far feet ~(730, 271), near shoe ~(365, 690).
- Both throws go from one person toward the other, so their depth changes a lot. Apparent sizes shrink toward the
  far person:
  - ball width ~33-35 px near the thrower, ~28-30 px at the apex, ~22-24 px just before the catch;
  - fruit width ~31-35 px in flight, long axis growing from ~45 to ~80 px as it approaches the near person.
- Any 3D question needs the given depths plus f ≈ 763 px.

## Reliability / ambiguities
- **Flight centroids** (ball f15-25, fruit f14-23): about ±1-2 px.
- **Flight mask extents**: lengthened along the motion by blur, by up to ~15 px for the fruit and ~20 px for the
  ball at f14-18. `width_across` is the better size measure.
- **Held phases**: the hands hide part of the object, so the centroid is biased by a few px and the extents are
  too small.
  - Ball f0-13: crescent-shaped mask.
  - Ball f27-48: only the visible part between the fingers.
- **Mixed-in pixels**:
  - Fruit f24-26: some hand pixels.
  - Ball f26-28: a few streaks from the arm or T-shirt. The far person's grey T-shirt has a similar colour; strict
    thresholds keep most of it out.
- **Fruit f18**: half covered by the ball.
- **Hidden frames have empty rows**: fruit f4-7 and f28-37.
- **People**: mask centroids are not pelvis positions. Both bodies are cut by the frame edges, and the near
  person's mask includes hair and arms. The masks contain whatever the person holds.
