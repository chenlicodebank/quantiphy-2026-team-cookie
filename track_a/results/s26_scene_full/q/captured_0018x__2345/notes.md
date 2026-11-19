# q 2345 — distance box ↔ pineapple toy (yellow plush) at 3.0 s, in cm

**Time:** At question_fps 24, 3.0 s is frame 72. The clip only has frames 0–48 (it ends at 2.04 s). The file rate is also 24 fps.
- By frame 48 the box is lying flat on the floor and has nearly stopped. The plush is still rocking slowly on the floor.
- So I used the frame-48 positions as the 3.0 s state. **This is the main uncertainty:** the plush may move further after the clip ends.

**Objects:** "Pineapple toy" is the yellow plush with green leaves (scene/ calls it yellow_plush). The box is white_box. The scene/ tracks were checked on the frames and are correct.

**Depth:** depth_info gives no distance for the box or the plush, so I estimated their depths.
- I used a floor-row model, Z = K / (v_floor − 360), with f = 763 px.
- K was calibrated from four references (script `measure.py`), giving K = 583–644, mean 617:
  - soccer-ball floor contact, using d = 2.80;
  - far person's feet, using d = 3.13;
  - near person's feet, using d = 2.002;
  - tennis-ball size (6.7 cm across 20.5 px) with its floor row of 616.
- **Box at frame 48:** centre (418.5, 594), floor row about 607. This gives Z = 2.50 m (Euclidean distance 2.71 m).
  - Check: the box's short side is 28.6 px at frame 48 and 26 px when held at frame 0, at about the ball's depth. That implies Z ≈ 2.45, which agrees.
- **Plush at frame 48:** centre (846.5, 596), bottom 617.
  - The floor-row model gives Z = 2.40.
  - The plush's width shrinks from 30 px while falling (Z 1.81) to about 24.5 px. That gives Z = 2.22.
  - I used the mean, Z = 2.31 (Euclidean 2.50). After its bounce the plush moved away from the camera, from Z 1.8 to 2.3.

**Distance:**
- Back-projecting with the ray × Z (true pinhole): 1.365 m.
- Back-projecting with the method card's ray × Euclidean distance: 1.480 m.

**Answer:** 144 cm, between the two conventions and within about 5% of both. Confidence is moderate: the depths are estimates and the plush's position at 3.0 s is extrapolated from the last frame.
