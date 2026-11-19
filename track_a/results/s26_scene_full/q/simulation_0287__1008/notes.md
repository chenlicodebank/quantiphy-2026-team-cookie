# q_1008 – displacement of the plane from 0.5 s to 1.0 s

Prior: plane speed = 22.16 m/s. 2D simulation, static camera, jet flies straight right-to-left at constant height.

## Measurements
- scene/tracks/jet.csv: from frame 2 on, the jet moves 41.6-42.4 px/frame (mean 42.08), vertical drift < 1 px
  over the whole clip, so speed is constant (only frame 0->1 is a duplicate, outside this interval).
- Frames 12 -> 24 (t = 0.5 -> 1.0 s at 24 fps): ref_x 2213.47 -> 1708.07 = 505.4 px.
- Independent check (check_disp.py): template of the jet in frame 12 matched in frame 24: dx = -504.6 px, dy = 1 px.
  Frame 25: -546.8 px (matches the record's 547.7).

## Scale and answer
- Route 1 (constant velocity): displacement = 22.16 m/s x 0.5 s = 11.08 m.
- Route 2 (pixels): scale = 22.16 / (42.08 px/frame x 24) = 0.02194 m/px; 505.4 px x 0.02194 = 11.09 m.

## Time base
File 24 fps (72 frames, 3.0 s), question_fps 25. The motion is uniform, so the displacement is the speed times 0.5 s
in either time base. Using the file's 24 fps gives frames 12 -> 24 (12 steps) and 11.08 m. With 25 fps the frame
indices become 12 or 13 -> 25: 10.64 m for 12 steps, 11.52 m for 13. Both are within about 4 % of 11.08, which is
also the true constant-velocity value. Jet length at the 24 fps scale is about 680 px x 0.0219 = 14.9 m, plausible
for a Harrier-type jet (the 25 fps scale gives 14.3 m, also plausible, so this check cannot tell the two rates apart).

Answer: 11.08 m. Confidence: high (the motion is uniform; the only uncertainty is the frame-rate convention, about 4 %).
