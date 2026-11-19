# q_232 – side length of the pool (prior: swim ring diameter = 1 m)

This is a 2D-type top-down render with a static camera. The ring floats on the water, roughly in the plane of the pool opening, so one metres-per-pixel scale comes from the ring.
fps does not matter here because this is a size-to-size question.

## Ring diameter (px)
- `measure.py`: saturated-pixel mask, filled outline at frames 0, 60 and 119.
  - Equivalent-area diameter: 74.7–75.3.
  - Ellipse axes: 72.8–75.8.
  - Bbox: 75–78 (includes antialiasing).
- `ring_diam.py`: radial half-level edge over 72 angles every 10 frames gives 73.1 (±0.3).
- Adopted value: 74 ± 1 px. The scene record says ≈73–74.

## Pool side (px)
`pool_edges.py` uses frame 48, where the deck is smooth after the texture change at frame 24. It takes profiles averaged over 250 rows or 240 columns.
- Water edge (inside the rim bevel):
  - x 312.5 → 765.5 = 453
  - y 309.5 → 765.5 = 456
- Outer edge of the rim highlight / deck boundary:
  - x ≈ 305.5 → 770 = 464.5
  - y ≈ 307.5 → 770.5 = 463
- The pool is square. I took a side of ≈ 458 px, between the water opening (454.5) and the rim (464), because the bevelled lip belongs to the hole edge.

## Answer
458 / 74 ≈ 6.19 m. Different combinations give:
- inner opening / larger ring = 6.08
- inner opening / half-level ring = 6.22
- rim / ring = 6.27–6.35

Answer: 6.2 m. Confidence is moderate: about ±3% from the edge-definition choice of the pool rim and the ring outline.
