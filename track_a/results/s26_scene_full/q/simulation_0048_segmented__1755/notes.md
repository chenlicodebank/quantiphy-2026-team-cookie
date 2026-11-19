# q1755 – distance between left pillar of near door and right pillar of far door

## Finding
- The asked objects (two doors with pillars) are NOT visible in this segmentation clip. The background has been
  replaced by white. `residue.py` averages all 99 frames and contrast-stretches the 240-255 range (`frames/residue.png`).
  Only the kiosk/bin, the pedestrian and the cyclist are non-white. No faint trace of any door or pillar survives.
- The only object with pillar-like posts is the kiosk/bin (front face posts at x~1110-1135 and ~1380-1405 px). It is a
  single box, not two doors, so it can't provide a "near" and a "far" door.

## Scale (for context only)
- Pedestrian (1.8 m): bbox height 200 px at frame 33 with depth 11.926 m gives f ~ 1325 px. At frame 66, 212 px with
  depth 10.817 m gives f ~ 1275 px. So f ~ 1300 px and hfov ~ 72 deg.
- The cyclist's given depths (16.49 m at t=1 vs 11.93 m at t=2) don't fit their pixel size against the pedestrian (the
  cyclist looks larger and sits lower in the image). The cyclist's depth labels may be swapped or scaled differently.
- At the pedestrian's depth the frame spans about 17.6 m horizontally.

## Answer
The doors can't be measured from this footage, so there's no second-route check. The answer is a prior-based guess:
two doors along a building facade or street, at different depths, with the far-right pillar to near-left pillar
span (door widths plus spacing) of roughly 4-15 m. Answer: 8 m (geometric middle).
Confidence: very low.
