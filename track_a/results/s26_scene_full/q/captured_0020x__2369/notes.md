# q_2369: distance between the two people (cm)

Lab clip, 1280x720, 24 fps (the file and question_fps match). Focal length f = 0.5959*1280 = 762.8 px, principal point (640, 360).
Depths from depth_info: near person 1.580 m, far person 3.237 m. Both people stand still apart from their arms, so time does not matter here.

Method (dist.py): back-project each person's image centre along its ray to the given camera distance, then take the 3D distance between the two points.
- Near person (bottom-left, cut off by the frame edges): candidate centres are the mask centroid (150,464), the torso (140,420), the hip (170,500) and the pelvis (190,520).
- Far person (top-centre, head cut off): candidate centres are the mask centroid (710,115), the pelvis (710,85), the waist (708,70) and the torso (708,40).
- If depth is treated as Euclidean range (the definition given for depth_info), the 16 combinations give 236-248 cm, about 242 cm in the middle.
- If depth is treated as z (the ray (x,y,1) times depth), the results are 242-266 cm, about 252 cm.

Answer: 242 cm. This uses the Euclidean reading with pelvis/hip-like centres.
The second route was varying which point counts as the centre: the answer changes by only about ±3%.
The main uncertainty is whether depth means range or z (about 4%). Confidence: moderate to good.
