# q_1714: acceleration of the orange car at t = 2 s

The file and the question both run at 30 fps.

## Finding: the car is not in this video
- The segmented video shows only the basketball player and the red ball on a plain white background. This matches scene/notes.md, which mentions no vehicles.
- probe.py looks for orange and green pixels. The only orange-ish pixels are the ball and the player's skin. There are no green pixels.
- probe2.py looks for any non-white pixel (min(RGB) < 245) outside the player and ball region. It found **0 pixels in every frame from 0 to 127**. Frames 128 and 129 are all black.
- So the orange and green cars named in depth_info were removed along with the background when the video was segmented. The car's motion cannot be measured in pixels.

## What depth_info gives
- Orange car: 10.1755 m at 1.5 s and 10.4022 m at 2.0 s, so its camera distance grows by 0.227 m in 0.5 s (about 0.45 m/s along the line of sight).
- Green car: 4.3204 m at 2.5 s and 6.9142 m at 3.0 s, about 5.2 m/s along the line of sight.
- Two distances to one car cannot determine its acceleration: its direction of motion and its start time are unknown.

## Estimate (this is a guess, not a measurement)
- Assume uniform acceleration from rest at t = 0.
  - The green car's change in distance then puts its acceleration at 1.9 m/s^2 or more.
  - The orange car's change in distance only puts its acceleration at 0.26 m/s^2 or more, because it can move largely across the line of sight.
- I answer **2.0 m/s^2**, a typical car acceleration that agrees with the green car's lower bound. I chose a value on the low side because an overestimate is penalised more heavily than an underestimate.

## Confidence
Very low. There was no second-route check, because the object does not appear in the video.
