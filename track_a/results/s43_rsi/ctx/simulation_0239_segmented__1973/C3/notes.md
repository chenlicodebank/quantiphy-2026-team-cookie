2D scene: scale from the brown (dark reddish-brown) horse, whose centroid track over frames 1-47 gives 64.0 px/s (linear fit 64.5, bbox-centre 63.3), so 0.874/64.0 = 0.01366 m/px. The house (SAM 3 mask, x 621-1420) is 800 px wide -> 10.9 m. Second route (threshold bbox 806 px, edge-based speed) gives 11.0-11.1 m.

Final message:
**Answer: 10.9 m** (question 1973).

Method: the scene is a 2D render (white background) with a large static "house" block structure and two low-poly animals. The brown horse is the dark reddish-brown animal (colour, SAM 3 "brown horse"/"brown animal" scores, and horse-size plausibility all favour it over the cream/tan one). Its centroid track over frames 1–47 gives 64.0 px/s (linear fit 64.5, bbox-centre 63.3, edges 63.1–63.5), so the scale is 0.874/64.0 = 0.01366 m/px. The house mask spans x 621–1420 → 800 px wide, giving 10.9 m; a second route (threshold bbox 806 px, edge-based speed) gives 11.0–11.1 m. Notes with the alternative reading (pale animal → 6.3 m) are in notes.md.
