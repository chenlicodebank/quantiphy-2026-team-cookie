# q_713 — length of the swimming ring (m)

Prior: black cat (the black animal on the deck; scene/ calls it "dog") speed = 1.041 m/s. 2D top-down scene, static camera, fps 24 (= question_fps).

## Scale from the cat's speed
- dog.py: my own mask (V<45, largest component in y 530-615) over all 50 frames.
  Centroid net displacement / 49 frames = 5.454 px/frame; linear-fit slope 5.457 (centroid), 5.462 (nose tip).
  scene/tracks/dog.csv agrees: cx 5.453, body_cx 5.449, body_x1 5.452 px/frame.
  Mean of per-frame centroid steps is 5.48 (inflated slightly by gait jitter); the motion is constant, so I use 5.455 px/frame.
- 5.455 px/frame x 24 = 130.9 px/s -> scale = 1.041 / 130.9 = 0.00795 m/px.

## Ring size
- measure.py: ring mask R>50 on dark water, every frame. x extent median 145 px (143-151; frames with spray pixels give the high values), y extent 134 px (133-135).
- The x extent includes the short tube/handle tip sticking out ~10 px past the torus on the right (column profile tapers out to x=1005). The world AABB includes it, so length = the longer horizontal extent = 145 px.
- Length = 145 x 0.00795 = 1.153 m. (Other reading: torus only/the y extent of 134 px = 1.07 m. Width (shorter extent) = 1.07 m.)

## Check
Nose-tip track and centroid track give the same px speed (within 0.1%), so the scale is solid. Deck tiles (144.6 px pitch) come out at 1.15 m, which is plausible. The ring sits on the water slightly lower than the deck, so there may be a small depth difference that can't be measured; I treat both as one plane.
Confidence: fairly high, about ±4%.
