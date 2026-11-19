# Q1541 – width of the blue car (light-blue utility cart), metres

Answer: **0.753 m** (bounding-box extent across the cart = outer face of near front tyre to outer face of far front tyre).

## Setup
- 3D Blender scene. The file and the question are both 24 fps, so frame = round(t*24). Static level camera, principal point
  about (960,540) (vanishing point of the record).
- The cart drives left to right, parallel to the image plane, at constant depth. Its right side faces the camera, so the
  "right front tire" is the near-side front tyre.
- Prior: cart tyre diameter 0.369 m. Near front tyre outer diameter is about 109 px (R 54-55 px; frame 39 profiles:
  right edge 1402, rim centre 1348.5, bottom ~949).
- depth_info: at t=1 s (frame 24) the Euclidean distance to the right front tyre is 9.312 m. The tyre centre is at
  (622.3, 893.5) px, offset (-338, 354) from centre. Solving with f = D_px·Z/D gives f ≈ 2690 px (HFOV ≈ 39°) and
  Z_tyre = 9.162 m. Z depends only weakly on f: a 5 % change in f moves Z by 0.15 %. Taking a tyre width of about
  0.12 m gives Z for the near tyre's outer face ≈ 9.10 m. Check: camera height = (949.5-540)·9.10/2690 = 1.39 m,
  which is consistent.

## Width via motion parallax (the cart is seen side-on, so its width lies along depth)
With motion parallel to the image plane, u - cx = f·X(t)/Z + const. Regressing one feature's u against another's over
the frames gives the depth ratio between them.
- The far-side front tyre is visible to the right of the near front tyre in frames 12-24. Its right silhouette at
  rows 892-906 is its outer face; overlays are in frames/overlay_far.png.
- The near tyre's left silhouette at the hub rows (889-897) in the same frames is the near outer face; see
  frames/overlay_near.png.
- Route 1 (direct, no hub track): regress the far edge on the near edge, giving Z_near/Z_far = 0.9233
  (rows 900-906, rms 0.4-1.0 px). Script: ratio_direct.py.
- Route 2 (via the record's hub track): far edge slope 0.929-0.931 (rows 892-906, rms 0.5-1 px; row_slopes.py),
  near edge slope 1.0059, ratio 0.9240.
- Width = Z_no·(1/ratio - 1) = 9.10 × 0.0827 to 0.0831 = **0.749-0.756 m**. I answer 0.753.

## Checks and caveats
- Lower rows (≥908) and the frames nearest the image centre are biased, because the inner face takes over the
  silhouette there. They were excluded.
- Near-side right-edge slopes in frames 33-41 relative to the record's ref_x looked inconsistent. The record's hub
  track drifts about 2-3 px late in the clip (the raw Hough hubs disagree), which is why route 1 avoids it.
- The rear far tyre cannot be measured: it sits in deep shadow and the detections landed on the sill shadow.
- Headlights on the front face, regressed on the near tyre edge: A at Z = 1.019·Z_no, B at 1.081·Z_no. B is just
  inside the far tyre's outer face (1.083), and the near-side body (cowl corner, roof edge) is inset about 0.15 m from
  the tyre. So the tyres define the bounding-box width. The headlights are not centred between the tyres (about 7 cm
  off).
- An absolute-position cylinder fit (far_model*.py) was too degenerate between radius and offset to use.
- Confidence: moderate-good, about ±5 %. Main uncertainty: the edge definitions (sidewall bulge, threshold level)
  and whether body parts outside the tyres widen the bounding box.
