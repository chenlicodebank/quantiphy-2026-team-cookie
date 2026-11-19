# q_2295 — distance between the two people (cm)

File fps = question_fps = 24. People stand still during the clip (only arms move), so frame 0 is used.

Method (lab card): f = 0.5959 x 1280 = 762.8 px, principal point (640, 360). Each person's centre = midpoint of the
body (head top to feet, torso centre in x), read from zoomed grid crops (frames/left.png, frames/right.png):
- far (left) person: head top y 173, soles y 575, torso x 345–420 -> centre (382, 374), depth 3.130 m
- near (right) person: cap top y 98, feet ~y 715, hips x 923–1043 -> centre (983, 406), depth 2.002 m
Back-projection ray-normalised x depth (depth = Euclidean distance to centre):
- far  = (-1.003, 0.054, 2.965) m, near = (0.820, 0.110, 1.823) m -> distance 2.151 m.

Second route / sensitivity: using hip points instead (382,360)/(983,440) -> 216.0 cm; chest points -> 215.4 cm.
The answer is insensitive to the vertical choice of centre (dominated by the lateral 1.82 m and depth 1.14 m
separation). The prior (gravity) is not needed; the scale comes from depth_info + fixed focal length.
Consistency: soccer ball (2.80 m) is held in front of the far person (3.13 m), plausible.

Answer: 215 cm. Confidence: good (~±5%, main uncertainty is where the annotator clicked the person centre).
