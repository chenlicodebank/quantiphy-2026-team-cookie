# q1340 — height of the walking pedestrian (simulation_0066, 3D Blender render)

File fps = question_fps = 24, so frame = round(t*24). The camera is static.

## Focal length (two independent routes)
1. Vanishing geometry (`poles.py`, `curbs.py`, run on scene/bg.png). Eight vertical poles were fitted (sub-pixel
   dark-centre per row): the vertical vanishing point is about (1066, 2105). Curb edges were fitted by gradient search:
   road A VP (620, 77) and road B VP (≈3140, 70). Assuming a centred principal point: f from A⊥B = 853–857;
   f from A and vertical = 849; f from B and vertical = 880–888. The orthocentre principal point is (1055, 520), which
   gives f = 842. **f ≈ 855 px** (HFOV ≈ 103°).
2. Prior check (`vanfix.py`). The white van's centroid rays at f14 and f38 times the given depths (23.589, 19.990)
   give a 3D displacement of 4.32 m at f=800, 4.24 m at f=855 and 4.19 m at f=900. With a = 4 m/s², that implies
   the van starts from rest at t0 = 0.00–0.04 s (frame 0–1). That matches the video: the image motion is tiny over
   f0–6, as expected for 2t² near t=0. A free fit to the whole track (`vanfit.py`) is poorly conditioned
   (f 1140–1513), because the centroid is not the origin. Fixing the start at t≈0 is consistent with f 800–900.

## Pedestrian height (`ped.py`, `height3d.py`)
- Mask: |frame − bg| > 14 with soft shadows removed, keeping components near the scene track column. The overlays in
  frames/pedmask.png show that the head top and shoe bottoms are covered.
- For each frame, each mask pixel is back-projected onto the world-vertical plane through the pelvis
  (pelvis depth from depth_info, interpolated linearly: 21.061 at f14, 21.349 at f38). The extent along world-up
  (from the vertical VP) is the height. This corrects the strong lean of verticals at the left edge of the image.
- f = 855: median over the clean frames (f29–33, f63–71) = 1.83 m; median over all frames including the lamp-post
  frames = 1.80 m. f = 800 gives 1.86 and f = 900 gives 1.80. A few outlier frames (f37, f69, at about 1.95) come
  from stray blobs.
- The image box is only about 90 px tall, about 4 cm per pixel. Walking extent (head top to lowest foot) ≈ 1.83 m.
  The rest standing height would be equal or slightly larger (the walk is crouched).

Answer: **1.85 m**. This is the walking extent with a small allowance for the standing height and for f uncertainty
in the range 830–855. Confidence: moderate, about ±5%. The main uncertainty is f (±4%) and mask edges (±2 px).
