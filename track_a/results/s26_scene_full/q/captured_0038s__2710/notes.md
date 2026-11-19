# q_2710: displacement of the white ball between 0.9 s and 1.4 s (cm)

The file and the question both run at 24 fps, so 0.9 s is frame 22 (round(21.6)) and 1.4 s is frame 34 (round(33.6)).
Camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360).

## Ball centre (pixels)
I took the centres from scene/tracks/ball.csv (template centre, with +3 px added to y as the record says) and checked them on the frames:
- f22: (527.5, 496.9). The mask centre is (526.5, 496.5).
- f34: (721.8, 505.1). The ball is in front of the cards there, but the crop shows the centre at about (722, 503-505).

## Depth
depth_info gives the ball depth only at 1.4 s: 0.7160 m, so P34 = ray(f34) x 0.716.
To get the depth at 0.9 s I assumed the ball rolls on the table, so its centre stays in a plane parallel to the table top
(no bounce happens between f22 and f34). That plane's normal comes from the horizon line in the image:
- The front-back table edges meet at a vanishing point near (716, 354). This point is well determined.
- The horizon slope is +0.0123, from the table corners (left-right edges, vanishing point near (-4422, 291)).
  A separate check, the lean of the vertical edges (pedestal and cup), gives +0.012 to +0.018. The two agree.
- The plane passes through P34. Intersecting the f22 ray with it gives d22 = 0.747-0.749 m.
- Result: displacement = 18.46 cm (template centre) or 18.61 cm (mask centre). If the camera had no roll at all,
  the result would be 18.85 cm.

## Checks
- Adding up the frame-to-frame steps on the same plane from f22 to f34 gives 18.46 cm, the same as the straight line.
  The path is straight, and the steps are a steady ~1.55 cm per frame.
- Sensitivity to the unknown depth at 0.9 s: 0.716 m gives 17.8 cm, 0.747 m gives 18.45 cm, 0.77 m gives 19.2 cm.
  The answer depends only weakly on this depth.
- The ball's apparent diameter (~34-37 px) is too noisy (±2 px) to settle the depth change. It does not contradict
  the plane result.

Answer: **18.5 cm**. I expect it to be within about 4%.
