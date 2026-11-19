# q_1594 — height of the black cat (incl. tail)

The file and the question both run at 24 fps, so frame = round(t*24).

## Method
- Focal length from the speed prior plus depth_info (`focal.py`). I back-projected the cat's reference point at
  f0 (depth 4.199) and f24 (depth 4.481), with the principal point at the image centre, and solved for the f that
  makes the 1 s displacement 0.94 m. Using the torso centroid gives f ≈ 2068-2109 px; the mask centroid or bbox
  centre gives 2113-2190. I used f ≈ 2100-2160 (HFOV ≈ 48-49°).
- Camera pitch: the 3D motion vector should be horizontal, which gives ≈1.7-2.3° down (`pitch.py`).
- Floor check (`check_floor.py`): at f=2100 the camera's height above the floor is 0.78 m from the mirror-bottom
  depth (6.407 m) and 0.80-0.81 m from the cat's paws. These agree (the small gap fits the slight downward pitch).
  The bench-leg centre comes out ≈0.2 m above the floor, which is plausible. This check depends only weakly on f.
- Height (`height.py`): for each of the 50 frames I put the cat's origin on the horizontal plane through P0 and
  P24, then back-projected the bbox top (tail tip, which is above the ears) and the bbox bottom (lowest paw, minus
  3 px of contact shadow) onto the vertical plane through the origin facing the camera. The world vertical
  extent is measured along the pitch-corrected vertical.
- The bbox was checked on a zoomed frame 24: tail tip y≈684, paws y≈920, which matches the record.

## Results
- f=2100: per-frame height 0.44-0.52 m, mean 0.483, median 0.484. The spread comes from gait and tail motion.
- f=2070: mean 0.489. f=2160: mean 0.470.
- Answer: 0.48 m. Confidence: moderate, about ±5%. The main uncertainties are the focal length (it depends on
  which point stands in for the origin and on assuming constant speed over 1 s) and which frame's bbox the
  reference used.
