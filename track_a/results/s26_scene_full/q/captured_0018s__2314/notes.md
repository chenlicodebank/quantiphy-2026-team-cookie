# q2314 – distance between the two people (cm)

Lab video, 24 fps (file and question rate agree), 1280x720. Camera: f = 0.5959*1280 = 762.8 px, principal point (640,360).
The prior (g = 9.8) is not needed. The scale comes from depth_info: far (left) person 3.130 m, near (right) person 2.002 m.

Method (`measure.py`): foreground mask = |frame - per-row background| (the background is a synthetic vertical gradient). For each person,
the centre is x = mean column of the body below the arms (torso and legs) and y = midpoint of head top to shoe bottom. I checked the mask
and the centres on `frames/mask0.png`. I back-projected the ray ((u-cx)/f,(v-cy)/f,1), normalised it, and scaled it by the given
Euclidean depth.
- f0: left (381.5, 375.5), right (992.5, 408.5) → 217.3 cm
- f12: 217.1, f24: 216.7 (people stand still). I did not use f48 because the fallen carton merges into the left person's mask.
- Second route: full-mask centroids, left (384.4, 372.0) and right (994.7, 407.0) → 217.1 cm.
- Reading the depth as z-depth instead of Euclidean distance gives 228 cm. I used the Euclidean reading, per the convention.
- Sanity check: the heights come out at 404 px*3.13/f = 1.66 m and 613 px*2.002/f = 1.61 m. Both are plausible and consistent, which supports the depths.

Answer: 217 cm. Confidence: good (about ±3%, mostly from where the "centre" is defined).
