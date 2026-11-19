# q_2358 — height of the yellow toy (cm)

Video: lab capture, 24 fps (file and question_fps both 24), 1280x720, f = 0.5959*1280 = 763 px, c = (640,360).
Yellow toy = the "carrot" in depth_info (yellow corn/banana-like plush with a green leafy end, thrown by the
far person); the white object = the "jar". At t=0.60 s -> frame 14 (release of both objects), carrot 2.630 m,
jar 1.9735 m.

Reading of "height": the toy is elongated; height is taken as its long (end-to-end, leaves included)
dimension, as when it stands upright. Other reading (thickness across the body): ~7.6 cm
(minor width ~29-31 px at D~1.75-1.9 m, frames 20-23).

## Depth per frame (fit_traj.py, fit2.py)
Ballistic fit of both flight tracks (scene/ centroids, frames 15-23 yellow, 15-25 jar), each anchored at its
frame-14 back-projection with the given distance, |g| = 9.8 m/s^2, shared gravity direction fitted (2 angles) +
two 3D velocities. RMS 1.2 px. Jar ends at ~3.0 m at the catch (far person 3.24 m), yellow toy at ~1.70 m at its
catch (near person 1.58 m) -> consistent. Yellow D: 15 2.482, 16 2.345, 17 2.221, 20 1.920, 21 1.845, 22 1.783,
23 1.736, 26 1.702 m. Alternative frame sets change late depths by ~±3 %.

## Length (feret_blur.py, profile_len.py, measure_len.py)
Foreground = (R-B) > -25 (blue background R-B ~ -55, toy +10..+45; threshold near the mid level so motion
blur does not change the extent), component at the track centre, max Feret diameter, endpoints back-projected
onto the plane through the centre perpendicular to the viewing ray at the fitted distance. Endpoints checked
on zoomed frames (frames/ends.png, frames/profile.png).

| frame | Feret px | D m | length cm |
|---|---|---|---|
| 15 | 61.3 | 2.482 | 18.6 (leaves sticking out to the right) |
| 16 | 60.4 | 2.345 | 17.2 |
| 17 | 63.1 | 2.221 | 16.9 |
| 20 | 65.1 | 1.920 | 14.9 |
| 21 | 70.7 | 1.845 | 15.6 |
| 22 | 76.3 | 1.783 | 16.2 |
| 23 | 75.5-80.5 (axis profile, hand near) | 1.736 | 15.7-16.7 |
| 26 | 92.5-98.5 (axis profile, tip at the hand) | 1.702 | 16.9-18.0 |
(14, 19, 23-26 Feret merged with hands / the white object: not used.)

The toy tumbles, so each projection is a lower bound of the true length; the maximum, 18.6 cm (frame 15,
near the depth anchor so least model dependent), is the answer. Second route: late frames near the catch, with
depths from the gravity fit, rise to 16.9-18 cm as the toy turns side-on (one tip partly behind the hand).

Answer: 18.6 cm. Confidence moderate (~±10 %): tumbling (lower-bound nature), soft leaves, depth model.
