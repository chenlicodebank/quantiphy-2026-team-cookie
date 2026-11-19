# q3096: diameter of the rolling ball (cm)

The prior is the ball's speed at 0.5 s (frame 15 at 30 fps): 2.94 m/s. The file fps and question_fps are both 30, so there is no re-timing.

**Pixel speed.** Taken from scene/tracks/basketball.csv, using camera-stabilised centres (the camera drift is ≤2 %).
- Forward difference from frame 15 to 16: 2362 px/s.
- Centred over frames 13–17: 2335 px/s.
- Over frames 10–20: 2335 px/s.
- Backward difference from frame 14 to 15: 2321 px/s.
- Used: the mean of the forward and centred values, about 2348 px/s. That gives a scale of 1.252 mm/px.

**Pixel diameter.** I used the blur-free diameter from the record's motion-blurred disk fit: median 225.2 px over frames 13–17. I checked this by eye on a zoomed frame 15 (frames/f15.png): the ball runs from y≈397 to 623, about 226 px.

**Result.** The diameter is 225.2 × 1.252 mm ≈ **28.2 cm**. Depending on the speed route, the range is 28.0–28.4 cm.
- Another reading would use the blurred horizontal extent (~245 px at frame 15). That gives about 30.6 cm, but it includes motion smear, so I did not use it.
- A real basketball is about 24 cm across, so the prior's speed appears somewhat high. I still followed the prior, because it sets the scale.

**Confidence:** moderate to high relative to the prior's convention.
