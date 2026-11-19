# q_2945 – height of the mario toy (cm)

File fps 24 = question_fps 24; t=1.4 s -> frame 34.

Object: the scene record calls it "teddy_bear" (brown plush lying on the floor, centroid ~(635,624)). It is the
Mario toy (white gloves, boots, head with cap). It lies on its back, so its height (boots to top of head) is the
longest extent of its image mask, running from the boot tip (580,599) to the head top (692,635).

Measurements (measure.py): threshold mask in the ROI, largest component; max Feret diameter is 117.0-117.7 px and the
min-area-rect length is 117.3 px in frames 5, 15, 25, 34, 40 and 47 (the toy is static). Overlay: frames/ov34.png.

Route 1 (lab card): f = 0.5959*1280 = 763 px; height = 2.016 m * 117.6 / 763 = 31.1 cm.
Route 2 (floor plane, floor.py): the board's depth along its track comes from its edge length (1/Z), scaled by
its 2.815 m depth at frame 34, which gives the floor plane (camera tilt ~42 deg; the ray to the mario meets the floor
at ~61 deg). Back-projecting both endpoints onto the plane through the toy centre parallel to the floor gives 29.8 cm.
Fronto-parallel with axial Z instead of range: 29.4 cm.

Answer: 30.5 cm (between the two routes; both are within ~2.5 pct). Confidence: moderate-high. The axis endpoints
(boot tip vs head/cap edge) are the main uncertainty, ±2 px, about 2 pct.
