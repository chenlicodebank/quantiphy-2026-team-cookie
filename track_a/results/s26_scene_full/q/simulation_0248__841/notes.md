# Q841: height of the rabbit (m). Prior: the speed of the horse at the back is 0.874 m/s

Time base: the file and the question both use 24 fps, so no re-timing.

**Which horse.** All three animals move to the right. The "horse at the back" is the red/chestnut horse: it is the trailing (leftmost) one, and its hooves sit at row ~630, against 634 for the dun horse, so it is also slightly farther from the camera.

**Scale (2D).** The red horse moves steadily over frames 0-48. Frame 49 is a loop reset, so I left it out.
- Mean step of the torso centroid: 77.2 px/s. The full-mask centroid gives 75.7 px/s.
- I used 77 px/s, which gives 0.874 / 77 = 0.01135 m/px.

**Rabbit height in pixels.** I checked it in code with chroma masks (`measure.py`) and with zoomed crops of frames 10 and 15 (`zoom.py`, `frames/z*.png`).
- The height changes with its hopping gait. Stretched with ears up (frame 10), it spans ~598 to 637, about 39-40 px. Crouched (frame 15), it spans ~606 to 635, about 30 px.
- The record's mask heights run 31-42 px (median 37). They are about 1-2 px larger than what the crops show.
- My own tight chroma mask gives a median of 32 px.
- I took 38.5 px as the representative height: the near-upright pose, which is likely the rest pose.
- 38.5 px × 0.01135 m/px = 0.437 m.

**Perspective correction.** The rabbit's feet sit at row ~637 and the red horse's hooves at ~630, so the rabbit is slightly closer to the camera.
- If the horizon were at the image centre (row 540), the rabbit's m/px would be 90/97 = 0.93 of the horse's. A camera tilted down would make that ratio closer to 1.
- I applied a factor of about 0.95, which gives about 0.415 m.

**Answer: 0.42 m.**

**Cross-check.** The red horse's height comes out at 170 px × 0.01135 = 1.93 m, ear tip to hoof. That is plausible for a horse model, so the scale is sane. A rabbit of 0.42 m (ears included) is large but plausible for a rendered model.

**Confidence: moderate.**
- The scale is solid, to about 3%.
- The main uncertainty is which pose or frame defines "height": crouched ~0.33 m, upright ~0.44 m.
