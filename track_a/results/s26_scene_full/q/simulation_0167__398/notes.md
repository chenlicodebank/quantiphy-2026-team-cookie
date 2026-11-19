# Q398 – width of the police car (m)

Prior: bike speed = 5.52 m/s. depth_info: none. fps = question_fps = 24, so no re-timing.
Scene: 2D top-down Blender render with a static camera. The road plane is parallel to the image, so one m/px scale applies.

## Scale from the bike speed
- Recorded pelvis track (scene/tracks/cyclist.csv): linear fit 14.415 px/frame, endpoints 14.423, mean per-frame 2D step 14.44 (`speed.py`).
- Independent check (`crate.py`): colour template of crate+helmet+backpack from frame 40, matched in all 80 frames:
  fit 14.45 px/frame, mean step 14.40, endpoints 14.37.
- Pedalling makes the per-frame speed oscillate (13-16 px/frame). The bike itself moves at constant speed, so I used the mean
  of 14.42 px/frame = 346.1 px/s.
- Scale = 5.52 / 346.1 = 0.01595 m/px. Sanity checks: lane 194.5 px = 3.10 m, car length 289 px = 4.61 m, bike ~107 px = 1.7 m. All plausible.

## Car width
- Vertical brightness profiles across the car body at many x offsets, frames 20-60 (`width.py`, `prof.py`): the outer body edges are at
  y ≈ 581.5 and 695.5, which gives **114 px** (range 113-116 px). The record gives 111-115 px for the body and 120-121 px including the mirrors.
- Body width = 114 × 0.01595 = **1.82 m**. With the mirrors included it would be 120.5 × 0.01595 = 1.92 m.
  I answer with the body ("wheel to wheel") reading, as the convention specifies.
- Perspective: from the roof/bumper parallax in the record, the camera is ~90 m (scene units) above the road. The tracked bike point
  (~1 m up) and the car's widest point (~0.9 m up) are at similar heights, so the magnification difference is under 1%.

Confidence: moderate-high. The main uncertainty is whether the reference includes the mirrors (+5%).
