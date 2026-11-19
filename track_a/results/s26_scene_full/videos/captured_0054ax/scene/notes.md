# captured_0054ax – measurement record

Lab clip (source "lab", 3D), 1280x720, 24 fps, 49 frames (t = frame/24, 0 … 2.000 s).
The people and balls were segmented onto a flat green background (SAM2 watermark bottom-right),
so **no floor, wall or other static scenery is visible**. All values are pixels (x right, y down,
origin top-left) and seconds. Camera intrinsics per the benchmark: f = 0.5959·1280 = 762.8 px, principal
point ≈ (640, 360). No metric scale is assumed anywhere here.

## Files
- `scene.json` – inventory, static-object note, pixel sizes, apparent-size-vs-time for the two big balls,
  events (frame + time), camera notes.
- `tracks/<object>.csv` – one row per frame the object is visible:
  `frame, t, cx, cy` (mask centroid = visible centre), for the two big balls also `circ_cx, circ_cy, circ_r`
  (circle fitted to the silhouette outline), `x0,y0,x1,y1,bw,bh` (bbox, inclusive pixels),
  `length, width, axis_deg` (mask extent along / across its principal axis; axis angle in image degrees),
  `area` (px), `truncated` (mask touches image border), `occluded` (1 = touching / overlapping a person or held).
  People CSVs: centroid, bbox, area.
- `scripts/` – `common.py` (decoder), `track.py` (all tracking; writes CSVs and overlay PNGs to ../frames/),
  `finalize.py` (scene.json), `explore.py`, `colmasks.py`, `dump.py`, `cropsheet.py` (inspection helpers).

## Objects
| name | identify by | motion | visible |
|---|---|---|---|
| person_crouching | black hoodie, squatting at left (x≈60-300, y≈386-640) | body nearly still; right arm pushes basketball (f5-11), left arm pushes soccer ball (f22-29) | 0-48 |
| person_standing | blue-grey hoodie, dark trousers, centre-right, feet at y≈542 | feet fixed; arms swing and throw two small balls (f15-24) | 0-48 |
| basketball | orange-brown, starts (241,572) at crouching person's right hand | rolls right/down toward camera, exits bottom edge | 0-32 |
| soccer_ball | white with black patches, starts (155,597) under crouching person's left hand | still 0-22, pushed down-left, exits bottom-left | 0-40 |
| yellow_ball | small yellow ball | held in standing person's right (image-right) hand, thrown, bounces, flies up past crouching person's head | 0-48 |
| pink_ball | small pinkish/lavender-grey ball | held in the other hand, thrown ~2 frames before the yellow one, bounces, flies up past crouching person's head | tracked 22-48 |

## Key pixel sizes (see scene.json → sizes_px)
- Basketball: free-rolling bbox diameter grows 74→98 px from f11 to f21 (approaching the camera); circle
  fit diameter ≈ 68 px at rest f0-10 (top partly under the hand; the dark underside is less saturated, so
  the at-rest fit is on the orange outline only and may be slightly small); f11+ uses the full fg blob.
- Soccer ball: ≈70 px diameter (circle fit; bbox 70-76) at rest f0-22; motion-blurred and elongated
  (length up to ~97 px) in f29-35.
- Yellow ball ≈ 15 px across (minor axis, f25-30); pink ball ≈ 18 px (f24-29). Both are heavily
  motion-blurred streaks (length 40-70 px) around the bounce (f34-38): use the centroid, not the size, there.
- Standing person: bbox height 335-342 px (top of hood to shoe sole), ~100 px wide with arms down.
- Crouching person: squatting, bbox ≈ 212×219 px at f0 (arms change it later).

## Events (frame / t)
basketball starts moving 6 (0.250 s), separates from hand 11 (0.458), touches bottom edge 22 (0.917), last seen 32.
Soccer: moves from 23 (0.958), separates 29 (1.208), cut by edge from 34, last seen 40.
Throw: yellow ball begins to move with the arm swing ≈15; pink released 22-23, yellow released 24-25.
Apex (image): yellow f26, pink f27. Bounce (max image y, floor itself not visible): yellow f37 (1.542 s),
pink f38 (1.583 s). From f42 both small balls are drawn over the crouching person; still in flight at f48.

## Camera / 3D cues
Static camera (standing person's feet and bbox fixed to ≤1-2 px through the clip; no background texture to
check beyond that). No horizon or ground markings. The crouching person (feet y≈610) is nearer to the camera
than the standing person (feet y≈542). The basketball rolls toward the camera (growing ~70→100 px apparent
diameter); the soccer ball's apparent size stays ~70-75 px until it leaves. The small balls travel from the
standing person toward the crouching person and pass in front of their head at the end.

## Reliability / ambiguities
- Centres of the free big balls: ±1 px. While touching a hand (basketball f0-10, soccer f0-28) the
  circle fit (`circ_*`) is the better centre (±2 px). When cut by the image edge (basketball 22-32, soccer
  34-40) the centroid is biased toward the visible part — use `circ_*` (extrapolated circle, less reliable at
  the last 2-3 frames when only a thin arc remains, e.g. basketball f32 r=54 is an over-estimate).
- Small balls: centroid ±2 px in free flight; strong motion blur f33-38 (centroid is the blur-streak centre);
  f42-48 they overlap the person and the pink ball is separated from skin/face by colour + proximity
  (±3-4 px). Pink ball in hand (f0-21) not tracked (indistinguishable from the fingers; ≈(628,380) at f0).
  yellow_ball f0-24 `occluded=1` = held in hand (fingers cover part of it).
- Which small ball is "pink" vs "grey/lavender/white" is a colour judgement on a green-spill image; it is
  the paler ball, while the other is clearly yellow.
- People: centroid/bbox of the silhouette; face regions are masked green (holes) – bbox unaffected.
