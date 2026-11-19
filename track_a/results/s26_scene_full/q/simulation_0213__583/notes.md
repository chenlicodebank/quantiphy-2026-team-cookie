# q_583 — dog length incl. tail (m)

Prior: black cat speed 0.94 m/s. fps 24 = question_fps (no retiming).

## Scale
- check.py: cat nose (bbox_x1) linear fit over unoccluded frames 0-22, 44-49: 17.76 px/frame (torso fit 17.86) -> 426 px/s.
- Cat lane scale: 0.94 / 426.3 = 0.002205 m/px.
- The dog walks in a nearer lane (paws y~1066 vs cat y~1020). Camera looks level (horizon taken at image centre y=540):
  depth ratio Z_cat/Z_dog = (1066-540)/(1020-540) = 1.096 -> dog lane scale 0.002012 m/px.
  (Horizon at y=300 would give 1.064; no correction would give 1.0.)

## Dog length
- Tail swings; with the tail stretched straight back (frames 6, 17-18, 39-40) the nose-to-tail-tip extent is 594-609 px
  (scene track, confirmed on grid crops frames/d_17.png, d_40.png: ~1043->1646, ~552->1148). Use 603 px.
- Length = 603 x 0.002012 = 1.21 m. (Uncorrected single 2D scale: 1.33 m; median-over-clip length 515 px -> 1.04 m.)

## Check / confidence
- Dog height ~290 px -> 0.58 m, tail-free length ~462 px -> 0.93 m: plausible medium dog. Implied camera height ~1.06 m.
- Main uncertainty: horizon row (perspective correction ±4%) and which tail pose the reference AABB uses. Moderate confidence.
