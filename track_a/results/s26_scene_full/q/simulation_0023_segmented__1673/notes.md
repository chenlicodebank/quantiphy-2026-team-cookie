# q_1673 — height of the boat (m)

File fps 25, question_fps 24: t=1 s -> frame 24, t=2 s -> frame 48 (frame indices used, not file seconds).

## Focal length (solve_f.py)
The eagle flies at a constant 11.84 m/s on a nearly straight path, so the eagle's net 3D displacement from frame 24 to frame 48 = 11.84 m.
Bird centroid (or bbox centre) at frame 24 is about (471, 372.5); at frame 48 it is about (742, 370). The depths are 116.05 and 108.28 m, and the principal point is the image centre.
Solving |P1 - P2| = 11.84 gives f = 3382–3396 px over all smoothing choices (0–3 frames, centroid or bbox). I used f = 3390 px (HFOV about 16.1°).
The radial change is 7.77 m, so the lateral motion is about 8.9 m.

## Boat pixel height (boat_h.py)
The boat mask runs from the mast tip to the keel. The faint mast tip makes the top jitter by 5–10 px between frames, so I used the upper envelope near each depth time:
- frames 19–27: about 324 px, giving H = 103.157 × 324 / 3390 = 9.86 m
- frames 44–51: about 312 px, giving H = 106.09 × 312 / 3390 = 9.76 m

The two depth times agree within 1% (second route). The pixel height ratio of 0.963 is consistent with the depth ratio of 0.972.

## Answer
9.8 m.
Confidence: moderate-good. Uncertainties:
- the faint mast tip (±2%);
- the slight downward view angle, which mixes a little of the horizontal extent into the vertical pixel extent (likely <3%);
- f depends on the bird's path being straight over 1 s.
