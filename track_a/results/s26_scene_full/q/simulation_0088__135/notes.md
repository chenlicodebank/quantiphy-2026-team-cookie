# Q135 — wingspan (width) of the small bird (crow)

2D simulation, 24 fps (file fps = question_fps, no re-timing). Two birds seen from below fly right-to-left
along the same horizontal line, so one depth plane: one metres-per-pixel scale for both.

## Scale from prior (big bird / eagle speed = 17.98 m/s)
measure.py: masks |RGB - sky| > 25/40/60, connected components, all three thresholds agree within 1-2 px.
Eagle moves rigidly and only horizontally: tail end x 1643 (f2) -> 206 (f14), head x 1504 -> 69, so 119.67 px/frame
= 2872 px/s, giving a scale of 17.98 / 2872 = 0.006260 m/px. The per-frame steps are constant at 119-120 px.

## Crow wingspan
The wings lie along the image vertical, so the wingspan is the vertical extent of the mask. It changes with the flap cycle:
the maximum is 164 px (f3; 162 px at f12 and f21) and the minimum is 106 px (f24). Frames 0-1 are excluded
because the eagle overlaps the crow there.
- Max (wings fully spread): 164 px x 0.00626 = **1.027 m**, which is the answer.
- Mean over the flap is about 140 px (0.88 m). The minimum is 0.66 m.

## Check
With the same scale, the eagle's maximum span is 324 px = 2.03 m, which is realistic for a bald eagle. The crow at 1.03 m
is plausible for a large corvid or raven. The scene record (scene/tracks) matches my own re-segmentation.
Confidence: moderate. The scale is solid (within about 1%). The main uncertainty is whether the reference uses the maximum spread
or a different flap phase.
