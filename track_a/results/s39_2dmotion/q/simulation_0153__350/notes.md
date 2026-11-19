# Q350 — acceleration of the blue car at t = 1 s (m/s^2)

Prior: tire diameter of the blue car = 0.369 m. 2D video, file fps = question_fps = 24, so t = 1 s → frame 24.
The "blue car" is the light-blue utility cart driving left→right side-on at constant depth.

## Scale (tire diameter in px)
- tire.py: vertical luminance profile through the front-wheel centre, frames 31–41: tire top 836.5–837.5, bottom 948.5
  → 111–112 px (frames where the profile hits a glare/hub artefact give outliers, ignored).
  The rear tire's top is hidden in the dark wheel arch, so it was not used for the vertical profile.
- tire2.py: horizontal profile on row 893 of frame 41 (front tire): half-level edges at x ≈ 1377.1 and 1488.6 → 111.5 px.
  The edges are sharp (2–3 px ramps), so there is no motion blur widening.
- SAM 3 "tire": frame 41 boxes 111.7 × 110.3 (rear) and 112.3 × 108.6 (front); frame 24 boxes 112.9 × 108.6 and
  113.2 × 108.7. SAM mean ≈ 111 px, so it matches mine within 1–2 % (< 3 %). The overlay shows clean tire outlines.
- D = 111 px → scale = 0.369 / 111 = 0.003324 m/px.

## Motion
- track.py: my own NCC template tracks (template from frame 24, sub-pixel parabola) of the lower body panel with the
  3 orange lights and the front-wheel hub, frames 14–34. Increments around frame 24 (panel): 45.46, 46.45, 47.25, 47.99,
  48.68, 49.18 px/frame. They are smooth.
- The motion is a smoothstep (Blender Bezier ease) profile. fit.py fits x = x0 + A(3s²−2s³), s = (i−i0)/T, to the
  record's panel track frames 18–41: i0 ≈ −0.14, T ≈ 59.3, A ≈ 1979 px, rms 0.05 px.
- a(24) = (v24 − v23)·fps = second difference x24 − 2x23 + x22 (px/frame²) × fps²:
  - raw panel 0.71; cubic fit 18–41: 0.740; cubic 18–30: 0.745; smoothstep: 0.740; my panel track: 0.744; my hub track: 0.746.
  - Adopted: 0.743 px/frame² = 428 px/s² → 428 × 0.003324 = **1.42 m/s²**.
- Patches higher up on the cart that include background (front body, canopy) gave biased, noisier increments (~45),
  so I did not use them. Silhouette edges (record bbox, SAM "blue cart" box) change in length with perspective and glare.
  For example, the SAM box over frames 22–29 gives x1 increments of 44–47 and x0 increments of 45–49. So I used points on
  the side face, which sits at the same depth as the tire's outer face where the scale was measured.

## Second route
- My own hub-template track (an independent point and template from the panel) gives 0.746 px/fr² → 1.429 m/s².
- The global smoothstep model (whole 18–41 window) gives 1.418 m/s².
- Routes agree within 1 %.

## Confidence
The main uncertainty is the tire pixel diameter (109–113 px, ±2 %). The acceleration in px is within ±1 %.
Expected error is about 3 %.
