# q1705 — length of the boat (m)

Video: 3D Blender render (segmentation), 960x960, 75 frames. The file is 25 fps but question_fps = 24 is used for all
time-to-frame conversions (t=1 s -> frame 24, t=2 s -> frame 48). I used the frame column from scene/, not its seconds.

## Geometry
- The boat moves bow first, towards the upper left and away from the camera. The bow is the high white prow at the upper left;
  the stern is the rounded red hull at the lower right, with the open aft deck, rail and crane.
- Boat depths: 130.35 m (f24) and 133.74 m (f48). The boat's bbox shrinks by 0.975, which matches the depth ratio of 0.975.
- Camera pitch from the boat moving horizontally (solve_cam.py): f*tan(theta) ~ 1450-1500 px, giving theta ~ 13 deg at f ~ 6200.
- Heading = horizontal part of the boat's 3D displacement between f24 and f48. It is about 33 deg off the line of sight,
  so the hull is strongly foreshortened.

## Focal length / scale
- Speed prior (1.3 m/s): under horizontal motion the person's downward image motion (+44 px) already implies a ~3.9 m approach,
  so speed >= 1.35 m/s for any f. The prior can only be met as f -> infinity, which is ill-conditioned. The person's pixel
  height also does not grow (78.4 px in the first 25 frames, 77.8 px in the last 25; the approach predicts +2.2 px).
  The given person distance is almost constant (139.95 -> 139.98 m). So the prior gives no reliable focal length.
- Scale taken from the standard object (adult person): standing pixel height ~80 px (my own mask, min RGB < 250, median 77,
  p90 81) at 139.97 m. For a height of 1.75-1.80 m, f ~ 6200-6400 px (human_h.py).
- Check from the eagle: 70 px maximum wingspan at about 137 m, foreshortened by cos 33 deg (it flies mostly towards the camera).
  This gives about 1.9 m at f = 6000, which is plausible.
- The person's speed at f = 6200 comes out at about 1.45 m/s, roughly 12% above the prior; this is noted as a known inconsistency.

## Length measurement (boat_len_final.py)
- Each bow and stern point is intersected with the boat's vertical centre plane (heading + up through the hull centre at the given depth).
  Length = separation of the points along the heading.
- Bow = the leftmost hull cluster (stem top; it lies on the centreline).
- Stern: the rightmost silhouette pixel is on the far stern quarter, off the centreline, so it overestimates the length
  (L = 10.8-11.1 m at f = 6200). I used centreline estimates instead, from the dark stern band (x ~405-455 px at f0):
  band centre (transom model) gives L = 9.8-10.1 m; rounded-stern aft-most point (75% across the band) gives 10.3-10.6 m.
- L depends only weakly on f (f 5600 -> 6800 changes L by about 6%). Three frames (0, 24, 48) agree within ±0.15 m.

## Answer
L ~ 10.3 m (range about 9.9-10.8 m). Plausibility: overall height keel-to-mast is about 9.2 m, which fits a ~10 m fishing boat.
Confidence: moderate. The main uncertainties are which stern point lies on the centreline (±0.4 m) and the focal length
from the person's height (±5%).
