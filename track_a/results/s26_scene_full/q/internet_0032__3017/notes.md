# q_3017 – average speed of boat, 2 s to 4.5 s

- Prior: boat length 3.5 m. The video is 2D: a side-on boat on a lake, filmed by a static camera (record's shift < 0.2 px).
- Time base: question_fps is 30 and the file is 29.85 fps. The difference is negligible: frames 60 to 135 at 30 fps, or 60 to 134 at the file rate. Both give 45.0 or 44.8 px/s. I used 30.
- Track: `scene/tracks/boat.csv` hull centre (cx_hull). I checked it on gridded crops at frame 60 (bow ~672, stern ~897, length ~225 px) and frame 134 (bow ~555, stern ~792, length ~237 px). Both agree with the track (224 and 235-236 px).
- Pixel speed: the mean per-frame |dx| × 30 over frames 60-135 is 45.0 px/s. The motion is monotonic, so this equals the net displacement rate. A Savitzky-Golay-smoothed track gives 45.0 too. The bow gives 47.2 and the stern 42.8 because the boat grows with perspective.
- Scale: I used one scale from the hull length, bow to stern. The mid-interval length is 231 px (the interval mean is 230.6 and the clip median is 232), so the scale is 3.5/231 = 0.01515 m/px.
- Speed = 45.0 × 0.01515 = 0.682 m/s.
- Sensitivity: the length at 2 s (224 px) gives 0.703 and at 4.5 s (235 px) gives 0.670. The clip median gives 0.679.
- Answer: 0.68 m/s. Confidence is moderate to high, at about ±4% from the choice of the scale frame.
