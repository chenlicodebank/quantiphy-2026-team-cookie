# q3277: height of the red package (internet_0073), prior: belt velocity 0.3 m/s

## Method (internet convention: one planar scale taken from the prior)
- **Belt pixel speed** (`measure.py`): I fitted lines to the camera-compensated `cx_bg` tracks in scene/tracks over
  frames 0-137 for the rigid parcels. Slopes in px/frame: white_pouch_left 2.003, white_box 2.003, cardboard_box
  1.967, red_parcel 1.961, flat_white_pouch 2.011, grey_pouch 1.942 and blue_bag 1.928. The mean is **1.97 px/frame**
  with a spread of about ±2%. Vertical motion is about 0.
- **Red package pixel height** (`edges.py`): I took the vertical brightness and redness profiles over the central
  50 columns of the parcel. The top edge is the dark-to-bright step at y≈351-353, and the bottom edge is the dark
  contact line just above the belt at y≈397-400. Heights at frames 0, 20, 40, 60, 80, 100, 120 and 137 were 48, 47.5,
  47.5, 46.5, 47, 47, 47 and 47.5 px, so I used **47 px**. The scene record's hand-read value is 48 px, which agrees.
  The redness-only mask (`measure.py`) gives 38-40 px, because it misses the pale top rim and the darker bottom band,
  so I did not use it.
- **Time base**: the file is 25.11 fps with uniform timestamps, and question_fps is 30.
  - The frame steps are uniform (about 2 px/frame, sd 0.3-0.4). There is only one double step, at frame 53→54. A
    30→25 fps conversion that dropped frames would show a double step about every 6 frames, so the frames were not
    resampled. They are consecutive original frames.
  - The difference is therefore a timestamp re-timing. I followed the stated question rate, **30 fps**.
  - Both rates give plausible parcel sizes, so plausibility does not decide between them.
- Scale = 0.3 / (1.97 × 30) = 5.08 mm/px. Height = 47 × 5.08 mm = **0.239 m → 0.24 m**.

## Checks
- **Second route:** the height measured on 8 frames spread over the whole clip ranges from 46.5 to 48 px. The scale
  derived from the red parcel's own speed alone (1.961 px/frame) gives 0.240 m.
- **Alternative time base:** if 25.11 fps were the true rate, the height would be 47 × 0.3 / (1.97 × 25.11) = 0.285 m.

## Confidence
Moderate. The pixel measurements are good to about ±3%. The main risk is which time base the reference answers used.
