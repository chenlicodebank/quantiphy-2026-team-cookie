# captured_0024s - measurement record (pixels, seconds)

Lab video (real recording; background replaced with a blue gradient, watermark "Modified with Segment Anything 2
Demo"), 3D scene, 1280x720, 24 fps, 49 frames (t = frame/24, 0 to 2.0 s). Camera is **static** (phase correlation
of the wall area: max shift 0.02 px). Task conventions give fx = fy = 762.8 px, principal point ~(640, 360).

## Scene
A pale-teal hardcover book slides down a white board used as a ramp. The board's lower edge sits on a square wooden
table; its upper edge rests on a stack of two books (a dark blue-grey hardcover at the bottom and a cream book on
top). The book sits still at the top of the ramp, slides down to the lower left, goes onto the table, slides a little
further left and stops. The teal book is the **only moving object**.

## Files
- `scene.json`: inventory (names, how to tell them apart, pixel extents/corners), events, camera and perspective cues.
- `tracks/teal_book.csv` (**primary**): every frame 0-48: frame, t_s, cx/cy (centroid of the full visible mask = visible
  centre), bbox x0,y0,x1,y1, min-area-rectangle length/width (main axis / across), bbox height, mask area, occlusion flag
  (always 0).
- `tracks/teal_book_cover_only.csv`: the same columns for the teal cover only (no page edges). Its centroid sits ~3-4 px
  higher than the full-mask centroid; use it as a second estimate.
- `scripts/track_book.py` (args `full` | `cover`), `scripts/static.py` (static masks + camera check), `scripts/probe.py`.

## Method
Clean background plate = median of the last 10 frames, with the book's final resting area taken from the median of
the first 8 frames. Mask = |frame - plate| > 45 AND (teal colour OR bright low-saturation pixels with diff > 60, which
adds the page edges). Then a morphological open/close and the largest connected component. I drew overlays at frames
0, 12, 20, 24, 28, 30, 32, 36 and 48 and checked them: the mask covers the whole book (cover + page block) and nothing
else. Static objects are colour masks at frame 48 plus reading corners from 3x zooms.

## Key numbers
- Teal book start (frames 0-18): centre (783.0, 373.6), bbox 720-848 x 352-397. Rest (frames 36-48): centre
  (570.0, 477.5), bbox 497-647 x 458-496. Net image displacement ≈ 237 px.
- Book apparent size: on the ramp the length is ~128-131 px and the width ~45 px (tilted view). Flat on the table the
  length is 150 px (long axis roughly along image x) with a bbox height of 39 px. The rest pose is the best view of its
  length. The change in apparent size mostly comes from the book's pose (tilted versus flat), not from depth. Its
  depth change cannot be measured without depth_info.
- Ramp corners: TL (750,360), TR (859,361), BL (610,468), BR (706,490). Slope length ≈ 188 px between the edge
  midpoints (177 px along the left side, 200 px along the right). The book's centre travels ~131 px in the image along
  the ramp (frame 19 → 29).
- Book stack: dark bottom book bbox 733-853 x 450-488; cream top book 757-835 x 437-456 (partly hidden by the ramp).
- Table top corners: left (414,470), front (640,608), right (1112,512), back hidden (~860,452). The top is ~20 px thick
  at the front corner. Post: bbox 745-797 x 601-719 (~50 px wide).
- Rough vanishing points of the table edges: (183,333) and (1527,428). The camera looks slightly down at the table.

## Events
Rest on the ramp from frame 0 to 18. Sliding starts at frame 19 (t = 0.792 s; onset between frames 18 and 19). Steps
grow steadily on the ramp (2.9, 5.6, 8.1, 10.3, 12.1, 15.7, 17.9, 19.3, 22.2, 22.5 px/frame for frames 20-29). The
book reaches the bottom of the ramp and contacts the table at about frame 29 (t = 1.208 s) and tips flat over frames
29-32. It slides on the table, slowing down, over frames 32-36 and stops at frame 36 (t = 1.5 s).

## Reliability / ambiguities
- Ramp phase (frames 19-28): the centroid is reliable to ~1 px. During the ramp-to-table transition (frames 29-33) the
  book rotates, so the mask shape changes and the centroid moves partly because of that. For example, the step 31→32
  (25 px) is inflated by the change of pose. The minrect length there (95-122 px) is not a size measurement.
- Light motion blur at frames 26-31. No occlusion of the teal book by other objects. The board's lower edge hides a
  sliver of the book at frames 29-31.
- The mask includes the cream page block and the cover thickness, but not the faint shadow. The white pages against the
  white ramp may lose a few px at the lower edge on the ramp.
- No depth values are known here. For 3D questions, back-project the pixel centres with the given depths and
  fx = 762.8 px.
- Little else in the scene could be confused with the teal book: the cream top book in the stack is static and whiter.
