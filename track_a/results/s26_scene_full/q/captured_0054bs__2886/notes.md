# q 2886: velocity of the green ball at 1.5 s (frame 36, question_fps 24, the same as the file's fps)

## Identification
- The green ball is the yellow-green tennis ball (`yellow_object` in scene/). The white ball is `grey_object`.
- Check with f = 763 px: at frame 24 (t = 1.0 s, distance 1.331 m, Z = 1.223 m) the green ball's blur-invariant diameter is 40.3 px, which gives D = 6.5 cm. That is a tennis ball, so the given depth is consistent.
- The orange depth at t = 1.0 s (1.81 m) is inconsistent with its apparent size. The 0.5 s value (2.24 m) is consistent with a 22 cm ball, and so is the soccer ball's 3.254 m at t = 2.0 s (22 cm).

## Measurements (scripts in this folder)
- `measure2.py`: background-difference and yellow mask → centroid per frame.
- `sigma.py`: blur-invariant diameter = 4 × σ across the motion direction. Motion blur preserves the chord profile across the motion.
- `fit2.py` / `fit3.py`: a pinhole projectile fit with g = 9.81 m/s² in a fitted direction and the depth at frame 24 fixed by depth_info.
  - Frames 35→36 contain a dropped source frame. The fit strongly prefers this: rms 1.85 px with the drop against 4.6 px without it.
  - With the depth left free, the fit returns 1.44 m (given: 1.33 m) and a ball diameter of 6.7 cm. This is an independent check of the scale.
- The bounce (floor) falls just after frame 37, at effective frame about 38.1.
- Depth Z from the model at frames 34–39: 2.21, 2.36, 2.70, 2.88, 2.85, 2.80 m. Depth from the measured size: 2.32, 2.43, 2.84, (2.39), 2.98, 2.92 m. These agree before the bounce.
- `orange.py`: a convention test on the prior.
  - Orange speed at frame 12 with depth anchored to 2.24 m: the clean forward difference gives 1.85 m/s.
  - A centred 5-frame window of forward differences, which includes the dropped-frame step 11→12, gives 2.14–2.26 m/s, matching the prior of 2.21.
  - So the reference seems to smooth over a centred window that includes anomalous steps.

## Candidate values at frame 36 (`variants.py`)
- Physical speed just before the bounce (model, instantaneous): about 5.4 m/s. A single forward difference 36→37 gives 5.3 m/s.
- Mean scalar speed over a 5-frame window: 5.25 m/s (model depth).
- Savitzky–Golay smoothing over 5 frames: about 5.2–5.3 m/s. Over 7 frames: about 4.1–4.4 m/s.
- Mean velocity vector over 5 frames (34..38): about 3.4 m/s. Over 7 frames: 2.9 m/s. These are reduced because the bounce reverses the vertical motion inside the window.
- The backward difference including the dropped frame: about 10 m/s. Not used.

## Answer
- **4.4 m/s.** This is a compromise between the window-smoothed vector (about 3.4) and the physical or forward-difference speed (about 5.3). It is close to the 7-frame Savitzky–Golay value.
- Confidence: moderate-low. The value depends on how the reference smoothed across the bounce at frame ~37 and the dropped frame at 35/36. The physical speed (about 5.4) is the better-determined quantity.
