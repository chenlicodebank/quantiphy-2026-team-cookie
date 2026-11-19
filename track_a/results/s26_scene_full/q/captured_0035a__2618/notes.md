# Q2618 – basketball velocity at t = 1.5 s (cm/s)

- File and question fps are both 24, so t = 1.5 s is frame 36. f = 0.5959 x 1280 = 763 px, principal point (640,360).
- depth_info: basketball 2.270 m at t=0.6 (frame 14). The second "t=1.6 soccer_ball 2.412 m" line must be the
  basketball, because the soccer ball already has 3.052 m at t=1.6. That puts the basketball at 2.412 m at frame 38.
  Check: the circle diameter gives 2.27 x 74.4/763 = 22.1 cm at frame 14 and 2.412 x 71.5/763 = 22.6 cm at frame 38.
  The prior is 23.2 cm, so the depths are consistent.
- Centres: the scene/ RANSAC track and my own re-measurement (orange-mask hull centroid, measure.py) agree to about 0.5 px.
- Depth per frame: 1/Z is affine in image v, fitted through the two given depths. This assumes the ball centre moves
  in a floor-parallel plane. Each centre is back-projected to 3D, then forward differences are taken x 24.
- Per-frame forward speeds near frame 36 are 36–42 cm/s. The exception is step 35→36 at about 80 cm/s: both balls
  jump about 2x there, which points to a dropped frame in the recording.
  - Speed without the glitch: 38–40 cm/s (both tracks).
  - 5-frame mean of forward speeds centred on 36 (frames 34–38), glitch included: 46 cm/s. Wider windows give
    42–45 cm/s.
  - Linear fit over frames 32–40: 45 cm/s.
- The reference smooths frame-by-frame differences over 5 or more frames and probably includes the glitch step
  (about 42–46). Without the glitch the physical speed is about 39. Answer: 43 cm/s, a compromise between the two.
- Confidence: moderate. The uncertainty comes mainly from how the reference handled the dropped frame, plus about
  5% from the depth model (linear-in-time depth interpolation would give about 5% more).
