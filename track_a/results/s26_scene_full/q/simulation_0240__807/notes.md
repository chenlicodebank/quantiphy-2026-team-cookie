# Q807 – length of the front horse (m)

Prior: speed of the horse at the back = 0.874 m/s. The back horse is the trailing chestnut horse; the front one is the pale horse.
fps = question_fps = 24, so no re-timing. Camera is static. Treated as 2D with a single m/px scale: both horses walk side by side
in front of the house, and their hoof-contact rows (~1045 vs ~1050 px) are too close and too grass-hidden to show a
depth difference.

## Measurements (m1.py, from the scene/tracks CSVs, which I checked against frames)
- Chestnut speed, from linear fits over frames 0–48 (frame 49 is an animation-loop reset, so it is left out):
  mask_cx 3.241, bbox_x0 3.239, bbox_x1 3.283, bbox_cx 3.261 px/frame. I used 3.241 px/frame = 77.8 px/s.
- Scale = 0.874 / 77.8 = 0.011234 m/px.
- Pale horse horizontal bbox extent (nose to tail) over 50 frames: mean 228.8 px, median 228, range 215–244.
- Length = 228.8 × 0.011234 = **2.57 m**.

## Second-route check
The speed from the bbox edges (3.24–3.28 px/frame) gives 2.54–2.57 m. The median length (228 px) gives 2.56 m.
A 2.5–2.6 m body length (with the head stretched forward) is plausible for a horse.

## Confidence
Moderate to high. The main risk is a small depth difference between the horses (up to ~5–10%) that the 2D convention ignores.
