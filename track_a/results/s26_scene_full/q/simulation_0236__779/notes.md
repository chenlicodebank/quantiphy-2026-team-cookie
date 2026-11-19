# q_779 — width of the house (m)

Prior: horse speed = 0.874 m/s. 2D simulation, static camera, 24 fps (fps = question_fps, no retiming).
There is only one horse; "the horse at the back" refers to it. It walks just in front of the house facade.

## Scale (from the prior)
- Horse x track (scene/tracks/horse.csv): the torso template chain moves 154.2 px over 49 frames, and the
  independent buttock-edge track moves 155.2 px. Vertical motion is negligible.
  Mean speed = 3.147 px/frame = 75.5 px/s.
  (Direct frame 0 -> 49 template matching has low correlation (0.47) because the pose changes. It gives about
  158 px, consistent within noise, but the chained track is used.)
- Scale = 0.874 / 75.53 = 0.01157 m/px. Sanity check: horse length 182 px -> 2.1 m, height 162 px -> 1.9 m. Both
  are plausible.

## House width (horizontal extent across the face, the axis-aligned bounding-box extent)
- Row edge profiles on frame 49 (measure.py, eave.py):
  - The widest part is the eave/trim band at y 620–622: x 175–902, **727 px**.
  - Upper storey: x 200–880, 680 px.
  - Brick ground floor: 579 px.
  - Roof: about 648 px.
- The overall bounding-box width is 727 px x 0.01157 = **8.41 m**.
- Other readings: upper-storey wall only, 7.87 m; brick ground floor, 6.70 m.
- Caveat: the horse's hooves (y about 1045) sit slightly in front of the house base (y about 1040), so the horse
  may be up to about 5–10% closer to the camera. In that case the true house width would be a little larger.
  Following the 2D single-scale convention, no correction is applied.

Confidence: moderate. The scale is good to about 2%. The main uncertainty is which extent the reference uses
(the overall bounding box versus the wall).
