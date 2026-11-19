# Q1179: length of the moving bicycle (m). Answer: 1.75 m

Question fps = file fps = 33. Prior: the bike's speed is 4.87 m/s. Depth_info: bike 12.12 m at t=1 s and 16.90 m at t=2 s; pedestrian 17.17 / 18.38 m.

## Geometry
- The blue bike rides straight away from the camera and is seen from behind, so its length runs along the depth direction.
  Length (bounding box) = wheelbase W (rear contact to front contact on the ground) + tire diameter D.
- Camera: static. Its pitch was measured from the convergence of more than 60 vertical building edges (`vert2.py`). They converge
  downward to a nadir at y_n ≈ 19 800 px, so the camera is pitched down. The bike's motion vanishing point is at (584, 209)
  (`vp.py`: head and ground tracks intersect there; the curbs meet at about (586, 194)). It is the horizon of a flat road.
  Principal point is taken as the image centre. This gives f² = (y_n − 383)(383 − 209), so **f ≈ 1840 px**
  (range 1806–1915 for a vanishing-point y of 194–215), with pitch ≈ 5.4°.
- Ground-plane model (`wheel.py`, `final.py`): back-project pixels onto a flat road with camera height H.
  - My own rear-tire contact track (`reartrack.py`, frames 6–98) fits a constant speed well in this model.
  - The scale H comes from the prior: mean speed = 4.87 m/s gives H = 2.24 m.
- Check against depth_info: the model gives a bike origin (0.5 m up, near the bike's centre) at 11.99 m (t=1) and
  16.79 m (t=2). The given values are 12.12 and 16.90, so they agree within about 1%, and the depth change matches
  (4.80 vs 4.78 m).
  - The pedestrian's depth_info (17.2 m) does not fit the image: their feet are at the same image rows as the bike,
    which puts them about 11 m away. So I did not use the pedestrian.
  - The record's height-based depth ratio (1.456) is skewed by the camera pitch. I did not use it either.
- The record's `ground_x/ground_y` for the cyclist is biased (it picks up shadow and the front wheel, by up to 9 px and
  40 px). I re-measured the contacts myself.

## Measurements
- Tire bottoms (front, rear) read on 4–7× zoomed crops (`crop.py`) at frames 6, 8, 10, 12, 18, 22, 26, 30 and 36.
  - Wheelbase per frame: 1.05, 1.11, 1.09, 1.05, 1.07, 0.96, 1.07, 1.09, 1.09 m. **Median W = 1.07 m** (sd 0.04).
  - The bike's axis is within 3° of its direction of motion.
  - W hardly depends on f, because the scale comes from the speed.
- Tire diameter: rear tire height from contact to the top just under the rack at frames 8, 18 and 30 gives
  **D = 0.66–0.675 m** (f = 1840). This is slightly a lower bound, since the rack can hide the top of the tire.
  The front-wheel arcs give ≥ 0.64 m (the top is hidden by the leg).
- L = 1.07 + 0.67 = 1.74 m at f = 1840. The variants are 1.72 m (f = 1806) and 1.79 m (f = 1915).
  The f that best reproduces the given depths lies between 1840 and 1915, which gives about 1.75 m.

## Second route
- Time shift: the rear contact reaches the front contact's earlier image position after 6–8 frames (mean ≈ 7.1–7.5).
  At 4.87 m/s that is W ≈ 1.05–1.11 m.
- Measuring W against the fitted rear track instead of the manual rear reads gives 1.11 m.
- Both agree with 1.07 within the noise.

## Confidence
Moderate to good, about ±5%. The main uncertainties are the tire-top location (rack occlusion), f (±4%, which affects only
D) and the manual contact reads.
