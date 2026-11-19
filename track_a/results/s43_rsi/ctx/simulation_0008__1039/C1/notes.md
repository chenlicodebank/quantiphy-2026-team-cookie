# Q1039 – distance from the pier's outer end to the boat at t = 3 s (minimum distance)

**Answer: 5.68 m.** This is the 3D distance between the boat origin and the pier origin at t = 3 s, which is also the boat's closest approach to the pier.

## Inputs
- Prior: boat height 0.75 m. Depths: boat 7.452 m at t=0 and 6.655 m at t=1. Pier 11.579 m. Stairs 17.623 m.
- Video: 66 frames. The file's rate is 22.80 fps and the question's rate is 24 fps. I used **24 fps**, the
  question's rate, which is taken to be the original render's rate: t=1 s is frame 24 and t=3 s is frame 72. The
  clip ends at frame 65, so frame 72 is extrapolated. A boat cannot tell the two rates apart physically: the speed
  is 1.44 m/s at 24 fps and 1.37 m/s at 22.8 fps, and both are plausible. The answer barely depends on the rate
  (5.68 m at 24 fps, 5.75 m at 22.8 fps) because at t ≈ 3 s the boat is passing right in front of the pier.

## Method (scripts: solve_f.py, answer.py, scale_match.py)
- Boat track: I used the `bow_x` track from scene/tracks/boat.csv (template-tracked bow tip). It moves very
  linearly at about -10.3 px/frame. I take the boat origin as the centre of the box, at bow_x + 324 px (half of
  the 648 px full length measured in frames 55-65), with v at about 697.
- Camera is static. The vertical apparent size (hull height of 88 px, post-top to waterline of about 138 px) stays
  constant over the clip, so the boat moves at a constant camera depth z. Full-template scale matching
  (scale_match.py) was unreliable because the boat's appearance changes as the viewing angle changes, so I did not
  use it.
- Focal length: I assumed the principal point is the image centre and the depth z is constant. The two given boat
  depths (d = z·|(u−cx, v−cy, f)/f|) then fix f ≈ 1001 px and z ≈ 5.85 m. Check: 0.75 m gives 128 px. The visible
  height from post top to waterline is about 138 px, but it includes about 25 px of extra vertical extent because
  the camera looks down at the boat's near side. A small draft also fits, so the prior is consistent.
- Pier: the jetty deck centre is at pixel (549, 618-645). Back-projecting it to 11.579 m gives (0.10, 1.04, 11.53) m.
- Boat at frame 72: the extrapolated origin is at u ≈ 567-575, which gives (0.16, 0.92, 5.85) m.
  The distance is **5.68 m**. Sweeping over frames, the closest approach falls at frame 73 at 5.683 m, so the
  minimum distance and the distance at t = 3 s agree.

## Checks and sensitivity
- Linear, quadratic and late-window extrapolation of the bow all give the same result within 0.002 m.
- Moving the origin ±30 px along the boat gives 5.63-5.75 m.
- Using 22.8 fps instead of 24 fps gives 5.68-5.83 m.
- Pier origin row 618-645 changes the result by ±0.01 m.
- Main risk: "outer end of the pier" could mean the lakeward edge of the deck rather than the pier origin. The
  reference answers use origins, so I answered with the pier origin.

Confidence: moderate (about ±4 %, from the focal-length / origin-placement assumptions).
