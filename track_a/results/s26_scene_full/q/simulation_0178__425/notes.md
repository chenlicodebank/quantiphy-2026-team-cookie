# Q425: speed of the small elephant at 1 s (m/s)

Prior: big elephant speed = 2.313 m/s. 2D side view, static camera, fps 24 (same as question_fps).
Both elephants' feet sit on the same ground line (y≈693–696, checked on the frame at t=1 s, frames/f1.png), so they are at the
same depth and one m/px scale applies -> v_small = 2.313 x (small px speed / big px speed).

Pixel speeds (an.py, scene tracks, linear fits of x vs frame; both walk at a steady pace, with only gait wobble):
- mask centroid_x, all frames: big 6.882, small 6.126 px/frame -> ratio 0.890
- centroid_x, frames 12–36 (around t=1 s): 6.904 / 6.209 -> 0.899
- body (opened mask) centroid_x: 0.889 (whole clip), 0.869 (window); body rear edge x0: 0.870 (both)
- path-length ratio 362/413 = 0.877
Per-frame centroid steps at f24 are noisy (±1.5 px from the legs), so I used the steady fitted speed (the rig root moves smoothly).

Ratio ≈ 0.885 ± 0.01 -> v_small ≈ 2.313 x 0.885 ≈ 2.05 m/s (range 2.01–2.08).
Second check: the scale from the big elephant (6.88 px/frame x 24 = 165 px/s -> 0.0140 m/px) makes the big elephant's
height 230 px ≈ 3.2 m and the small one 156 px ≈ 2.2 m, which is plausible.
Confidence: good (about ±3%).
