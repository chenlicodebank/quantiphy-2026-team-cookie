# simulation_0145: measurement notes

2D Blender render, 24 fps, 29 frames (0 to 1.1667 s), 1920x1080. A side view of an olive 3-axle rocket-launcher
truck (HIMARS-like) facing left on a desert road, with its launcher pod raised about 39 deg. One rocket slides out of
the pod's upper end and flies in a straight line up and to the left, speeding up, until it leaves the top of the
image. **The camera is static.** Everything is in pixels and seconds. No metric scale has been assumed.

## Files
- `scene.json`: inventory (rocket, truck, pod, road, dunes, shadow), static extents, flight axis, rocket length
  and width, events, camera.
- `tracks/rocket.csv`: one row per frame, frames 4-25.
  - `cx,cy`: rocket centre, the reference point.
  - `s_axis`: centre position along the flight axis (px). It increases in the flight direction from the axis point
    (672.42, 208.80), unit direction (-0.77732, -0.62910). Distances between frames along the path equal differences
    in `s_axis`, because the path is a straight line.
  - `nose_*`, `tail_*`: centre ± L/2 along the axis, with L = 201.8 px.
  - `ref_method`: how the centre was obtained.
  - `bbox_*`: bbox of the |diff| > 30 mask. This includes motion-blur smear and covers only the visible part.
  - `visible_len_px`: visible length.
  - `len50_px`: blur-free length, given only when the whole rocket is visible.
  - `width_px`: across-axis width.
  - `mask_len_d30_px`: raw length of the d > 30 mask, blur included.
  - `occluded`: occlusion flag.
- `scripts/`: every measurement script.
  - `diffscan.py` / `diffviz.py`: change detection against frame 0.
  - `rocket_free.py`: first segmentation pass.
  - `rocket_track.py`: axis fit and nose/tail ends at threshold 30. Writes `_rocket_raw_t30.json`.
  - `rocket_profile.py`: blur study.
  - `rocket_final.py`: writes the csv and the overlay.
  - `static_check.py`: camera and truck shifts, truck mask.
  - `pod_extent.py`: pod extents.
  - `cropsheet.py`: zoomed crops for viewing.

## Method
- **Segmentation:** |frame − frame0| (max over RGB). The background never moves, so only the rocket and the
  truck's tiny rocking change.
- **Flight axis:** a line fitted through the free-flight centroids (frames 15-21). The residuals are under 0.05 px,
  so the path is straight, at 38.98 deg above horizontal and heading up-left. The rocket's orientation matches the
  path.
- **Rocket ends:** taken from the band-summed along-axis profile (band ±13 px) at 50% of the body plateau.
  - Motion blur is a symmetric smear along the axis, so the 50% crossings sit at the true ends.
  - The result is length L = 201.8 px (median of frames 13-21; range 199-210).
  - The raw d > 30 mask is 226-240 px long and grows with speed, which shows blur. The shutter covers roughly
    0.75 of the frame interval.
  - A second estimate, the 10%-level length minus 0.75 × displacement per frame, gives about 205 px. Best value:
    **202 px (±5)**.
  - The 50% point at the tapered nose may sit a few px behind the actual tip, so the true length could be slightly
    larger, perhaps up to about 210.
- **Width:** 16.7 px.
- **Centre:**
  - Frames 13-21: midpoint of the two ends.
  - Frames 4-12: the tail is inside the launch pod, so centre = nose − L/2. The centre itself is hidden behind or
    inside the pod.
  - Frames 22-24: the nose is above the image, so centre = tail + L/2. These centres can lie outside the image
    (cy < 0).
  - Frame 25: only a 48 px tail stub remains, so centre = tail(d > 30) + 20 + L/2. Low reliability, ±5 px.
- Overlays drawn on frames 6, 9, 12, 15, 18, 21, 23 and 24 (`frames/rocket_overlay.png`, a scratch file) confirm
  that the nose, centre and tail points and the bboxes sit on the rocket.

## Reliability
- **Free-flight centres (frames 13-21):** about ±1 px.
- **Partial frames (4-12):** ±3-4 px. Per-frame advances are noisy there; for example the jump from frame 7 to 8 is
  33 px and from 8 to 9 is 25 px. Frames 4-5 are the least reliable, with only 3-20 px of nose visible. Fit a smooth
  motion rather than trusting single-frame differences.
- **Frames 22-24:** ±2 px. **Frame 25:** ±5 px.
- **Along-axis advance of the centre (px/frame), for orientation only:** f5 17, f6 16, f7 23, f8 33, f9 25, f10 32,
  f11 35, f12 37, f13 38, f14 42, f15 48, f16 46, f17 50, f18 52, f19 54, f20 57, f21 58, f22 61, f23 60, f24 62.
  The rocket is clearly accelerating.
- **Truck and pod static extents:** read from 2× zoomed crops at frame 0, ±3 px. The pod's lower end is ±10 px
  because it merges with the lifting gear.

## Events
| Event | Frame | Time (s) |
|---|---|---|
| Truck starts rocking (first sign of launch) | 2 | 0.083 |
| Rocket nose first visible at the pod mouth (980, 458) | 3 | 0.125 |
| Tail leaves the pod mouth (estimated from nose − L) | between 11 and 12 | ~0.48 |
| First frame where the whole rocket is clearly free | 13 | 0.542 |
| Truck rocking ends | 14 | 0.583 |
| Nose reaches the image top | 22 | 0.917 |
| Last trace of the rocket | 25 | 1.042 |
| Rocket gone (frames 26-28 have no rocket) | 26 | 1.083 |

The true start of the rocket's motion is hidden inside the pod. It is before frame 3, probably around frame 1-2.

## Camera and scale
- The camera is static: background shift ≤ 0.01 px in every frame.
- This is a 2D scene, so use one px-to-metre scale from whichever prior a question gives. Possible priors include
  rocket length 202 px, rocket diameter 16.7 px, truck length 672 px (front bumper 568 to rear outrigger 1240),
  cab-roof height 227 px, wheel diameter 98 px, and a rocket speed or acceleration measured from the csv.
- The truck is seen exactly side-on and the rocket appears to fly in the same plane.

## Ambiguities
- **Motion blur** makes the raw rocket mask about 25-40 px too long. Use L = 202 px for size priors.
- **The bbox columns are blurred and visible-part-only.** A world-space axis-aligned box for the rocket would be
  about 157 × 127 px for the axis span, or about 168 × 140 px including the diameter.
- **There is only one rocket.** No exhaust plume or smoke is visible. There is a faint light smear behind the tail
  from motion blur.
- **The truck does not move,** apart from rocking under 1 px during frames 2-13.
