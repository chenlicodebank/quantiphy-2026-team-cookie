# Q2784: height of the trash bin (cm)

Method (lab method card): f = 0.5959 x 1280 = 763 px. Height = depth x pixel height / f, with
depth_info distance_trashbin_camera = 2.977 m at t = 1.0 s (frame 24, question_fps 24 = file fps).

Measurement (measure_bin.py): Lab b < 118 blue mask with the largest component at frames 24 and 47
(the bin is static). The bbox is x 680-775, y 482-591: 96 x 110 px including mask spill. The top-edge
gradient is at y 483.5 and the bottom of the bin is at ~591 on the overlay (frames/bin_mask_24.png). The
yellow label at the bottom lowers the per-column mask bottom, so I used the bbox and the overlay. The
scene record gives 108 px, and I take ~108.5 px.

Height = 2.977 x 108.5 / 763 = 0.423 m, so 42.2 cm (range 42.1 to 42.9 for 108 to 110 px).

Checks: the basketball is 92 px at 1.9365 m, which gives 23.3 cm (a real basketball is ~24 cm), so f
and the depth are consistent. The bin width is 96 px, which gives 37.5 cm, a plausible bin.
Caveat: the front face is closer than the centre depth, so a front-face-depth reading would give
~40 cm. I followed the card (centre depth).
Confidence: good, about ±4%.
