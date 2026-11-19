# q_1723: eagle wingspan (m)

File fps = question fps = 24. Scripts: crops.py (bird crops, frames/cycle.png), measure.py (sub-pixel widths and heights at 25 % and 50 % darkness, saved to meas.npy), span.py (geometry).

## Focal length (from the prior)
- Human height at 50 % edge threshold: median 38.4 px over frames 0-64 (90th percentile 39.5; the 25 % threshold gives 40.3). Head clipped in 65-71, so those frames are excluded.
- Human range 139.10 m at pixel (165, 727) -> Z = 137.8 m. With H = 1.75 m: f = 3026 px (3115 if I use the 90th-percentile height). That gives a horizontal FOV of about 20 deg.
- Check: the human walks at 1.13 m/s (plausible).

## Eagle 3D motion
- Back-projected the body centre (ref_x/ref_y) with the given ranges. At t=1 s (frame 24) P = (-12.3, 2.2, 139.1); at t=2 s (frame 48) P = (-3.1, 2.7, 147.1).
- Velocity is (9.2, 0.45, 7.96) m/s, 12.2 m/s in total (a plausible eagle speed). It flies right and away, about 41 deg out of the image plane.
- Check: a straight constant-velocity path predicts a pixel speed of 9.5 / 8.5 / 7.5 px per frame in the three thirds of the clip. Measured: 9.5 / 8.5 / 7.65, so the motion is straight and receding.
- The raised wings show broad blade surfaces rather than edge-on lines (frames 20-28), which also points to an oblique view.

## Wingspan
- Flat-wing peaks of the bird's width at 50 % threshold: frame 5 = 29.0 px, frame 30 = 29.75 px, frame 53 = 27.7 px.
- Projected span = w * Z / f, giving 1.27 / 1.39 / 1.36 m.
- The wing axis is horizontal and perpendicular to the velocity. Its image foreshortening, |w_x - (X/Z) w_z|, is 0.54 / 0.60 / 0.65 for those three frames.
- True span: 2.35 / 2.31 / 2.10 m, mean 2.25 with f = 3026 and about 2.19 with f = 3115.
- Answer: **2.2 m**, which is plausible for an eagle.

## Second route and caveats
- The three flap cycles are independent estimates, at different depths and viewing angles, and they agree within ±6 %.
- If I ignore foreshortening (wings assumed parallel to the image), the span would be about 1.34 m. I reject that because the depth_info clearly shows strong recession and the wing surfaces look oblique.
- Uncertainties:
  - flap peak sampling at 24 fps (the frame-53 peak is probably under-sampled);
  - whether the body heading equals the velocity direction;
  - human pixel height ±1 px (±3 % in f).
- Confidence: moderate.
