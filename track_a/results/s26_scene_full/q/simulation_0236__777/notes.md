# Q777: length of the brown horse (m)

- The video is a 2D simulation with a static camera and only one horse (chestnut/brown), walking left to right side-on. The prior's
  "horse at the back" can only be this horse. fps = question_fps = 24.
- Scale from prior speed 0.874 m/s:
  - Trunk template track (scene/tracks/horse.csv, ref_x): 154.2 px over 49 frames = 3.146 px/frame. Every
    step is positive, so the mean per-frame speed equals net/time. The independent buttock-edge track gives 3.168 px/frame.
  - Speed = 3.146 x 24 = 75.5 px/s, so the scale is 0.874 / 75.5 = 0.01158 m/px.
- Pixel length (nose to rear, tail included):
  - Keyframes give 182, 182, 181, 182 and 185 px.
  - My own checks:
    - Frame 49 vs frame 0 difference (measure.py, nose.py): nose edge at x = 496-497 in frame 49, which matches
      the keyframe (497).
    - Frame 0 vs frame 49: rear edge at 152-156.
    - On a zoomed crop, the frame 0 nose is at about 337-338.
  - So the length is 182-186 px; I use 183 px.
- Length = 183 x 0.01158 = 2.12 m.
- Second route: the buttock-edge speed (3.168 px/frame) gives 2.10 m. A horse about 2.1 m long is a plausible size.
- Confidence: moderate-good. The main uncertainty is ±2% from the pixel length (pale face, tail). Whether the
  reference used the root speed or a gait-varying speed adds a little more.
