# Q792 – height of the front horse (m)

- 2D side-view Blender clip, 24 fps (file fps = question_fps; no retiming). Both horses walk +x on the same ground
  line in front of the wall, so they are at the same depth and one m/px scale applies to both.
- "Front" horse = the leading tan horse on the right; "back" horse = the trailing chestnut horse on the left (prior: 0.874 m/s).
- Brown speed in pixels (frames 0-48; frame 49 is a loop reset):
  - record rump `torso_x0` net 156→305 = 3.10 px/frame; `ref_x` net 3.15; linear fits 3.13-3.24
  - my own template matching of the torso band frame to frame (match.py): median 3.09 px/frame, about 3.12 with the
    bad matches at frames 29-31 left out
  - adopted value: 3.12 px/frame = 74.9 px/s → scale = 0.874 / 74.9 = 0.01167 m/px
- Tan horse height in pixels (ear top to hoof): the record's per-frame bounding-box median is 169 px (p10-p90 164-172).
  I checked it on zoomed frames 0 and 24: ears at y≈880, hooves at y≈1048, so about 168 px.
- Height = 169 × 0.01167 = 1.97 m. For comparison, the brown horse comes out at 159 px ≈ 1.86 m, and the tan horse's
  ratio of speed to body length is plausible.
- Uncertainty: the speed (±3%) and the height in pixels (±2%) give a range of about 1.90-2.02 m. Confidence is moderate to good.
