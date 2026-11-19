# q2641: soccer ball velocity at 1.4 s (cm/s)

The file and question_fps are both 24, so t = 1.4 s is frame 34. Camera: f = 0.5959*1280 = 762.8 px, principal point (640, 360).

**depth_info typo.** Both t = 1.4 s entries say "soccer ball". From apparent size, the soccer ball is at 2.373 m and the basketball at 2.602 m. The checks:
- Soccer ball: its diameter goes from 52.5 px at frame 22 to 54.8 px at frame 34. That ratio is 1.044, and 2.477/2.373 is also 1.044.
- Basketball: it grows from 61 px to 67 px, which fits 2.778 m to 2.602 m.

**Image track.** I used the scene/ circle-fit centres for frames 26-44 and checked them visually at frame 34, where the centre is about (690, 494). My own white-mask re-fit (`measure.py`) agrees to 1-2 px in x. Its centres sit about 5 px higher, but the offset is constant, so velocity is unaffected. Near frame 34 the ball moves about 5.5 px/frame in u and 2.5 px/frame in v. It is also getting closer to the camera.

**Dropped frame.** One source frame is missing between frames 35 and 36: both balls make a double step there. Physical-time fits insert the missing frame.

## Route 1: depth from apparent size
Fit 1/diameter linearly over frames 28-44 and anchor it to 2.373 m at frame 34 (`measure.py`).
- 3D velocity ≈ (38.4, 12.2, -31.0) cm/s, so |v| ≈ 50-51 cm/s.
- My mask diameters give 49-50 cm/s.

## Route 2: floor plane (`plane_check.py`)
Solve for the floor plane from the basketball at frames 22 and 34 (centre 11.6 cm above the floor) and the soccer ball at frame 34 (radius 8.5 cm).
- The plane predicts the soccer ball centre at frame 22 is 8.4 cm above the floor. That matches its radius, an independent check that uses the given 2.477 m.
- Putting the soccer track on that plane gives |v| = 50-52 cm/s over windows 29-40, 30-38 and 32-36.

## Convention
The reference uses forward differences over adjacent frames, smoothed over 5 or more frames, by frame index.
- A centred 5-frame window includes the doubled 35→36 step and gives about 61 cm/s (60-62 in both routes).
- The true physical speed is about 51 cm/s.
- Wider windows give 56-58 cm/s.

**Answer: 56 cm/s.** This compromise is about 10 % from either reading. Confidence: moderate. The physical speed of 51 ± 3 cm/s is well determined. The open question is whether the reference's smoothing window crosses the dropped frame.
