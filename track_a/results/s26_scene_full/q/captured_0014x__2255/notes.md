# q_2255 – cookie diameter (captured_0014x, lab, 24 fps = question_fps)

Method (lab method card): D = depth_info distance x pixel diameter / f, f = 0.5959 x 1280 = 762.75 px.
- Cookie: round chocolate-chip cookie standing upright, leaning against the cup (static all clip), centre ~(486, 391).
- Median of frames 0, 10, 40 (static object), crop 440-530 x 340-430 (crop.py). Saturation mask (S >= 100) with
  sub-pixel edge crossing per row/column (measure2.py); overlay in frames/mask.png.
- Horizontal extent at the widest rows (y 388-398): L ~469.4, R ~503.7 -> 33.5-34.6 px (mean ~34.2).
- Vertical extent: top ~375.5 at centre columns, bottom rim ~408.5 (read on 6x crop) -> ~33-34 px. The face is close to
  perpendicular to the view ray, so the disc looks almost circular; diameter taken as ~34.2 px.
- D = 1.7355 m x 34.2 / 762.75 = 0.0778 m = 7.8 cm.

Checks: the scene record's bbox (470-502 x 373-408, 32 x 35 px) agrees within ~1-2 px (7.3-8.0 cm range).
Sanity: ball 30 px at 1.818 m -> 7.2 cm, cup 38 px at 1.727 m -> 8.6 cm; a 7.8 cm cookie is consistent with these.
The prior (ball acceleration) does not bear on the size; the scale comes from depth_info.
Confidence: about ±5 % (edge blur ±1 px).
