# q_2322 – soccer ball velocity at 3.4 s (cm/s)

## Problem: 3.4 s is outside this clip
The clip is 49 frames at 24 fps (0–2.04 s); frame round(3.4×24)=82 does not exist. The file is the
background-replaced (segmentation, "…s") version of a longer lab recording. Its answers come from the original
footage, so the original timeline is offset from this clip by an unknown amount.

The playback is real-time. The fall gives a = 8.95 m/s² at 2.8 m (with the dropped frame between f35 and f36), which
is close to the 9.8 prior. So the clip is not time-scaled, and only the offset is unknown.

## Measurements (scene/tracks/soccer_ball.csv, checked; fit.py)
- Scale at the ball: 2.8 m / 763 px = 3.67 mm/px.
- Release happens at effective frame ≈28.6. Impact is at f39, where the bottom of the ball is at y≈577. The fall is ≈277 px ≈ 1.02 m, so v_impact ≈ 4.3 m/s.
- Quadratic fit f30–39, adding one frame after f35 for the dropped frame: a = 2440 px/s² = 8.95 m/s², rms 1.2 px.
- Per-frame speeds: f33→34 21 px (185 cm/s), f34→35 26 px (229 cm/s). After the bounce the speed drops from about 2.6 m/s to about 0.2 m/s by f48.

## Assumption used
The question uses the gravity prior, so it most likely asks about a moment during the free fall. I assumed the clip
starts 2.0 s into the original. Then 3.4 s maps to clip t = 1.4 s, which is f34 (mid-fall).
- Fit route: v(f34) = 8.95 × 5.43/24 = 2.03 m/s. With g = 9.8 it is 2.22 m/s.
- Pixel-difference route: the mean of the 33→34 and 34→35 steps is 207 cm/s. A forward difference smoothed over 5 frames gives about 220 cm/s.
- Answer: about 215 cm/s.

Alternative reading: if the clip were the start of the original, then at 3.4 s the ball would be making small late
bounces or rolling at well under 1 m/s.

Confidence: low. The time mapping cannot be determined from the clip.
