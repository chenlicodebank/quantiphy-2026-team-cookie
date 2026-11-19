# Q306: width of the helicopter (m)

The prior is "speed of the car = 11.155 m/s". There is no depth_info. The video is a top-down 2D render at 24 fps, and question_fps is also 24.

## Scale
- **The "car" is the towing tug.** It moves straight up the image together with the towed airliner. Motion starts after frame 1.
- **My own tracking** (`measure_speed.py`) used sub-pixel template matching:
  - tug: 5.2457 px/frame (total over frames 1→71), or 5.2495 px/frame from a fit;
  - plane nose: 5.2462 px/frame from both the total and the fit.

  Per-frame steps are 5.0–5.5 px with no trend, so the speed is constant at 5.246 px/frame = 125.9 px/s.
- **Scale:** 11.155 / 125.9 = **0.08860 m/px**.
- **Plausibility check:**
  - The airliner's length of 423 px gives 37.5 m, and its wingspan of 386.5 px gives 34.2 m. Both match an A320 (37.6 m long, 34.1 m span).
  - The tug body is 48.5 px, or 4.3 m (6.3 m including the towbar prongs).

  So the scale is a real-world one.

## Helicopter
- **The helicopter is static.** Its rotor is stopped, with blades at fixed angles. Its nose points up the image.
- **Horizontal bbox extents:**
  - x, across the body, set by the rotor-blade tips: left tip x ≈ 1285.5, right tip x ≈ 1619.5. That is **334 px**, read at 8x zoom and from column minima in `tips.py`, ±1.5 px.
  - y, along the body: blade tip and nose at ≈197–205 to tail at ≈600, about 400 px.
- **Width** is the shorter horizontal extent, across the body. That is the x extent of 334 px × 0.08860 = **29.6 m**.

## Alternatives and caveats
- **Rotor-blade tips decide the width.** The answer assumes the world-space bounding box includes the rotor blades.
  - If only the fuselage with its stub wings and pylons counted, the span would be about 195 px (x ≈ 1355–1550), giving about 17.3 m.
- **The helicopter model is oversized.** It looks like a Mi-24-type. At this scale its rotor is about 30 m against a real 17.3 m.
  - The plane and the tug both confirm the scale, so the helicopter model itself was built large. I kept the prior's scale.
- **Confidence:** the scale is high. The width is moderate, mostly because of the bbox-definition question.
