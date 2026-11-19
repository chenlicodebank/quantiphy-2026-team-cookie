# q_1490 – forklift length (fork tips to rear bumper)

Prior: forklift height = 2.47 m (exact). Depth: t=1 s (frame 24) 16.7953 m, t=2 s (frame 48) 19.0980 m.
The file and the question are both 24 fps, so t = 1 s is frame 24 and t = 2 s is frame 48.
**Answer: 4.37 m** (plausible range 4.27–4.46).

## Method (3D, pinhole; principal point at the image centre; roll assumed 0)
1. **Motion vanishing point.** The forklift translates in a straight line (no yaw). I tracked about 80 rigid LK features on the body
   (`track_lk2.py`, `track_rear.py`); every track is straight to within 1.5 px. Their least-squares intersection is
   VP_d = (−1982, −783) (`recon2.py`, rms 2.5 px). With roll 0, the horizon is the line y = −783, so tan(pitch) = 1503/f.
2. **Affine depth from pure translation.** For each feature, |x(0) − v| / |x(t) − v| − 1 = w(t)/Z_i. A rank-1 factorisation
   over frames 20–71 gives the relative depth Z_i of every feature (relative residual 0.06%). The fork tips were detected in each
   frame with two different detectors (`forktips2.py`, `forktips4.py`). Each tip track was then fitted to the same model with outlier rejection
   (`tipfit.py`); the two detectors agree on depth to within 0.3%.
3. **Focal length.** Four routes:
   - Fork-tip pair: the line between the tips is lateral, and its vanishing point lies on the horizon. Median over frames 0–50: f ≈ 3505 (sd 126).
   - Rear reflector bar of the canopy: in the affine-depth 3D it must be perpendicular to d. This gives f ≈ 3545 (`f_bar.py`).
   - Trunk tilt of the right pine (crooked): vertical VP at about y = 8800, so f ≈ 3500. The left pine is noisier and gives about 3900.
   - The prior's scale combined with the given depths and an origin at the bbox centre: f ≈ 3440 (t = 1 s) and 3490 (t = 2 s).
   - The fork-tip pair in 3D alone prefers about 3150–3300, but it is noisy.
   Adopted value: f ≈ 3450 ± 100, pitch ≈ 23.5°.
4. **Length and height in model units** (`final2.py`). The front is the mean of the fork tips' along-d coordinate. The rear is the
   rear-most tracked feature, a rear lamp on the lower rear bumper face; the rear-face features cluster within about 1%. The height is
   the highest feature (canopy rear corners and mast top) above the fork-tip level. Small offsets are added: the roof top about 0.04 m
   above the bar features, the fork-tip corner about 0.04 m above the ground, and about 1–2 cm for the tip end and the bumper surface.
   Scale: (H_units + offsets) = 2.47 m.
   - Result: L/H ≈ 1.77, so **L ≈ 4.37 m** at f = 3450. L is 4.32–4.40 for f = 3300–3600 and 4.27–4.46 under the offset variations.

## Second route / checks
- Depth scale instead of the prior: put the origin at the 3D bbox centre at f = 3450. The predicted distances then match 16.80 / 19.10 to
  within +0.3% and −1.0%. So the depth-based scale gives L ≈ 4.36–4.41 m, which agrees with the prior-based value.
- Caveat: the given depth ratio 19.098/16.795 = 1.137 is about 1.5% larger than any central origin reproduces (about 1.12).
  Matching it exactly would need an off-centre origin, for example about 1.5 m to the side. The absolute values still agree with the prior scale.
- Sanity: a real Toyota 8FG25 is about 3.6 m long with forks and 2.1 m tall (ratio 1.7). The ratio here is 1.77, which is plausible for
  the model.

## Assumptions and confidence
- The forklift is aligned with the world axes, so its AABB length equals the vehicle's length along the direction of travel.
- Camera roll is 0. Principal point is at the image centre.
- Confidence: moderate. Expected error is about ±4%, dominated by f, the fork-tip depth and the roof-top and ground offsets.

## scene/ record
The track CSV and the mask bounding boxes cover the forklift correctly. scene/ gives no camera or scale information. Everything above
was re-measured from the video.
