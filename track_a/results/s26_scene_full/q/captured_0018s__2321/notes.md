# q_2321 – velocity of the box (white carton) at 3.4 s, cm/s

## Time-base problem (main uncertainty)
The file is 49 frames at 24 fps (0–2.0 s), and question_fps is also 24. t = 3.4 s would be frame 82, which is not in
the clip. The free fall agrees with real-time 24 fps (pixel acceleration ≈ 3.6–4.6 px/frame², about what g gives at
Z ≈ 2.8 m), so the clip has not been sped up or decimated. It seems to be a trimmed piece of a longer recording.
The answer has to be positive, so the box must be moving at 3.4 s. Here it moves only while falling (f29–f39) and
tipping (f39–48). I assumed the clip starts 2.0 s into the original (exactly 48 frames). That puts 3.4 s at clip
frame 34, in the middle of the fall. **This mapping is an assumption, and the answer depends on it.**

## Measurements (scene/tracks/white_carton.csv; checked visually on frame 34)
- Box released at f29. Lands upright at f39, then tips to the left.
- A frame is dropped between f35 and f36, so every falling object makes a double step there. With one frame inserted,
  a parabola fits the f34–38 points to an rms of about 0.6 px. Without it the rms is about 8 px.
- Parabola fit (fit2.py, clean frames f34–38, frame numbers corrected for the dropped frame): pixel velocity at
  f34 = 27.5 px/frame, a = 3.6 px/frame².
- Raw forward difference f34→f35 = 29.5 px/frame (fit value at 34.5: 29.3).
- Box depth was not given. Two routes give about 2.8 m:
  1. A ground-plane model: the far person's shoes are at row 577 at 3.13 m, so camera height ≈ 0.89 m. The box
     lands upright with its bottom at row ≈ 603, which gives Z ≈ 2.80 m.
  2. The box and the soccer ball (2.8 m) are held side by side by the same person and fall with similar pixel
     accelerations (ratio ≈ 1.05). That gives Z ≈ 2.8–2.95 m.
  I used Z = 2.8 m.
- v = 29.3 px/frame × 24 × 2.8 / 763 = 2.58 m/s, so **≈ 258 cm/s**. The parabola's instantaneous value at f34
  gives 242 cm/s.

## Second route
Gravity: the time since release, about 5–6 real frames (0.21–0.25 s), × 9.8 gives 2.0–2.5 m/s. The release instant
is uncertain because the hand covers the box, so this broadly agrees.

## Confidence
Low. The pixel measurement and depth are probably good to about 10 %, but the 3.4 s → clip frame mapping is a guess.
