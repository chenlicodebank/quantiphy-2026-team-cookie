# q421: height of the stone cliff (simulation_0175)

The video is 2D, side-on, with a static camera, at 24 fps (file fps and question_fps agree). I used one metres-per-pixel scale, taken from the airplane's speed prior.

## Scale
- `measure.py` measures the airplane's per-frame shift by integer plus sub-pixel SSD matching of the y 80–200 band over frames 10–31. The shift is **61.57 px/frame** (range 61.41–61.70). That matches the scene record's 61.5 ± 0.2.
- Pixel speed = 61.57 × 24 = 1477.6 px/s. Scale = 153.582 / 1477.6 = **0.10394 m/px**.
- Check: the airplane's 466 px length gives 48.4 m. That is large for a business jet, but rendered scenes are not to real-world scale.

## Cliff height (frame 0; the cliff is static)
- The top of the vegetation-capped rock asset is at y = 520, the first non-sky row found in code (treetops near x 935).
- The base, where the dark rock meets the sand, is at y ≈ 1005–1011 on the left and centre and 1025–1030 at the front-right corner. I take the base as ≈ 1020.
- The full height is therefore ≈ 500 px, which gives **≈ 52.0 m**. This agrees with the scene record (531 to 1030, ≈ 500 px).
- Alternative reading, bare rock only (rock top ≈ 625 to base ≈ 1020, ≈ 395 px): ≈ 41 m. I answer with the whole cliff object (rock plus trees, one asset, so its bounding box includes the trees).

## Second route
- The scene record's per-frame shift of 61.5 px gives 0.1040 m/px, which leaves the answer unchanged.
- Base at 1010 instead of 1020 changes the answer to 51.0 m (−2 %).

## Confidence
Moderate. The main uncertainty is whether the reference includes the trees and how the base is defined.
