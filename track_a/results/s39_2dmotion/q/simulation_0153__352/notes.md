# Q352 — acceleration of the blue car (utility cart) at t = 1.5 s

question_fps = file fps = 24 -> t = 1.5 s is frame 36. 2D video: cart moves side-on, left to right, at constant depth
(tyre contact line y ≈ 948 in all frames; tyre size constant), so one m/px scale from the prior.

## Scale (prior: tyre diameter 0.369 m)
- `tire_profile.py`: sub-pixel edges (level 50) of the front tyre on vertical and horizontal profiles through its
  centre, frames 28–41. Vertical 111.3–112.0 px (median 111.5), horizontal median 111.2 px (level 70: ~112.5).
  Use D = 111.5 px -> 0.369 / 111.5 = 0.003309 m/px.
- SAM 3 "tire" at frame 36: rear box 820–930 x 842–951 (horiz 111, vert 108), front 1155–1264 x 841–948
  (horiz 114, vert 108–109). The SAM vertical extent is ~3 % smaller than mine. I checked the vertical grey profile
  at the front tyre: brightness drops 146 -> 112 -> 54 -> 6 over rows 835–838, so the top edge is at y ≈ 837. SAM's
  top at y ≈ 841 cuts off the tyre's upper rim, so I use my value. The horizontal extents agree within 1–2 %.
  The scene record's "≈105 px" was read by eye and is too small. I did not use it.

## Motion
- `track.py`: sub-pixel NCC tracking of rigid, non-rotating patches (templates from frame 36): lower lights panel
  (frames 17–41), rear box (20–41), canopy front (31–41), front body (34–41). The scene record's panel template
  track is also used for comparison.
- `analyze.py`: a(36) = (v36 − v35)·fps = (x36 − 2x35 + x34)·fps². The speed profile rises to about 50 px/frame
  near frame 30 and then falls. A cubic in frame index fits the positions over frames 20–41 to an rms of 0.03–0.07 px,
  so the motion has constant jerk.
  - lights panel, cubic: −0.633 px/frame² -> −1.207 m/s² (raw second difference −0.64)
  - rear box, cubic: −0.629 to −0.634 -> −1.198 to −1.208 m/s² (raw −0.69)
  - scene panel track, cubic: −0.627 -> −1.196 m/s² (raw −0.53)
  - canopy and front body (short, noisier tracks): quadratic fit gives −1.4 to −1.6. These are less reliable
    because the tracks are short and the patches include some background.
- Second route: the three independent rigid-point tracks, each fitted over a different frame window, give
  −1.196 to −1.208 m/s².

## Answer
|a| = 0.63 px/frame² × 576 × 0.003309 m/px ≈ 1.20 m/s². The cart is slowing down, so the signed value is −1.20.
The answer is given as the positive magnitude, 1.20.
Confidence: good. The main uncertainty is the tyre pixel diameter (±1.5 %).
