# Q835: length of the horse at the back (m)

- The "horse at the back" is the trailing, leftmost chestnut horse (`horse_red` in scene/). The prior gives its speed (0.874 m/s), so the same object sets the scale.
- 2D side view with a static camera. fps = question_fps = 24, so no re-timing.
- Speed in px: the torso x goes from 646.9 to 801.3 over frames 0-48, which is 77.2 px/s. I left out frame 49, which is a loop reset. As checks, the centroid gives 75.7 px/s and the snout tip (x_max) gives 76.5 px/s, so the three agree within 2%.
  Scale = 0.874 / 77.2 = 0.01132 m/px.
- Length in px: the mask x-extent (scene track; checked on zoomed frames 0 and 30) has median 194 (range 182-216) as the gait spreads the legs. With the legs gathered, the snout-to-buttock length is about 181-185 px. I used 192 px, between the rest-like extent (~184) and the median over the animation (194).
- Answer: 192 x 0.01132 = **2.17 m**. The range is 2.06 m with the legs gathered to 2.20 m at the median extent.
- Confidence: moderate, about ±5%. The main uncertainty is which pose the reference bounding box used. The scale is solid.
