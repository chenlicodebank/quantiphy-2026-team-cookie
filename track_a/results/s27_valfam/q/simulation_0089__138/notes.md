# q_138 – wingspan of the small bird (bird B, crow-like, flies right)

The file and the question both run at 24 fps. The scene is 2D, seen from directly below, with a static camera, so one m/px scale applies.
Prior: the small bird's length is 0.94 m. Its length runs along image x and is stable at 107–108 px in frames 0–8 (half-contrast threshold; 109–110 px with the faint antialiasing included).
Scale = 0.94 / 108 = 0.0087 m/px.

I measured wingspan as the y extent of the mask in `measure_b.py` (|diff| against the empty-sky frame 20, thresholds 18 and 40). By frame, 0–8:
169, 169, 198, 204, 199, 173, 133, 161, 169 px. The wings flap, giving a min of 133 px and a max of 204 px.
The question gives no min or max. I used the rest/first-frame pose (frames 0–1, when the bird is still), which is also the median over frames 0–8: 169 px.
Wingspan = 169 / 108 × 0.94 = 1.47 m (1.44 with the thr-18 length of 110 px; 1.485 with the record's 107 px).

Second route: the record in scene/ gives the same numbers (169 px wingspan, 107 px length, so 1.485 m). Averaged over all frames the result would be about 1.52 m.
Confidence: the pixel measurement is good to about 2 %. The main uncertainty is which wing pose the reference uses: max 1.78 m, min 1.17 m.
