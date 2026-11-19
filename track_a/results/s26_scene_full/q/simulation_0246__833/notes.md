# Q833: length of the rabbit (m). Prior: antelope (kudu) speed = 1.277 m/s

2D top-down render, 30 fps. The file's fps and question_fps are both 30, so no re-timing. Camera is static. Both animals walk in +x along straight rows. The "rabbit" is the small orange animal with a pale grey head (the record calls it the "rodent").

## Scale (from the antelope speed)
- Pixel speed of the kudu (scene/tracks/kudu.csv, net displacement over frames 0-74): core 9.08 px/frame, rump (trunk_x0) 9.14, whole-mask centroid 9.36, trunk centre 9.45, nose 9.47.
- Independent check (kudu_speed.py): template matching of the hip and mid-back texture over 30-frame gaps gave 9.14-9.37 px/frame for the hip (mean 9.21) and 9.27-9.48 for the mid-back (mean 9.39). I discarded the long-gap matches that failed (false matches).
- Adopted 9.3 px/frame = 279 px/s, uncertain by about ±2%. Scale = 1.277 / 279 = 0.00458 m/px.

## Rabbit length (measure3.py)
- The scene record's mask covers only the orange fur (median 67 px) and misses the pale head. I segmented the orange fur by chroma (B/R < 0.5) and the head by G/R < 0.85 at bright intensity, kept only the parts joined to the body, and checked the result on overlays and 5x crops.
- Frames 0-26 (head detected reliably): nose-to-rear x extent has median 92 px (mean 94, range 84-111; the stride changes it). The head adds a median 24 px beyond the orange fur.
- After frame ~30 the lighting makes the head too faint for the threshold. A visual read at frame 60 (1451 → ~1535) gives ~85 px, which agrees within a few px.
- Adopted 91 px (nose to rear, the longer horizontal extent).
- Length = 91 × 0.00458 = 0.417 m, about 0.42 m.

## Sanity check
On the same scale, the kudu's body is ~2.3 m (3.1 m including the tail), and a rabbit is about 0.4 m long. Both are plausible.

Confidence: moderate, about ±7%. The pale head edge and the choice of pelvis reference for the kudu speed dominate the uncertainty.
