# simulation_0277 — measurement notes

**Scene:** a 2D simulation (Blender) video, 2560x1440 px, 24 fps, 72 frames (t = 0 to 2.958 s). It shows a static side view of a forest clearing. The **only moving object is a grey raccoon** with a ringed tail. It gallops from left to right across the clearing for the whole clip. It never leaves the frame and nothing ever hides it.

## Files
- `scene.json`: the object list (raccoon, small conifer, bush, pine trunk, background forest, ground), the camera, events and static extents.
- `tracks/raccoon.csv`: one row for each frame 0–71. The columns are:
  - `cx,cy`: mask centroid (the proxy for the body origin)
  - `bbox_cx,bbox_cy` and `x0,y0,x1,y1`: the bounding box, inclusive
  - `bbox_w`: nose to tail tip
  - `bbox_h`: top of back to lowest paw
  - `axis_len`, `axis_wid`, `axis_deg`: PCA main-axis length, width and angle (degrees mod 180)
  - `area`: mask pixels
  - `occluded`: always 0
- `scripts/`:
  - `bg.py`: camera-shift check and median background
  - `track.py`: segmentation and track; it also writes check overlays to `frames/ov_*.png`
  - `static_check.py`: frame-duplicate check and gridded crops of the static objects
  - `probe.py`: colour sampling

## Method
1. **Camera:** I checked for camera motion with phase correlation of the upper (tree) region against frame 0. The maximum shift is 0.001 px, so the camera is fixed.
2. **Background:** a per-pixel median of 9 frames spread over the clip gives a clean background.
3. **Raccoon mask:**
   - Pixels where |frame − background| > 30, below y = 550.
   - **Shadow removal:** I removed pixels that are uniformly darker than the background (ratio 0.5–0.97 in all channels with spread < 0.08) and keep the ground's reddish tint. Without this step the cast shadow stretches the box about 150 px to the left.
   - The largest component, then a second pass at threshold 14 next to the blob. This recovers the semi-transparent-looking grey snout and the dark tail tip in front of the dark trunk.
4. **Checks:** I compared overlays at frames 0, 12, 24, 33, 47 and 56. The box covers nose to tail tip and back to paws.

## Reliability
- **Box edges:** about ±5 px.
  - The snout tip is faint (low contrast with grey ground), so `x1` can jump by about 10 px between frames (for example, frames 0 and 1).
  - Paws can lose 2–5 px at the bottom.
  - In front of the dark pine trunk (frames ~45–60) the dark underside has holes inside the mask. This shifts `cx/cy` by a few px but not the box.
- **Reference point:** `cx` is the centroid of the whole animal, including the tail. The Blender rig origin (pelvis/root) is not observable. Over a stride, displacements of `cx` and `bbox_cx` agree. Frame-to-frame values jitter by about ±3 px from gait and mask noise, so per-frame differences are noisy.
- **Scale:** I kept the raccoon size statistics robust:
  - Length (`bbox_w`) is 277–329 px, median 300.5, including the tail. The body without the tail is about 180–200 px.
  - Height (`bbox_h`) is 108–145 px, median 122. It is largest in the gathered/arched gallop phase (frames 0–1, 16–17, 32, 47, 62–63).
  - The apparent size shows no trend over time, so the raccoon stays at constant depth and one px scale applies to the whole track.
- **Motion:**
  - `cx` goes from 707 (frame 0) to 2287 (frame 71), about 1580 px. The motion is nearly pure +x, with `cy` oscillating between 774 and 794.
  - Frames 0 and 1 are almost identical (the raccoon has barely moved), and steady running starts from frame 1→2.
  - The gallop period is about 15.3 frames.
- **Static objects:** extents come from a gridded view of the median background and are good to about ±15 px:
  - Small conifer: trunk at x ≈ 540, base y ≈ 900, height ≈ 570, crown about 375 wide.
  - Bush: x 1190–1677, top y ≈ 358, base y ≈ 860.
  - Pine trunk: x 1706–1847 at its base (y ≈ 852), about 100 px wide at y = 600, cut off by the top edge.
  - These objects sit at somewhat different depths from the raccoon (the conifer base is lower in the image), so a raccoon-based scale is only approximate for them.
- **Ambiguities:**
  - There is no second animal or object of the same kind.
  - The shadow is excluded from all extents.
  - Gallop phase changes length and height, so per-frame size values differ from the rest-pose size. For a size prior, use the median or maximum depending on the question.
