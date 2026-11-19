# q_1598 — diameter of the table-lamp shade (m)

File fps = question fps = 24, so there is no time-base issue. Static camera, 3D Blender render. The "wooden bench" in depth_info is
the reddish side table that the lamp stands on.

## Focal length (focal.py, check.py, fitf.py)
- Cat reference point: torso centroid from scene/tracks/cat.csv (the record was checked; it covers the cat for all 50 frames).
- Two-point solve (frame 0 at 4.199 m, frame 24 at 4.481 m, |P24-P0| = 0.94 m): f = 2099 (torso), 2161 (mask), 2145 (bbox).
- Full-track fit (all 50 frames, straight constant-velocity 3D path, both depths and |V| = 0.94 as constraints):
  f = 2086 / 2097 / 2100 px (+-16), rms 3-4 px. **f = 2095 px** (hfov ~49 deg). The walk direction comes out parallel to the back wall.
- Check: floor plane fitted through the cat's feet (frames 0-48) plus the mirror bottom centre at 6.407 m. Residuals are under 1 cm and the
  camera is 0.60 m above the floor. The closest table leg's foot (1410,840), intersected with this floor, lies 5.745 m away; the given
  value is 5.69 m. So the geometry agrees to about 1 %.

## Lamp depth (feet.py, legs3d.py, lampz2.py, profile2.py)
- Table feet on the floor: front-left (1.19, 0.79, 5.57) m, back-left 0.49 m behind it, front-right 0.76 m along the wall. The legs
  splay sideways, and the bottom of the apron is 0.385 m above the floor (the same from all three legs).
- The lamp base's contact shadow (y ~661) sits about 75 % of the way from the top's back edge (y 656.5) to its front edge (y 662.5). The
  lamp axis ray (u = 1370) passes just inside the left end of the top. Together these put the lamp axis about 0.15-0.25 m behind the
  front edge, which gives Z = 5.75-5.86 m. **Z = 5.81 m** (the distance from the camera is about 5.92 m). This depth hardly changes
  with f.

## Shade width (shade2.py)
- Row-by-row edges of the white shade against the wall. The widest row is the bottom rim (y ~490) at 191 px, or about 193 px with the
  pleated rim. **w = 192 px**, centred at u = 1370.

## Result
- A horizontal circle seen at azimuth theta (tan theta = 410/2095) has an image width of f·D/(Z·cos theta). So
  D = 192 x 5.81 x 0.9815 / 2095 = **0.523 m**.
- If the scale is lowered by about 1 % to match the given leg distance, D is 0.517 m. **Answer: 0.52 m.**
- Uncertainty: f +-1 %, Z +-1.5 % (where the lamp sits front to back), w +-1 %. Overall about +-3 %.
- Second check: the shade is 0.52 m against a table whose leg spacing is 0.76 m, which matches their image ratio of 192 px to
  ~300 px at about the same depth.
