# q_2654 — diameter of the soccer ball (cm)

Prior: basketball diameter 23.2 cm. depth_info: t=0.9 s (frame 22) soccer 2.4770 m, basketball 2.7777 m;
t=1.4 s (frame 34) "soccer 2.6020 m" and "soccer 2.3730 m" (one label is evidently a typo for the basketball).
File fps = question fps = 24. Lab camera: f = 0.5959 x 1280 = 763 px.

## Pixel diameters (own measurements; scripts in this folder)
The video is a SAM composite on a synthetic gradient background, so ball silhouettes are pixel-sharp
(diff-to-median-background jumps from <=7 to >100 at the edge, `dbg.py`). Methods: `maskfit.py` (silhouette mask,
area-equivalent / LSQ circle / Feret width perpendicular to the motion, thresholds 10/20/40), `profile.py`
(band profiles), `measure.py`/`radial*.py` (directional widths; the radial max-gradient variants were biased by
inner panel edges / halo and were discarded). Overlays: frames/dbg_*_21.png, frames/ov_*_21.png.

- Soccer ball, frames 20-23: silhouette area-equivalent 59.3-60.6 px (T20), LSQ circle 59.5-62, scene circle fit
  60.8; perpendicular-to-motion width ~59-60. Silhouette is slightly lumpy (SAM), true circle ~60.3 px at frame 22.
  At frame 34: ~59.8-60 px (nearly the same apparent size as at frame 22).
- Basketball, frame 21-22: ~63.5-65 px (horizontal 60-62, vertical ~68: silhouette slightly egg-shaped, dark
  lower fringe included). Check of the prior: 2.7777 x 63.5-65 / 763 = 23.1-23.7 cm vs 23.2 given -> scale OK.

## Soccer diameter
- Route 1 (t = 0.9 s, unambiguous labels): 2.477 x 60.3 / 763 = 19.6 cm (19.35 with the area-equivalent 59.6).
- Route 2 (t = 1.4 s): soccer = 2.602 (label as written) -> 2.602 x 59.9 / 763 = 20.4 cm; if instead 2.373 is the
  soccer ball -> 18.6 cm. The basketball's growth 64 -> 70 px between frames 21 and 34 implies ~2.55-2.6 m for it
  at 1.4 s, which favours basketball=2.602, but the soccer ball's unchanged apparent size implies ~2.47 m for it,
  matching neither value: the depth readings carry ~5 % noise.
- Ratio to the basketball at t=0.9: 23.2 x (2.477 x 60.3)/(2.7777 x 64.3) = 19.4 cm.

Answer: ~19.8 cm (weighted to the unambiguous t=0.9 route, averaged with route 2 as labelled).
Confidence: moderate, ±5 % (depth-reading noise and the lumpy SAM silhouette dominate).
