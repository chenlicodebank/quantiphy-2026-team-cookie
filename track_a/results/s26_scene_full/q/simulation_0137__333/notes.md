# q_333 – height of the house (m); prior: bird speed = 9.146 m/s

2D simulation, 60 fps (file fps = question_fps, no re-timing). One metres-per-pixel scale from the bird's speed.

## Scale (speed.py)
- I used the bird track in scene/tracks/bird.csv, fully visible frames 4–99. The mean per-frame step is 19.84 px
  (median 19.77). Three reference points (eroded centroid, plain centroid, bbox centre) agree within 0.2%.
- A cubic fit to x(t), y(t) gives a speed of 1165–1239 px/s, mean 1191 px/s, so the speed is nearly constant
  (±3%) and the prior is taken as the bird's mean speed.
- Scale = 9.146 / 1190.3 = 0.007684 m/px.

## House pixel height (house.py, base.py, frame 60)
- Top of the roof ridge: y = 520–525 across the width (≈521).
- Bottom: the siding ends at about y 946. Below it a dark grey block (not grass-coloured, so it belongs to the
  house: foundation) runs down to y ≈ 984 at x 610–680, where the grass in front is low. Elsewhere grass
  covers it from about y 955. The scene record's 438 px (520–958) stops at the grass line.
- Height including the foundation ≈ 984 − 521 = 463 px → 3.56 m.
  Without the foundation (record's 438 px): 3.37 m.

## Check / confidence
- Cross-check of the speed scale: the windowed mean step stays between 19.5 and 20.3 px/frame in every 16-frame
  window. Other scale choices (min/max fitted speed) change the answer by ±3%.
- The main uncertainty is where the house's bottom is, since grass hides it (±3% between the two readings). There
  is also possible depth difference between the bird and the house, which the 2D convention ignores (at this scale
  the door would be 1.45 m tall).
- Answer: 3.56 m (medium confidence).
