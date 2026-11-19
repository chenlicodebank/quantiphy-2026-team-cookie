# Q116: speed of the bike at 1.0 s (m/s)

Prior: the car's acceleration is 4.03 m/s². This is a 2D top-down scene at 24 fps (file and question rates match). Both objects are on the same ground plane, so one metres-per-pixel scale applies to both, and I took it from the car's pixel acceleration.

## Car pixel acceleration
- **track2.py:** For each frame I took the column profile of |frame − empty frame 71| over rows 560–745. I modelled it as the frame-0 profile shifted by s and box-blurred by width w, and fitted s and w by least squares to subpixel precision. The per-frame steps grow very linearly:
  - slope of the steps over frames 2–30: 0.528 px/frame²
  - frames 10–50: 0.531
  - frames 2–55: 0.538
  - Later frames, where blur is heavy or the car is clipped by the frame edge, give about 0.56. I treat those as less reliable.
- **fit.py:** Integer edges from the scene record give 0.546 for the front bumper (biased high because blur widens it) and 0.524 for the rear edge (biased low). Their mean is 0.535.
- **Adopted value:** a = 0.535 ± 0.008 px/frame², which is 308.2 px/s².
- **Scale:** 4.03 / 308.2 = 0.01308 m/px. Sanity check: the car is 438 px, or 5.73 m (a Cybertruck is about 5.7 m), and the bicycle is 129 px, or 1.69 m. Both are plausible.

## Bike pixel speed
- The cyclist moves at constant speed from frame 2 onward.
- A linear fit of the bounding-box centre over frames 2–57 gives 16.040 px/frame. The rear-wheel edge x0 gives 16.045. Profile cross-correlation gives about 16.2, but the pedalling legs bias that method.
- **Adopted value:** 16.04 px/frame, which is 385.0 px/s. Because the speed is constant, frame 24 (t = 1.0 s) has the same value.

## Answer
v = 385.0 × 0.01308 = **5.03 m/s**.

**Range:** with a between 0.528 and 0.546 px/frame², the answer falls between 4.94 and 5.10 m/s.

**Confidence:** good, within about 3 %.
