# Q786 – length of the brown horse (m)

Prior: speed of the horse at the back = 0.874 m/s. The horse "at the back" is the trailing (left) brown/chestnut
horse, so the prior and the question are about the same object. The video is a 2D side view and fps = question_fps = 24.

- Speed in pixels (scene/tracks/horse_brown.csv, frames 0-48; frame 49 is a loop reset): linear-fit slopes are
  ref_x 3.24, rump (torso_x0) 3.23, nose 3.16 and tail 3.26 px/frame. Net displacement gives 3.10-3.15 px/frame.
  I used 3.2 px/frame = 76.8 px/s, which gives a scale of 0.874/76.8 = 0.01138 m/px.
- Length in pixels (an.py, view.py → frames/brown.png). The mask bbox clips the flat grey-brown nose patch in later
  frames, so I checked the edges on the overlays. Frame 0: 186 px. Frame 10: about 185 px. Frame 32: about 205 px.
  Frame 40: about 182 px. Frame 48: about 200 px. The mask-bbox median is 183 px. The length changes with the
  hind-leg stride and head carriage. I used 190 px (range 182-205).
- Length = 190 × 0.01138 = 2.16 m. This is a plausible horse length.
- Second route: using the record's median of 183 px with the fit slope of 3.24 px/frame gives 2.06 m. The answer
  rests mostly on the pixel length.
- Confidence: moderate, about ±7 %.
