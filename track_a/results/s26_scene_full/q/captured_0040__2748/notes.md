# Q2748 – velocity of the white ball at t = 1.4 s (cm/s)

t = 1.4 s -> frame round(1.4*24) = 34 (file fps = question fps = 24; container pts regular).
Frame 34 is one frame after the first bounce on the table (frame 33).

## Method (lab card)
- f = 0.5959*1280 = 762.8 px, principal point (640,360).
- Ball centres: scene/tracks/ball.csv, re-checked with own mask (size.py) and zoomed strips
  (strip.py, strip2.py -> frames/): centroids agree within ~1-2 px except bounce frame 33 (~5 px, blur/table).
- Depth: given d(f36)=0.7045 m, d(f48)=0.627 m. Back-projected P36, P48. Depth at other frames from
  (A) a straight top-view path (ball stays in the camera-vertical plane through P36,P48) -> d34 = 0.764 m,
  d35 = 0.738, d33 = 0.792; (B) apparent diameter perpendicular to motion blur (38.0 px at f36 -> K = 26.8 px·m):
  d34 = 0.765 (35.0 px) – agrees with A. Pre-bounce size ~34.7 px -> d ≈ 0.77 m.
  Size model also reproduces d48 (≈43 px in f42-47 -> 0.62 m vs given 0.627).
- Gravity check: after the apex, image-y second difference 18.3 px/frame² at d≈0.72 m -> 9.9 m/s² (scale ok).

## Speeds at frame 34 (model A, cm/s)
- forward diff 34->35: 143.4; backward 33->34: 145.5; central 33-35: 144.3 (vector (0.75,-1.10,-0.55) m/s)
- mean of forward speeds 32..36: 153; 33..37: 128; Savitzky-Golay 5-frame slope: 120; 5-frame position
  smoothing then diff: 109 (crosses the bounce -> biased low).
- Model B (size depths) forward 202 / central 168 – noisy per-frame size, less trusted.

## Caveats
- Frame 35->36 image step is 60 px vs ~33 px neighbours: probably a dropped camera frame; frame 33 is the bounce.
  These make the 5-frame-smoothed conventions scatter (110-153).
- Answer 135 cm/s: between the local physical speed (~144) and smoothed-convention values (~110-128).
  Confidence: moderate (±15%).
