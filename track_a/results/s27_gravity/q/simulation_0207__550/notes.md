# q550 — length of the letter under the gun (simulation_0207)

The question and file both use 24 fps. There is no depth_info. I treated the scene as 2D, with one m/px scale taken from the prior (the typewriter's fall at 9.8 m/s^2).

## Object
The "letter under the gun" is the cream paper card lying flat on the desk to the right of the alarm clock, with a small pistol and a dark block resting on it. The scene record calls it "white_card_scissors". At frame 0 a colour mask (measure.py, frames/cardmask.png) gives a horizontal extent of x = 1193–1386 px. Seen in perspective, the card is a parallelogram:
- front edge: about 1197–1389 px (192 px)
- back edge: about 1192–1379 px (187 px)

I took the length as 190 ± 3 px. Its long side runs horizontally (left to right). It lies on the desk at about the depth where the typewriter landed, so the fall-plane scale applies.

## Scale
- Route 1, scene track (bbox centre): a quadratic fit over frames 0–9 gives 7268 px/s^2. The top and bottom edges give 6800 and 7700, but they are biased because the visible height of the typewriter changes as the viewing angle changes, so I used the centre.
- Route 2, template match (track2.py): tracking the keyboard area from frame to frame gives second differences of 12–13 px/frame^2, which is 7300–7320 px/s^2. Fits over frames 0–9 and 0–10 both give about 7300.

I adopted a = 7300 px/s^2, so the scale is 9.8 / 7300 = 1.342 mm/px.

## Answer
190 px × 1.342 mm/px = 0.255 m (range 0.251–0.258 m).

Plausibility check: the typewriter's width of 291 px comes out at 0.39 m, which is realistic for a portable typewriter. A letter or card about 0.25 m long is also realistic.

Confidence: fairly good. The main uncertainties are the card's edges (±2%) and whether the scene's origin is the typewriter's centre (±3%).
