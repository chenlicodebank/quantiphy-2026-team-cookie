# q_2723 — diameter of the white ball (cm)

File fps = question_fps = 24, so t=1.0 s → frame 24 and t=1.5 s → frame 36.
Lab method card: f = 0.5959 × 1280 = 762.8 px. D = Z × pixel diameter / f, using depth_info Z(t=1 s)=1.014 m and
Z(t=1.5 s)=0.737 m.

Pixel diameter, two routes (measure.py):
- scene/ track circle fit to the upper outline: f24 29.6 px, f36 42.4 px
- my own horizontal half-max edge profile across the equator: f24 28.2 px, f36 42.1 px (neighbouring frames agree
  to within ±1 px)

D:
- f24: 3.94 cm (circle fit) / 3.75 cm (profile)
- f36: 4.10 cm (circle fit) / 4.07 cm (profile)

At f36 the ball is larger, so a 1 px error matters less, and both routes agree there (4.07–4.10). At f24 the ball is
smaller and more blurred, and its values spread more (3.75–3.94). Combined estimate ≈ 4.0 cm, which matches a standard
40 mm ping-pong ball (used only as a sanity check).

Answer: 4.0 cm. Confidence: good (±4%).
