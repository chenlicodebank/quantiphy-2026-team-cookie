# Q8: height of the person (m). Answer: 1.73 m

The file runs at 29.9977 fps and question_fps is 30. That makes no difference here, because the question asks for a size.

## Why gravity gives no scale here
The ball's pixel motion does not show constant acceleration in any phase (numbers from scene/tracks/ball.csv):
- Flight, frames 21–78: vertical acceleration is about 0.17 px/frame², and the horizontal speed falls steadily from 11 to 1 px/frame.
- Drop below the net, frames 99–119: the drop speed levels off at about 13 px/frame. Early on the acceleration is about 1 px/frame², and later it is about 0.
- Bounce, frames 120–126: rising 29 px in 3 frames would need g of about 5900 px/s².

If 9.8 m/s² is applied to these, the person comes out anywhere from about 0.6 m to 14 m. The person's hop, frames 8–12, does not fit 9.8 m/s² either. The motion is animation, not physics, so I did not take the scale from the prior. I took it from a standard object instead, the regulation basketball (diameter 0.24 m).

## Measurements
- Ball diameter near the player, frames 21–34 (just after release, about the player's depth): circle fit median 29.2 px. Free-flight median over frames 25–77: 29.6 px. I used 29.3 px, which gives **122 px/m**.
- Person's standing height in pixels (frame 105, also frames 49–130). My scripts are feet.py and feet2.py, and feet_cmp.png shows the crop:
  - Head top: dark hair starts at row 583. Rows 580–581 are the bright window frame.
  - Shoe soles end at row about 793–794. Below that is the wet-floor reflection.
  - Height = about 211.5 px.
  - The record's bbox, y 588–811 (224 px), is wrong at the bottom: its cut at 811 includes part of the shoe reflection.
- Height = 211.5 / 122 = **1.73 m**.

## Check
- If I keep the record's 224 px, the height is 1.84 m. Both values fall inside the plausible adult range of 1.5–2.0 m.
- I chose 211.5 px because the zoomed crops clearly show where the soles end.
- If the ball's diameter is 0.239–0.245 m, the answer moves to 1.72–1.77 m.

Confidence: moderate. The main uncertainties are the ball scale (about ±3%) and the exact foot and head rows (about ±2 px).
