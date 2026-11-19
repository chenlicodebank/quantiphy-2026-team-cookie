# q1101: boat speed at t = 1.0 s

The file runs at 25 fps and the question at 24 fps. I followed the question's rate: t=1 is frame 24 and t=2 is frame 48 (scene/ frame column).

Method (solve.py):
- Camera is static. Principal point is the image centre (480,480). The 3D point is depth * unit ray (u-cx, v-cy, f).
- Focal length: the eagle (bird track) pixel positions at frames 24 and 48 come from local quadratic fits (±6-10 frames, wing-phase-biased frames excluded). They are back-projected with the given eagle depths 116.05 and 108.28 m. I solved for the f that makes the 1-s chord equal 11.84 m. Result: f ≈ 3375-3402 px, about 16° horizontal field of view.
- Check: the eagle's instantaneous speed from pixel velocity plus a linear depth rate comes out 11.7-12.3 m/s at frames 24 and 48. That is consistent with the prior.
- Boat: I fitted the box-centre and hull-centre tracks locally at frame 24. Depth is interpolated linearly between 103.157 and 106.091 m (+0.122 m/frame).
  - One-frame backward-difference speed at frame 24: 4.10-4.11 m/s.
  - Second route, the average over the 1-2 s chord: 4.05-4.06 m/s. The boat moves steadily, so this agrees.
- Breakdown: about 2.93 m/s of the speed comes from the depth change and about 2.9 m/s from lateral motion (about 3.9 px/frame).

Answer: 4.10 m/s. Confidence: good (±5%). The main uncertainty is whether the eagle's motion is straight and at constant speed, which the f calibration assumes.
