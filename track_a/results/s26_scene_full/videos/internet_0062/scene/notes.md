# internet_0062 – measurement record

## Scene
2D internet clip, 30 fps, 121 frames (t = frame/30), 1920x1080. The footage is rotated 90 deg:
white wall on the left (x 0-1437), black baseboard strip (x 1438-1581, 143 px wide), wood floor at
right (x >= 1582). **Gravity points to image +x.** A hand at the left edge holds a black zippered
pouch still (frames 0-65), releases it at frame 66 (t = 2.200 s); the pouch falls in pure
translation along +x (tilt stays ~15 deg, y changes < 5 px), hits the baseboard at frame 81
(t = 2.700 s), tumbles over it, and lies at rest on the floor from frame 91 (t = 3.033 s).
Camera is static (slow drift ≤ 2 px in x, ≤ 6 px in y over 4 s; < 0.5 px during the fall). No cuts.

## Files
- `scene.json` – inventory, sizes, static extents, events, camera.
- `tracks/pouch.csv` – every frame: centroid (cx, cy) of the dark mask, bbox x0..x1, y0..y1,
  bbox_w/bbox_h, min-area-rect mask_len (long side)/mask_wid (short side), axis angle, area,
  occluded flag, background shift bg_dx/bg_dy vs frame 0 (baseboard patch phase correlation).
  `region` = wall (frames 0-90) or floor (91-120).
- `tracks/hand.csv` – coarse skin-colour bbox/centroid of the hand/arm (low reliability).
- `scripts/` – track.py (first pass), shifts.py (camera check, shifts.json), final_track.py
  (produces CSVs + overlay), summarize.py, probe*.py (viewers), raw_track.json.

## Pouch size (pixels) – for the scale factor
- Held still (clean frames 0-17, 49-65): long side 246 ± 1 px, short side 155 px (min-area rect).
  Long axis tilted ~15 deg from the fall direction.
- Extent along the motion direction (image x, bbox): 258-260 px when held; 255-264 (mean 260) in flight.
  Across motion (y bbox): 197-200 px.
- In flight frames 67-80: mask_len 241-253 (mean 247), mask_wid ~153. Late flight frames have motion blur
  (~ +5 px along x at frame 80).
- On the floor (91-120) a different pose is seen and the part over the baseboard is cut off (mask clipped
  at x = 1588): 220 x 97 px – do not use as the object's size.
If a prior gives the pouch length, use ~246 px (true long side) or ~259 px (bbox extent along the fall
direction) depending on what "length along motion" means; the difference is ~5%.

## Motion
- Frames 0-65: pouch static at cx ≈ 159-162, cy ≈ 611-615 (slow 1-2 px drift = camera drift).
  Frames 18-48 the hand's fingers touch the pouch's left edge; the mask is cut at x = 22, so x0 = 22 there.
- Release frame 66; free fall frames 66-80 (15 frames). cx: 158.5 (66), 164.7, 181.5, 210.1, 250.4,
  302.5, 366.5, 442.5, 529.7, 628.9, 739.0, 860.5, 994.7, 1141.2, 1302.3 (80). The second difference is a
  nearly constant ~11.8 px/frame² (check only). Fall of the centroid 66→80 = 1144 px.
- Frames 81-88: the pouch overlaps the black baseboard (same colour). Only the wall-side part is segmented,
  so cx/cy there are NOT the pouch centre (flag occluded = 1). Frames 89-90: blurred over the baseboard, no mask.
- Frames 91-120: at rest on the floor, centroid of the visible part (1631, 659), with the baseboard-side part clipped.

## Reliability / ambiguities
- Frames 0-80 centroids: ±1 px (sharp, high-contrast black on white). Motion blur grows after frame 76,
  but the centroid stays unbiased along x.
- Shadow: a soft grey shadow falls below/right of the pouch. It is lighter than the threshold (V < 70) and
  is excluded.
- The impact is with the baseboard (black strip), not the wood floor; the final rest is on the wood floor.
- The hand track is coarse; wall shading sometimes merges into the skin mask (frames ~72-86).
- No metric scale is assumed anywhere.
