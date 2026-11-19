# Q1178 — height of the moving (blue) bicycle, handlebar to ground

Answer: **0.97 m**

The file and the question both run at 33 fps. t=1 s is frame 33 and t=2 s is frame 66.

## What was measured (scripts in this folder)
- `seg_me.py`, `widths.py`: my own background-subtraction mask of the cyclist. Head-top and wheel-bottom rows agree
  with scene/tracks/cyclist.csv. The apparent height ratio between frames 33 and 66 is 1.455.
- `multicrop.py`, `wheelcrop.py`, `crop.py`: zoomed crops used to read the left grip (centre of the fist), the
  front-wheel ground contact and the rear-wheel ground contact at frames 20, 33, 40, 50, 60, 70, 80 and 90.
  At frame 33: grip ≈ 392, front contact ≈ 535, rear contact ≈ 563.5.
- `vert.py`, `vert2.py`: tilt of clean vertical edges (window frames at x≈70 and x≈1421, phone-booth edges). They
  give a consistent dx/dy = −(x−cx)·5.0e-5, so the camera is pitched down. With f ≈ 1960 the horizon falls at
  y ≈ 191, the same row as the street's vanishing point (curbs meet at ≈(586,194)). So the road is level and the
  apparent "crest" at y≈358 is just where the road model ends.
- `ratio.py`: road-plane ratios. For an object standing on a plane, height / camera height = (v_base − v_top) /
  (v_base − v_horizon).
  - Bike: (front contact − bar top) / (front contact − horizon) = 0.4155 ± 0.004, steady over 8 frames.
  - Pedestrian (white T-shirt) on the raised sidewalk: (feet − head) / (feet − horizon) = 0.814 (median over the gait).
  - Curb: the face measured at x≈925 makes the curb about 0.069 of the camera height.

## Scale and conflicts
- The given distances do not agree with the image:
  - Bike: d2/d1 = 1.394, but the bike's own apparent size shrinks by 1.455 between t=1 and t=2.
  - Pedestrian: the given 17.17 m at t=1 would make a person 1.75 m tall about 2.7 m tall with any focal length that
    fits the bike. So the pedestrian's given distance belongs to an origin away from the body, and I did not use it.
- Because of this, the scale comes from standard sizes, checked against the bike's distance at t=1:
  1. **Pedestrian as a standard adult** (1.75 m walking height): camera height ≈ 2.26 m, which gives a bike height of
     0.96 m to the grip. The value stays within 0.94–0.98 for horizon rows 186–196 and curb fractions 0.055–0.085.
  2. **Bike distance at t=1** (12.12 m, focal length ≈ 1960 from the vertical-edge pitch plus the street's vanishing
     point): camera height 2.19–2.28 m, depending on whether the bike origin is at the bike's centre or its rear
     wheel. This gives 0.91–0.95 m to the grip.
  - Cross-checks with this scale:
    - Rider's head top while seated on the bike: about 1.73 m.
    - Wheelbase: about 1.0 m.
    - Parked cream cruiser bicycle on the left sidewalk: about 1.13 m tall.
    - All of these are plausible real sizes.
  - The speed prior (4.87 m/s) agrees with the change in the given distances (4.78 m in 1 s). It only fixes depth,
    not the focal length, so it cannot fix the scale. The bike's apparent size also shows it speeding up by about
    0.6 m/s² over the clip.
- The grips sit roughly 0.25 m behind the front-wheel contact, so they are slightly closer to the camera. This
  correction adds about +0.025 m.

Final value: 0.955 + 0.025 ≈ 0.98 by the pedestrian route and 0.94–0.975 by the distance route. **Answer 0.97 m.**

Confidence: moderate, about ±5%. The main uncertainties are the true size of the pedestrian, where the bike origin
sits, and how far the bars sit behind the front axle.
