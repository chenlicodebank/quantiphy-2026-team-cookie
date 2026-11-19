# Q2357 – displacement of the white jar, 0.60 s → 0.80 s (cm)

- The white jar is `white_ball` in scene/ (the small white object the near person throws to the far person). File fps = question fps = 24.
  t=0.60 → frame 14, t=0.80 → frame 19 (both in free flight).
- Camera: f = 0.5959·1280 = 762.8 px, principal point (640,360). depth_info is a Euclidean distance, so D14 = 1.9735 m along the ray.
- Pixel centres (checked on overlays, `size.py` → frames/sizes.png): f14 ≈ (405–408, 235–238), f19 ≈ (481–482, 63–65).
  The scene track, my own half-contrast mask and a polynomial-smoothed track all agree to within about 3 px.
- **The unknown is the depth at frame 19** (depth_info only gives it at 0.60 s). Ways I estimated it:
  1. Apparent size (`size.py`): minor axis ≈ 31 px just after release (f12–13), ≈ 25 px at f20–25 (sharp). With D linear in time,
     ratio 1.15–1.30 gives D19 = 2.11–2.26 m (central value 2.19), and D at the catch (f27) ≈ 2.5–2.7 m. That fits the far person
     (torso 3.24 m) reaching forward and bending to catch.
  2. Ballistic fit with g = 9.8 (`fit2.py`; pitch and roll unknown, roll 5–8° as the verticals near the image centre lean): the free fits give D19 = 2.07–2.16
     (rms 5–7 px, so the fit is poor because the blurred centroids are noisy). If I force the catch distance to 2.9–3.1 m, D19 = 2.22–2.47, but those fits are
     worse.
  3. Camera orientation from the baseboards (`vp*.py`) was inconclusive (blurred background, lens distortion), so I did not use it.
- Displacement (`final.py`) = |P19 − P14| with the back-projected points:
  D19 = 2.11 → 48 cm; 2.19 → 52 cm; 2.25 → 55 cm; 2.30 → 58 cm.
- Answer: **52 cm** (D19 ≈ 2.19 m). Confidence: moderate. The ±0.08 m uncertainty in the frame-19 depth gives about ±10 % on the answer.
