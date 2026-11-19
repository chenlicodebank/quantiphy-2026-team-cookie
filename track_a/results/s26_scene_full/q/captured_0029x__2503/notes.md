# q_2503 – length of the table (cm)

Lab video, 1280x720, 24 fps (file fps = question_fps = 24). f = 0.5959*1280 = 762.8 px, principal point (640,360).

## Method
1. `edges.py`: table silhouette (non-black mask) per column over frames 5,26,30,40,48 (ball columns excluded), median;
   top boundary -> back edge and the two side edges; strongest dark-going vertical gradient -> top-surface/front-face
   boundary (front top edge). Results in `edges.json`.
2. `recon.py`: robust line fits (residuals 0.3-0.8 px). Corners by line intersection (handles the rounded corners):
   BL (450.2,448.5), BR (919.4,468.1), FL (211.1,535.7), FR (1140.5,587.3).
   Side-edge vanishing point (708,354); front/back edges meet at (-6830,145).
   Check of f: the two table axes back-projected with f=762.8 are at 89.3 deg (should be 90) -> intrinsics consistent.
   Table-plane normal = d1 x d2; horizon y ≈ 352.
3. Scale: ball centres back-projected with depth_info (frames 24, 30, 38 = t 1.00, 1.24, 1.60 s at 24 fps), ball centre is
   R = 3.35 cm above the table plane -> camera height above table plane h = 0.1587 / 0.1590 / 0.1620 m (three
   independent depths agree within 2 %). Corners intersected with the plane.

## Result
- h mean(f30,f38)=0.1605: front = back = 72.0 cm, sides 58.3 cm. (h f30: 71.4; h f38: 72.7; h f24: 71.2.)
- Length (longer horizontal extent, left-right) = **72.0 cm**; width (front-back) ≈ 58.3 cm.

## Checks
- Ball at the "hit whiteboard" frame 30 lies 2.0 cm in front of the reconstructed back edge (expected ~3.35 cm if the
  board stands at the edge) – consistent geometry.
- Three depth_info values give the same plane height (spread 2 %).
- Caveat: the ball's apparent circle-fit diameter implies distances ~8 % larger than depth_info (e.g. f30: 1.246 vs
  1.144 m); if that were the truth the table would be ~78 cm. Following the method card, depth_info is used.

Confidence: moderate-high (±3 % from geometry; ±8 % systematic if depth_info is biased).
