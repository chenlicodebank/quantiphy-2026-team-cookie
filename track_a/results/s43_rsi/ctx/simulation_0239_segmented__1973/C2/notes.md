2D scene: scale from the brown horse (dark-red animal, SAM score 0.75 vs 0.40 for the tan one; its 152 px body then measures 2.08 m, a realistic horse). Horse pixel speed from linear fits over frames 0-48 (frame 49 is an animation reset): head edge 63.53 px/s, centroid 64.13 px/s -> 63.8 px/s, so scale = 0.874/63.8 = 0.01370 m/px. SAM 3 'house' mask spans 800 px horizontally (x 621-1420, whole three-tier structure) -> width = 800 x 0.01370 = 10.96 m. Second route with the centroid speed gives 10.90 m.

Final message:
Answer: **10.96 m** (house width).

Method summary:
- Identified the "brown horse" as the dark-red animal (SAM 3 score 0.75 vs 0.40 for the cream one; with that scale its body length is 2.08 m, a realistic horse, whereas the cream one would be only 1.37 m).
- Horse pixel speed from linear fits over frames 0–48 (frame 49 is an animation reset): head edge 63.53 px/s, centroid 64.13 px/s → 63.8 px/s.
- Scale = 0.874 m/s ÷ 63.8 px/s = 0.01370 m/px.
- SAM 3 "house" mask horizontal extent = 800 px → 800 × 0.01370 = 10.96 m (second route via centroid speed: 10.90 m).
