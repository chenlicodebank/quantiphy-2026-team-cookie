# q_2800 — height of the trash bin (cm)

File fps 24 = question_fps 24. The bin (blue recycling bin, centre about (729,534)) does not move. f = 0.5959 x 1280 = 762.8 px,
principal point (640,360). Given distance from the camera to the bin = 2.977 m; Z on the optical axis = 2.977/1.0335 = 2.88 m.

## Pixel measurements (code: measure_bin.py, rim_profile.py, widths.py)
- The silhouette's vertical extent is the same in every frame: top 484.5 (back rim), bottom 591 (front bottom edge).
  That is 106.5-107 px.
- A bright line at y = 497-498 is the front rim. The band from 485 to 497 is the top opening seen from above. The camera
  is about 0.85 m above the floor (from the basketball's floor contact and the bin's bottom), so it looks down onto the rim.
- Front face (front rim to bottom): 93.5 px.
- Rim width ≈ 95 px (680-775). Bottom width ≈ 76 px (the bin tapers).

## Height under each reading
- Whole silhouette x given distance / f: 107 x 2.977 / 762.8 = 41.8 cm. This is too high because it includes the top
  opening seen from above.
- Front face x Z (2.88 m): 93.5 x 2.88 / 762.8 = 35.3 cm. Using 2.74 m for the front plane (centre minus half the bin's
  depth) gives 33.6 cm.
- A 3D check with a level camera fits well: the floor is about 0.83-0.87 m below the camera from both the bin bottom
  and the basketball, and the opening's front-to-back depth comes out at about 0.29 m.

## Second route
The bin has the shape of a standard deskside recycling bin, with a height/width ratio of about 1.04 (front-face height
roughly equal to the rim width in px). Its rim width is 95 px x 2.88 / 762.8 = 36 cm, which gives a height of about
1.04 x 36 = 37.5-38 cm.

## Answer
38 cm. This falls between the front-face measurement (35) and the full silhouette (42) and matches the ratio route.
Confidence: moderate, ±8%.
