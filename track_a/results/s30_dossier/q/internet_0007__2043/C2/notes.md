Dark-blue (only dark) car tracked over frames 1-127: mean 11.87 px/frame at 30 fps = 356 px/s (linear-fit route 359 px/s). 2D scale from the prior: the visible paved strip is 75 px wide and 3.66 m maps to it (0.0488 m/px), which makes the car 3.5 m long and gives 63 km/h - the alternative lane-half reading would make the car 7 m long at 126 km/h. Speed = 356 x 0.0488 = 17.4 m/s.

Final message:
**Answer: 17.4 m/s**

Method summary:
- **Object**: only two vehicles exist — a dark-blue car (northbound, left lane, frames 0–131) and a white car. The dark-blue car is the only dark/"black" car.
- **Pixel speed**: SAM-verified track, mean backward difference of the bbox centre over frames 1–127 = 11.87 px/frame → 356 px/s at question_fps 30 (linear-fit route 359 px/s, 0.8% apart).
- **Scale**: the paved strip is 75 px wide (measured from a brightness cross-section); the prior 3.66 m lane width maps to that strip (0.0488 m/px). This makes the car 3.5 m long and 63 km/h, whereas the half-road reading would make it 7 m long at 126 km/h; painted STOP letter height (~2 m) and centre-line width (~0.1 m) independently support the chosen scale.
- **Result**: 356 × 0.0488 ≈ 17.4 m/s (second route 17.5 m/s).
