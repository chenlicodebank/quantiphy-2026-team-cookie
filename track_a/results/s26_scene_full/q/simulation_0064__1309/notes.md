# Q1309: width of the white car (the van), simulation_0064

The white car is the white Chevrolet Express-style van that drives straight at the camera. The file fps and
question_fps are both 24, so frame = round(t*24): t=0.58 s is frame 14 and t=1.58 s is frame 38.

## Focal length (the main scale step)
The van moves almost along the line of sight, so its own depths and the 4 m/s^2 prior constrain f only weakly
(they set the street direction cosine Dz, which is about 0.95–0.98 for any f between 1500 and 3000).
- **Main route:** the vertical vanishing point from near-vertical scene lines, using subpixel edge fits in frame 0
  (`vlines2.py`). The lines are the right signal pole, the left signal pole, the right lamp post and two pillars
  on the right building. The camera roll is about 0, so the VP x = cx. The horizon is y ≈ −121 (street vanishing
  point and the curb-width rule in scene.json). Then f² = (cy − y_h)(y_v − cy).
  Results per line: 2105/2210 (two edges of the right pole), 2167, 2090, 2223, 2239 px. **f ≈ 2180 ± 80 px.**
  A horizon error of ±40 px changes f by about ±3 %.
- **Check 1 (kinematics):** with f = 2180, Dz = 0.957. The depths give Z14 = 37.73 and Z38 = 33.74 (camera-axis
  depth), so ΔZ = 3.987 m. Constant 4 m/s² starting from rest at frame 1 (t0 = 1/24; frames 0 and 1 are
  identical) predicts ΔZ = 3.987 m. This is consistent, but the test is weak.
- **Check 2:** the pedestrian is 103 px tall at a pelvis distance of 38.72 m. With f = 2180 that gives a height of
  1.70 m, which is plausible.
- The image scale from template matching between f14 and f38 is 0.886 ± 0.008. The depth-implied ratio is 0.894.

## Van pixel width
I measured the width against frame 71 as a background, since the van has left rows < 320 by then
(`mirror14.py`, `width_series.py`).
- Mirror to mirror, using half-max edges: f10–18 ≈ 147.5 px; f34–41 ≈ 155–162 px (f38: 159.3 px).
  A simple threshold gives values 2–3 px larger.
- Front body without mirrors: about 138 px at f38 (headlight rows) and 120–129 px at f14.
- Note: the van's image size grows much faster in the last frames (f68–71) than 4 m/s² allows. Only frames
  8–42, which bracket the depth times, were used.

## Width
W = w_px · Z / f. Z is the origin depth from depth_info, interpolated with the 4 m/s² kinematics. I corrected it
by about 1.0 m because the mirrors sit roughly 1 m nearer to the camera than the van's centre origin
(mirrors near the A-pillar, about 1.6 m up).
- Mirror to mirror (axis-aligned bounding box): 2.43–2.50 m. Frames 8–20 average about 2.55 and frames 28–41
  about 2.47 with the threshold edges; the half-max edges are 2 % smaller. **Answer: 2.45 m.**
- Other reading, body width without mirrors ("wheel to wheel"): 138 px × (33.74 − 2.7 m, front face) / 2180
  ≈ 1.96 m (2.14 m with no offset).

I answer with the bounding-box width including the mirrors, because the reference sizes are world-space AABB
extents and the mirrors are part of the mesh.

Confidence: about ±5 % on the mirror-to-mirror value (the focal length dominates). The main risk is which
reading the reference uses: with mirrors 2.45 m, without about 2.0 m.
