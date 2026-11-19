Bicycle = the cyclist's bike (only bike in the clip). Scale from the 1.8 m walking man via the common ground plane: (y_ground-y_h)/h_px = h_c/H gives H_bike = 1.8*k_p/k_b = 1.01 m (handlebar top y=426 to wheel contact y=561 at t=1, man's head/feet 250/449). Independent check with a standard 0.68 m wheel (90 px at f33, 103 px at f45) gives 1.02 m. The given bike depth (16.49 m) is inconsistent with the image (the bike is visibly closer than the man), so it was not used.

Final message:
I measured the bicycle's height as **1.01 m**.

**Method:** The only bicycle in the clip is the one ridden by the dark-suited man toward the camera. I used the prior (walking man = 1.8 m) with the common ground plane: for a vertical object, `(y_ground − y_h)/h_px = h_c/H`, so `H_bike = 1.8 · k_p/k_b`. Measuring the man's head/feet (white-background silhouette, frames 0–95) and the bike's handlebar top / front-wheel contact (SAM 3 track, frames 0–54) gives 1.01 m, insensitive to the horizon estimate.

**Second route:** using a standard 0.68 m wheel diameter (90 px at f33, 103 px at f45) gives 1.02 m — agreement.

**Note:** the given `distance_bike_camera` (16.49 m at t=1) is inconsistent with the image — the bike's wheel contact is far lower in frame than the man's feet, i.e. the bike is clearly *closer*, not farther — so the depth_info could not be used for scale; the scale came from the prior via the ground plane (documented in notes.md).
