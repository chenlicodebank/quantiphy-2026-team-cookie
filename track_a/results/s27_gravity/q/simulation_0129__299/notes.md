# q_299 – forklift length (m)

Prior: g = 9.8 m/s^2 (red ball falling). depth_info: none. 2D-style render, static camera, 24 fps (file fps = question fps).

## Scale from the ball (ball.py)
Red-blob centroid per frame, quadratic fit of y(frame):
- frames 2–38: a = 515.8 px/s^2 (rms 0.35 px) -> 0.01900 m/px
- frames 15–38: 514.2; frames 4–36: 517.5; frames 2–20: 499.9 (short baseline, less reliable)
- record (scene/): 519 px/s^2. Adopted ~516 px/s^2 -> 0.0190 m/px.

## Forklift pixel length (fklen.py, orange paint + forks, rows 840–932)
Frame 0: 256 px (near left edge, sees part of rear face), f10: 254, f20: 254, f30: 252, f39: 251 (near image centre).
The side-on length is taken as ~251 px (least off-axis view).

## Depth check
The forklift tyres touch the floor at y≈928, just in front of the facade kerb (y≈910–925), and it casts a shadow on
the glass wall ~45 px ahead of itself, so it is close to the wall plane. The ball passes behind the mast at frame 39, so
the ball lies between the forklift and the wall: both at nearly the same depth, a single m/px scale applies.
Floor-line perspective (horizon ≈ y 540) allows the forklift to be at most ~5 % closer than the wall.

## Answer
251 px × 0.0190 m/px ≈ 4.77 m; allowing a slightly nearer forklift (≤5 %) -> 4.55–4.77. Answer 4.7 m.

Plausibility: under this scale the forklift is ~3.9 m tall, about 1.8x a real 2.5-t forklift, while the building (storey
~4.5 m, door ~2.9 × 3.1 m, pillar pitch 8.3 m) is realistic, and the floor/shadow evidence puts the forklift next to the wall,
so the forklift asset itself appears scaled up in the scene. I kept the gravity scale. If the forklift were real size, the
answer would be ~2.5 m (body only). Confidence: moderate.
