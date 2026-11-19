# Q190 — shark height (prior: boat length = 10 m)

2D side-view simulation at 24 fps; question_fps is also 24, so no re-timing. I used one metres-per-pixel scale taken from the boat prior.

- **Boat length:** measured in `measure.py` as the red-hull column extent once the whole hull is in frame (frames 44–57): 852–854 px. The scene record gives 859 px for stern to bow tip, which includes the bow fitting and stern edge. I used 857 ± 3 px, which gives 10/857 = 0.01167 m/px.
- **Shark height:** the vertical extent of the bounding box, from the dorsal-fin top to the pectoral-fin bottom. I measured it with a background-difference mask against the flat blue panel, every 4th frame. The result is 107–108 px (y 850/851 to 957) and stays constant over the clip. The scene record gives 106 px.
- **Height:** 107.5 × 0.01167 = **1.25 m**.

**Check:** the record's values (106 px / 859 px) give 1.234 m, which is 1.5 % lower. As a sanity check, the shark's length (≈265–274 px) works out to about 3.1–3.2 m, which is plausible for a shark of this height including fins.

**Confidence:** high, within about ±3 %. The main assumption is that the boat and shark panels share one scale, per the 2D convention.
