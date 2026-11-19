# q_275 – width of the black car (simulation_0124)

The prior is the black car's speed, 26.085 m/s. The video is a 2D top-down view at 24 fps (file fps equals question_fps,
so no re-timing). The black car is `dark_car` in scene/.

## Scale (from the prior)
- I took the dark_car track from scene/tracks and checked it: the per-frame steps are nearly constant from frame 2 on.
  The mean step over frames 3–45 is 27.01 px, the median 26.97 px, and the mean over frames 10–40 is 26.99 px
  (`mirror.py`). Tracking noise inflates path length slightly, so I use 26.97 px/frame = 647.3 px/s.
- Scale = 26.085 / 647.3 = 0.04030 m/px.

## Pixel width
- `prof2.py` takes three separate groups of frames: 4–12, 17–26 and 28–42. In each group the frames are rotated so
  the car is aligned and points right, upsampled 4x and averaged. The shadow direction is fixed in the world, so it
  lands on a different side of the car in each group.
- **Dark body outline:** the minima sit at about rows 36.5–37 and 81.5–82 where the car is widest (rear haunches).
  That is 45 px between the outline minima.
- **Outer edges** (`edge.py`): taken at the half-level crossing.
  - The top (unshadowed) edge is at row 35.0 ± 0.4.
  - The bottom edge is at row 84.5, but the cast shadow inflates it.
- **Centre line:** the midpoint between the headlights is row 58.25 in group B and row 59.0–59.1 in groups A and C.
- **Width:** twice the unshadowed half-width gives 2 × 23.25 = 46.5 px. The scene record says 46 ± 4 px, and the
  outline-minimum spacing plus about 1 px of edge gives 46–47 px.
- **Door mirrors:** none are visible beyond the body silhouette on the dark car. The silver car's mirrors add about
  5 px, but nothing like that is resolvable here, so the width is the body width.

## Answer
Width = 46.5 px × 0.04030 m/px = **1.87 m**. The range is 1.85–1.89 for 46–47 px; this reading includes no mirrors.

## Check
- The body length is about 117 px (scene record), which gives 4.72 m. A length/width ratio of 2.5 is typical for a
  sports car, so 1.87 m wide is plausible.
- A threshold mask on the background difference, on clean frames without shadow (frames 8–12), gives a width of
  47–49 px (blur included). That is consistent with 46.5 px.

**Confidence:** moderate–good, about ±3 %. The main risk is whether the reference bounding box includes the mirrors.
