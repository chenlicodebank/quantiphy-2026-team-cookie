# q811: width of the house (m). simulation_0241, round-2 check

Prior: speed of the horse at the back = 0.874 m/s. No depth_info. The file and the question both run at 24 fps, so there is no time-base issue. 50 frames; frame 49 is a loop reset of the brown horse, so I measured frames 0-48.
Submitted: 9.153, a fixed-rule blend of C1 = 8.25 and a DeepSeek median of 11.665. Round 1 proposed switching to 8.2 (following C1). My first job was to verify that.

## Crux
Which pixel extent counts as the width, and at what depth it is converted:
- C1 / round 1: the main block's gable-to-gable span (image y) at eave depth.
- DeepSeek (C2-C4, blend component B): the silhouette's image-x extent, 806 px (the cross wing's ridge ends), times the horse scale.

## My measurements (own code)
- speed_me.py, horse at the back (brown, trailing):
  - Template matching: 2.605 px/frame (lag 24), 2.631 (lag 36), 2.644 (lag 48).
  - Rear edge: 2.612. Largest-component centroid: 2.693.
  - Adopted 2.63 px/frame = 63.1 px/s, giving **0.013847 m/px at horse-back depth**.
- roof_me.py, main-block outline on a median frame (B-0.6G feature, threshold crossings, robust lines; rms 0.2-0.7 px). Overlay in frames/roof_overlay.png; the fitted lines sit on the edges.
  - Eave corners: N (658.8, 93.1) / (1363.8, 92.1); S (660.4, 716.3) / (1361.8, 716.7).
  - **Route 1 (eave level): Y span = 623.9 px.**
  - **Route 2 (ridge level):** ridge ends at y = 17.8 / 745.7, span 727.9 px. Eave/ridge depth ratio 1.1672 (N) / 1.1654 (S); the two match, so the view is nadir and centred. 727.9 / 1.1663 = **624.1 eave-px** (agrees with route 1 to 0.03%).
  - X span (main eaves) = 703.2 px at the same eave depth.
  - X > Y in world terms even before the higher cross wing is counted (the wing can only add to X). So **width = Y extent** (shorter horizontal), and length = X.
  - These reproduce round 1's figures (624.7 / 705 px, 2.632 px/frame) within 0.3%.
- Width without correction: 623.9 × 0.013847 = 8.639 m. The eaves are nearer the camera than the horse's back, so width = 8.639 × (1 − Δ/D_hb), with D_hb = 0.013847 f and Δ = eave height − horse-back height.
  - The roof perspective links f to the main pitch: f = 2469 tan(pitch).
  - For a pitch of 30-45° (f 1425-2469) and Δ = 1.1-1.9 m (one-storey eave), the width is 7.8-8.3 m; at central values it is 8.1-8.25.
  - **Answer 8.2 m.** A two-storey main eave (Δ ≈ 4.5 m) would give about 7.0 m; I judge it unlikely.
- I found no route to f itself. The ground shadow and the animals' own shadows are not usable because the animals walk inside the house and tree shadow. The roof-on-roof shadow gives only sun-angle × f.

## Rechecks
a. **Closure:** the scale comes from the prior. The independent speed routes (rear edge 2.612, template 2.605-2.644, centroid 2.693) re-derive 0.874 m/s within −0.9% to +2.4% at the adopted scale. closure_pct ≈ 1.
b. **Plausibility** at 0.01385 m/px:
   - Brown horse: 126-144 px long, i.e. 1.75-2.0 m, walking at 0.874 m/s.
   - White animal: about 2.45 m (cow-sized).
   - House footprint about 8.2 × 9.2 m; main ridge about 3 m above the eave at f ≈ 1700. All realistic.
c. **Units and time:** metres; 24 fps throughout.
d. **Fault proof:**
   - C2/C4 and the blend's component B (806 px × horse scale): they measured the image-x extent of the cross wing's ridge ends. That is (i) the longer horizontal dimension (main eave X span 703 px vs Y 624 px at the same depth), not the width, and (ii) taken at roof-ridge height, nearer the camera than the horse scale assumes.
   - C3: also used ×1.139 on the premise of an oblique camera with the house farther away. The symmetric eave/ridge ratios (1.167 / 1.165) show the view is nadir and the roof is nearer.
   - C1: no fault. Its span (622.4 px) and speed (2.62) match mine within 0.5%.
   - The other reading, width = world X extent, gives 703 × 0.013847 × 0.94 ≈ 9.15 m, about equal to the submitted blend. The convention (width = shorter horizontal extent) excludes it.

## Decision
I verified round 1's switch: I reproduced the fault (component B uses the wrong, longer extent at the wrong depth), and my own value (8.15-8.2) agrees with round 1's 8.2.
Answer **8.2**: switch, following C1. Confidence: medium. The eave height and f are unmeasured (±3%), and the naming reading would put the X extent at 9.15.
