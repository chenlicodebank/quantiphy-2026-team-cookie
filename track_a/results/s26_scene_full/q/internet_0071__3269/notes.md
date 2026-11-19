# q_3269 – toilet-paper velocity at 1.00 s (cm/s)

**Time base:** the file runs at 24.098 fps and the question at 30 fps. The clip has 60 frames, which is exactly 2.00 s at 30 fps, so the frames look like the original 30 fps footage re-timed for playback. I used 30 fps: t = 1.00 s is frame 30, and velocity = px/frame × 30.

**Scale:** I took the prior "width = 10 cm" to mean the roll's axial length (end to end, horizontal, along the motion direction). The diameter is about 698 px against an axial length of about 585–600 px, a ratio of 1.19. That fits a standard roll (10 cm wide, about 12 cm across), so the reading is consistent. Width ≈ 590 px (585 at rest, 588–600 face-on around frames 20–31), giving 10/590 = 0.01695 cm/px. The camera is static (per the scene record).

**Motion at frame 30** (one scale for everything, planar):
- Record's left-edge x: 29→30 = −20.7 px, 30→31 = −20.1 px. Its centre (cx) gives 30→31 = −19.3 px.
- My own template match of the upper roll at full resolution (`measure.py`, score 0.99): 29→30 = −20.3 px, 30→31 = −20.6 px (dy ≈ −1). Frames 31–33 give −20.4 and −20.3 px.
- Speed ≈ 20.4 px/frame × 30 = 612 px/s.
- 612 × 10/590 = **10.4 cm/s**. The range is 10.2–10.5 for widths of 600–585 px.

**Check:** two independent position measures (the record's edge fit and my template match) agree within about 3%.

**Alternative:** if the file's 24.1 fps were the right base, frame 24 would apply at about 15 px/frame, giving about 6 cm/s. I rejected this because 60 frames at 30 fps is exactly 2.00 s.

**Confidence:** medium-high on the measurement. The main risk is the choice of time base.
