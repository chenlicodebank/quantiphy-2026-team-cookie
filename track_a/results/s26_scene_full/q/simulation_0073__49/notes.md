# Q49: length of the white car (van), in metres

The prior is the bicycle's speed, 5.33 m/s. The scene is a 2D top-down view with a static camera. The file and the
question both run at 24 fps, so no re-timing was needed.

## Scale (measure.py)
- I tracked the cyclist by template matching (frame-30 patch, sub-pixel parabola fit) over frames 0–71.
- The motion has constant velocity from frame 1→2 onwards. The per-frame steps are 8.44–9.64 px. The linear-fit slope
  is 8.980 px/frame, and the mean and median steps are 8.969 and 8.968 px. The scene record's value (about 8.9) agrees.
- 8.980 px/frame × 24 = 215.5 px/s, so the scale is 5.33 / 215.5 = 0.02473 m/px.

## Van length (vanlen3.py, vanlen2.py)
- I took a difference image against frame 71, which is clean in the lower half, and read the row profile of the van at
  frame 0, when it is at rest with no motion blur.
- Front edge: the dark outline of the front bumper starts at about y 800. The grey bumper sits at rows 804–810, and the
  white body starts at row 811. Rows 785–799 are only a soft shadow gradient (difference below 22), so I excluded them.
- Rear edge: the half-max point is at about y 1046.5.
- The length is about 247 px. Cross-checks:
  - frame 5 gives 796→1042 (247 px);
  - frame 10 gives about 247 px;
  - the scene record's median bbox height is 245 px (range 242–249).
- Later frames are motion-blurred: frames 20–60 show 233–237 px at a stricter threshold and 252–262 px with the blur
  and shadow included. I did not use them.
- 247 px × 0.02473 m/px = **6.11 m**.

## Check
- An independent route gives the same result: the record's 245 px length with the record's 8.9 px/frame speed gives
  245 × 5.33 / 213.6 = 6.11 m.
- The uncertainty is ±3 px in length (about 1%) and about 0.5% in the scale. A van of about 6 m is plausible.
- Confidence: good. The main residual risk is how the reference bounding box treats the bumper and mirrors.
