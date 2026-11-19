# Lessons library, harness v1 (seeded from earlier rounds of this campaign; procedure only, no question values)

1. A segmentation clip keeps the original scene's answers: if the object the question names was removed with the
   background, the answer is still about that object; never re-read the question as being about another visible object.
2. Agreement is weak evidence. Sessions of one model share its readings, and the open-weight agent's repeated runs share
   its errors; on held-out scores the Claude sessions are usually the more accurate measurers, but not always.
3. When one candidate's answer is close to a constant multiple of another's, the difference is almost always one scale
   step (pixel scale, focal length, which point the depth refers to, a unit). Decide it by closure on the question's own
   prior, never by which candidate looks more self-consistent.
4. In a 3D scene, a focal length from two references at nearly the same depth, or from a short baseline, is
   ill-conditioned; check that the focal you use reproduces every given distance, and prefer the route that does.
5. A speed or acceleration asked at a time is a short-window derivative around that time, not an average over the
   clip; check which window each candidate used, and never fit across a bounce, impact or occlusion.
6. An earlier answer that substituted a typical real-world value for a measurement is a guess; prefer a measurement
   that passes closure, and keep the guess only when nothing in the clip can be measured.
7. When the asked object changes depth during the clip, its pixel extent and its depth must be read at the same frame.
