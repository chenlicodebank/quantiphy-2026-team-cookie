# q_2982: average speed of the canoe (m/s). Prior: the boatman is 1.75 m tall

**Method** (internet-video convention: one scale from the prior, planar, no perspective correction). The script is `measure.py`; `view.py` and `view2.py` make the zoomed crops in frames/.
- **Boatman height in pixels.** The boatman stands on the low stern deck at the left end of the boat, and his feet are at the top of that deck. Per frame I measured from the top of the head (topmost foreground pixel in the columns from stern+18 to stern+38) down to the top of the stern deck (median top row over the columns from stern+3 to stern+15).
  - Median 38 px, mean 36.6 px. The low values come from frames where he bends or the segmentation drops pixels.
  - Upright frames give 37–39 px, and I checked this by eye on the zoomed crops at frames 0 and 150 (about 38 px and 36 px).
  - I used H = 37.5 px, so the scale is 1.75 / 37.5 = 0.0467 m/px.
- **Boat motion in pixels.** The boat moves steadily to the right across the whole clip. I measured it over all 305 frames, T = 304 / 29.97 = 10.14 s:
  - stern end: +156 px, 15.4 px/s
  - bow tip: +153 px, 15.1 px/s
  - centroid of the lower hull band: +150 px, 14.75 px/s
  - Linear fits give 14.9–15.7 px/s. I took the mean of the three net rates, 15.07 px/s. With forward differences, the average speed is the net path divided by T, because the motion is monotonic.
- **Answer.** 15.07 × 0.0467 = 0.703 m/s, so **≈ 0.70 m/s**.

**Second-route check.** The three reference points (stern, bow, hull centroid) agree to within ±2%. Using 38 px or 37 px for the height gives 0.694 or 0.713 m/s. As a sanity check, the boat comes out at 234 px × 0.0467 ≈ 10.9 m, which is plausible for a long wooden riverboat.

**Time base.** question_fps (30) and the file rate (29.97) differ by only 0.1%, which is negligible.

**Caveats.**
- The background is white, so I cannot check for camera panning. The image motion is taken as the true motion.
- Confidence is moderate. Most of the uncertainty comes from the boatman's pixel height (±1.5 px is about ±4%).
