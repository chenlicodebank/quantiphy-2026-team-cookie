# q_1173 – eagle wingspan (prior: eagle length 0.8 m)

The file and question_fps are both 24 fps. The camera is static and looks almost straight down, and the eagle is the only
moving object. The answer is a size ratio (SS): wingspan = 0.8 m × (span px / length px) × (depth at span frame / depth
at length frames). Both measurements are on the same bird at about the same depth (175.3 m at t=1 s, 173.0 m at t=2 s;
I interpolated linearly), so the focal length cancels. For reference it is f ≈ 17.3 px × 175.5 / 0.8 ≈ 3800 px, which
gives a horizontal field of view of about 16°.

## Measurements (scripts: measure.py, measure2.py, profile.py, crops*.py)
- **Wingspan direction:** the mask's main axis is about 110–120° in the image, which is perpendicular to the flight
  direction (about 8–24°).
- **Span** (measure.py: half-max darkness mask, 6× cubic upsampling, extent perpendicular to the flight direction, and
  Feret diameter):
  - Over the sand, the flap peaks are 35.3 px at frame 5 and 35.3 px at frame 31.
  - Over the water, the peak is 39.7 px at frame 54 (frames 53–55 give 39.3–39.7). The crops (frames/crops3.png) show
    the wings really are longer here: both wing tips reach 2–3 px further than at frame 5.
  - I take the fullest spread seen, 39.7 px at frame 54 (depth about 172.4 m), as "fully spread". Wings in a dihedral
    pose would only look shorter.
- **Length** (head to tail, along the flight axis):
  - The head is pale, so the darkness mask cuts it off on the sand (about 15–17 px).
  - Colour profiles along the body line (profile.py) put the tail edge at about −8.6 to −10 px and the pale/white head
    tip at about +7.5 to +9 px. Frames 5, 31, 40 and 58 give lengths of 17.0, 17.5, 17.6 and 16.7 px, so about
    17.3 px (sand frames, depth about 175.5 m).
  - Over the water, the white head shows up brighter than the background: frame 54 gives about 18 px.

## Result
- Main route: 0.8 × 39.7 / 17.3 × 172.4 / 175.5 = 1.80 m.
- Second route, using only the water frames (same depth, length measured on the same frame 54): 0.8 × 39.7 / 18 =
  1.76 m.
- Lower bound from the smaller sand flap peaks: 0.8 × 35.3 / 17.3 = 1.63 m.

Answer: **1.8 m**. Confidence: moderate, about ±8%. The main uncertainty is the pixel length of the pale head, which is
only about 17 px, and which flap peak counts as "fully spread". A real eagle's wingspan is about 2.3–2.5 times its
length, so a real-world check would favour the higher value.
