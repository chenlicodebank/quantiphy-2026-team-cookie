# Q1129 – eagle speed at t = 1.0 s

The file is 25 fps and the question uses 24 fps. I converted all times with 24 fps: t = 1 is frame 24 and t = 2 is frame 48, and the per-frame speeds are multiplied by 24.
I used the scene/ tracks after checking them: the bird is the eagle, its centroid is tracked in frames 0–53, and the frame at t = 1 confirms it.

## Geometry (geom.py, eagle.py)
- The principal point is the image centre (480, 480), and the focal length f is unknown.
- **Camera pitch as a function of f.** The boat moves on the water, so its displacement must be horizontal. I used its depth_info at t = 1 and t = 2 (130.35 m and 133.74 m) and its linear pixel track. At f = 6000 this gives a pitch of 13°.
- **Eagle.** I back-projected its smoothed centroid at t = 1 and t = 2, with the centroid fitted over about one wing beat, using its depths (139.76 m and 130.25 m). The 3D displacement over that second comes out nearly level for every f. The pixel speed at t = 1 matches the pixel speed at t = 2 once the change in depth is accounted for (6.84 vs 6.86 m/s tangential), so the 3D speed is steady.
- **Choosing f.**
  - The person's depth_info barely changes (0.03 m/s) while the body walks, so the character's origin stays put. Its distance only places the body near 139–140 m.
  - The person is 76 px from head to lowest foot. With a standing height of about 1.77–1.8 m (about 1.72–1.75 m while walking) and a cos 14° tilt correction, f ≈ 6200–6300.
  - Cross-checks at f = 6200:
    - The eagle's maximum spread of 75 px gives about a 1.65 m wingspan.
    - The boat's mast is about 10 m and its hull about 7 m.
    - On flat ground the person's walking speed comes out at 1.45 m/s against the prior's 1.3 m/s. A gentle beach slope of about 2.5° toward the camera would explain the gap. Forcing exactly 1.3 m/s on a flat plane would need f > 10000 and make the person shorter than 1.1 m, which is implausible. So the scale comes from the person's height, with the speed prior used only as a consistency check.
- I chose f ≈ 6200 px, which is a horizontal field of view of about 8.9°.

## Result
| f (px) | displacement from t = 1 to t = 2 (m/s) | instantaneous approximation (m/s) |
|---|---|---|
| 5500 | 12.04 | 12.24 |
| 6000 | 11.67 | 11.85 |
| 6250 | 11.52 | 11.68 |
| 6500 | 11.38 | 11.53 |

Answer: **11.6 m/s**, made up of about 9.5 m/s along the line of sight and about 6.85 m/s across it.

Confidence: moderate. Across the plausible range of f the answer moves by about ±4%.
