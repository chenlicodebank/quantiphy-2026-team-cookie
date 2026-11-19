# q_2324 – pineapple toy velocity at 3.4 s (cm/s)

## Main problem: 3.4 s is outside the clip
The clip has 49 frames at 24 fps (0–2.04 s; question_fps = file fps = 24). 3.4 s would be frame 82, which does not exist.
The container has no start-time offset (pts start at 0). This is the segmentation version ("…s", background replaced
by SAM2), so it was most likely cut from a longer original recording, and the question time uses the original's timeline.
That offset cannot be recovered from the clip, so the frame the answer refers to is a guess. This is the main uncertainty.

The time scale is real-time. The soccer ball (depth 2.8 m) falls with 4.3–5.0 px/frame², and real gravity predicts
9.8·763/(2.8·576) = 4.64 px/frame². So the clip is not slowed down or sped up. Its frame timing is irregular, though:
there are dropped or double steps (f35→36, and the pineapple jumps about 30 px between f27 and f28).

## Pineapple (scene "yellow_fruit")
The right (near) person holds it close to her body. Release is at about f27 and it lands at f36 (bottom y≈697). After
that it tumbles slowly (under about 1 m/s).

Depth: no depth is given for the pineapple, so I estimated it two ways:
- **From the floor plane.** The people's shoe rows give a camera height of about 0.85 m: the far person gives
  0.284·Z and the near person gives 0.467·Z, and both work out to 0.85 m. The pineapple's ground contact at y≈697 then
  gives Z≈1.92 m, which agrees with the near person's distance of 2.0 m.
- **From the free-fall pixel acceleration.** This gives about 2.3 m. It is noisy because of the irregular frames.

I used Z≈1.92 m, so the scale is 1.92/763 m per px, and 1 px/frame ≈ 0.060 m/s.

Vertical pixel steps during the fall (bbox centre):

| Frames | Step (px) | Speed (m/s) |
|---|---|---|
| f30→31 | 33.5 | 2.0 |
| f31→32 | 39.5 | 2.4 |
| f32→33 | 47 | 2.8 |
| f33→34 | 55 | 3.3 |
| f34→35 | 53 | 3.2 |

The fall height is about 430 px, roughly 1.07 m, which gives an impact speed of about 4.6 m/s.

## Answer
The question's gravity prior implies the asked moment is during the free fall. I took the middle-to-late part of the
fall, around f32–33, smoothed over 5 frames: about 2.8 m/s. The check v = g·Δt from the fitted fall start (about f25)
gives 9.8·7/24 = 2.86 m/s at f32, which agrees.

**Answer: 280 cm/s.**

Confidence: low. The measurement itself is good to about 10%, but the frame that 3.4 s refers to is unknown. The true
value could be anywhere from about 1 to 4.6 m/s during the fall.
