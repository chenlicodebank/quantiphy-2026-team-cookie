# q_2806: distance between the trashbin and the basketball (m)

The file runs at 24 fps and question_fps is also 24. I measured at t=1.0 s, which is frame 24. Both objects are static.

## Method
I used the lab camera: f = 0.5959 x 1280 = 762.8 px, principal point (640,360). Each centre was back-projected along
its unit ray and scaled by the depth_info distance, which is the Euclidean distance to the camera centre.
- **Basketball** (`measure.py`): green-screen mask, then a least-squares circle fitted to the edge. Centre (801.5, 671.1),
  diameter 94 px. This agrees with scene/ (801.7, 671.9). Depth is 1.9365 m.
- **Bin:** the scene/ bbox (676-773, 486-589) and my component bbox both take in the person's hand above the rim.
  On a zoomed crop the bin itself spans x 680-775, y 484-591, so its centre is (728, 537.5). Depth is 2.977 m.
- **3D distance** (`dist.py`): 1.1235 m.

## Checks
- **Sizes:** the basketball diameter comes out at 94 x 1.9365 / 762.8 = 0.239 m, a regulation ball (0.24 m). The bin
  comes out at 0.37 m wide x 0.42 m tall, which is plausible. This confirms the focal length and depths.
- **Sensitivity:** moving the bin centre to the scene/ value (729, 533.7) or to (726, 540) gives 1.122-1.128 m.
  Most of the distance comes from the depth difference (1.04 m).
- **Depth convention:** treating depth as Z instead of ray length would give 1.047 m. I rejected this because
  depth_info is a camera-centre distance.

## Answer
1.124 m. Confidence is high, about ±3%.
