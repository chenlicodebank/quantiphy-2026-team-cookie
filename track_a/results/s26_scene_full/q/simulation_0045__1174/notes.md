# q_1174 — average speed of the walking person (m/s)

Prior: bike speed 4.87 m/s. depth_info: bike 12.1238 m (t=1), 16.9027 m (t=2); human 17.1691 m (t=1), 18.3768 m (t=2).
question_fps = file fps = 33. The pedestrian (white T-shirt, right sidewalk) walks straight away from the camera at a
steady pace through the whole clip, so the average speed ≈ the steady walking speed.

## Checks
- Bike: depth ratio 16.90/12.12 = 1.394. A homography fit of the bike's image track (u,v = (a+bt)/(1+ct)) gives a Z ratio
  of 1.385–1.396, so it agrees. f is only weakly set by the bike speed: requiring a 4.87 m displacement between t=1 and t=2
  gives f ≈ 1430 (rider pelvis point) to 1970 (wheel contact). I used f ≈ 2000 with the principal point at the image centre.
- Pedestrian: image cues give Z(2)/Z(1) ≈ 1.11–1.12 (smooth height 1.122, x-convergence to the VP 1.11–1.12, feet row
  matching 1.109), but the given distances give 1.070. The pedestrian's feet at t=1 sit on the same image row as the
  bike's wheel contact at about t=0.95, so visually the body is at about Z≈12 m, not 17 m. The human depth_info seems to point
  to an origin that is offset from the visible body. A constant offset does not change the speed.

## Routes
1. depth_info back-projection (rider ref point, pedestrian pelvis ref, t=1→2): 1.43 at f=1434, 1.37 at f=1710, 1.33 at
   f=1970. Along the street direction (VP) instead: 1.26–1.30.
2. Ground-row matching (rowmatch.py): the bike's wheel-contact row→Z relation (Z from bike depth_info, constant speed)
   applied to the pedestrian's lowest-foot row in every frame. Linear fit dZ/dt = 1.277 m/s, divided by cos(direction to VP)
   0.976 gives 1.31 m/s. Scaling by the bike check (route gives 4.82 vs 4.87) gives about 1.32. Leaving out the curb height
   (~4%) and the wheel/origin offset adds ±5%.
3. Rate × depth: dlnZ/dt ≈ 0.103–0.115 per s × Z(1.5) ≈ 11.4–12.4 m gives 1.2–1.4.
The routes give about 1.26–1.43, centred at about 1.32–1.34. Answer: 1.33 m/s (a normal walking pace; a step every ~0.52 s
means steps of about 0.7 m).

Confidence: moderate (about ±7%). The main uncertainty is the mismatch between the human depth_info and the image.
Scripts: solve.py, fit_c.py, ground.py, rowmatch.py.
