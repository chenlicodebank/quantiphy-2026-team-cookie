# Q1024: height of the column below the drone

The "column" is the black cylinder hanging below the drone's light-grey rotor plate. The column and drone rise together as one rigid body. The video is treated as 2D: the motion is purely vertical in the image plane, and one metres-per-pixel scale comes from the prior speed. Time base is 24 fps (the file's rate and question_fps agree).

## Pixel speed
Source: scene/tracks/drone.csv, checked with m.py and m2.py.
- **Cylinder top edge `cyl_top`, frames 2-71:** linear, 170.4 px/s, rms 0.38 px. A quadratic fit gives 169.9 to 170.9 px/s, so the speed is constant.
- **Cylinder bottom, frames 26-71:** linear fit gives 169.4 px/s.
- **`top_y`:** gives 166 px/s, but it is noisy in the early frames because it blends with the robot. Over frames 26-71 it gives 169.7 px/s.
- **Value used:** 170.4 px/s, giving a scale of 0.96 / 170.4 = 0.005634 m/px.

## Pixel height of the column
I measured the column myself (m3.py) from the mean intensity profile across the cylinder width (x 1300-1360) at frames 30, 40, 50, 60 and 70.
- **Top:** where the light plate ends and the dark begins.
- **Bottom:** the lower edge of the dark rim, including the base ring.
- **Result:** about 174-176 px. The scene record gives 173 px from its own cylinder finder (stable over frames 26-66).
- **Value used:** 174 px.

## Answer
174 px × 0.005634 m/px = **0.98 m**.

Spread of the result:
- Height from 173 to 176 px gives 0.975 to 0.99 m.
- Using the bottom-edge speed instead (169.4 px/s) gives 0.986 m.

Confidence: high, about ±2%.
