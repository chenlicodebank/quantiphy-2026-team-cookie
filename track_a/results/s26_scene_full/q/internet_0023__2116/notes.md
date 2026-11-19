# q2116 — pool length (excluding stair area)

Prior: swimmer height = 1.8 m. Single planar scale (top-down near-nadir drone shot, internet convention).

- Swimmer height in px, frame 0 (body flat at surface, clearest frame): toe tips x≈578 to top of head x≈783
  → **205 px** (zoomed crop frames/sw0.png at 3× with 20 px grid; measure.py: head dark blob ends x=802 incl. hair/arms
  edge, non-water run ends 783 at head rows). Arms-forward length 256 px is not "height".
- Scale = 1.8 / 205 = 0.00878 m/px.
- Main basin water length (excluding step bay at bottom right), frame 0, colour mask rows y=520/600/800:
  x 564–568 → 1717–1721; scene record 566–1725 (inner coping edge). Use **1157 px** (±4).
- Length = 1157 × 0.00878 = **10.16 m** → answer 10.17.

Check: top lounger 246 px → 2.16 m (real loungers ~1.9–2.0 m), pool width 542 px → 4.76 m; 10 × 5 m pool is
a typical residential size, so the scale is plausible. Time base irrelevant (static size).
Confidence: moderate; main uncertainty is the swimmer's pixel height (pointed toes, head tilt) ±5 %.
