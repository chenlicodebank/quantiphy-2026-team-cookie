# q_2970 — speed of the right hand's (middle) fingertip at t = 0.4 s, in cm/s

Clip: 34 frames, file fps 30.0003, question_fps 30 -> t = 0.4 s is frame 12. 2D top-down view, camera static (scene/ record
confirmed: static objects' centroids std < 1 px). Frames 3, 9, 15, 21, 27, 33 repeat the previous frame (25->30 pulldown);
the 12->13 step is a real step.

## Scale (main uncertainty)
The prior's object, a credit card (5.4 cm), is **not present** in the segmented video. The background was replaced, so the card
was probably on the desk in the original. SAM 3 finds no "credit card" on frame 12, and zoomed crops show no card (the left hand
pinches a small dark object, not a card). So the card's pixel width can't be measured. As a substitute I used the keyboard
on the same desk plane. It is an Apple Wireless Keyboard (A1314, aluminium with battery tube), 27.9 x 13.0 cm. Its measured footprint
ratio of 2.18 matches that model's ratio of 2.15 and not the Magic Keyboard's 2.42.
- Keyboard footprint (kb.py, minAreaRect): SAM 3 mask 362.4-363.5 x 165.3-167.4 px; my grey-pixel mask 362.5-363.6 x 166.2-168.0 px
  (frames 0, 12, 18). The two agree to within 1 %, and both agree with the scene/ record (363 x 167).
- Scale: 27.9/363 = 0.0769 cm/px, 13.0/166.5 = 0.0781 cm/px; I use 0.0773 cm/px. At this scale a credit card would be about 70 px wide.
- Sanity check: the middle finger is about 26 px wide = 2.0 cm, which is plausible.

## Fingertip motion
- Right hand palm down with the thumb hidden. Two fingers are extended: A at x≈955 on frame 12 (index) and B at x≈990
  (middle, taken as the asked finger). Ring and pinky are curled at the right.
- SAM 3 masks (sam_tips.py; box prompts from SAM 3 tracks tracks/finger_0.csv and tracks/index_finger_0.csv; frame 14 of the
  finger_0 track glitched, so I re-prompted that frame). Tip = centroid of the mask's top 10 px:
  - B: f11 (1003.8,334.6), f12 (987.5,317.4), f13 (980.6,307.4), f14 (972.1,302.4)
  - A: f11 (976.4,323.6), f12 (954.7,308.8), f13 (945.6,299.9)
- My own skin-colour tracker (tips.py) loses the pale nail of finger B: its tip is about 10 px low, (983,322) vs SAM's top at y=311
  on frame 12. On the zoomed crop (crops.py -> frames/crops.png) the nail tip is at y≈311-313, so SAM is right.
  For finger A, which has no nail problem, my tracker agrees with SAM: the 11->12 step is 27 px (SAM 26.3) and the 12->13 step
  is 12.7 px (SAM 12.7).
- Per-frame tip steps for B: 10->11 30.7 px, 11->12 23.7 px, 12->13 12.1 px, 13->14 9.9 px. The finger is decelerating
  towards its farthest reach at frames 14-19.

## Speed at frame 12 (forward difference, the internet-video convention)
- B (middle) tip: 12.1 px/frame x 30 = 363 px/s. Finger A tip: 12.7 px/frame, mask centroids 10.6-15.8 px/frame.
  I use 12.2 px/frame = 366 px/s.
- 366 px/s x 0.0773 cm/px = **28.3 cm/s**.
- Other readings of "speed at 0.4 s": backward difference (11->12) 23.7 px/frame gives about 55 cm/s; central difference
  about 41.5 cm/s. The forward difference was used because the stated convention for internet videos uses it.

## Second route
Finger A's tip and both mask centroids give 10.6-15.8 px/frame, i.e. 25-37 cm/s. They are consistent with B's tip.

## Confidence
Low to medium. The scale is a substitute: the prior's credit card is missing from the video, so the scale comes from the
keyboard model, which is probably within about 5 %. The finite-difference convention can change the answer by up to a factor of 2.
