# Q842: length of the horse at the back (m)

**Object:** the dark brown horse in the top lane. It is behind the tan horse in the walking direction (+x) and is in the top lane, so both readings of "at the back" point to it. The video is a top-down 2D scene at 24 fps; question_fps is also 24, so there is no re-timing.

**Scale (prior: this horse's speed = 0.874 m/s):**
- `measure.py` builds its own mask (a local polynomial background per frame, plus chroma, dark and bright thresholds). It writes `brown_track.csv`, with overlays in `frames/ov*.png`.
- Speed in pixels, frames 0–48: the core-centroid slope gives 104.3 px/s, the bbox centre 105.7, the rear edge 104.9, the front edge 106.4, and core end-to-end 106.6.
- The animation loops: frame 49 resets to the frame-0 pose and position. One full cycle gives (811.4 + ~4.4 − 598.2)/49 frames, about 4.44 px/frame = 106.6 px/s.
- I adopted 106 px/s, giving a scale of 0.874/106 = 0.008245 m/px.

**Length in pixels:**
- The tail-to-muzzle x extent per frame is 238–272 px (median 246, mean 249). It is longer around frames 27–33 because of the gait pose.
- The overlay at frame 20 shows the whitish muzzle tip sticking out about 5 px past the mask. I took the length as about 250 px.

**Answer:** 250 × 0.008245 = **2.06 m**. Using 246 px gives 2.03 m, and 254 px gives 2.09 m.

**Second check:** the speed scale is consistent across 5 reference points (±1.5%). A real horse is about 2.0–2.4 m long, so the answer is plausible.

**Confidence:** about ±4%. The main uncertainties are which pose the reference bbox used and the muzzle edge.
