# q_1741: length of the eagle (m)

File: 25 fps, 75 frames, with duplicate frames 1, 26 and 51. It is a 24 fps render (72 unique frames), and
question_fps = 24. Render frame r24 (t=1 s) is file frame 25, and r48 (t=2 s) is file frame 50.

## Where is the eagle?
- The scene record lists a boat, a person and a large brown "rock" (blob at the top, 767 px wide, cut by the top edge).
- The blob is **static** (`edges.py`): its edges and lowest point stay constant to about 1 px over all 75 frames. The
  eagle's given distance falls from 179.27 to 177.10 m in 1 s. A radial approach alone would enlarge the blob by
  about 1.2% (about 9 px), and that does not happen. At 179 m the blob would also be about 15 m wide. So the blob is not
  the eagle; it is a rock or islet, as the record says.
- The only possible eagle pixels are tiny marks at the top image edge in frames 0-1 only (`bits.py`). These are
  components at x of about 1147, 1199 and 1342, y 0-9, each 4-17 px in size. They are gone by file frame 2, so
  the object leaves the frame through the top edge immediately. The eagle is therefore essentially out of view for the
  whole clip, and nothing about its length can be measured from the pixels.

## Scale (computed, but not usable for the eagle)
- Boat prior 4 m/s with the r24 and r48 positions (record ref point) and depths 177.21 / 178.00 m gives
  f = 9070 px (HFOV 9.7 deg), so 0.0196 m/px at 178 m (`geom.py`).
- Checks: person walking speed 0.99 m/s (plausible); boat length 512 px, about 10 m (plausible fishing boat). So the
  scene is at real-world scale.

## Answer
The eagle is not measurable in the clip. The scene is at real-world scale, so I use a real eagle's body length (beak to
tail). Bald and golden eagles are about 0.7-1.0 m long, and I take **0.9 m**.
- Alternative reading: if the edge marks were parts of one eagle at about 181 m, they span 214 px, about 4.2 m. That
  would imply an unrealistically large model, so I did not use it.

Confidence: low. There is no direct measurement; the answer is a typical real-world size.
