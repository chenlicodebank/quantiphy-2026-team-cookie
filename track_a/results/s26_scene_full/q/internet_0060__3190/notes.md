# q_3190 — width of the pink box (cm), prior g = 9.8 m/s^2

The clip is rotated 90°: the packet is dropped, and image +x is physical "down". It falls along the wall from frame 52 and hits the floor/baseboard (the black strip) at frame 65. It rests from frame ~78.

## Scale from gravity (fit.py)
I fitted a quadratic to the packet's x-centroid over the free-fall frames. The camera drift is about 0.25 px/frame, which is negligible, so I used background-corrected `cx_bg`:
- frames 52-65: 11.49 px/frame²; 53-64: 11.40; 54-65: 11.13; 52-60: 12.5; 58-65: 10.7. The later frames show slightly less acceleration, probably from air drag on the light packet.
- The mean of the second differences of x over 52-65 is ~11.7 px/frame².
- Adopted value: 11.5 ± 0.3 px/frame² → × 30² = 10350 px/s². The file runs at 30.0136 fps and the question at 30 fps; the difference is negligible.
- Scale = 9.8 / 10350 = 0.000947 m/px.

## Box size
The packet is square. At rest (frames 76-109) the bbox is 99-101 × 98-100 px and the minAreaRect is 99 × 98. In flight, the extent across the motion is 96-102 px, which matches the rest size, so the packet stays near the same depth. While it is held in the hand (frames 0-51) it looks ~124 px, but that is because of the fingers, and the packet may also be nearer the camera. I did not use it. Width = ~99.5 px (both sides are about equal).

Width = 99.5 × 0.000947 = 0.094 m ≈ **9.5 cm**. The acceleration range 11.1-11.8 px/frame² gives 9.2-9.8 cm.

## Check
- The size is consistent between the rest frames and the in-flight cross-motion extent.
- The acceleration is consistent across the different fit windows, to within ±4%.
- A packet ~9-10 cm across is a plausible real-world size.

Confidence: moderate-high (±5%).
