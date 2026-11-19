# Q1700: height of the boat (m)

File fps 25, question_fps 24: t=1 s -> frame 24, t=2 s -> frame 48 (frame indices used, not scene/ seconds).

## Focal length (focal.py)
The prior is eagle speed 12 m/s, with eagle depths 139.70 m (frame 24) and 147.16 m (frame 48). I back-projected the bird centroid
(cx_best/cy_best, raw or locally fitted) at both frames, with the principal point at (480,480), and solved for the f at which
|P48 - P24| = 12 m (1 s at constant speed). Result: f = 2648-2654 px, i.e. 2650 px (HFOV about 20.5 deg).
Sanity check: the bird's 30 px max wingspan at about 140 m gives about 1.6 m, which is plausible for an eagle.

## Boat pixel height (height.py, tip.py)
The boat's AABB height is taken from the keel bottom to the mast tip, because the mast is part of the boat.
- Keel bottom row: about 680 (strong edge at 677-681).
- Mast tip: the thin white top segment is faint and flickers. When visible (frames 4, 24-28, 38) its top is at about 488-490
  (frames 26/28 only reach 496; the dark segment starts at 513).
- Pixel height: about 192 px.

## Scale
- Frame 38: depth 132.38 m (interpolated), Z = 132.16 m -> 192 * 132.16 / 2650 = 9.58 m.
- Second route, frame 4: depth 136.2 m (extrapolated), the same 192 px -> 9.86 m.
- The two differ by 3 %, which is about 2 px of tip/keel noise. The answer is their mean, about 9.7 m.

## Other reading
Hull plus cabin only (without the mast): about 100 px -> 5.0 m. Not used.

Confidence: moderate (about ±5 %). The main uncertainties are the faint mast tip and the focal length, which rests on the eagle's straight constant-speed motion.
