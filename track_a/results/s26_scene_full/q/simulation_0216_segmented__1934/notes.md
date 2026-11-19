# q1934: length of the floor mirror (m)

The video is 2D and seen side-on. The file and the question both give 24 fps, so no re-timing was needed. The prior is the black cat's speed, 0.94 m/s.

## Scale (speed.py)
The cat walks at a steady pace, and I took its speed from the track in scene/tracks/cat.csv. The net displacement per frame was 17.64 px for `cx`, 17.83 for `dark_cx` and 17.60 for `bbox_cx`. A linear fit gives 17.65, 17.80 and 17.56. I used 17.7 px/frame, which is 424.8 px/s.
The scale is 0.94 / 424.8 = 0.002213 m/px.
The mean per-frame step is about 1% higher (17.9) because of gait jitter in the centroid. Using it would change the answer by about 1%.

## Mirror (mirror.py)
I took the per-pixel maximum over all frames, which removes the cat, and found the non-white extent of the mirror. It spans x 1580 to 1845 (266 px) and y 390 to 967 (578 px). These match scene/static_objects.json. The mirror leans: its right edge slants about 30 px over its height, so the length along the slant is still about 578 px.
I read "length" of a floor mirror as its long side, which here is the vertical extent:
578 × 0.002213 = 1.28 m. The width would be 266 px, or 0.59 m.

## Check
The cat's body without the tail is about 260 px, which gives 0.58 m. The 1.28 m mirror is about 2.2 times the cat's body length, which is a plausible size for a floor mirror. One caveat: the mirror's base (y 967) sits a little higher in the image than the cat's paws (y 1021), so the mirror may stand slightly behind the cat. That would make it slightly larger in reality, but I used a single scale, following the 2D convention.

Confidence: moderate. The scale is good to about 2%. The main risk is how "length" is meant: if it means the horizontal width, the answer would be 0.59 m.
