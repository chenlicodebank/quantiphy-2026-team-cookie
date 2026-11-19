# q_1194: height of the moving bicycle (handlebar top to ground), in metres

**Answer: 1.49 m.** Plausible range 1.45–1.55 m. The naive ratio gives 1.71 m; it is rejected below.

The file and the question both use 33 fps, so t = 1 s is frame 33 and t = 2 s is frame 66.

## Inputs
- Prior: the walker's height is 1.8 m.
- Depths, bike: 16.4919 m at t = 1 s and 11.9277 m at t = 2 s.
- Depths, walker: 11.9259 m at t = 1 s and 10.8165 m at t = 2 s.
- At t = 2 s the bike's wheel is below the image edge, so the bike can only be measured at t = 1 s (frames 0–60 for the checks).

## Pixel measurements (my own, checked against scene/tracks)
**Bike at frame 33 (`c33.png`, `bar_f33.png`, `tire.py`):**
- top of the handlebar/grip: y ≈ 422
- bottom of the front tyre: y ≈ 560
- bike height: 138 px

**Bike at other frames:**
- frame 0: top 312, contact 416.5, so 104.5 px
- frame 60: top 579, contact 761, so 182 px

**Walker (`w33.png`, `w66.png`):**
- frame 33: head top 252 to lowest foot 451, so 199 px
- frame 66: head top 275 to lowest foot 488, so 212.5 px

**Horizontal image scale of the rider's head and shoulders, relative to frame 33** (template matching, `scalematch*.py`):
- frame 0: 1/1.30
- frame 60: 1.315
- frame 66: 1.40–1.41

## Camera
- **Pitch.** Vertical edges in the background meet at a vanishing point at about (958, 8620): a building column, a door frame and two kiosk edges, with line fit rms 0.1–0.9 px (`verticals.py`). The roll is about 0, and tan(pitch) = f/8237, which gives about 8°.
  - The people's paths converge at (1771, −177). So in this camera they come down a street that rises away from the camera.
- **Focal length.** It comes from the walker's 1.8 m in a full pinhole model with the pelvis at the given depth (`model.py`): f = 1196 from t = 1 s and 1163 from t = 2 s. I used about 1185.

## Bike height (`fit_rH.py`)
**Model:**
- The front-wheel contact sits on its pixel ray.
- The bike origin is taken at ground level in the middle of the wheelbase, at the given distance of 16.49 m. The front contact is therefore about 0.5·H nearer the camera.
- The grip top is at height H and lies r·H behind the front contact.

**Fit:** I fitted H and r to the handlebar-top rows at frames 0, 33 and 60, with depths scaled by the template scale. The residuals are under 0.7 px.
- The fit gives r ≈ 0.25, which is normal bike geometry.
- H = 1.484 / 1.496 / 1.509 m for f = 1198 / 1185 / 1170.
- With r fixed anywhere from 0 to 0.4, H stays between 1.46 and 1.55 m.

## Checks and why the naive answer is rejected
- **Do the bike depths match the bike itself?** The rider's horizontal scale from t = 1 to t = 2 is 1.40–1.41. The given depths, with the off-axis cosine, predict 1.39. So the depth is to the bike, not to a far-off origin.
- **The scene is not physically consistent.** At the given depths the cyclist's ground lies about 2.6–2.9 m below the walker's ground, and the cyclist is about 1.6× the walker's size. I followed the given depths, because the prior and depth_info are exact.
- **Naive ratio, 1.71 m.** This is 1.8 × (138/199) × (16.49/11.93). It ignores two things:
  - the larger off-axis angle of the bike: its axial depth is about 0.86·D, against about 0.92·D for the walker;
  - the handlebar standing behind the contact point, seen from a camera looking down.
- **Alternative pitch.** If the people's path vanishing point were on the horizon, the pitch would be 23° and f = 1287.
  - Then the fit needs r = 0.61, which is implausible, and gives H = 1.29.
  - With a normal r of 0.2–0.3 it gives H = 1.43–1.49, so this route also supports about 1.45–1.5.

**Confidence: moderate.** The main uncertainties are the camera pitch, the position of the bike origin (±4 %) and the walker's walking height against its rest height (±2 %).
