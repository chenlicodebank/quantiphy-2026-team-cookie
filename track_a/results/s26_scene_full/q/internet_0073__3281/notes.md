# Q3281: displacement of the blue bag between 2.00 s and 3.50 s (prior: belt velocity 0.3 m/s)

- Time base: question_fps = 30, so the interval is frame 60 to frame 105 (45 frames). The file runs at 25.11 fps;
  the frame indices are used as given, following the benchmark convention.
- Frame 50 (t = 2.0 s at the file's fps) shows the blue bag lying on the belt at x~810-960, y~360-405. Like the
  other parcels, it rides the belt to the right.
- The tracks come from scene/tracks, in camera-drift-corrected background coordinates (`cx_bg`, `cy_bg`). I
  checked them with m.py:
  - The blue bag moves (88.06, -0.47) px from frame 60 to frame 105, so |d| = 88.06 px. That is 1.957 px/frame,
    and the line fit over frames 20-125 gives 1.916.
  - The belt's pixel speed is the mean of the parcels' fitted vx (white_pouch_left, white_box, grey_pouch,
    flat_white_pouch, red_parcel, cardboard_box, brown_box and blue_bag), about 1.978 px/frame. At 30 fps that is
    59.3 px/s.
- Scale: 0.3 / 59.3 = 0.00506 m/px.
- Displacement: 88.06 px x 0.00506 = 0.445 m.
- Second route: the bag rides the belt at constant speed, so the displacement is 0.3 m/s x 1.5 s = 0.45 m.
  Measuring the belt from individual parcels, the result ranges from about 0.44 to 0.45 m.
- If the 25.11 fps file rate were used for the velocity instead, the answer would be about 0.53 m. I rejected that
  reading because the convention times everything by question_fps.
- Answer: 0.445 m. Confidence: high.
