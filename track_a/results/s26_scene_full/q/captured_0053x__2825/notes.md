# Q2825: diameter of the white cup's rim (cm)

The file and the question both run at 24 fps. t=0.4 s is frame 10. The cup does not move (its bbox is the same, 553-578 x 405-449, in frames 5 to 47).

Method (lab card): size = depth x pixel extent / f, with f = 0.5959 x 1280 = 762.8 px and cup depth = 2.516 m (from depth_info).

Measurements of the rim width (the widest horizontal extent near the top of the cup, rows 411-425):
- Route 1, `measure_cup.py`: inclusive pixel width of the non-green mask. 26 px in frames 5, 8 and 10, and 25 px in frames 12-47, which gives 8.58 / 8.25 cm.
- Route 2, `edges.py`: sub-pixel half-threshold edge crossings of the greenness profile in frame 10. Width is 25.6-26.3 px across rows 411-425 (about 26.0 px), which gives 8.55-8.68 cm.
- The cup body narrows to about 20 px near the bottom, which confirms that the widest part is at the rim.

Answer: 26 px x 2.516 / 762.8 = 8.6 cm. That is a plausible size for a tumbler rim.
Confidence: moderate-high. The video looks upscaled 2x (rows come in pairs) and the edges are soft, so expect about ±1 px, which is ±4%.
