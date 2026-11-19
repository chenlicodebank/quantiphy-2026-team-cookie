# q_3212: distance from the bottle's bottom to the floor at 1.50 s

## Setup
The camera is rotated 90°, so gravity points along image +x. The bottle is upright in the world: the cap is the top (left) and the base is the bottom (right). The floor is the wood region on the right. The black strip from x ≈ 1380 to 1517 is the skirting board, so the wall/floor junction is the black→wood edge.

## Time base
File fps is 30.016 and question_fps is 30, which is effectively the same. t = 1.50 s → frame 45.

## Scale from the prior (g = 9.8 m/s²)
I fitted quadratics to the x positions of the cap, the centre and the base during free fall (frames 41–52, 42–51, 41–48, 44–52) in `measure.py`.
- The pixel acceleration is 11.4–12.6 px/frame². I take **12.1 px/frame²**, the fit over the full window; the frame-by-frame second differences agree (about 12–13).
- 12.1 px/frame² × 900 = 10890 px/s², so the scale is 9.8 / 10890 = **9.0e-4 m/px**.
- Sanity check: the bottle's 260 px length gives 0.23 m, which is plausible.

## Positions at frame 45
- Bottle bottom (base end): x ≈ 562 px. This comes from the record (cap end + 260 px along the axis) and matches the zoomed frame, where the blurred base edge is at about 555–565.
- Floor line: the black→wood edge at the bottle's rows (y ≈ 520–650) in frame 45 is at **x ≈ 1518** (measured in code).
- Gap: 1518 − 562 = 956 px → **0.86 m**.

## Check
I used the free-fall model to predict when the base reaches the floor line. From release (base at x 371, onset at frame ≈ 39.2), reaching x = 1518 needs √(2·1147/12.1) = 13.8 frames, so impact at about frame 53. That matches the observed impact at frame 53, after which motion along x stops. This supports the black→wood edge as the floor.

The other reading, taking the floor at the top edge of the skirting board (x ≈ 1380), gives 818 px = 0.74 m. That would put the impact at frame ≈ 52, but the bottle visibly passes x = 1380 between frames 52 and 53, so I rejected this reading.

## Confidence
Moderate. The main uncertainties are the scale (about ±4 %) and exactly which line the annotator took as the floor.

Answer: 0.86 m
