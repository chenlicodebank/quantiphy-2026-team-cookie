# simulation_0169_segmented – measurement record

2D segmentation video (a Blender render with the background replaced by plain white). 1920x1080 px, 24 fps, 80 frames (0-79), t = frame/24.

## Files
- `scene.json`: inventory, sizes, start/end positions, orientation, events and camera.
- `tracks/person.csv`: one row per frame (0-79). Columns: `frame`, `time_s`; `cx, cy` = centroid of the mask (the reference point); `bbox_x0..y1`, `bbox_w`, `bbox_h`, `bbox_cx`, `bbox_cy`; `mask_area`; `axis_len` / `axis_wid` = mask extent along / across its PCA main axis (body length / width); `axis_angle_deg` = direction of the main axis in image coordinates (90 = vertical); `ncomp` = number of mask blobs of 30 px or more (always 1); `small_blobs` = count of tiny noise blobs that were ignored; `occluded` (always 0).
- `scripts/track.py`: segmentation and tracking. `scripts/overlay.py`: draws the outline, bbox, centroid and path on frames 0/20/40/60/79 so they can be checked (writes `frames/overlay.png`, which is scratch).

## Scene content
- **person** is the only object. It is a small human figure in a light-grey/white suit with a dark head or helmet (it looks like an astronaut), with one arm bent across the body. Its pose stays rigid: no walking and no limb motion. It is visible and unoccluded in all frames.
- Over the clip it rises almost straight up the image. The centroid goes from (1295.2, 519.1) at f0 to (1310.2, 244.7) at f79: dx = +15 px, dy = -274 px, net 274.7 px. The path length is slightly larger (sum of per-frame steps, including jitter).
- It also tilts slowly clockwise, head towards the image right. The main axis goes from 94° to 119°, about 25° in total.
- There are no static objects, ground, markings or other props. The background is uniform white.

## Size (pixels)
- Body length along the main axis (head to feet) is 91.4 px on average, ranging from 90.4 to 93.5. At f0, where the figure is nearly upright, the bbox height is 90 px. Use about 91 px for "height of the person".
- Width across the axis is 42.7 px at f0, growing to about 47-49 px late in the clip as the figure turns.
- The bbox is 43x90 at f0 and 63x83 at f79 (the bbox widens because of the tilt).

## Events
- At rest from f0 to f2 (centroid y ≈ 519).
- Starts moving up at about f3 (t = 0.125 s).
- Speeds up until about f33: the per-frame rise grows from about 1 px to about 5 px.
- Fastest from about f30 to f47: roughly 5.0-5.5 px/frame (the peak, about 5.3 px/frame, is near f35-f45).
- Slows down from about f47 to f77.
- Stops at f78 (t = 3.25 s), at y ≈ 244.7. The step from f78 to f79 is about 0.06 px.
- The overall profile is a smooth speed-up followed by a slow-down; no bounce or contact.

## Camera / perspective
The camera is static: no background exists to check against, and the benchmark keeps the camera fixed. The scene is 2D, and the figure's apparent size stays constant within ±1.5 px, so there is no depth change. Use a single metres-per-pixel scale from the prior.

## Method and reliability
- **Mask:** pixels whose minimum RGB value is below 225 on the white background, keeping connected blobs of 30 px or more. The overlay check confirms that the outline follows the full figure, including the dark head and the pale suit edges. Light-grey edge pixels may be lost: about ±1 px on the extents.
- **Reference point:** the mask centroid lies at about waist/hip level, so it serves as the proxy for the pelvis origin. Because the pose is rigid, the pelvis-to-centroid offset is constant apart from the 25° rotation, which could shift it by about 1-2 px in total.
- **Accuracy:** the centroid jitters about ±0.5 px from frame to frame, because of compression and antialiasing changes in mask area (2490-2770 px). One-frame differences are therefore noisy by about ±0.7 px/frame. Smoothing over a few frames is advisable when you need speeds or accelerations.
- **Ambiguity:** there are no similar objects, no shadows and no occlusion. Motion blur is negligible.
