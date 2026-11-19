# q_2285: distance between the two people (cm)

- The lab video and question_fps are both 24 fps. t = 1.5 s is frame 36. Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
- depth_info at t = 1.5 s: near person (the thrower) 0.843 m, far person (the catcher) 2.372 m. The prior (gravity) does not set the scale; the depths do.
- Centres at frame 36: the scene/ record's mask centroids, thrower (142.3, 510.1) and catcher (1085.8, 192.9). I checked these on frame 36 (frames/f36.png). The thrower is mostly outside the frame, so its centre is the centroid of its visible torso. The catcher's head is cut at y = 0, so its centroid is mid-torso.
- Back-projection: P = unit ray(u, v) x depth. With the centroids the distance is 217.3 cm.
- Second route (sensitivity), in dist.py: I tried 5 plausible click points per person (the torso, hip and visible-centre variants). That gave 25 combinations, with a range of 211.7-221.5 cm and a median of 216.5 cm. The result is dominated by the depth difference (1.53 m) and the lateral separation, so it hardly depends on the exact click.
- Answer: 216 cm. Confidence: good (about ±3%), with the main uncertainty being where the annotator clicked each person's "centre".
