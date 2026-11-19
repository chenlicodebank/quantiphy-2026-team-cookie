# q_1362 – length of the turning yellow car (taxi), simulation_0074

Answer: **5.37 m**

## Setup
- 3D Blender scene, static camera, 24 fps (file fps = question_fps, no re-timing). t=0.58 s -> frame 14, t=1.58 s -> frame 38.
- Asked object: yellow taxi (scene/ "taxi"). Prior object: the white van, 6 m long. Length = bumper to bumper.
- Taxi frames 0-20 have the cyclist in front of the rear, so only frames 21+ are used (record's occlusion flags checked).

## Camera (vp.py, camheight.py)
- Focal length from road kerb vanishing points (Hough lines on the median background, frames/lines.png). The two road
  directions are assumed orthogonal. VP_A ≈ (-1298,-256), VP_B ≈ (2688,-259); f = sqrt(-(vA-c)·(vB-c)) = **1785 px**
  (the 9 line-pair combinations give 1778-1836). Horizon at y ≈ -257, no roll. The coplanarity test of the four objects'
  depth-given displacements (coplanar.py) is weak but agrees (~1800-2000).
- Ground-plane rotation from the VP directions. Camera height: 9.45-9.70 m from pedestrian and cyclist (ground contact +
  given depth). The taxi's own depth at frame 38 implies 9.37-9.43 m.

## Taxi length (wheels3.py, len3d.py)
- Near-side wheel hub centres found per frame with Hough circles (overlays frames/hc_38.png, hc3_30.png). Both hubs sit at
  wheel-radius height, so back-projecting them gives the car heading (yaw) and the wheelbase directly. Yaw passes through 0
  (exactly side-on) at frames 30-32: the front is turned toward the camera before that and away after.
- Bumper tips = extreme left/right mask pixels within 25-80 % of the box height, which excludes the ground shadow and the
  roof. Their rays are intersected with vertical planes parallel to the car axis: the mid-plane ± lateral offset w of the
  tip (near/far corner chosen by the sign of the yaw). Length = separation along the heading.
- Frames with |yaw| < 12° (27-35): L = 5.43-5.45 m before the scale correction (frames 30-33: 5.459, 5.450, 5.428,
  5.434). This is insensitive to w (w = 0.6 / 0.9 gives 5.45 / 5.41) and to wheel radius / half-track (±0.03).
- Scale correction to the given taxi depth (30.4267 m at frame 38): the model puts the car centre at 30.72-30.93 m (origin
  height 0.7-0 m), so all distances are scaled by 0.984-0.990 (0.987 at mid height). **L = 5.44 × 0.987 ≈ 5.37 m.**
- Wheelbase 3.02 × 0.987 ≈ 2.98 m, giving L/wheelbase = 1.82. The asset looks like a Ford Crown Victoria (real 5.39 m,
  2.91 m wheelbase, ratio 1.85); this is a sanity check only.

## Second routes and checks
- All frames 26-46 at yaw up to 34°: median 5.37 m before / 5.30 m after the scale correction with w = 0.75. With w = 0.6
  the larger-yaw frames agree with the yaw-0 value (5.45 before scaling). Earlier mid-plane-only estimates (midplane.py) at
  near side-on frames gave 5.47-5.55 before the corner correction.
- f sensitivity: given the depth, L ∝ ~1/f. f = 1750 / 1785 / 1820 gives 5.47 / 5.36 / 5.26 m.
- Van prior (vancheck.py): the van is ~65° off side-on at frame 14, so its silhouette width is dominated by its
  (unknown) width and the length check is ill-conditioned (a 2.0 m wide box needs L ≈ 5.0 m at f = 1785). Its near-side
  hub spacing (hand-read hubs) gives a wheelbase of 3.70 m at the given depth, which is consistent with a 6 m van
  (wheelbase/length of an Express van is 0.60-0.64, giving 5.8-6.1 m). So the prior is consistent with f ≈ 1785 at the
  ~4 % level, but it does not pin f down more tightly.

## Record corrections
- scene/ track bboxes for the taxi are fine for frames 21+. Its bbox-centre trajectory is too noisy for heading, so the
  heading here comes from the wheels.

Confidence: moderate-good. The main uncertainty is f (±2 % → ±2 % in L); the scale and geometry errors are each ~1 %.
Estimated total ±3-4 %.
