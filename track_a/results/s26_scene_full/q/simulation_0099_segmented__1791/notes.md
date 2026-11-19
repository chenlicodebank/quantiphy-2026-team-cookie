# q_1791 — shark height (prior: boat length = 10 m)

2D video, 24 fps (file fps = question_fps; no re-timing). Static camera, white background.

Method (measure.py): segmented the non-white pixels in every frame (min RGB < 238 or saturation > 25, 3x3 opening).
The boat is the part above y = 740 and the shark the part below it.
- Boat bbox length (stern rail/rudder to bow), frames 2–47 while the whole boat is in frame: median **857 px** (range 855–860). This matches scene/.
- Shark bbox height (dorsal-fin tip to pectoral-fin bottom), frames 2–60: median **103 px** (range 103–105), y 853–955.
  Frames 71–72 are clipped at the left edge and were not used.
- Overlays in frames/full_30.png and frames/shark_30.png confirm both boxes cover the full objects.

Scale: 10 m / 857 px = 0.011669 m/px. Shark height = 103 × 0.011669 = **1.20 m**.

Check: the shark's length is 278 px, which is 3.24 m. A height/length ratio of 0.37 (with fins) is plausible for a shark.
The height is stable within ±1 px over 60 frames. Scale uncertainty is about 0.3%.
Confidence: high (about ±2%).
