# q_1668 — "average walking speed of the person" (m/s)

## Object mismatch
No person appears anywhere in the clip. `scan.py` checks every frame for foreground outside the boat bbox and the
static island mask, and finds only island-edge anti-aliasing noise. The only moving object is the boat, and the
prior (boat length 10 m) and the depth_info (boat distance) are both about it. So the question is taken to mean the
average speed of the moving object, the boat. Low confidence that this is the intended reading.

## Method (speed.py)
- Time base: question_fps = 24 (file is 25 fps; frame indices used, t = frame/24).
- Depth: d(f24) = 148.7451, d(f48) = 146.9726. Linear in frame (constant velocity, as in the scene record):
  radial rate -1.7725 m/s.
- Focal: f = bbox_w x d / 10 m over fully visible frames 35-62 gives 4266 px (sd 19). Using the hull bow-to-stern
  length gives 4202 px. Horizontal FOV is about 12.8 deg.
- Positions: back-project the template-tracked bbox centre (or the hull centre) with the depth at each frame.
- Speed: mean of the per-frame |dP| x 24 = 4.22-4.28 m/s. Net 0->72 gives 4.20-4.25 m/s
  (lateral 3.93-3.99, radial 1.77).

## Second route / caveats
- Net-displacement speed (4.20) agrees with the mean per-frame speed (4.23); the small excess is tracking noise.
- If the boat moved along its own heading at 27 deg toward the camera (foreshortened length), the speed would be
  about 3.90 m/s. The boat looks broadside, so the projected length was taken as the true length.
- Answer: 4.21 m/s.
