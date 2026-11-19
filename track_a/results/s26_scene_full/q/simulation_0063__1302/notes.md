# Q1302: height of the streetlight (m). Answer: 3.74 m

The file and question_fps are both 24 fps. t=0.58 s is frame 14 and t=1.58 s is frame 38.

## Object
All the street lamps are the same double-lantern model. Lamp A (pole at x≈618, base on the near sidewalk) and
lamp C (x≈1990) are fully visible. Lamp B (the large one at the centre) has its base cut off by the image edge. If B
is the same height (L/Hc = 1.65), its base would be at y≈1100, just below the frame, which fits.
The AABB height is measured from the base bottom to the finial tops.

## Pixels (scripts lamps.py, crops.py)
- Lamp A: finial top 337.5, front-bottom of base 837 (sub-pixel edge profiles), base half-width 26.5 px.
- Lamp C: top 397.5, base 740.5.
- Ground point under the lamp origin = front-bottom moved up by the base radius (about 1.3 % of the depth).

## Focal length (vp.py, vp2.py, vp3.py)
Ground lines were fitted with sub-pixel edges (rms 0.1-0.2 px):
- Direction D2: far road curb and far sidewalk/sky edge on the right meet at (4834, 533.3), on the horizon. The
  left sidewalk front edge points to x≈4460.
- Direction D1: near curb, with VP at x≈-93 on the horizon; right sidewalk front edge at x≈-46.
- If the two streets are perpendicular, f² = (cx-x1)(x2-cx). This gives f = 1990-2117. I used **f = 2060 (±3 %)**.
- Horizon y≈533 (D2 VP). The man-based fit in scene/ gave 532.3. I also tried a version with a slight roll through
  both VPs; it changes the result by less than 0.3 %.

## Scale (final.py)
- Man's ground contact (planted sole, read on 6x zooms): y = 826 at f14 and 847 at f38. The record's 820.5 is
  under-counted.
- Camera height: Hc = d·(y_g − y_h)/sqrt(f² + r²) gives 2.254 m at f14 and 2.256 m at f38. The two depths agree to
  0.1 %.
- Lamp height: L = Hc·(y_c − y_top)/(y_c − y_h). Lamp A gives 3.72-3.73 m and lamp C gives 3.74-3.75 m.
  **Mean 3.735 m.**
- Lamp A stands at almost the same image row as the man's feet, so the horizon error cancels out.
  The result scales roughly as 1/f: f = 1990 gives 3.85 m and f = 2120 gives 3.64 m.

## Checks
- Bike vs man depths at t=1.58 need a bike wheel bottom of y≈690.5 for f=2060. The template estimate in scene/ is
  689.4, so they agree, though this check is weak.
- Prior (white van acceleration = 4 m/s²): I tracked the rear wheel hub over f26-41 (wheel.py, vanacc.py). This
  gives 4.2-4.4 m/s² at f=2060. That is 6-9 % high, but the 16-frame window is noisy (about ±15 %), so it only
  loosely constrains f. It would favour a slightly longer f, which would make the lamp shorter.
- Sanity check: the taxi works out to 1.78 m tall including the roof sign (a real Crown Vic plus sign is about
  1.77 m). The van roof sits on the horizon, so the van is about 2.25 m tall. Both are plausible.
- Ground-plane depths of the road vehicles come out 2-3.5 % larger than the given depths. That points to a small
  vertical inconsistency (curb, origin offsets or horizon). It does not affect the lamp, which shares the
  sidewalk with the man.

Confidence: about ±4 %, set mainly by the focal length.
