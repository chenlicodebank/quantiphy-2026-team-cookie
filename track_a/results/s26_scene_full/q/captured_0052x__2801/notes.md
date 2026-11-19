# q_2801 — length of the shoe (cm)

Lab clip, 24 fps (the file and question_fps agree), 1280x720. f = 0.5959*1280 = 762.8 px, principal point (640,360).
depth_info: shoe at 2.231 m (t = 1.0 s, frame 24). The shoe is static (bbox is the same in frames 0-47).

## Measurement (shoe_mask.py)
- I made a green-screen mask of the white shoe. It lies on the floor, rotated about 36 deg in the image: toe at the
  lower-left (250,684), heel at the upper-right (318,~650).
- Max Feret diameter 84.4-85.1 px over frames 0-47. The long side of the min-area rectangle is 84.2-84.9 px.
  Short side ~35 px. Overlay: frames/shoe_mask.png.
- Method card: L = 2.231 * 84.8 / 762.8 = **0.248 m = 24.8 cm**. The scene/ record's "78 px diagonal" was an
  underestimate; I re-measured it.

## Second route: floor geometry (tilt.py, shoe3d.py)
- Ball rolling path (range from apparent diameter, anchored at 2.612 m at frame 24): the centre height stays constant
  (dy/dz = -0.008), so the camera is nearly level. Floor y is about 0.85 m below the camera, from three objects:
  ball centre + r, basketball centre + r, bin centre + h/2.
- Toe and heel sole points back-projected onto the floor plane give a 3D length of 21-22.5 cm (h = 0.83-0.86).
  Using the given shoe depth for scale instead gives about 20 cm. The given shoe depth puts the shoe centre about 10 cm
  above that floor, so it is about 5-8% short against the floor model.
- This route is very sensitive to the ~30 px vertical toe-heel offset (±3 px gives ±10%), so I used it only as a check.
  It suggests the true length is slightly below the card value.

## Scale sanity checks
- Basketball: 92 px at 1.9365 m gives 23.4 cm (a real ball is 23-24 cm).
- Yoga ball: 52 cm.
- Ball speed after frame 24 is about 2.2-2.4 m/s, consistent with the 2.19 m/s prior.

## Answer
24.8 cm (method card, Feret length). Confidence: moderate. The floor route gives 20-22 cm.
