# Q1859: acceleration of the astronaut at t = 0.5 s

- This is a 2D segmentation video at 24 fps, and question_fps is also 24, so t = 0.5 s is frame 12.
- **Scale:** I re-measured the upright figure in frames 0-3 (`measure.py`). With mask thresholds from 200 to 248, its height is 90-92 px, which matches the record's 91 px. The prior says 2.2 m, so the scale is 2.2/91 = 0.02418 m/px.
- **Motion:** I used the mask centroid from scene/tracks/person.csv. The rise (275 px, mostly vertical) fits a smoothstep ease-in/out (3s²−2s³, the shape of a Blender Bezier with flat handles) very well. The best fit has t0 = −0.4 frames and T = 78.65 frames, with an rms error of 0.33 px over 80 frames.
  - Following the benchmark convention, I took one-frame backward-difference speeds of the fitted positions. The change in speed at frame 12 is 0.1895 px/frame².
- **Second route:** I fitted local quadratics and cubics to the raw centroid y around frame 12. The 4-20 window gives 0.188, the 6-18 window 0.191 and the 3-24 cubic 0.185 px/frame². The bbox-centre track fitted with smoothstep gives 0.188. Idealised keyframes at 0 and 78 would give 0.195.
- **Result:** a ≈ 0.19 px/frame² × 576 × 0.02418 m/px ≈ **2.64 m/s²**. It is positive, because the figure is speeding up.
- **Confidence:** good, about ±4%. The main uncertainties are the pixel height (±1 px) and the exact keyframe timing.
