# q1532 – acceleration of the yellow car at t = 1 s (frame 24), m/s^2

Time base: file fps = question_fps = 24, so frame 24 (no re-timing issue).
The camera is static. The car drives side-on right→left at constant depth from frame ~14 on: wheel-centre y and
rim size stay constant to <1 %. The rim at frame 12 (t=0.5 s, when the depth is given) is the same size (~122 px),
so the front tyre's depth did not change.

## Motion (measure.py, accel.py)
- Wheel centres = circle fit to the white rim outline, which does not depend on wheel rotation. Front wheel usable
  frames 14-26, rear wheel 22-34. Combined track = rear wheel shifted by the 709.5 px wheelbase.
- Reference definition a(24) = (speed24 − speed23)·fps → second difference p24 − 2p23 + p22.
  Raw values: front 1.577 px/frame², rear 1.651 px/frame². Local cubic/quartic fits over ±4…±8 frames
  (combined track): 1.536–1.593, median 1.55. I used **1.57 px/frame² = 904 px/s²**.
  The speed rises to a peak at about frame 30 and then falls (smooth ease curve), so the car is accelerating at frame 24.

## Scale
Only the tyre gives a metric scale (diameter 0.764 m). Because the car translates rigidly at constant depth,
ΔX(origin) = ΔX(wheel) = Δu · Z_wheel / f, and f = D_px · Z_tyre / 0.764. The scale is therefore 0.764 / D_px, and
the depth and focal length cancel (to <1 %).
- Tyre outer diameter (radial.py, chroma.py, prof.py, vis2.py): the lit flat sidewall ends at r≈88 px. The rounded
  shoulder or silhouette reaches r≈93 at the top, and the floor contact below the centre is at r = 93.3–94.6 px
  (frames 16-31). A darker band out to r≈98 is the wheel-arch interior/shadow (brownish chroma).
  **D = 187 px** (±~4 %).
- Focal length check: with D = 187, the depth at t=0.5 s (11.38 m to the tyre at u = 1657, v = 791.5) gives
  Z ≈ 10.96 m and f ≈ 2658 px (HFOV ≈ 40°). This is plausible.
- Size sanity check with 0.764/187 = 4.09 mm/px: wheelbase 2.90 m and height 1.45 m. These match a 1.21×-scaled
  RX-7 (tyre 0.63 → 0.764 m: wheelbase 2.93, height 1.49).
- The floor/B1-sign route (h from the wall base at y≈705.5 and Z_sign = 23.44, horizon y = 539.2 from the
  light-tube vanishing point) gives a larger f (~2800–2900, implying D ≈ 196–204 px). That contradicts the visible
  tyre bottom at y≈885, so the sign's depth or the wall-base line is probably not at the plane I assumed. I did not
  use it.

## Result
a = 904 px/s² × 0.764/187 m/px = **3.69 m/s²**.
Sensitivity: D = 175 → 3.95; D = 196 → 3.52; a_px ±3 %.
Confidence: moderate. The main uncertainty is the tyre's pixel diameter, about ±5 %.
