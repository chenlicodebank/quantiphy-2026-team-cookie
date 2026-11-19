# q_2479 – max height of ping pong ball (cm)

File fps = question fps = 24. Frames: t=1.0 -> 24 (falling), t=1.1 -> 26 (first bounce on tabletop), t=1.3 -> 31 (apex).
Reading: max height = vertical rise of the ball centre from the first bounce (frame 26) to the apex (frame 31),
i.e. the bounce height above the table contact. Same value for centre or bottom of the ball.

Method (measure.py): threshold the ball blob in a local window.
- Apex frame 31: top edge 293, width 21 px -> centre (748, 303.5). Frame 32: (750, 301.5) (1-2 px higher).
- Bounce frame 26: vertical streak 389-420, width 18 px. Centre at contact = bottom - r ≈ 410.5; streak midpoint 405.
Back-projection with f = 763 px, principal point (640, 360), depth_info taken as Euclidean distance along the ray:
- apex: Z = 1.394 m, Y = -0.103 m (frame 32: -0.107)
- bounce: Z = 1.541 m, Y = +0.102 m (contact centre) / +0.091 m (streak midpoint)
Height = 0.205 m (contact centre) or 0.194 m (streak midpoint); frame-32 apex adds ~0.4 cm.
Answer 20.0 cm (middle of these readings).

Check: apparent widths are consistent with the depths (21 px at apex -> 1.45 m vs given 1.41; ~18 px at bounce -> 1.70 m
vs given 1.56). Camera tilt is unknown and ignored (a few degrees would change the result by ~1 cm because the ball
moves ~0.15 m toward the camera between bounce and apex). Confidence: moderate (±10 %).
