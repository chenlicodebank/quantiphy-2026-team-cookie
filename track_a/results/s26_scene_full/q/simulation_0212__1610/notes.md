# Q1610 — diameter of the table-lamp shade (m)

File fps = question_fps = 24, so the frame numbers and times agree. The camera is static.

## Focal length (two routes)
- **Cat route** (`focal.py`, `final.py`): I used the cat core centroid at f0 (408.5, 842.7) with d = 4.199 m and at
  f24 (869.4, 805.3) with d = 4.481 m. Back-projecting these and requiring a 0.94 m displacement in 1 s gives
  **f = 2156 px** (HFOV 48°). Using the f24 bbox centre instead gives 2060.
- **Room route** (`lines.py`, `pitch.py`): I measured the back-wall/floor line (y = 908.8 − 0.0749x) and the
  right-wall/floor line (slope +0.13) in code. Making the two walls perpendicular with a level camera gives
  **f = 2112 px**. Solving at f = 2150 gives pitch −0.09°, so the camera is level.
- The floor height from these numbers is consistent. The mirror bottom centre (1520, 815) at 6.407 m gives a camera
  height of 0.797 m. The front-left table leg bottom (1410, 840) at 5.69 m gives 0.779 m. The cat origin comes out
  ~0.22 m above the floor and the dog origin ~0.35 m above it, which is plausible.
- I used the mean, f ≈ 2134 px.

## Lamp depth
- The "closest wooden bench leg" is the side table's front-left leg: bottom at (1410, 840), centre at about (1417, 765).
  From 5.69 m this gives Z_front = 5.52 m (5.54 m if the leg's origin is its centre).
- The back-left leg bottom is at (1330, 825). On the level floor, Z_back = Z_front·300/285 = 5.81 m.
- The lamp axis (x ≈ 1370) sits between the two left legs. Taking it as centred front-to-back on the table gives
  **Z_lamp ≈ 5.67 m**.

## Shade width
- `shade2.py` plus row profiles on frames 0, 20 and 48 give the widest silhouette at the bottom rim, y ≈ 491: from
  x = 1273.3 to 1466.0, so **192.7 px**. This matches the 193 px in scene.json.
- I modelled the rim as a horizontal circle at (X, Y, Z_lamp) and solved for the radius that reproduces 192.7 px.
  This includes the off-axis correction of cos 11° ≈ 0.98.
- Result: **D = 0.502 m** (f = 2134, lamp centred). The naive w·Z/f gives 0.511.

## Sensitivity and confidence
- Using f = 2156 or f = 2112 gives 0.497 or 0.506.
- If the lamp stood at the front-leg depth or the back-leg depth, D would be 0.489 or 0.515 (about ±2.5 %).
- Leg origin at the bottom or at the centre changes D by 0.3 %.
- Answer: **0.50 m**. Expected error is about 3–4 %; the main uncertainties are where the lamp sits front-to-back and f.
