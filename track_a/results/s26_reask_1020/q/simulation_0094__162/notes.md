# q_162: length of the plane (m)

Prior: car speed = 30 m/s. 2D side-view scene, 24 fps (the file rate and question_fps are the same). depth_info is not given.

## Method (measure.py)
- I re-segmented every frame by colour difference from the background (threshold 20) and split the two objects at y = 590.
- **Car pixel speed** (linear fits over its unclipped frames 11–37):
  - rear edge: 28.52 px/frame
  - front edge: 28.26 px/frame
  - scene origin proxy: 28.39 px/frame
  - I used the mean, 28.39 px/frame = 681.4 px/s.
- **Scale:** 30 / 681.4 = 0.04403 m/px.
- **Plane length:** the bbox x-extent (nose tip to tail tip) is 853–855 px at frames 29–37, near the image centre. The larger values at frames 22–28 (up to 874 px) are perspective inflation off-centre. I used 854 px.
- **Plane length** = 854 × 0.04403 = **37.6 m**.

## Checks
- An A320 is 37.57 m long, so this matches a real airliner (the plane is an Air China A320-like).
- The car is 130 px near centre, which gives 5.72 m. A Cybertruck is about 5.68 m, so the car is plausible too, and a single scale fits both objects.
- The scene-record values agree with my re-measurement to within 1 px.

Confidence: high (about ±1 %).
