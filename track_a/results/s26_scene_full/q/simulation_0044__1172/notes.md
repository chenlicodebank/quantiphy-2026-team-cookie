# Q1172: speed of the eagle at t = 1.0 s (m/s)

The prior is eagle length = 0.8 m. The depths are 175.3081 m at t = 1 s and 172.9881 m at t = 2 s. The question and the file are both 24 fps, so t = 1 s is frame 24 and t = 2 s is frame 48.

## Object and length
- The only moving object is the bird, tracked in `scene/tracks/bird.csv` (I checked it). The other dark blob is its shadow.
- The mask's main axis is about 110–120° in the image, nearly perpendicular to the flight direction (about 15° below +x).
  - The extent across the flight direction swings between 20 and 41 px with the wing beat, so that is the wingspan.
  - The extent along the flight direction stays near 17 px, so that is the body (beak to tail) length. I used it as "length". Per the conventions, a flying animal's wing extent is its wingspan/width.
- How I measured it (`measure.py`, `subpix.py`): darkening against the median background, upsampled ×8, then the extent projected on the local flight direction.
  - Frames 12–35 over the sand: median 16.98 px at a threshold of 0.5 × peak, 17.57 px at 0.35 × peak. I took **L = 17.2 px**.
  - Over the water (frames 46+) the lower contrast makes the extent shrink. Those frames are not used.
- Alternative reading: if the length were the wingspan (about 40 px), the speed would be about 5.1 m/s. I rejected this.

## Scale and speed (`speed3d.py`)
- Focal length: f = L_px × D / 0.8 ≈ 3770 px, a horizontal field of view of about 16°.
- Pixel speed: the backward step at frame 24 is 10.66 px/frame (frames 18–30 average 10.69).
- 3D speed: back-project frames 23 and 24 with the given depths (depth at frame 23 interpolated linearly) and take the backward difference.
  - At L = 17.0 px this gives 12.13–12.23 m/s; at L = 17.5 px, 11.80–11.89 m/s.
  - The depth change of −2.32 m/s is included. It adds only about 0.2 m/s over the image-plane speed.
- Second route: the 3D displacement between frames 24 and 48 using both given depths is 12.15 m over 1 s at L = 17.0 px (11.82 m at 17.5 px). This agrees with the per-frame value because the motion is nearly uniform.

**Answer: 12.0 m/s.**

Confidence: moderate. The main uncertainty is the pixel body length (±3%) and whether "length" means the body length, which I think is the likely reading.
