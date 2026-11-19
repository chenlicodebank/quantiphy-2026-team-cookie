# q_3163 – basket (rim) to floor distance, internet_0057

Prior: g = 9.8 m/s^2. fps = question_fps = 30 (no re-timing; the parabola then gives a scale consistent with
the rim size, see below).

## Scale from gravity (fitg.py)
Quadratic fits to the ball's bg-fixed centre y (scene/tracks/ball.csv, checked against frames):
- shot flight 55–96 (excluding degraded 73–77): 2.058 px/frame^2 = 1852 px/s^2 (rms 1.6 px)
- sub-windows 55–72: 1897; 78–96: 1810; bounce arcs 100–134: 1885, 137–163: 1829, 166–186: 1870
Used 1852 px/s^2 (full shot arc, near the hoop depth) -> scale = 9.8/1852 = 0.00529 m/px.
Sanity check: rim outer width 90 px; a real rim of ~0.475 m gives 0.0053 m/px at the hoop depth, which agrees.

## Rim and floor pixels (frame-0 / bg-fixed coordinates)
- Rim centre row 316 (ring 302–330, checked on a 4x crop, frames/rim.png).
- Floor directly below the rim (it is in front of the wall; the wall base at y≈795 is farther back):
  - route A, perspective: the horizon (lane-line vanishing point) is at y≈600. Floor offset below the horizon scales with
    1/depth, like the ball diameter: at the bounces (y_floor−600)/diam = 6.65, 6.30, 6.14 (frames 97/135/164), mean ≈ 6.35.
    At the rim depth the ball would appear ≈ 90×0.24/0.475 ≈ 45.5 px -> floor y ≈ 600 + 6.35×45.5 ≈ 889.
    Rim–floor = 573 px -> 3.03 m.
  - route B: floor level of the shooter's feet / first bounce (same depth band as the hoop), y ≈ 898 ->
    582 px -> 3.08 m.
- Other readings in case an annotator meant a different floor point: rim to wall base (795) 479 px -> 2.53 m;
  rim to baseline line (~857) 541 px -> 2.86 m. These use floor points farther back than the hoop, so I rejected them.

## Answer
3.05 m (routes A and B are 3.03–3.08 m; it also matches the regulation 3.05 m rim height). Confidence: moderate-high.
The main uncertainty is which floor point the annotators picked.
