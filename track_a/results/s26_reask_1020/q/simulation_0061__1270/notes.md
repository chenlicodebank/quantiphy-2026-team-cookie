# Q1270: width of the lane (road surface, curb to curb). Answer: 12.0 m

The file's fps and question_fps are both 24, so t=0.58 s is frame 14 and t=1.58 s is frame 38.

## Which road
This is a static camera on an intersection. The van (the white car in the prior), the cyclist and, at first, the taxi all drive along the
cross road, which runs left-right across the image. Its curbs are image lines: far curb y = 580.4 + 0.017x and near curb
y = 616.3 + 0.0246x, measured in code on the left arm (x 20-450) and the right arm (x 1660-2160) of frame 0. The two arms are collinear (rms 0.3 px).
The taxi later turns into the main road, which runs toward the camera. That road comes out at about 11.4 m (a rough measure) and is not my answer.

## Calibration (calib.py)
- **Correction to the record:** the scene record puts the horizon at y≈535, which is wrong. The vanishing point of the main road's edges is (1766, 478).
  The cross road's vanishing point is at about (-4800, 498). Lamp posts C and D, if they are the same height, give a horizon at 485.
- Model: a pinhole camera with principal point (1080, 540), zero roll, a pitch θ and a height h over a flat ground. For each f, θ and h are fitted so that four ground contacts
  match their given distances. The contacts are the pedestrian's feet at f14 and f38 (pelvis 0.95 m above the feet) and the cyclist's wheel bottoms at rows 624 and 630, measured from the rim pixels in wheels.py.
  The residuals are under 0.08 m. The fit puts the horizon at about 472-475, which agrees with the vanishing points.
- Focal length, from checks that do not depend on each other:
  - The van's 3D displacement f14→f38, from the depths, is 4.32 m at f=2300. The prior (4 m/s² from rest at frame ~0, which the pixel-track fit supports) gives 4.33 m.
  - The van's motion is perpendicular to the main road at f≈2300.
  - The cross road and the main road are perpendicular at f≈2200-2300.
  - The pedestrian's box height is 1.80 m at f=2300, which is plausible.
  - So f ≈ 2250-2300 px, with θ≈1.7° and h≈2.8 m.

## Width
- I back-projected the curb lines onto the ground plane and took the perpendicular distance between the two parallel lines (their spread is under 0.06 m).
  - Using the visible edges (top of the far curb face, near pavement edge): 12.18 m (f=2300) and 12.3 m (f=2250).
  - Using the road-level edges (base of the far curb face +3.5 px; near curb base +4.5 px for the hidden face): 11.85-11.93 m.
- Sensitivity to f: about 0.2 m per 100 px. **Answer: 12.0 m.**
- Second check: the movers' distances from the near curb are taxi 2.3 m, cyclist 4.8 m and van 7.0 m. The van's distance stays constant (7.00 m at both f14 and f38), so it moves parallel to the curb lines and sits inside the 11.9-12.2 m road.

Confidence: moderate-high, about ±4%. The main uncertainties are where exactly the curb line sits (±1.5 px) and f.
