# q1040 – width of the wooden stairs (m)

**Answer: 1.9 m**

## Object
The "wooden stairs" are the short flight of steps under the boathouse, leading from the grass up to the deck. They have two light
newel posts at the bottom and horizontal treads behind them, at about x 490-600 and y 525-580 in frame 0. The camera is static.
The stepped platform in front, at the water (x 458-638), is the "pier" (depth 11.579 m). The given 17.623 m stairs depth places the
stairs behind it, which agrees with this identification.

## Pixel width (stairs_profile.py, frame 0, row and column grey profiles)
- Newel posts: the left post's outer edge is at x≈499.5 and the right post's outer edge at x≈599.5, so the posts span **100 px**.
- The treads start at x≈490-492 on the left (left of the left newel) and end at about 585-588 on the right. The two newels sit about
  10 px to the right of the treads, either because the model is asymmetric or because the stairs are slightly yawed.
- The full horizontal extent (an axis-aligned box over the treads and newels) is x≈489-600, about **110 px**.
- I used 108 ± 5 px, leaning towards the full-object extent.

## Focal length (focal.py)
The boat moves across the image at constant depth: its apparent length and hull height stay constant within about 2%. Its
Euclidean distance therefore changes only because of its sideways image position:
d² = Z²(1 + r²/f²). The two given depths, 7.452 m at t=0 and 6.655 m at t=1, give two equations for the unknowns f and Z.
- Time base: question_fps is 24 (a Blender render rate). I took t=1 s as frame 24, since the reference follows the original timing.
- The boat origin is the centre of the full boat box: bow_x + 645/2 px, with v at the box centre.
- Result: **f ≈ 999 px**, Z_boat ≈ 5.86 m.
- Sensitivity: frame 23 to 25 gives f 972-1025. Moving the origin ±10% of the boat length gives f 965-1028. Putting the origin at the
  waterline instead of the box centre lowers f by about 18 px.

## Size
The stairs are near the image centre (r ≈ 16 px), so Z ≈ 17.62 m.
W = 108 × 17.623 / 999 ≈ **1.90 m**.
- Reading the width as newel to newel (100 px) gives 1.76 m.
- Reading it as the full extent (110-112 px) gives 1.94-1.98 m.

## Second-route check
- **Boat height:** with f = 999 and Z = 5.86, a 0.75 m tall box spans 128 px. The visible boat (stem-post top y 620 to near-side
  waterline y 757) is 137 px. This fits a level camera about 1.1 m above the water: the near-side hull projects lower, and the boat
  has a small draft. Solving that model gives a post top about 0.67 m above the water, i.e. about 0.08 m of draft. The result is
  consistent with f ≈ 1000, but it is not a tight independent constraint.
- **Boat length:** 645 px corresponds to 3.78 m, giving a length-to-height ratio of about 5 for a rowboat with stem posts. This is
  plausible.

## Ambiguity
The stairs' run (front to back) is unknown, though the rise is about 55 px ≈ 0.97 m. If "width" is read as the shorter horizontal
extent, it could instead be the run, which is probably about 1.2-1.7 m. I answered with the conventional across-the-steps width.

## Confidence
Moderate, about ±8%. The main error sources are the pixel extent (100-112 px) and f (965-1028).
