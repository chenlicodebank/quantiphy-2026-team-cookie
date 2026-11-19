# Q2594: length of the pencil bag (cm). Answer: 24.7

The question's fps (24) is the same as the file's fps. The pencil bag does not move during the clip (measured at frames 0, 29 and 48).

## Key finding: depth_info does not match the prior
With the lab focal length f = 0.5959 x 1280 = 763 px:
- A 6.7 cm tennis ball at the given 0.776 m would appear about 66 px wide. It actually appears about 29 px wide (scene track, rolling frames).
- From its apparent size, the ball is really about 1.75 m away (763 x 0.067 / 29.3).
- The soccer ball (91 px) and the table (about 300 px wide) also fit a camera distance of about 1.5–1.8 m.

So the given depths (0.71–1.05 m) are too small by a factor of about 2.3, and they are not even consistent with each other (the pencil bag lies in front of the soccer ball but is given a larger depth). Reference sizes are ruler measurements, so I took the metric scale from the exact prior (tennis ball = 6.7 cm) and not from depth_info.
- The method-card value 1.05 m x 99 px / 763 = 13.6 cm is recorded here, but I rejected it: it contradicts the prior.

## Measurement (`measure.py`, `check.py`)
- **Mask:** HSV mask of the pencil bag (H 20–32, S ≥ 60; the table has H about 16–17). Checked visually in `frames/mask_*.png`.
- **Length in pixels:** the extent along the principal axis is 98.8, 99.8 and 96.6 px at frames 0, 29 and 48. Width is about 33 px. The scene record gave 98 px, which agrees.
- **Table plane orientation:** taken from the vanishing points of the table-top rectangle (corners from scene.json). The two in-plane directions come out orthogonal (cos = −0.001), which confirms f = 763. The plane is tilted 53° from the optical axis.
- **Table plane offset:** from the tennis ball centres. Each ball is placed at its size-based distance, and the table is one radius (3.35 cm) below the centre. This gives n·X = −0.926 m from ball_right (frames 28–48) and −0.947 m from ball_left (frames 28–31).
- **3D length:** the two ends of the bag were back-projected onto the plane at about 1.5 cm above the table (mid-height of the bag). This gives 24.7 cm at frame 29, 24.5 at frame 0 and 24.0 at frame 48. The range over the plane offsets and heights tried is 23.7–25.4 cm.

## Second route
Simple same-scale check: 6.7 cm x 99 px / 29.3 px = 22.7 cm.
- This ignores two effects. The bag is closer than the back-right ball, which makes it smaller. The bag's axis is foreshortened on the tilted table, which makes it larger.
- The plane route includes both, and its net value is about 9% larger. The two routes are consistent.

Sanity check: the plane gives a soccer-ball diameter of about 18 cm, which is plausible for a small (size 3) ball. A pencil bag 24–25 cm long is realistic.

## Confidence
Moderate: about ±5%, from the ball-size noise and the mask edges at the ends of the bag. The main risk is that the reference instead used the inconsistent depth_info, which would give about 13.6 cm.
