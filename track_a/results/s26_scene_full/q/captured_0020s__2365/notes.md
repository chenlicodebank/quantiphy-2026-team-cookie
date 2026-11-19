# q_2365 — displacement of the white jar, 0.60 s -> 0.80 s (cm)

Frames: question_fps = file fps = 24 -> t=0.60 -> frame 14 (release, free flight starts), t=0.80 -> frame 19.
Scale: lab camera f = 0.5959*1280 = 763 px, principal point (640,360); jar depth 1.9735 m at frame 14 (given).
Depth at frame 19 is not given, so it comes from a 3D ballistic fit.

## Track
scene/tracks/white_object.csv was re-checked (measure.py, strip.py, frames/m*.png, frames/strip.png). Frames 14-17 and 20-24
are fine (my mask centroids are within ~1-2 px). At 18-19 the jar overlaps the yellow toy, so the scene centroids there are
biased. At 19 the jar-only blob centre is ~(482, 66), not (472.6, 68). At 25-26 my mask picked up the far person's arm,
so I kept the scene rows. Frames 18-19 were left out of every fit.

## Method (fit3d_b.py)
P(t) = P14 + V t + 0.5 g t^2, |g| = 9.8 m/s^2. |P14| = 1.9735 m, with its direction free. V is free, and the gravity
direction has a Gaussian prior. Each prediction is projected with f = 763 and least-squares fitted to the image track.
- Gravity priors: (a) the body-axis vertical vanishing point (835,1068) from scene/; (b) the far person's hip->feet
  geometry (pelvis ~(725,95) at 3.237 m, feet ~(728,265), assumed hip height 0.93 m). The two are 5.8 deg apart.
- Jar-only fits: free g gives 50.2 cm (rms 1.7 px). Person prior with sigma 0.5/3/6 deg gives 51.5/50.5/50.2 cm. VP prior
  gives 50-58 cm; the tight-VP fits have higher residuals (rms 2.7-3.4 px).
- A joint fit with the yellow toy (carrot depth 2.63 m) is inconsistent (yellow rms 6-11 px). The toy tumbles and its
  mask leaves out the green end, and the joint fit drags the jar toward the camera (depth falls below 1.9 m), which
  cannot be right for a throw toward the far person. I did not use it.
- Plausibility: the jar's depth at the catch (frame 27) is ~2.9 m, a little in front of the far person's 3.24 m, as it
  should be for her hands. Depth at 19 is ~2.16 m.

## Second route (check.py)
Back-projection of the clicked-style centres: (408.1,237.5) at 1.9735 m and (482,66) at the model depth 2.16-2.18 m give
50.7-51.6 cm. Size check: the jar's minor axis shrinks 34 -> 25.7 px from frame 16 to 24, a ratio of 1.32. The fitted
depth ratio is 1.31, which matches.

## Answer
~51 cm. Confidence: moderate. The main uncertainty is the depth at frame 19 (+-0.1 m -> +-5 cm).
