# internet_0023 — measurement record

2D internet video, 2560x1440, 26.636204 fps, 130 frames (t = frame/fps). Units: full-resolution pixels, seconds. No metric scale guessed.

## Scene
Top-down drone shot of a rectangular pool on a dark wooden deck. One moving object: a **swimmer** (man, white trunks, dark hair) who dives in at the left end and goes right (+x) along y ≈ 680–700. The video starts mid-dive, with the body flat at the surface and the fingertips just touching the water. He is fully under water from frame ~19 and glides, then swims underwater (breaststroke-like arm sweeps) until the end. Static items: the pool (main basin plus a step bay at bottom right), the stone coping, 4 coping lights, 6 teal loungers (2 above, 4 below the pool), 4 umbrellas (3 white; 1 top right that looks grey because it is in shade), a thatch roof at the top, and trees.

## Files
- `scene.json`: inventory, pixel sizes, events, static object extents, camera summary.
- `tracks/swimmer.csv`: one row per frame (0–129). Columns:
  - `mid_x, mid_y`: visible centre = (rear+front)/2 and the centre of the body's y extent. Only where the feet are known (frames 0–18, 74–129).
  - `front_x` (+`front_src` m = manual read, i = interpolated): leading tip (fingertips, splash front underwater, or tip of the head patch). Every frame.
  - `rear_x` (+src): toe tips. Frames 0–18 and 74–129.
  - `length_px` = front−rear, `width_px` = y extent, `bbox_*` = rear/front × y extent.
  - `head_x, head_y` (`head_src`): manual head centre for frames 0–6. For frames 22–129 it is the automatic centroid of the smooth head/shoulder patch. Missing for 7–21.
  - `headpatch_*`: bbox of that patch. `hip_x`: centre of the trunks, frames 0–8.
  - `*_bgcomp`: the same value minus the camera drift (dx, dy).
  - `visibility`: air/entering (0–5), partly_submerged (6–19), submerged (20+).
- `camera.csv`: per frame dx, dy (px, the shift of image point (1100,700) relative to frame 0), rotation, scale and inlier count. From LK feature tracking on deck, coping, loungers and umbrellas (pool water masked) and a RANSAC similarity fit.
- `camera_shift_raw.json`: an earlier, cruder check from an older version of camera.py. It holds [frame, dx_top, dy_top, dx_bottom, dy_bottom], phase correlation on the top and bottom image strips. It agrees with camera.csv to a few px. Use camera.csv.
- `scripts/`: camera.py, patch.py (head-patch tracker, writes `_patch.csv`), build_track.py (holds every manual keyframe value), overlay.py, zoom.py and strip.py (viewers), pool_edges.py, statics.py, seg.py and probe.py (exploration).

## Methods and reliability
- **Camera**: near-nadir and essentially static. It drifts slowly: dx reaches +12.8 px and dy dips to −8.4 px, with scale −0.4 % and rotation < 0.05°. This is about 1 % of the swimmer's ~650 px travel. Use the `_bgcomp` columns to measure against the background.
- **Frames 0–9** (body clearly visible): toes, head, trunks and fingertips were read on 2× zooms with a 20 px grid, ±3 px. The best full-body length is in frame 0: **256 px feet→fingertips** (arms stretched forward), **205 px feet→top of head**, body width ≈ 47 px. Frames 1–3 read 266–274 px because the body is diving down at an angle and splash hides the hands. For a person-length prior, the frame 0 value is the cleanest.
- **Frames 10–21**: the swimmer is under the splash. The front is a splash/body front (±8 px). Toes were visible up to frame 18. Head not visible.
- **Frames 22–129**: the head/shoulders show as a distinctive flat, texture-free blob. `patch.py` tracks it automatically (local std < 2.5 grey levels, dilated 4 px). Its bbox agrees with manual reads to about ±5 px. The centroid jitters by a few px with arm position, especially during the arm sweep at frames 92–107, when the patch becomes cross-shaped. Smooth over ≥3–5 frames before differencing.
- **Rear/front for 74–129**: manual keyframes about every 6 frames, interpolated linearly. Toes are ±5–8 px because of underwater blur and kicking. In frames 74–86 the legs are bent or kicking downward, so the apparent length shrinks to 150–190 px. Underwater straight-body length is ~200–210 px (frames 110–122). The underwater body looks smaller than at the surface (depth plus refraction).
- **Interpolated rows** (`*_src = i`) are linear between keyframes. They give piecewise-constant per-frame speed. For speeds, prefer differences over several frames, or use `head_x` (per-frame automatic) for t ≥ 0.83 s.
- **Motion summary** (head-patch x, bg-compensated, px/frame): entry glide ~17–20 px/frame (front, frames 0–9), ~12 (9–18), then strong deceleration to ~1–2 px/frame (26–36). Underwater swimming then goes ~4–5 (58–72), ~2 (78–86), stalls (94–101) and returns to ~4–5 (102–125). Overall the head goes x 1071 (f22) → 1419 (f129).
- **Static extents** (frame 0): main basin water x 566–1725 (1159 px long), y 478–1020 (542 px wide). Step bay to x 1942. Outer coping x 526–1983, y 440–1057. Coping ~40 px wide. Steps have ~38 px pitch. Top loungers 246 × 89 px. Bottom loungers are 80–86 px wide, and their lower parts are hidden in palm shadow (true length ~240 px). Umbrellas measure ~260–300 px across (flat-to-flat vs corner-to-corner). Edges are ±2 px for water, ±5 px for furniture.

## Ambiguities
- The swimmer's dark **shadow on the pool floor** runs up-left of his body: early it is offset ~50–80 px above it, and later it trails as a wavy dark band. Do not confuse it with the swimmer.
- The **head patch** is the swimmer's upper body seen through calm water. Its front tip includes the hands when the arms are forward.
- No take-off is visible (video starts mid-air/at entry), so a "dive start" question can only refer to frame 0.
- "Swimmer length" could mean the frame 0 body (256 px with arms, 205 px without), or the underwater apparent length (~200–210 px). Choose the one matching the prior's definition.
