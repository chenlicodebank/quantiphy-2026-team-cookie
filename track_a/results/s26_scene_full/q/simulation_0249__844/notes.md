# q_844: length of the horse in the front (m)

The prior is "speed of the horse at the back = 0.874 m/s". There is no depth_info. fps = question_fps = 24.

## Scene
- The camera is static and looks straight down: a 2D planar scene, so one m/px scale applies.
- Two horses walk toward +x.
  - **Back horse** (the prior's horse): the brown one in the top lane, x ≈ 500–960.
  - **Front horse** (the asked horse): the tan one in the middle lane, x ≈ 840–1530, ahead of the brown one the whole time.
- The small animal in the bottom lane is not a horse.

## Scale (from the back horse's speed)
- **Torso template matching** (`speed.py`, frames 0→48): mean step 4.442 px/frame, steady between 3.8 and 4.9 px/frame.
- **Core centroid track** (scene/): (811.44 − 598.4) / 48 = 4.438 px/frame, which agrees.
- Frame 49 is an animation-loop reset (the horse snaps back to its frame-0 pose), so it is excluded.
- Speed = 4.44 × 24 = 106.6 px/s, so the scale is 0.874 / 106.6 = **0.00820 m/px**.

## Front horse length
- **Mask** (`measure2.py`): built against a background composited from frames 0 and 49. On its own it misses the grey muzzle tip.
- **Muzzle correction** (`muzzle.py`): the muzzle is darker than the local background by 5–20 grey levels. The front edge is extended along the head rows while luminance < local background − 5.
- Checked against pixel probes (`probe.py`) and the zoomed frame 24:
  - Frame 0: tip ≈ 1140, measured 1142.
  - Frame 24: tip ≈ 1334, measured 1334.
  - Frame 36: tip ≈ 1427, measured 1426.
- The measured front edge then advances smoothly at about 8 px/frame.
- Tail-to-muzzle length over frames 0–49 (it varies with the gait): median **307 px**, mean 307, range 295–327.
- Length = 307 × 0.00820 = **2.52 m**. The gait range gives 2.42–2.68 m, and frame 0 alone gives 2.47 m.

## Checks
- The speed comes from two independent routes (torso template matching and the core centroid), which agree within 0.1%.
- Sanity check with this scale:
  - The front horse walks at about 8 px/frame, i.e. 1.6 m/s, a normal walk.
  - The back horse is about 246 px long, i.e. 2.0 m.
  - Both are plausible horse sizes.
- If the prior had been averaged across the frame-49 reset jump, the scale would roughly halve (front horse about 1.3 m). That is implausible for a horse, so the reset frame is excluded.

**Confidence:** moderate-high. The main uncertainty is which gait pose the reference bounding box uses (about ±5%).
