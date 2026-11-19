# Q3005 — boat speed between 0.5 s and 1.0 s (prior: speedboat length = 3.2 m)

Method (annotator convention: one planar scale from the prior, pixel tracking, pan-compensated):
- Checked scene/tracks/boat.csv bow (red) and stern (flag on transom, green) markers on frames 0, 15, 29, 41
  (view.py -> frames/check.png): they sit on the bow tip and the stern flag. So the length_px record is right.
- Camera pans right at about 0.75 px/frame, so I used the background-stabilised x (`*_stab`).
- Window: frames 15–29 (file fps 29.15) or 15–30 (question fps 30). The mean per-frame displacement is
  bow 14.64, stern 14.95, centre 14.80 px/frame.
- Scale: the mean bow-to-stern pixel length over the window is 196.6 px (the boat foreshortens slowly from 208 to 190 px
  over the clip) → 3.2/196.6 = 0.01628 m/px.
- Speed with the centre track: 7.02 m/s at 29.15 fps, 7.22 m/s at 30 fps. The bow and stern tracks give 6.95–7.30 m/s.
- Time base: both rates give a plausible boat speed (about 25 km/h), so the scene cannot pick one. I answer 7.1 m/s,
  which is within 2% of either.
- Other readings: using the frame-0 length (208 px) would give about 6.6–6.8 m/s. Without pan compensation the result is about 6.6 m/s.

Second route: the bow and stern tracks are independent template tracks and agree to within 2%.
Confidence: moderate–high. The main uncertainties are which frame the annotator took the pixel length from (±5%) and the fps (±1.5%).
