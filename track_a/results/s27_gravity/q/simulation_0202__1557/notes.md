# q1557 – length of the table (desk), simulation_0202

The file and the question both use 24 fps. This is a 3D Blender render with a static camera.

## Desk corners (frame 29, brightened crops: bright.py, frames/*.png)
- Near corner of the top (front-left, closest to the camera): (698, 880) px. Given distance: 3.593 m.
- Front-right corner (far right in the image): (1980, 641) px. Given distance: 5.009 m.
- Left-back corner: (468, 688). Back-right corner: about (1595, 528), behind the telephone.
- The long side (length) runs from the near corner to the front-right corner. The short side runs from the near corner to the left-back corner.
- The scene.json desk corner coordinates were partly wrong. It placed the back-right corner at (1900, 530), but that point is wall shadow. Its front-left corner was also loose.

## Focal length and pitch (principal point at the image centre)
1. Fall fit (fitfall.py, final.py). The magnifying glass track over frames 0-10 starts at the given distance of 4.2401 m and falls with g = 9.8.
   - Fitting the fall alone gives f = 2620-2680 px and a pitch of 13-17°.
   - Focal length and pitch are partly correlated in this fit, but f stays within 2620-2810 for any pitch from 0 to 30°.
2. Desk rectangle (rect.py). The near corner is put at 3.593 m and the other corners on the same horizontal plane.
   - A right angle at the near corner requires a pitch of about 13°.
   - At that pitch, the front-right corner lands at 5.010 m on the plane. This reproduces the given 5.009 m, which confirms that "far right" means the front-right corner.
3. Joint fit (fall + right angle + 5.009 m): f = 2590-2620 px, pitch 13.1-13.2°, fall rms 0.5 px. Horizontal field of view is about 44°.
   - Check: the glass at t = 0.5 s (4.4097 m) lies about 1.5 cm above the desk-top plane, which fits a glass resting on the desk.

## Length
- Route 1: 3D distance between the two corners, back-projected with their given distances.
  - f = 2590: 2.49 m. f = 2620: 2.47 m. Over f = 2550-2700 the result is 2.43-2.51 m.
- Route 2 (independent of the second distance): the desk-plane intersection at a 13° pitch with f = 2620 gives a front edge of 2.47 m.
- **Answer: 2.48 m.**

## Plausibility
2.5 m is large for a real desk. The other objects also look about 1.3-1.5 times real size: the magnifying glass is about 0.30 m, the typewriter about 0.5 m. The scale here comes from the given distances and the gravity prior, which agree with each other, so I kept it.

## Confidence
Medium-high. The answer moves about ±3% with focal length and ±1-2% with corner picking (±3 px).
