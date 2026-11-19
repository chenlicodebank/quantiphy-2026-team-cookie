# q149 — length of the small bird (m); prior: small bird speed = 11 m/s

2D side-view scene (static camera, blue sky). Small bird = the black crow flying right (the other bird is a large eagle).
File fps = question fps = 24.

Method (measure.py): background = median of empty frames 14-29; mask = RGB distance > 15 (also checked at 30), restricted to x > 1000.
- Speed in px: crow right edge 1199 -> 1904 over frames 1->10 = 78.3 px/frame; darkness-weighted centroid 1160.1 -> 1866.0
  = 78.4 px/frame; per-frame edge dx 76-80, constant. -> 1881 px/s -> scale = 11 / 1881 = 0.005848 m/px.
- Length (tail tip to beak, horizontal extent): 90-92 px at thr 15, 87-92 at thr 30 in every fully visible frame 0-10
  (static frame 0: 1108-1199). The scene record's 89 px is consistent. Taking 90 px (removing ~1 px anti-alias fringe).
- Length = 90 x 0.005848 = 0.526 m (range 89-91 px -> 0.52-0.53 m).

Check: two independent speed references (edge and centroid) agree to 0.2 %; length is stable across 11 frames with
different wing poses. 0.53 m is plausible for a crow/raven (realistic prior, real-world scale). Confidence: high (~3 %).
