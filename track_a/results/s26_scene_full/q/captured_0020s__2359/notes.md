# q2359 — height of the white jar (cm)

Answer: **12.5 cm** (low confidence: the plausible range is about 10–15 cm).

## Inputs
- Lab video, 24 fps (the file rate and question_fps are the same), 1280x720, f = 0.5959*1280 = 762.8 px, c = (640,360).
- Jar distance at t=0.60 s (frame 14) = 1.9735 m. The jar is the white cylinder thrown by the near person
  (scene/tracks/white_object.csv; the track is correct: release at frame 14, free flight 14–26, caught at 27).
- The gravity prior is used only for the ballistic depth fit.

## Method
1. **Depth per frame** (traj.py): a 3D ballistic fit, p(t) = p0 + v0 t + ½ g t², with p0 at 1.9735 m on the
   frame-14 ray and g = 9.8 m/s². The gravity direction was left free; it comes out 9° from the body-axis
   vertical vanishing point. RMS error 2 px. Depths: f15 1.99, f16 2.03, f17 2.08, f20 2.31, f22 2.52, f25 2.91 m
   (the catch is near the far person at 3.24 m, which fits).
2. **Blur-robust silhouettes** (alpha.py, prof.py): per-pixel colour-mix fraction between the background and
   the jar's white. The leading edges along the motion are sharp (10–90% ramp 3.5–7 px against 1.5–3 px across
   the motion), so motion blur is only about 4–7 px. The long soft ramp at the trailing end is the jar's shaded
   end, not blur, so masks use alpha ≥ 0.3.
3. **Important geometry point:** pixel size scales with the optical-axis depth z = range·cosθ, and is stretched
   further radially (1/cos²θ) off-axis. At the jar's position θ ≈ 20°, so the naive conversion
   (depth × px / f) overestimates sizes by 7–15%.
4. **Cylinder tumble model** (tumble.py, hprofile.py): a cylinder H × D whose axis rotates rigidly at constant
   ω, projected with the true pinhole camera at the fitted depths and fitted to the masks of frames 15–17 and
   20–25 (mean IoU about 0.88).
   - D is well determined: **6.8–6.9 cm** in every run.
   - H is degenerate with the axis tilt ψ: the cost is flat for H = 10–15 cm (0.1187 at 10 → 0.1160 at 15).
     H = 8 is clearly worse (0.138) and H = 9 slightly worse (0.122).
   - Frames 15–17: projected length along the axis ≈ 12–14 cm (H·sinψ + D·cosψ) and width ≈ D.
5. **Cues for choosing H in the 10–15 range:**
   - In-hand views (frames 7–11) show the lid ellipse at ψ ≈ 40°, which continues smoothly into the
     H ≈ 12–15 solutions (ψ ≈ 36–44° at frames 15–17).
   - The naive annotator-style length near t = 0.6 s is 55–58 px × 1.97 / 763 ≈ 14–15 cm. This is an upper
     bound because it is inflated by the off-axis factor.
   - Frame 4 (held, near-static) suggests a shorter jar (about 8 cm), but the jar's bottom there may be hidden
     against the trousers, and it conflicts with the sharp-edged flight silhouettes.
   - I chose the middle of the range: 12.5 cm.

## Checks
- D = 6.85 cm is consistent with frame 4: a 33 px lid at about 1.8–2.0 m with the off-axis factor.
- The record in scene/ (centroid track, phases) is correct for this object. Its pixel sizes include shading
  and blur, and it does not apply the off-axis scale.

## Confidence
Low to moderate. The answer is within ±20% of the plausible range 10–15 cm; the diameter (6.85 cm) is much
better determined than the height.
