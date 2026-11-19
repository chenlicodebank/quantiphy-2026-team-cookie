# q_2890: orange ball (basketball) displacement, 0.5 s to 1.0 s

- question_fps = file fps = 24, so t=0.5 s is frame 12 and t=1.0 s is frame 24.
- Orange ball = the basketball in scene/. It is unoccluded and "good" in both frames.
- I re-measured it in measure.py with an HSV orange mask and the largest component, and drew the overlays in frames/check_12.png and check_24.png. The masks cover the whole ball.
  - f12: centroid (716.4, 536.4), diameter from area 77.5 px
  - f24: centroid (537.6, 385.8), diameter from area 62.5 px
  - These match the scene record to within 0.1 px.
- Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
- Back-projection: I took the unit ray through each centre and multiplied it by the given Euclidean distance (2.24 m at f12, 1.81 m at f24).
  - Displacement = **0.741 m**.
  - If the given distances were read as z-depth instead, the result would be 0.782 m. depth_info is defined as the Euclidean distance, so the answer uses 0.741.
- Second route: the pixel displacement is 233.7 px. At a mean distance of about 2.0 m that is about 0.61 m sideways. Combined with the 0.43 m change in distance, this gives about 0.75 m, which agrees.
- Caveat: the ball's apparent size shrinks (77 to 63 px), which suggests it is moving away from the camera, but depth_info says it gets closer (2.24 to 1.81 m). I followed the given depth_info, as the method card requires. If the depths were scaled from the apparent size instead, the answer would differ. Confidence: moderate.
