# q_2367: height of the white jar (cm)

Answer: **6.7 cm** (likely range about 6.1-7.2 cm).

## Setup
- Lab clip, 1280x720, 24 fps (the file fps and question_fps are both 24). f = 0.5959 x 1280 = 762.75 px, principal point (640, 360).
- The scene record's "white_ball" is the white jar, a squat plastic tub with a lid. The near person throws it underarm.
  t = 0.60 s is frame 14 (round(14.4)). The given depth there is 1.9735 m.
- The gravity prior (9.8 m/s^2) was used only in the trajectory fits (joint_fit.py, pitch_scan.py) that give per-frame
  depths for the flight frames.

## Key findings
1. **Motion blur is large: about 0.47 of the frame interval.** In flight, the mask's long axis follows the image
   velocity direction in every frame (110 -> 198 deg over f15-24). (Length along motion - width across) / speed is
   about 0.47 at every speed from 18 to 52 px/frame. So the in-flight elongation (about 60 x 31 px at f15) is smear,
   not the jar's real shape. Only widths across the motion are clean.
2. **Shape from the frames where it is held still (f3-f5, speed 3 px/frame, sharp).** The lid is a clean ellipse
   (lidfit.py): long axis 2a = 35.8 / 37.1 px, b/a = 0.77 / 0.73. The side wall hangs below it. Its lower edge is
   real: background shows between the jar and the trousers. A tapered-tub fit (taperfit.py; bottom ellipse scaled by
   k, centre shifted by s) gives H/D = 0.83 (f4) and 0.73-0.78 (f5) for any k in 0.7-1.0. I use H/D ≈ 0.79 ± 0.05.
3. **Diameter at the depth-given frame (f14, d = 1.9735 m).** The jar is still upright, with its axis tilted about 15°
   (bottom to the left, nearly along the motion). Its rows clear of the hand (y 225-241) are 35-36 px wide
   horizontally (rowwidth.py). Converting to the width perpendicular to the axis and removing about 2 px of smear
   gives D ≈ 33 ± 1.5 px. That makes D = 33 x 1.9735 / 762.75 = **8.5 cm**.
   - Check at f15 (free flight, depth about 2.03-2.05 m from the joint ballistic fit): the width across the motion is
     31-32 px, so D ≈ 8.4 cm.
4. H = 0.79 x 8.5 ≈ **6.7 cm**.
   - Equivalently, H is about 28.5 px at f4 against D ≈ 36 px there. This implies the jar is about 1.8 m from the
     camera at f4, which is plausible for hip height below a high camera.

## Second route / cross-checks
- f23 (near the apex, slow, side view with the lid seam): after removing the smear, D ≈ 25-27 px, the top ellipse
  minor is about 19 px and the side about 14 px. That gives H/D ≈ 0.8-0.85, which matches the ratio from the resting
  frames.
- f47 (held by the far person, depth about 3 m): width about 22.5 px, so D ≈ 8.7-9 cm. This is consistent with
  D ≈ 8.5 cm. The height there is partly hidden by fingers and was not used.
- The scene record's extents for this object in flight include the motion smear, so they should not be used as sizes.

## Confidence
Moderate. The diameter is solid to about ±5%. The height/diameter ratio comes from one resting view, with a
foreshortening/taper model, and is uncertain by about ±7%. Overall about ±10%.

Scripts: masks.py, profiles.py, ballistic.py, joint_fit.py, pitch_scan.py, caliper.py, handphase.py, lidfit.py,
taperfit.py, rowwidth.py, colprof.py, f14width.py, zoom.py, crops.py.
