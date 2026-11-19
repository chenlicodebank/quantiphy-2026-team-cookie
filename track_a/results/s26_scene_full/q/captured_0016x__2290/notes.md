# q_2290 – soccer ball diameter (cm)

Lab video, 24 fps (file fps = question_fps = 24). t = 1.5 s -> frame 36 (ball in flight, slightly motion-blurred).
depth_info: ball at 1.402 m at t = 1.5 s. Lab focal f = 0.5959 x 1280 = 762.75 px.

## Main route (method card)
`measure.py`: green-screen mask of the ball, frames 33-41. Frame 36: bbox 754-872 x 28-126, min-area rect
117.9 x 93.8 px, PCA extents 118.8 (along motion) x 94.9 (across motion). Blur only lengthens the blob along the
motion, so the across-motion width is the diameter: ~94.3 px (frames 37/38 give 93-94, the sharp circle fit at f38
gives 94 px, so the value is consistent). Mask overlay: frames/mask36.png.
D = 1.402 x 94.3 / 762.75 = 0.173 m -> **17.3 cm**.

## Second route (gravity prior)
`gravity_check.py`: flight frames 32-40, depth Z = f*D/d_px from the apparent size of each frame, then
Y = (v-cy)*Z/f; a quadratic fit of Y(t) with g = 9.8 gives D ≈ 18.2 cm (about 5% from the main route; the blur in
32-35 makes those frames' sizes noisy).

Confidence: good (±5%). Answer 17.3 cm.
