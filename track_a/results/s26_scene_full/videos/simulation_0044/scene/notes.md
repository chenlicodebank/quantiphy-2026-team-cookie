# simulation_0044 – measurement record

Video: 1080x1080 px, 24 fps, 72 frames (t = frame/24, 0 … 2.958 s). Source: simulation, a 3D scene.
Pixel coordinates: x points right and y points down, with the origin at the top-left corner.

## Scene
The camera looks almost straight down on a beach. A pale pink sand spit fills the upper left of the image, and a large
rock (white-lit on its left side, dark facets on its right) sits in the upper middle. Dark green sea lies along the
bottom and the right. **One bird** (dark, flapping wings) flies across the image from left to right and slightly
downwards. It starts over the sand and is over the water by the end. Its **soft cast shadow** moves on the sand about
240 px to the upper right of it. Nothing else moves: there are no people, vehicles or other animals.

## Files
- `scene.json`: inventory (bird, bird_shadow, rock, sand_spit, water), camera, pixel extents, events.
- `tracks/bird.csv`: frames 0–71, all of them.
- `tracks/bird_shadow.csv`: frames 0–41.
  Both track files have these columns: frame, time_s, cx_px/cy_px (mask centroid = reference point), axis-aligned
  bbox (x0, y0, x1, y1, w, h), length_main_axis_px / width_across_px (PCA extents of the mask), main_axis_deg
  (image angle, 0 = +x, measured clockwise because y points down), area_px, contrast_peak (grey levels darker than the
  background), occluded (always 0).
- `scripts/`: the scripts.
  - `bg_camera.py`: median background and camera-shift check. Its output `bg_median.png` is used by the other
    scripts.
  - `detect.py`: lists blobs.
  - `pair_crops.py`: compares the bird with its shadow.
  - `track.py`: tracking, CSVs and overlay images.
  - `static_rock.py`: rock mask and track statistics.

## Method
- **Camera:** static. Phase correlation against frame 0 gives shifts below 0.03 px, so no background correction is
  needed.
- **Masks:** each mask is made from d = (median background − frame grey), taken in a 90x90 px window around the
  predicted position. The threshold is half the window's peak darkening, and the largest component is kept.
  - A half-maximum threshold keeps the mask size consistent when the bird passes over the darker water.
  - I drew the overlays (frames 0, 12, 24, 36, 44, 56, 66, 71) and checked them: the mask covers the whole silhouette
    of the bird, including the wings.
- **Reference point:** the silhouette centroid, used as a stand-in for the bird's origin (body centre). The flapping
  wings move the centroid by about ±1 px from frame to frame.

## Key numbers (pixels)
### Bird
- Moves from (117.1, 549.7) at frame 0 to (835.0, 744.0) at frame 71.
  - Net displacement: 744.1 px. Path length: 749.4 px.
  - Heading: about 15° below +x.
- **Frame 1 is an exact duplicate of frame 0** (the step is 0 for the whole image). Every step from frame 1 onwards
  is 10.0–11.4 px/frame (median 10.8). The steps creep up slightly, from about 10.5 in frames 1–35 to about 10.9 in
  frames 36–71, so the bird's motion is nearly uniform.
- Apparent size changes only with wing pose:
  - main-axis length 20–40 px (median 28.7)
  - width across 11–19 px
  - bbox up to 24 x 37 px
  - area 154–323 px

  There is no trend over time, so the camera distance is roughly constant (as expected when a bird flies level under
  a nadir camera).
- Wingspan in pixels: in an open-wing pose the mask's maximum extent is about 36–40 px (for example frames 30–31 and
  48–60; see the length column). In folded or vertical poses it is smaller.

### Shadow
- Moves from (350.3, 514.3) to (761.1, 618.8) over frames 0–41. Offset from the bird is about (+233…+245, −35…−48) px.
- Clear on the sand up to about frame 26.
- Fades over the shallow water from frame 27 onwards. Contrast drops below 40 after frame 35, so positions from
  frames 35–41 are less reliable (±3 px). It is lost after frame 41.
- Its centroid steps vary between 8.5 and 14.6 px/frame because its shape stretches with the wing pose. **Use the
  bird track, not the shadow, for the bird's motion.**

### Rock (static, frame 0)
- bbox x 385–919, y 0–456 (535 x 457 px). Centroid (641, 203).
- Main axis about 543 px (at 154° in the image), width about 422 px, area about 172k px².
- Accurate to ±15 px. The rock may be cut off by the top of the frame.

### Sand edge
The edge between sand and water runs from about (0, 470) down to its lowest point near (360, 770), then up to the
right to about (1000, 0).

## Events
| Frame | Time (s) | Event |
|---|---|---|
| 0 | 0 | Bird already in flight. |
| 1 | 0.042 | Duplicate of frame 0. |
| ~27 | 1.125 | Shadow reaches the shallow water and starts fading. |
| 42 | 1.75 | Shadow no longer detected. |
| ~45 | 1.875 | Bird crosses the sand edge and is over the water; its contrast drops from about 178 to 120. |
| 71 | 2.958 | End of the clip; the bird is still flying. |

There are no bounces, impacts or contacts.

## Ambiguities and reliability
- **Shadow or second bird?** The second dark shape could in principle be a second bird. I recorded it as the shadow
  because:
  - it is blurred while the bird is sharp;
  - it mirrors the bird's wing pose;
  - it keeps a near-constant offset from the bird;
  - it disappears over the water, where a real bird stays visible.

  If a question mentions "two birds", the shadow track is the second object.
- **Low contrast over water:** after frame 45 the bird's contrast drops, but the half-maximum masks still look
  complete (checked at frames 56, 66 and 71). Centroids are accurate to about ±1 px. Extents are accurate to about
  ±2 px on the sand and about ±3 px over the water.
- **Perspective:** none can be measured. There is no horizon and no vanishing points, and the camera is close to
  nadir. Ground features and the bird lie at different depths (the bird is closer to the camera), so a scale derived
  for the ground does not apply to the bird. Use depth_info and focal-length estimation for 3D questions.
