# q_3273: credit card velocity at 1.00 s (cm/s)

**Prior:** the card is 8.56 cm long. This is a 2D internet video and the camera is static (see scene/notes.md), so one planar scale applies.

**Scale:** the card's long side in pixels is 421 px at frame 27, about 425 px at frame 30 and 432 px at rest (mask and grid crop agree). I used 428 px, so the scale is 8.56/428 = 0.0200 cm/px.

**Time base:** the file runs at 26.85 fps and the question states 30 fps. A file rate that odd suggests the clip was re-timed from 30 fps footage, and the reference follows the original footage. So I used 30 fps, which puts t = 1.00 s at frame 30. A hand-moved card gives no physical check on the rate.

**Track:** I template-matched the card face (chip, text and digits, avoiding the thumb) in `track_tm.py`, with sub-pixel peaks. It agrees with the mask centroids in scene/tracks/card.csv to within about 1 px. Per-frame steps near frame 30:
- 28→29: 11.4 px
- 29→30: 13.6 px
- 30→31: 12.2 px
- 31→32: 8.1 px

**Velocity:**
- Forward difference at frame 30: 12.2 px/frame. A linear fit over frames 28–32 gives 11.2, and the central difference gives 12.9. I took about 12.0 px/frame.
- 12.0 px/frame × 30 fps = 360 px/s.
- 360 px/s × 0.0200 cm/px ≈ **7.2 cm/s**.

**Second route:** the mask centroid track in card.csv gives steps of 11.4, 13.3 and 11.2 px around frame 30, which is consistent.

**Alternative reading:** at the file rate (26.85 fps), t = 1.00 s is frame 27. The forward difference there gives about 6.5 cm/s and a smoothed value gives about 8 cm/s.

**Confidence:** moderate. The main uncertainty is the time base.
