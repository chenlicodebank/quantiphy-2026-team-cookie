# Q776 — height of the brown horse (m)

There is only one horse in the clip (a chestnut horse walking left to right in front of the house). "The horse at the back"
in the prior is this same horse. The video is a 2D-style side-on walk with a static camera. fps = question_fps = 24.

## Scale from the prior (speed 0.874 m/s)
- Horizontal pixel speed from the scene tracks (measure.py re-computes it): torso template track 3.146 px/frame, buttock
  edge track 3.168 px/frame. Mean is 3.157 px/frame = 75.8 px/s. Vertical motion is under 2 px.
- Scale = 0.874 / 75.8 = 0.01154 m/px.

## Pixel height
- measure.py diffs each keyframe (0, 12, 25, 37, 49) against a frame where the horse is somewhere else, then finds
  the top and bottom rows of the horse.
- Results: ear top at y 881–883, hoof bottom at y 1046–1048, so the height is 164–167 px at threshold 60–90.
- The hand-read keyframes in scene/ give 160–164 px (mean 162).
- I adopted 163 ± 2 px.

## Answer
- Height = 163 × 0.01154 ≈ 1.88 m. The range is 1.87 (162 px) to 1.92 (166 px).
- Second route: the record's hand-read heights and my code-measured heights agree to within about 2%.
- The two independent x tracks give speeds that agree to 0.7%.
- Sanity check: 1.88 m to the ear tips is plausible for a horse.
- Confidence: good, about ±3%. The main risk is how the reference defines the speed: if the rig root moves non-uniformly,
  the mean per-frame speed could be slightly above the net-displacement rate.
