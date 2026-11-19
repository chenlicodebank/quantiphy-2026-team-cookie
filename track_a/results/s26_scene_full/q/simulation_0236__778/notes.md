# Q778: height of the house (m)

- This is a 2D Blender render with a static camera, 24 fps (question_fps is also 24). There is only one horse, and it walks left to right in front of the house's brick wall.
- **Scale from the prior.** The prior is a horse speed of 0.874 m/s.
  - The torso template track in scene/tracks/horse.csv gives a mean per-frame step of 3.164 px/frame. The buttock-edge track gives 3.168, and the net displacement gives 3.146.
  - That is 75.9 px/s, so the scale is 0.874 / 75.9 = 0.01151 m/px.
- **Same depth.** The horse's hooves (y ≈ 1045) sit on the same ground line as the base of the house wall (≈ 1040–1050, partly hidden by grass), so the horse and the house are at the same depth and one scale applies.
- **House height in px (frame 0).**
  - house_extent.py finds the top of the gable apex at y ≈ 256–258 (the first non-sky pixel at x = 540).
  - Zoomed crops put the bottom of the brick base at y ≈ 1045. The grass hides the exact line.
  - Height ≈ 788 px (±8). The scene record's rougher 270–1040 = 770 px would give 8.86 m.
- **Answer:** 788 × 0.01151 = **9.07 m**.
- **Check.** At this scale the horse's ear-top height (162 px) is 1.86 m and its withers (122 px) are 1.40 m, which are plausible horse sizes, so the scale is consistent.
- **Confidence:** moderate–good, about ±4%. The main uncertainties are the base hidden by grass and the gait wobble in the speed.
