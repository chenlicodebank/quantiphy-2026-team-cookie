# Q1886: astronaut speed at t = 2 s (m/s). Answer: 2.05

Time base: the file and the question both use 24 fps, so t = 2 s is frame 48 and the speed is the backward difference from f47 to f48 (lightly smoothed).

## Method (3D pinhole model, fixed camera)
- **Depth:** Z(f24) = 18.147 m (from depth_info). For relative depth I matched a template of the upper body (helmet,
  backpack and shoulders; top 30% of the bbox) over a range of scales (`tmatch.py`, `tscale.py`).
  - The 4-frame scale chain from f24 to f48 gives 1.090. The bbox-height ratio 413/380 = 1.087 agrees.
  - So Z48 = 16.65 m.
- **Local depth rate at f48:** a long-baseline template scale fit around f48 (±8 to ±16 frames, two template sizes) gives a scale growth of
  +0.20 to +0.34 %/frame, meaning the astronaut is approaching. Over the whole clip the size grows 1.27x, also about 0.3 %/frame.
  - bbox_h falls slightly near f48 (about −0.3 %/frame), but the stride widens there (bbox_w goes from 240 to 254), so I treat that drop as a pose effect.
  - Either sign gives a similar size of depth component (about 1 m/s).
- **Focal length:** f = Z24 × H_rest_px(24) / 2.2.
  - The walking bbox height at f24 is 380 px. The largest depth-normalised walking height (in f24 scale) is about 390 px, at f32.
  - I take the rest height as 390–395 px, so f ≈ 3220–3260 px (horizontal FOV ≈ 39°).
  - With this model the m/px at f48 is about 2.2/(rest px height at f48), so it depends only weakly on f.
- **Image motion at f48:**
  - Template track: (13.5, 7.5) px/frame from f47 to f48, and (14.0, 7.75) averaged over f46–50.
  - Heuristic pelvis from the record: (13.2, 7.1) from f47 to f48.
- **Calculation:** I back-projected the f47 and f48 points with their depths and took the 3D norm × 24 (`speed.py`).

## Results (speed.py)
- With H_rest 390–395 px and dlnZ 0.0022–0.0028 per frame, the four point sources give **1.93–2.17 m/s**, centred near 2.05.
- With no depth motion the result would be 1.81–1.99 m/s. With H_rest = 380 px (the raw f24 bbox) it is 1.99–2.22 m/s.

## Second route / checks
- Two translation sources (the rigid upper-body template and the record's pelvis heuristic) differ by about 4%.
- Two depth-ratio sources (template scale chain and bbox height) agree on f24→f48 to within 0.3%.

## Caveats
- The clip has odd motion: abrupt changes in image velocity at f14, f29 and f60, and a vertical rise and fall from f16 to f60.
- The background is removed, so camera motion could not be checked; the camera is assumed fixed.
- The depth rate is the main uncertainty (about ±7% on the answer). Confidence: moderate.
