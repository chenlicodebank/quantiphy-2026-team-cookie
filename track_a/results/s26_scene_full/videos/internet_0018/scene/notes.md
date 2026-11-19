# internet_0018 — measurement record

**Scene.** A drone looks straight down on a red clay tennis court (3840x2160, 29.97 fps, 51 frames, t = i/fps). The court's long axis runs along image x. The **server** (right baseline, x≈3650) tosses the ball and serves it leftwards. The serve flies across the court, crosses the right service line, and **hits the net tape at frame 48** (net fault, no bounce). The **receiver** stands at the left baseline near the top singles-sideline corner and hardly moves. There is no metric scale in this record: everything is in pixels and seconds.

## Files
- `scene.json`: inventory, events, camera summary, court-line fits at frame 0 and derived court dimensions in px, ball post-hit per-frame steps, mask-size statistics.
- `tracks/ball.csv`: per frame: centre `cx,cy` (raw image px), `cx_stab,cy_stab` (mapped into frame-0 coordinates), yellow-pixel bbox, apparent diameter `diam_px`, `occluded` flag, note.
- `tracks/server_right.csv`, `tracks/receiver_left.csv`: per frame: mask centroid (raw and stabilised), bbox, PCA mask length/width and axis angle, area, and `core_cx,cy` (centroid after a 21 px opening, which keeps the torso and drops limbs and racket).
- `camera_motion.csv` (+ `camera_affine_half.npy`): per-frame similarity transform from frame 0 to frame i (ORB + RANSAC). Gives the image-centre shift, scale and rotation.
- `scripts/`: every script used (`camera_motion.py`, `track_ball.py`, `track_players.py`, `court_lines.py`, `build_scene_json.py`, `overlay_check.py`, viewers `montage.py`, `crops.py`, plus exploratory `diff_blobs.py`, `stab_blobs.py`, `yellow.py`). Run them from `scene_ws/`.

## Camera
The drone hovers with a slow drift. The image content shifts smoothly by dx≈+5.5, dy≈−14 px over the whole clip (≈0.3 px/frame), with a 0.3 % zoom-out (scale 0.9971) and no meaningful rotation. This drift is negligible next to the ball (115–156 px/frame after the hit), but it matters for the players. Use the `*_stab` columns for player motion.

Perspective is near-orthographic. The court is a rectangle to within ~1 %: the right end is ~0.9 % wider than the left end, and the lines are rotated ~0.4°. There is no horizon. A single planar scale is appropriate (the annotator convention).

## Court (static, frame 0, line centres)
| Measurement | px |
|---|---|
| Baseline to baseline | 2680 |
| Doubles width at net | 1235.5 (1230 at left baseline, 1241 at right baseline) |
| Singles width | 924.7 |
| Net to service line | left 729.3, right 711.8 |
| Service line to baseline | left 615.7, right 623.2 |
| Service line to service line | 1441.1 |
| Doubles alleys | ~155 |

These ratios match a standard court: 23.77 × 10.97 m gives ≈112.7 px/m from both length and width. Small ±2 % differences between segments come from lens distortion and slight tilt. Lines are 4–6 px wide.

The net is a near-vertical line at x≈2186–2192. Its tape is visible from y≈300 to y≈1790.

Other static items:
- benches with bags at the top edge (x 1930–2500)
- a coiled yellow hose (x 1925–2200, y 1915–2050)
- a drain at (2185, 1855)
- sprinkler covers (see scene.json)
- a fence and blue windscreen at the left edge

## Ball (reliable)
The centre is the G−B-weighted centroid of the yellow blob, accurate to about ±1 px in clear frames. Every frame was checked visually (`frames/chk_ball.png`).

- **Frames 0–36: the toss.** The ball rises from the server's hand. Seen from above, the vertical toss shows up as a slow drift: x goes 3634 → max 3772.5 at frame ~20 (the apex) → 3662 at frame 36. The apparent diameter grows from 8.5 to ~12–13 px as the ball nears the camera.
- **Frame 37: just after contact** (contact is between frames 36 and 37). The ball is beside the racket, only a 3 px yellow fragment shows, and it is flagged occluded. Its position fits the back-extrapolated post-hit path.
- **Frames 38–47: free flight to the left.** Clear images with no motion streak. The per-frame step falls from 150 to 115 px. Part of that is real slowing and part is perspective: the ball descends, so its apparent diameter drops from 12 to 9 px. No motion model is applied.
- **Frames 42 and 43:** the ball is over or near the white service line, so contrast is low (flagged occluded, but still measured).
- **Frame 48:** the ball is hidden in the net tape. Its position (2190, 974) is the centre of the tape bulge, an estimate to ±5 px.
- **Frames 49–50:** the ball sits against the net (~2183–2188, 963–969) and is partly hidden.

The true ball diameter would be ≈7.5 px at the court scale. The measured 9–13 px is inflated by blur and halo and by the ball being above the ground, so don't use it as a size prior unless a question asks for apparent size.

## Players (moderate reliability)
Masks are the non-clay pixels (white clothes, skin, dark shorts, racket) in a window that follows the camera. Court-line bands (±7 px) are blanked out and bridged with a closing. Shadows are clay-coloured and therefore excluded.

The masks were checked visually at frames 0, 20, 37, 44 and 50:
- The racket is sometimes inside the mask and sometimes dropped (e.g. the server at frame 20), which makes the bbox and length jump by tens of px.
- Thin limbs or a shoe can be missed (the receiver's lower foot at frame 20).
- Centroids are stable to ~5–10 px. For body position, `core_cx/core_cy` is more robust.

Because the view is top-down, the bbox shows the body's footprint and arm span, not standing height. **Player height cannot be measured here.**

- **Server:** body mask length ~140–160 px. After the hit (frames 38–50) the server lands and steps into the court, leftwards and up in the image.
- **Receiver:** mask ~95–115 px. Shifts stance by less than about 30 px.

## Events (frame / time in s)
| Frame | t (s) | Event |
|---|---|---|
| 0 | 0.000 | Ball just released and rising in the toss |
| ~20 | 0.667 | Toss apex (±2 frames) |
| 36→37 | 1.235 | Racket contact (between these frames) |
| 42 | 1.401 | Ball crosses the right service line |
| 48 | 1.602 | Ball hits the net tape |
| 49–50 | | Ball held at the net; clip ends |

## Ambiguities
- **Ball versus hose:** the yellow hose is static and excluded.
- **Contact time:** sub-frame.
- **Ball height:** unknown from a single top-down view. Pixel speed mixes horizontal motion with radial perspective motion, since the ball is off the image centre.
- **No bounce occurs.**
- **Scale:** the annotator convention is one scale = prior / pixel measurement. For a court-dimension prior, use the matching px value above. For a ball-speed prior, use pixel steps from `ball.csv` (raw `cx,cy`; the drift is negligible).
