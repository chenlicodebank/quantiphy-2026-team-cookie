# q_1768: height of the turning yellow car (the taxi)

Answer: **1.65 m**. This is the ground-to-roof-sign-top height. Confidence is moderate, about ±8%; the focal length is the main uncertainty.

The video is a 3D Blender render at 24 fps, and question_fps is also 24. The given depths fall at frames 14 (t = 0.58 s) and 38 (t = 1.58 s). The yellow car is the "taxi" in scene/. The white car in the prior is the "van".

## Camera (pinhole, principal point at the image centre, roll assumed 0)
- **Ground plates as squares:** the two brown plates are back-projected to the ground and their second moments must be isotropic (`patchcal.py`, `curves.py`). This alone gives f = 1158, pitch 25.4°. With roll left free the fit returns 0.03°, which supports roll = 0. On its own this cue is weak.
- **Sidewalk corner = 90°:** this gives a curve a(f) (`sidewalk.py`, `curves.py`).
- **Pedestrian upright:** the mean head-to-feet axis over all frames is 69.6° (std 3.3°). It must point at the vertical vanishing point, which gives another curve a(f).
- **Combined:** the plate curve crosses the sidewalk and pedestrian curves at f ≈ 930–975 px with a ≈ 28–28.7°.
- **Van check:** the van's straight-line direction from KLT tracking must be horizontal; this crosses the curves at f ≈ 890–925.
- **Adopted camera:** f = 925 px (HFOV about 99°), pitch 28.8°.
- **Camera height:** h = 7.38 m. It comes from the pedestrian: pelvis = mask centroid back-projected at the given depth, and the lowest foot lies on the vertical through it (`camh.py`, `rootcheck.py`). Over frames 10–45 the median is 7.28–7.39 depending on f. Frames 14–16 have a detached leg and were not used.
- **Checks:**
  - The taxi's near-side wheel contacts are 2.88–2.96 m apart on the ground in frames 38, 50, 60 and 71. That is consistent across frames and matches a Crown-Victoria-like wheelbase of about 2.9 m.
  - The pedestrian comes out about 1.77 m tall.
  - The van's front tyre contact on the ground fits an acceleration of 4.1–4.2 m/s², against the prior of 4.
- **Rejected route:** the van kinematics alone (KLT rigid track with a = 4 plus the two depths) are too sensitive to the motion start time t0. They gave f ≈ 600–1000 px and were not used to set f.

## Height (`signh.py`)
- The silhouette top is the far roof edge, not the sign. So I located the roof sign top on contrast-stretched crops: (742, 419.5) at frame 38 and (365, 491) at frame 71.
- That pixel's ray is intersected with the vertical plane of the car's centreline. The centreline is the line through the near-side tyre ground contacts, shifted 0.85 m (half track plus half tyre) away from the camera.
- Results at f = 925: H = 1.623 m (frame 38, oblique view) and 1.669 m (frame 71, side view). The mean is **1.65 m**.
- Sensitivity:
  - Moving the centreline offset between 0.8 and 0.9 m changes H by ±0.02 m.
  - f = 900 gives H = 1.68 and f = 950 gives 1.62. More broadly, f = 850 gives 1.74 and f = 1000 gives 1.56.
- The taxi's own root depth (16.549 m at frame 38) puts the root about 0–0.4 m from the near contact line rather than at the car centre. That points to a slightly lower f (about 850, H about 1.74), or the root may not be at the body centre. I did not adjust for it.
- Roof height without the sign would be lower (about 1.45 m); the bounding-box height includes the sign.
