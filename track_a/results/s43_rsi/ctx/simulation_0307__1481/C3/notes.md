# Q1481 – length of the plane (m)

Prior: speed 22.16 m/s. depth_info: 102.6664 m at t=1 s (frame 24) and 121.8263 m at t=2 s (frame 48). question_fps = file fps = 24.
The camera is static and frames 0 and 1 are identical. A VTOL gunship (twin long pods, a central fuselage with a canopy, wings with
ducted fans, wingtip fins and a ventral fin) flies up-left in the image and away from the camera with a constant attitude.

## Where the candidates part ways
- C1 (17.4) answered with the **wingspan**. The conventions say an aircraft's length runs nose to tail and that a wingspan is never its
  length, so C1's reading is rejected. C1's own nose-to-tail figure was 13.2 m. Its aft points (ventral-fin bottom, "fuselage end") were
  triangulated from frames 24–71 only, which is poorly conditioned in depth: those points come out about 4 m behind the pod tips.
  In the image, though, the fuselage end lies forward of the right pod tip along the projected body axis, and the ventral fin's trailing
  edge is vertical under it. So the pod tips are the rear-most points.
- C3 (15.9) took PCA extents of the silhouette, which mix span and length.
- C2 (10.7): pod front corner to pod rear tip, from a bundle adjustment with constant velocity. I agree with this reading.

## My measurement
- Constant-velocity fit of the hull centroid with |V| = 22.16 and both depths (fitf.py): f = 3400 px, V_cam = (-10.6, -6.3, 18.4) m/s,
  rms 2.3 px. With the bbox centre as the origin, f = 3296.
- I checked C2's clicks on CLAHE zooms (crop.py, predcrop.py). LF is the left pod's front corner: frame 2 (1392,787), frame 24 (1068,595),
  frame 48 (810,449). LR is the left pod's rear tip: (1601,971), (1218,734), (920,551) and frame 71 (709,422).
  The right pod tip matches C1's clicks.
- Triangulation of each feature moving with the common V (tri.py): LF–LR = 10.40 / 10.55 / 10.70 m at f = 3300 / 3400 / 3500.
  The axis is about 7.6° from the flight direction. The canopy, antenna and fin tops all fall behind LF along the axis.
- Joint fit (joint.py) of f, V direction, the origin (hull centroid plus both depths), LR (NCC track over frames 2–71) and the LF keyframe clicks:
  f = 3315–3343 and L = 10.97 m, with rms 0.9 px (LR) and 2.0 px (LF). With f fixed at 3300–3500, L = 10.91–11.00.
  Using the automatic LF track gives 10.0–10.1 m, but that track drifts on the low-contrast corner (checked visually at frames 48 and 71),
  so I gave it little weight.
- Range of the credible routes: 10.4–11.0 m. C2's bundle adjustment gave 10.6–11.0.

## Answer
Nose-to-tail length ≈ **10.8 m**, the pod front to the pod rear tip, measured along the body axis.
Caveats:
- If the reference is a world-axis box of an aircraft that is yawed or pitched in the world, the value could differ by a few percent.
- The wingspan reading would be about 17.4 m (C1), but the convention excludes it.

Confidence: moderate.
