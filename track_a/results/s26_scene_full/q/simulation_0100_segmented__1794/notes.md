# q_1794 — shark length (m)

2D planar scene (segmentation render, static camera, constant pixel sizes, both objects side-on). Prior: boat length = 10 m, so one m/px scale.
fps = question_fps = 24, no re-timing issue (sizes do not depend on time anyway).

Method (measure.py): non-white mask (min channel < 225 or saturation > 40), split at y=740 into boat (above) and shark (below);
horizontal extent of columns with >= 3 mask px (drops specks), over frames 22-57 where the boat is fully in frame.
- Boat length (stern hull at x=666 to bow tip at 1521 at frame 57): median 857 px (855-860).
- Shark length (nose to tail tip): median 278 px (274-279).
- Scale 10/857 = 0.01167 m/px -> shark = 3.24 m.

Second route: scene record values (boat 856 px, shark 277.5 px) give 3.24 m, the same; per-frame ratio median 0.3238.
Check on frame 57 image: the boat's leftmost point is the hull stern (rudder and a thin vertical line are inside that extent), the bow tip is the rightmost point.
Confidence: high (about ±1%), assuming the boat's length = its horizontal bbox extent.
