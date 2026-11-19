# q_2752 – diameter of the white ball (cm)

Lab clip, 1280x720, 24 fps (file fps = question_fps = 24). f = 0.5959*1280 = 762.8 px, principal point (640,360).
Depth anchors: ball 0.7045 m at t=1.5 s (frame 36), 0.6270 m at t=2.0 s (frame 48).
The ball is motion-blurred in every flight frame, so its diameter is the blur-streak width *perpendicular* to the motion.

## Scale check (prior)
Credit card = the dark card lying flat at the front (x≈510–617, y≈529–550). Its long edges measure ~92–104 px
(the image parallelogram is sheared), mean ≈ 97.6 px → 97.6*0.69/762.8 = 8.83 cm against the true 8.56 cm (+3 %).
So depth x px / f is consistent in this clip.

## Measurements (scripts: measure.py, width.py, circfit.py, f36cols.py, f36edges.py)
- Frame 36 (t=1.5 s, near the apex, motion almost horizontal → vertical extent ≈ diameter). The ball's lower edge is
  over the white cup rim, where the edge is ambiguous. Top edge at mid-streak 337.7 px (sub-pixel, vs background frame).
  Centre line from the end chords (against green) is 358.7–359.4 → R ≈ 21–21.7 px → D ≈ 42–43.4 px →
  **3.9–4.0 cm** at 0.7045 m. Raw visible extent down to the rim (~40 px) gives 3.7 cm, but that is a lower bound.
- Frame 48 (t=2.0 s): the perpendicular width of the long diagonal streak (len 113 px) is 55.8 px → 4.59 cm. This is
  inflated: the widths track the streak length (len 76–87 px → width 47–48; len 101–113 → 54–56) and jump by 18 % in
  3 frames (45→48). That would need ~0.8 m/s of motion toward the camera, but the depth anchors only show ~0.16 m/s
  on average. Likely causes are blur and rolling-shutter shear on the fast downward motion. Not used directly.
- Second route, flight 3 at the apex (frames 44–46, motion nearly horizontal, clean green background):
  width 46.9–47.8 px. Depth interpolated between the anchors at the observed ~0.155 m/s approach rate gives
  Z(45) ≈ 0.646 m → 47.5*0.646/762.8 = **4.02 cm** (frames 44 and 46 give 3.9–4.0).

## Answer
D ≈ 4.0 cm. Frame 36 gives 3.9–4.0 and flight-3 frames 44–46 give 4.0. A table-tennis ball is 40 mm, which fits.
Confidence: moderate (±5 %). Using the raw frame-48 value instead would give 4.6 cm.
Scene record: `width_minor` in tracks/ball.csv at frames 47–48 is inflated by blur (see above). At frame 36 it covers only
the part visible above the cup rim (39 px).
