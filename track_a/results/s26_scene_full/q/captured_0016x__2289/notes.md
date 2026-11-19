# q_2289 – distance between the two people (cm)

Lab video, 24 fps (the file and question_fps match), 1280x720. depth_info is given at t=1.5 s, which is frame 36:
near person 0.843 m, far person 2.372 m.
Method: lab pinhole model with f = 0.5959*1280 = 762.8 px and principal point (640,360). Each person's centre is
back-projected as a unit ray times the given (Euclidean) depth. The answer is the 3D distance between the two points.

Person centres at frame 36 (masks made in dist.py, then checked on frames/f36.png):
- Far person (catcher): mask centroid (1089,185). Her head is cut off at the top, so I took the torso/pelvis centre as about (1085,193-250).
- Near person (thrower): cut off by the left and bottom edges. Mask centroid (150,495); I took the torso centre as about (100-150, 420-520).

Result: across all of these click choices the distance is 213-219 cm, and about 217 cm for the central choice
(near (120,470), far (1085,220)). The result barely depends on the click positions because most of the separation
is in depth (2.372-0.843 = 1.53 m) and the lateral separation is about 1.5 m.
Second-route check: this is a sensitivity sweep over the click positions, which gives a spread of about ±1.5%.
It is not a fully independent second method.
Answer: 217 cm. Confidence: good, but the result relies on depth_info being measured to the person centres.
