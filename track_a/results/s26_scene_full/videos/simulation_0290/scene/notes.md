# simulation_0290 – measurement record

Video: 2560x1440, 24 fps, 72 frames (t = frame/24). Source: simulation, declared 2D. All values are full-resolution pixels and seconds. No metric scale is assumed.

## Scene
- **One moving object: a shark**, seen from directly above. Its head points left (-x) and it swims right-to-left across the frame. It has a pale blue-grey body, a green patch on top of the head, a dark rear body and tail, two pale pectoral fins, and a thin pale caudal-fin tip.
- **Shark shadow:** a black silhouette with the same outline (fins and tail) cast on the seabed. It is offset toward the image centre. In frames 0-30 it lies ahead of the head and partly covers it (about 150-250 px to the left). Around frames 35-45 it is roughly under the shark. In frames 54-71 it lies behind the shark and darkens the rear body and tail (+80…+170 px). It is not part of the shark. Because the shadow is offset, the shark is some height above the seabed, which adds slight perspective, but the motion is effectively planar.
- **Background:** a seabed or water surface with animated caustics and diagonal light bands. There are no static objects, props or markings.
- **Camera:** static. No pan or shake was found, though the animated texture leaves no fixed landmark to test against precisely.
- **Duplicate frames:** frames 0 and 1 are pixel-identical (the whole image). The shark does not move between frames 70 and 71 (the water still changes). The shark therefore moves over frames 1→70.

## Files
- `scene.json`: inventory, camera, events, manual extents per sampled frame, and a pixel motion summary.
- `tracks/shark.csv`: one row per frame (0-71), with these columns:
  - `ref_x, ref_y`: a template-tracked body point on the head and pectoral region (1080, 750 at frame 50). It lies about 178 px behind the snout tip. This is the most reliable point for displacement: sub-pixel, with per-frame noise of about ±1 px.
  - `mid_x, mid_y`: the midpoint of the snout tip and tail tip, an estimate of a body-centre origin. Accuracy is about ±5 px, and it moves with the tail swing.
  - `snout_*, tail_*`: the front of the grey snout wedge and the caudal-fin tip.
  - `rot_deg`: rotation relative to frame 50 (positive = clockwise on screen). It ranges from about −14° (frame 10, tail raised) to +6° (frame 34) and back to −6.5°.
  - `match_score`: the template-match score.
  - `bbox_*`: the axis-aligned box over the snout, tail and pectoral-fin tips. It is clipped at x = 2559 while the tail is off-screen (frames 0-6).
  - `length_px`: snout to tail tip. `width_px`: pectoral fin tip to fin tip, measured across the body axis.
  - `extents_source`: `manual` at frames 10, 18, 26, 34, 42, 50, 58, 66 and 70 (read from 1.25x and 2x gridded crops). Elsewhere the values are interpolated in the shark's body frame and placed with the template pose, so treat them as approximate.
  - `occlusion` flags.
- `manual_keypoints.json`: the raw manual readings (wedge, pale-head front, tail tip, upper and lower fin tip).
- `tm_track.json` and `tm_track_full.json`: the coarse (half-resolution) and refined (full-resolution, sub-pixel) template tracks.
- `scripts/`: every script. `track_tm.py` and `refine.py` do the tracking, `whole_crops.py` and `tips_crops.py` make the crops for manual reading, `build_record.py` writes the CSV, `overlay.py` draws the check overlays and `finalize.py` writes scene.json. `seg.py` is a failed background-difference attempt; it does not feed the record.

## Method and reliability
- **Segmentation by background difference failed:** the animated caustics differ as much from the median background as the shark does. The track therefore comes from template matching instead: a 240x140 head and front-body patch from frame 50, searched over rotation, refined at full resolution with parabolic sub-pixel peaks. Scores are 0.57-0.69 in frames 0-31, where the shadow and caustics overlap the head, and 0.75-1.0 later. Overlays were checked by eye on frames 4-71, and the points sit on the shark every time.
- **Motion in pixels:** the ref point moves from (2238, 758) at frame 1 to (610, 751) at frame 70. The mean per-frame step is 23.6 px (range 21.1-26.5; the range is mostly match noise of about ±1-2 px, so smooth over several frames before differencing). The path is almost straight and leftward. y drifts down by about 37 px until frame 24, then back up to about 747.
- **Shark length depends on which frames and which snout point you use:**
  - Snout wedge to tail tip: about 712 px in frames 10-26, and 614-655 px in frames 34-70 (mean 640 over frames 42-70).
  - Textured (pale) head front to tail tip, wedge excluded: about 660 in early frames and 556-604 in later ones.
  - The body bends and the tail sweeps while swimming, which changes the projected length.
  - **Ambiguity:** the flat grey wedge ahead of the head looks like an untextured snout. In early frames, where the black shadow sits over the head, the pale textured region reaches further forward. The early "pale head front" readings may therefore really be the snout. For a length prior, the clearest frames are 42-70: wedge to tail 625-655 px.
- **Width** (pectoral fin span across the axis): 225-260 px, typically about 236.
- **Height** cannot be seen in a top-down view.
- **Uncertainty:** tail-tip readings are ±5 px, because the thin pale tip fades into the caustics. Fin tips are ±4 px.
