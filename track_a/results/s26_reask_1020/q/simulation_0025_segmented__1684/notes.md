# Q1684 — length of the eagle (m)

Time base: question_fps = 24 (file is 25 fps); t=1 s -> frame 24, t=2 s -> frame 48.

## Scale (focal length)
- The person's distance stays at 114.83 m at both times, but the body visibly walks. Crops (frames/human.png) show a
  front/back view, so the person walks mostly along the line of sight. The image x drift is only ~13 px/s, so the
  speed prior (1.3 m/s, mostly radial) gives no usable focal length: treating the motion as sideways would make the
  person 5.4 m tall, which is impossible.
- I therefore took the scale from a standard adult. Measured pixel height (human.py; faint head included) is about
  54.5 px. With H = 1.75 m: f = 54.5 x 114.83 / 1.75 = 3576 px.
- Check: lateral speed = 13 x 114.83 / 3576 = 0.42 m/s, which leaves about 1.23 m/s radial. That is consistent with
  the front/back view, the slight growth in apparent size (52 -> 55 px) and the feet moving down the image.

## Eagle geometry (bird3d.py)
- 3D positions: ray(u, v, f) x depth, with depth linear in time through the given values (116.05 m at frame 24,
  108.28 m at frame 48).
- Velocity (8.2, 0.1, -7.9) m/s, speed 11.4 m/s (plausible). The bird flies about 42-53 deg off the line of sight,
  toward the camera and to the right.
- Seen from this angle, both the body axis and the wing axis project horizontally in the image.
- Wingspan check: the bbox width at flat-wing frames, corrected for foreshortening, gives 2.1-2.5 m. That is
  realistic for an eagle, so the scale is consistent.
- Length: at the wings-raised (V) frames the wings are near vertical, so the horizontal extent is the body
  (beak-to-tail) projection.
  - Frames 23, 24, 25, 48: 22, 24, 24, 28 px, which gives 1.00, 1.09, 1.08, 1.10 m after dividing by sin(theta).
  - These are slight overestimates: about 1 px from the inclusive anti-aliased bbox, plus the wing chord.
  - Best estimate is about 1.0 m.
- Second route: the narrowest frame of the first cycle (frame 6, 24 px) gives 1.2 m, an upper bound. A typical eagle
  is 0.8-1.0 m long with a 2.0-2.3 m wingspan; the length/span ratio of ~0.45 matches.

## Answer
1.0 m.

## Confidence
Moderate (about ±15%). Main error sources:
- f depends on the assumed person height (1.75 m).
- The body is foreshortened, and the body extent is mixed with the wing chord at only ~22-28 px.
