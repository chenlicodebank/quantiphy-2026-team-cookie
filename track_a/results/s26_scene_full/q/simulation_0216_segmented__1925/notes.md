# Q1925: black cat length including the tail (m)

- This is a 2D side-on walk with a static camera, at 24 fps (file rate and question_fps are the same). Prior: the cat's speed is 0.94 m/s.
- Pixel speed comes from scene/tracks/cat.csv, from linear fits over all 50 frames: cx 17.65, dark_cx 17.80, bbox_x0 17.66 and
  bbox_x1 17.46 px/frame. I took about 17.7 px/frame, which is 425 px/s, giving a scale of 0.94/425 = 0.00221 m/px.
- Length is the horizontal bounding-box extent, from the tail or hind paw to the nose.
  - Frames 0–9, where the cat is on a clean background, give 300–307 px.
  - The median over all frames is 294.5 px, but later frames can miss up to about 20 px of grey muzzle against the console.
  - I checked the mask by eye on frame 0: it runs from about x 226 (hind paw and tail) to x 528 (nose).
  - Adopted value: about 298 px, which gives 298 × 0.00221 = 0.66 m.
- Second route: using the clean frames only (303 px) gives 0.67 m. Using the overall median gives 0.65 m.
- Confidence: moderate. If the reference used the rest-pose mesh with the tail stretched out, its value would be larger.
- The command for my own scripts and the zoom crops was refused. The only crop I could make was frame 0, so everything
  else here comes from the existing track record.
