# simulation_0048: measurement record

This is a 3D Blender render: 1920x766 px, 33 fps, 99 frames (t = frame/33, 0 to 2.97 s). Everything is in pixels:
x points right, y points down, and the origin is the top-left corner of the full frame. No metric scale was assumed.

## Scene
- **Camera: static.** I compared the static left half of frame 0 with every 10th frame. The mean difference is under
  1.4 grey levels and the shift is a constant 0.5 px. That 0.5 px is an artefact of the estimator: it also appears at
  frame 10, where the two frames are nearly identical. No background correction is needed.
- **View.** The camera looks down from above, along a sloping street. The near foreground holds a blurred blue wall
  with a yellow "M" logo, an "O LAB" sign and a grey kiosk. Further back are a pale concrete sidewalk with stoop stairs
  and railings, the curb, an asphalt road that rises to a crest at y≈310, and a tree.
- **Moving objects: two people. Both come toward the camera, roughly parallel to the street.**
  - **walker**: a man in a light grey T-shirt and dark jeans, on the sidewalk. He is the left person at frame 0 and
    moves slowly.
  - **cyclist**: a rider in a dark jacket and blue shirt on a white/silver bicycle, on the road. He is the right person
    at frame 0 and moves fast. He leaves through the bottom edge: his wheel's ground contact reaches the image bottom
    at about frame 61, and his head is last visible at frame 91.
- **Perspective.** Three lines meet within about 2 px at the vanishing point of the street direction, (1771, −177),
  which is above the image:
  - the walker's foot path,
  - the cyclist's wheel-contact path,
  - the right edge of the curb.

  So the camera is pitched down and both people move along the street direction. The horizon is not visible.
- **Apparent size growth:**
  - walker height: 185 px (f0) → 225.5 px (f98), ×1.22;
  - cyclist (rider + bike) height: 178.5 px (f0) → 306 px (f60), ×1.71;
  - width over the same spans: walker 57.5 → 66 px; cyclist 55 → 87 px.

## Files
- `scene.json`: inventory of all objects (how to tell them apart, whether they move, visible frames, static pixel
  extents and positions), camera and perspective cues, and events.
- `tracks/walker.csv` (frames 0–98), with these columns:
  - `ref_x, ref_y`: pelvis proxy, i.e. the torso centre x at the shirt/jeans belt line. `ref_y` is the detected belt
    line smoothed over 5 frames; `ref_y_raw_belt` is the unsmoothed detection.
  - bbox (`x0` = left extreme, `x1` = right extreme incl. hands, `y0` = head top, `y1` = lowest shoe), `height_px`
    (head top to lowest foot), `width_px`, `is_manual_keyframe`, `occlusion`.
- `tracks/cyclist.csv` (frames 0–91), with these columns:
  - `ref_x, ref_y`: pelvis proxy, i.e. the torso centre x at the handlebar-grip line, where the seated hips are. It is
    filled for frames 0–60 only.
  - `chest_x, chest_y`: a template-tracked point on the chest/neck, for frames 0–84. It is a consistent point for
    motion after the hips leave the frame.
  - The offset `ref_y − chest_y` grows with apparent size: 25.5 px at f0, 42 px at f60.
  - bbox from the mask (left/right = elbows or handlebar grips; `y0` = head top; `y1` = front-wheel ground contact,
    or 765 once the contact is cut off), `height_px` (head top to ground contact), `width_px`, `ground_contact_y`
    and its source (manual / fit / below the frame), `mask_area`, `occlusion`.
- `scripts/`: every script used.
  - `bg.py`, `bg2.py`, `bg3.py`: background model.
  - `segment.py`, `segment2.py`: masks.
  - `track_template.py`: torso template tracking.
  - `walker_measure.py`, `cyclist_measure.py`, `build_tracks.py`: the tracks.
  - `write_scene.py`: scene.json.
  - `viz.py`, `viz2.py`, `gridcrops.py`: overlays and gridded crops for checking.
  - Intermediate json/npz files are kept there as well.
  - To stay under the size limit I deleted `bg_crop.npy` and `bg_crop2.npy` (inputs of `bg2.py`/`bg3.py`) and the
    outputs of the first `segment.py` pass. Rerun `bg.py` and then `bg2.py` to regenerate them; `bg_crop3.npy`
    (crop origin x=1380, y=150) is kept.

## How it was measured and how reliable it is
- **Walker extents.** I read them by hand on 2× gridded crops at 15 keyframes (every 7 frames from 0 to 91, plus 98),
  to about ±2 px, and interpolated linearly between keyframes. Head-top and foot values between keyframes are therefore
  smoothed, and the gait oscillation of the lowest foot (a few px) is only partly captured.
  - Automatic background subtraction was not usable for the walker. He moves slowly, so part of the median background
    never shows bare sidewalk, and his cast shadow lies to his left. Those masks (in `seg2.json`) have ±10–25 px of
    junk; do not use them for his extents.
- **Walker ref_x.** It comes from frame-to-frame template tracking of the torso, corrected to the keyframes with a
  linear residual fit (keyframe residuals ≤2 px).
- **Walker ref_y.** It is the strongest light-to-dark step (shirt to jeans) in each frame, ±1–2 px, and agrees with
  the manual belt readings within about 2 px.
- **Walker pelvis.** It is taken at the belt line: assuming a standing pelvis about 0.55 of body height above the feet
  gives a point within about 3 px of it. The true hip joint may be a few px lower.
- **Cyclist mask.** Background subtraction works well here: dark rider on the asphalt and sky, with a clean head top
  (±1 px) and clean left/right extents.
  - The cast shadow at the wheel extends the raw mask bottom 3–12 px too low. Ground contact therefore comes from 10
    manual keyframes (frames 0, 7, 14, …, 56, 60), and is fitted against head top in between (residuals ≤3 px, one of
    6.6 px).
  - From about frame 80 the mask's right side is clipped a few px by the shadow-cleanup window, so the late widths are
    under-estimated.
- **Cyclist handlebar line.** It comes from manual keyframes, fitted against head top (residuals ≤4 px).
- **Cyclist origin.** This is ambiguous: a rider's pelvis versus the bicycle root (which may sit lower, near the
  bottom bracket or at ground level). Use whichever the question implies. The ground-contact point is also recorded.
- **Static extents.** These were read by eye from gridded crops, ±3 px. The kiosk's bottom is outside the frame.

## Ambiguities
- **Occlusion.** No occlusion between the two people. From about frame 86 the walker's left hand reaches the kiosk's
  right edge (x≈1462); at most a few px may be hidden.
- **Faces.** Both faces are blurred into grey patches. Head top means the top of the hair.
- **Shadows.** The sun is from the right, so shadows fall to the left of each person. They are excluded from all
  extents.
- **Leaving the frame.** The cyclist leaves through the bottom edge:
  - from about f61 his lower body is cut off, so his ground contact, height and `ref_y` are left blank;
  - after f84 only his head and shoulders are visible.
- **Events.** There is no start or stop of motion, no contact and no bounce. Both people move toward the camera for
  the whole clip.
