Yellow taxi tracked over all 72 frames (colour mask, clean centroid/bbox). Camera calibrated on the 4 depth_info points + the 6 m white-van prior: f=1659 px, h=11.77 m, pitch 0.507 rad (van length reproduces 5.99 m, van wheelbase 3.76 m, pedestrian 1.72 m, cyclist 1.81 m). Taxi 3D path from the ground-contact track (tyre bottoms back-projected through the ground plane) gives mean per-frame speed 4.12 m/s (net/T 3.87); independent centroid track on the constant-height plane gives 3.86 m/s (net/T 3.69). Mean of the two routes ~3.9-4.0 m/s; answer 3.9 m/s.

Final message:
I measured the yellow taxi's average speed as **3.9 m/s**.

Method summary:
- **Scale/camera**: calibrated a pinhole ground-plane model (focal, camera height, pitch) on the four `depth_info` distances at t=0.58 s plus the 6 m white-van prior → f = 1659 px, h = 11.77 m, pitch 29°. Cross-checks at that focal: van length 5.99 m (prior 6 m), van wheelbase 3.76 m, pedestrian 1.72 m, cyclist 1.81 m, taxi wheelbase 2.85 m — all realistic.
- **Motion**: the SAM video track leaked into the background after frame ~24, so I re-segmented the taxi by colour for all 72 frames and reconstructed its 3D path two independent ways (tyre-contact points back-projected through the ground plane; centroid mapped to the constant-height plane). Both give a mean per-frame speed of 3.9–4.1 m/s (net displacement/time 3.7–3.9 m/s), and the given depths at t=0.58/1.58 s are reproduced within ~1 m.
