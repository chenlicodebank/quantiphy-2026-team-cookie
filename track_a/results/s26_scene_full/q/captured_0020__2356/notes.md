# q 2356 – displacement of the yellow toy, t = 0.60 s → 0.80 s (cm)

**Answer: 60.2 cm**

## Identification
- The yellow toy is the scene record's `yellow_fruit`: a yellow body with a green leafy end, thrown by the far person to the near person.
  depth_info: "carrot" = 2.63 m at t = 0.60 s, which fits the yellow toy just after release from the far person (pelvis 3.237 m).
  The "jar" (1.9735 m) is the white object thrown by the near person (pelvis 1.58 m).
- Frames at question_fps 24 (same as the file's fps): t = 0.60 → frame 14, t = 0.80 → frame 19. Both are free flight with no occlusion.
  Centroids (scene track, checked on zoomed frames): f14 (565.7, 97.5), f19 (447.7, 87.2).
- f = 0.5959 × 1280 = 762.8 px, principal point (640, 360).

## Depth at frame 19 (not given) – 3D ballistic fit
- Camera gravity direction from vanishing geometry: the right-wall vertical seams (slope dx/dy −0.154 at x ≈ 1125) plus the orthogonality
  of the two floor baseboards give pitch 34°, roll 11.4° (`pitchroll.py`). A second route crosses the seam with the far person's body line
  and gives pitch 30°, roll 9°. The right-wall seams alone, with roll 0, would give 15° – rejected, because then the white ball would be caught at 1.9–2.1 m
  when the catcher is at 3.24 m.
- Fitting with g fixed at 9.8 (`fit3d_c.py`, `fit_joint.py`) leaves systematic 4–5 px residuals. Both throws show less image curvature than 9.8 m/s² at the given
  depths (`fit_freedepth.py`). With g left free (`fit_gfree.py`), both objects independently give g_eff ≈ 7.5–8.1 (a shared timing/scale factor)
  and fit at 1.0–1.7 px rms. The endpoints are then physically consistent: yellow release about 2.86 m (far hand), yellow catch about 1.65–1.75 m (near person's
  hands), white release 1.97 m, white catch 2.5–2.7 m (far person's hands).
- d19 (yellow) = 2.10–2.16 m over pitch 28–36° / roll 8–12° and frame windows 13–24, 13–23, 14–24. Central value 2.13 m.

## Result
- P14 = back-projection of f14 at 2.63 m; P19 = back-projection of f19 at 2.13 m (`final.py`).
- Displacement = 60.2 cm (range 56–64 cm for d19 = 2.18–2.085 m).
- Other routes: fits with roll 0 give 42–51 cm, but they put the catches at implausible depths. Free pitch/roll pixel-only fits are degenerate (pitch 56°, ruled out by the seam slope).

## Confidence
Moderate (about ±6%). The answer depends on the inferred depth at 0.80 s, which is not given. The image displacement alone (118 px ≈ 0.40 m laterally) is
well measured; the depth change (~0.5 m toward the camera) dominates.
