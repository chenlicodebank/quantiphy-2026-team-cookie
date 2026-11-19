# q_1680 notes

Question: length of the rock (m). Prior: boat speed 4 m/s. Depth: boat 90.11 m at t=1 s, 90.44 m at t=2 s.

Method:
- Boat pixel speed from a linear fit of the boat track over frames 3-74: about 6.44 px/frame. hull_cx, centroid_x and ref_x agree to within 0.02 px/frame.
- Time base is question_fps = 24, so 4 m/s is 0.1667 m/frame. The file runs at 25 fps.
- The depth change is 0.326 m/s, so the boat moves mostly across the image plane. The lateral part is about 0.166 m/frame.
- Scale is about 0.0258 m/px at the boat's depth (0.166 / 6.44).
- Rock bbox width is 634 px (from scene/). It is the longer horizontal extent. The right tip touches the image edge, so it may be truncated by a few px.
- I assumed the rock is at the same depth as the boat. Its depth is not given, so this is the main uncertainty.
- Rock length = 634 x 0.0258, about 16.4 m.

Second-route check: the boat hull length is 396 px x 0.0258, about 10.2 m. That is plausible for a fishing boat, so the scale looks sensible. I did not do an independent check of the rock depth.

Confidence: moderate.
