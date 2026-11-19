# captured_0020s — measurement record (pixels, seconds)

Lab recording (24 fps, 49 frames, 1280x720, t = frame/24), background replaced by a synthetic blue
gradient (SAM2 demo, watermark bottom-right). 3D scene. **Camera static** (shoes of both people fixed to
<0.7 px std over the clip). Benchmark intrinsics: f = 0.5959*1280 = 763 px, principal point ~(640,360).

## What happens
Two people stand still and exchange two objects with underarm throws, released at the same time:
- **near person** (lower-left, close to camera, long brown hair, dark grey/black oversized T-shirt, black
  trousers, white sneakers; cut by the left image edge) throws the **white object** to
- **far person** (top centre, far, light-grey fitted T-shirt, dark navy trousers, white sneakers with black
  stripes; head above the top image edge), who throws the **yellow toy** (elongated yellow, green leafy end;
  banana / corn-cob like) to the near person.

## Files
- `scene.json` — inventory, phases, apparent sizes, events, camera/perspective summary.
- `tracks/white_object.csv`, `tracks/yellow_toy.csv`, `tracks/person_near.csv`, `tracks/person_far.csv`:
  one row per frame: `frame, t_s, cx, cy` (mask centroid = visible centre, the lab-convention reference point),
  `bbox_x0..y1, bbox_w, bbox_h`, `mask_len_major, mask_wid_minor` (PCA extents of the mask in px),
  `major_axis_deg` (image angle, 0 = +x, 90 = down), `mask_area`, `occluded` (0 clear, 1 not visible,
  2 partly covered / merged), `note` (phase).
- `static_measure.json` — per-frame shoe blobs (camera-stability check), body axes and vertical vanishing point.
- `scripts/`: `track.py` (all tracks + overlays), `static.py` (shoes, axes), `dump.py`, `mosaic.py`,
  `ovsheet.py`, `probe.py`, `blobs.py` (viewers / exploration).

## Method
- Foreground = colour distance > 30 from a quadratic 2D fit of the blue background (a temporal median was
  rejected: it absorbs the almost-static near person).
- Yellow toy: HSV H 19-42, S>=70, V>=90 core, nearest component to a constant-velocity prediction; in flight
  grown by weaker yellowish foreground pixels within 8 px (blur, green end), never white pixels.
- White object: S<=38, V>=165 within the foreground; in flight the full foreground blob minus yellowish pixels.
  After the catch (26-48) the object is separated from the far person's light-grey top by brightness
  (object V>=205, top V 140-185) inside a 24 px disc around a by-eye seed (seeds listed in track.py, WHINT).
- People: large foreground components (near: touching left edge; far: touching top edge), objects removed.
- All tracks were drawn on frames and checked (frames 0-48, zoomed on hands and the crossing).

## Phases / events (frame, t = f/24)
- White object: held by near person 0-13 (backswing lowest at 4-5, forward swing from 6), **release 14**
  (t=0.583, ±1 frame), free flight 14-26, highest image point frame 22 (y=37), **caught by far person 27**
  (t=1.125; at 26 just above her hand), then carried down to y~163 (35-36) and back up to y~70 (47-48).
- Yellow toy: held by far person 0-13 (hidden behind her hand/leg 4-7), forward swing from ~9, **release 14**
  (t=0.583, ±1), free flight 14-26, highest image point ~17-18 (y~67-73), touches near person's hands 26,
  **caught 27** (t=1.125), hidden 28-37, held in front of the near person 38-48.
- The two objects cross in the image at 18-19 (white in front at 18) — not a physical collision.
- People do not walk; feet fixed. Far person bends forward to catch (~26-36).

## Apparent size changes (3D cues)
- White object in flight shrinks (moving away): major axis ~61 px (15) -> ~32-34 px (24-25); minor 34 -> 24.
- Yellow toy in flight grows (approaching camera) and tumbles: major 53 px (14) -> 74 (22) -> 88 (24) -> 96 (26),
  minor ~29-46 px. Its length is best seen near-side-on at 25-26 (87-96 px) and 21-22 (68-74 px).
- Camera looks steeply down: body axes converge at a vertical vanishing point ~(835,1068) (below the image),
  i.e. pitch ~45° down, horizon far above the image (~y -400). Rough (±10°). No floor or markings visible
  (background replaced), so no ground-plane measurements are possible.

## Static references (frame 0, unchanged all clip)
- Far person shoes: image-left bbox x704-723 y241-268 (centre 713.9,255.1); image-right x735-753 y242-269
  (743.2,255.8); shoe spacing ~29 px; visible body y 0-271 (head cut off, so no full pixel height).
- Near person right shoe: bbox x340-389 y652-708 (centre 366,676).

## Reliability / ambiguities
- Flight tracks (14-26) of both objects: good, centroid ±1-2 px; frames 18-19 lower (overlap, motion blur;
  yellow at 18 mostly hidden behind the white object, its centroid biased toward the visible part).
- Frame 14 (white) and 26 (white), 24-26 (yellow): hands adjacent, masks may include/omit a few px.
- Held phases (occluded=2): centroid of the visible part only; sizes are not object sizes. Yellow toy masks
  while held include the green end only partly (0-13) and are fragmentary at 27 and 38.
- Yellow toy not visible 4-7 and 28-37 (empty rows). White object visible every frame.
- Person tracks are visible-mask centres (both people are cut by the image border), not pelvis positions.
- Object identity is unambiguous (one white, one yellow object). The far person's grey top and both people's
  white shoes are similar in colour to the white object but are spatially separate except during 27-48.
