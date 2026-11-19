# Q3023: speed of the plate (bowl) of tomatoes from 1 s to 1.6 s (m/s)

Prior: fork = 20.3 cm. Internet video, top-down view. I used one planar scale, following the annotators' convention.
The file runs at 19.29 fps, but question_fps is 25, so t = 1.0 s is frame 25 and t = 1.6 s is frame 40 (15 steps).

## Where the earlier answers split
- C1 gave 0.275: fork A = 147 px and a path of about 120 px (200 px/s).
- C2 gave 0.2025: fork = 175 px and 174.5 px/s.
The two differ in both steps. C2's 174.5 px/s (104.7 px over 15 steps) is less than the bowl's net displacement over
the same frames (112 px). A path can't be shorter than the displacement, so C2's motion figure is wrong.
I also could not find any free fork that measures 175 px.

## Motion (speed.py)
I used the scene track, with camera drift removed (the camera drifts about 1 px/frame up). The rim centre and the
tomato centroid agree:
- Raw per-frame path: 129 px / 123 px. The raw path is inflated by jitter in the rim fit at frames 31-33.
- Savitzky-Golay smoothing over 5-9 frames: path 115-120 px, giving 192-199 px/s.
- Net displacement: 112 px (187 px/s).
I take **192 px/s**. Without drift removal the path would be about 214-220 px/s, but the conventions say to measure
against the background.

## Scale (fork_profile.py, crops in frames/)
- **Fork A** (lying on the pink diner's plate, top right, image y ≈ 250): fully visible. The profile runs from the
  handle end (1832, 207) to the tine tips (about 1719, 299), giving **146-147 px**.
- **Fork B** (lying on the table, bottom middle, y ≈ 1040-1197): the tine tips are at about (1268, 1037). The handle
  end is at about y = 1195 in frame-0 coordinates in frames 0-22, next to a hand. That gives **≈162 px**.
- Fork C is held in a hand with its tines in the pasta, so it is not usable.

The 10 % difference between A and B matches the perspective seen in the identical plates: about 226-238 px near the
top and 249-256 px near the bottom. So both forks are the same 20.3 cm fork seen at different distances.

The bowl moves at image y ≈ 530-635. Interpolating the fork length to that height gives about 153 px, so the scale
is 0.203 / 153 = 1.327 mm/px.

## Answer
192 px/s × 1.327e-3 m/px = **0.255 m/s**.

Under the other fork readings:
- Fork A alone: 0.265 m/s.
- Fork B alone: 0.241 m/s.

Sanity checks at 1.33 mm/px: plates come out at about 31 cm, cherry tomatoes at about 3 cm and the table short side
at about 1.15 m. These are plausible.

Confidence: moderate. The main uncertainties are which fork the annotators used (±5 %) and smoothing versus the raw
path (±4 %). I agree with C1's method but not exactly with its scale or its unsmoothed path. C2 is rejected because
of its motion figure.
