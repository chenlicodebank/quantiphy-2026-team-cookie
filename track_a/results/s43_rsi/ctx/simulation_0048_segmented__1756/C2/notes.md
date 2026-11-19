# q1756 – height of the moving bicycle (handlebar to ground)

Answer: **1.49 m**. The file and the question both run at 33 fps, so t=1 s is frame 33 and t=2 s is frame 66.

## Where the earlier answers part ways
- **C1 (1.41):** uses the given bike depth (16.49 m at t=1) with a pinhole camera fitted to the walker.
- **C2 (1.00):** rejects the given bike depth. It puts the bike on the walker's ground plane at about 8–10 m.

So the deciding step is whether depth_info for the bike is the bike's real camera distance.

## My test of that step (`ground.py`, `sizetest.py`)
- **Ground-plane reading (C2):** the bike's distance comes from its wheel-contact pixel, using the camera fitted to the walker (pitch about 13°, f about 1210, camera about 3.2 m up).
  Against that, the given depth is a constant ~6.5 m more, not a constant multiple.
- **Apparent sizes, frames 0–57:** rider shoulder width, head width and bbox height, each multiplied by the camera-axis depth Z, should stay constant.
  - Given depths (constant speed 4.56 m/s): relative scatter 1.1% (shoulders), 2.7% (head), 1.4% (height), with no trend.
  - Ground-plane depths: 7–8% scatter and a 20–27% drift.

The apparent size follows the given depths, so the given depth really is the visible bike's distance. The cyclist and bike are therefore a scaled-up asset (rider + bike about 2.5 m), riding below the walker's ground plane. C2's rejection is wrong.

The prior (1.8 m walker) and its depths fix the camera, and the bike's own depth fixes the bike's size. The bike comes out about 40% larger than a normal bike. That is right at the plausibility limit, but two direct image tests support it, and the given depths are exact. I keep the depth-based value: falling back to a standard bike size would mean throwing away a given depth that the image confirms.

## Measurement (`solve.py`, `bar.py`, `final.py`)
- **Camera:** the pitch from the kiosk's vertical vanishing point (1031, 6509) is about 11–12°.
  - The walker's head and foot pixels at t=1 and t=2 (H = 1.8 m, pelvis at 0.95 m, given depths) give f = 1222 / 1180 at a 12° pitch; I use the mean, about 1200–1210.
  - The walker's back-projected pelvis motion is level at a pitch of 12–14° and moves about 1.14 m/s, which is plausible.
- **Bike at t=1 (frame 33):**
  - Front-wheel bottom v = 559.5.
  - Handlebar: centre/stem v ≈ 433, grips v ≈ 425 (found from the light-grey bar pixels, and checked on zoomed crops).
- **Model:** the wheel contact lies on its pixel ray. The handlebar sits at H·up from the contact, minus a setback k·H toward the rear. The origin is 0.4·H above the contact, at the given distance of 16.4919 m.
- **Results across pitch 12–13.5° and f 1190–1230:**
  - Stem, k = 0.08–0.18: 1.45–1.51 m.
  - Grips, k = 0.22–0.38: 1.46–1.55 m.
  - Central value: 1.49.

## Second route
I scaled from the walker by ratio: 1.8 m × (133/200 px) × (Z ratio 13.91/10.78) × (vertical foreshortening 0.987/0.964). That gives about 1.58 m before removing the setback, and about 1.51 m after it (k ≈ 0.15). This agrees.

## Caveats
- Repeating the model at frame 50, with the depth interpolated at constant speed, gives 1.53–1.60 m. The bike's vertical pixel span grows about 3% faster than 1/Z, which this model cannot explain. I used t=1, where the depth is given exactly.
- Confidence: about ±5%. I agree with C1's reading; my value is 5% higher because I use the bar top (grips) or the stem with a smaller, realistic setback.
