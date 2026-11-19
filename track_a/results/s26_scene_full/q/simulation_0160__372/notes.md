# Q372: length of the billiard table (m)

- 2D top-down view with a static camera, so one metres-per-pixel scale comes from the prior: ball diameter = 0.0757 m.
- Ball diameter in pixels: the moving ball 13 measures 48.4 px (median ellipse axis in the scene record), and the
  static balls have 47–49 px bounding boxes (scene record; ball 1 was checked on a 6x zoom crop at about 918–965 px).
  I used 48.2 px, so the scale is 0.0757 / 48.2 = 1.571e-3 m/px.
- Table length: the outer extent of the wooden rail along x, 110 to 1781 px = 1672 px at frame 39. I re-measured this in
  measure2.py with a brown-colour mask (rows 500–700 give 110–1781; in the upper rows the right rail is shaded and the
  mask misses part of it). I also checked it on zoomed crops of both edges.
  The question asks about the table object, so I used the whole table (its bounding box, rails included).
- Answer: 1672 × 1.571e-3 = **2.63 m**.
- Second route and alternative: the felt playing surface measures 1524 px (green mask, every row), which gives 2.39 m.
  The 1672/1524 ratio matches the rail thickness (74 px per side). If the reference meant the playing surface, the
  answer would be about 2.39 m.
- Confidence: the scale is good to about ±2%. The main uncertainty is whether the reference counts the rails (2.63 m) or only the felt (2.39 m).
