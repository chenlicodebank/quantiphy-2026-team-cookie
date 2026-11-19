# q1993 — average speed of the rabbit (m/s)

- Objects: "brown horse" = the larger plain-brown horse in the middle (scene record `brown_horse`; the left one is
  chestnut/red). "Rabbit" = the small orange-brown animal at the right (record calls it `hamster`).
- 2D side view, static camera, all motion horizontal; fps = question_fps = 24, no re-timing.
- Scale from prior: brown horse net horizontal motion frames 0→49 = 5.918 (torso) / 5.942 (centroid) px/frame
  (linear-fit slopes 5.93–5.98) → 5.930 px/frame = 142.3 px/s → 0.874/142.3 = 0.006141 m/px.
- Rabbit: net 6.27 px/frame (centroid, bbox, torso all agree; fit slope 6.24); mean of per-frame 2D steps 6.29
  (centroid), higher for bbox/torso only through jitter. → 6.27 × 24 × 0.006141 = 0.924 m/s (path-length route 0.927).
- Second route (check.py, own segmentation): ratio of rabbit/horse net displacement 0→49 = 307.3/291.1 → 0.922 m/s;
  window 10→39 → 0.948 (gait-phase noise of the short window).
- Answer 0.925 m/s. Confidence: good (±3 %).
