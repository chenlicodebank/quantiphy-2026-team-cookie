# Q305: length of the helicopter (m)

The scene is a 2D top-down view, 24 fps (the file rate and question_fps agree). The camera is static and looks straight down.

## Scale from the prior
- The "car" in the prior is the airport tug. It tows the airliner straight up the image at constant speed from frame 1 to frame 71.
- I tracked it with my own template match on the tug and nose region (`track.py`): 367.23 px over 70 frames, which is 5.2461 px/frame or 125.91 px/s.
- That agrees with the scene record (5.247 px/frame).
- Scale = 11.155 / 125.91 = **0.08860 m/px**.

## Helicopter extent (frame 71; `heli_prof.py`, `ends.py`, `heli_zoom.py`)
- The helicopter is static, nose up, with its axis at x ≈ 1450–1457.
- A thin nose probe starts at y ≈ 176 (column x = 1457). The fuselage nose is at y ≈ 207.5.
- The tail rotor and fin end at y ≈ 600.5.
- The main-rotor blade tips reach only y ≈ 195.5 and 198.5, so they do not extend the bounding box in y.
- The x extent (rotor tips, about 1285–1620, roughly 335 px) is shorter, so the length is the y extent.
- Length of the bounding box, including the probe: 424.5 px × 0.08860 = **37.6 m**.
- Fuselage only, without the probe: 393 px, which gives 34.8 m. This is an alternative reading. I answered with the full mesh bounding box, which includes the probe.

## Check
- The same scale makes the airliner 423 px × 0.0886 = 37.5 m long (an A320 is 37.57 m), with a wingspan of 34.2 m (A320: 35.8 m).
- It makes the tug body 4.3 m long.
- So the scale is realistic. The helicopter model itself is unusually large for a real helicopter, but the scale is set by the exact prior and confirmed by the airliner.
- Rotor hub sits directly over the fuselage axis, so there is no visible perspective lean.

Confidence: moderate to high. There is about ±1 % from the pixel ends. The main risk is whether the nose probe counts (−7 % if it does not).
