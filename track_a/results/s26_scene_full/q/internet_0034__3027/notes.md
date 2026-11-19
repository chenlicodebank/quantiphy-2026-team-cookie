# q_3027 – average speed of the toilet roll, 0.5 s to 1.73 s (cm/s)

## Scale
Prior: roll size = 100 mm. The roll is seen side-on: its length end to end (horizontal, along the motion) is
589-593 px, and its diameter (vertical) is ~697 px. A real roll is ~10 cm wide and ~11-12 cm across, so 100 mm
is the length. That is also the "pixel length along the main motion direction" the annotators used.
Scale = 10 cm / 591 px = 0.01692 cm/px (frames 49-59; frames 13-34 give 593 px, within 0.4 %).
Diameter reading (not used): 10/697 would give ~9.2 cm/s.

## Time base
File fps = 24.098 (60 frames); question_fps = 30. The odd file rate points to a re-timed clip (60 frames of 30 fps
footage = 2.0 s). I used 30 fps (the original footage), giving frames 15 to 52. A hand sliding a roll onto a holder
is plausible at either rate, so physics cannot decide between them.

## Measurement
Static camera (scene record: shift <= 0.3 px). The roll track is scene/tracks/toilet_roll.csv, with edge-refined
corners. I checked the overlays on frames 12, 15 and 52 (frames/ov*.png), and they match the silhouette.
measure.py:
- Centre point: mean of per-frame speeds = 10.96 cm/s; net displacement / time = 10.65 cm/s.
- Left end-face midpoint (second, independent reference point): 11.14 / 10.59 cm/s.
- At 24.098 fps (frames 12 to 42) the same method gives 9.5-9.8 cm/s, about 12 % lower.
Path length runs slightly above net displacement because of a small real downward curve (the roll settles on
the rod) plus corner jitter.

Answer: 10.8 cm/s. Confidence is moderate. The main risk is the fps choice (±12 %); the measurement itself is
good to about ±3 %.
