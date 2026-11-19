Focal length from the exact speed prior (1.29 m/s) plus the two given depths: a rigid body point tracked by template matching (mask centroid is unusable, wing-beat swings it +-150 px) gives a constant-speed 3D reconstruction with |P24|=5.2108, |P48|=6.3261 -> f ~ 4400 px (4000-4700); validated by a constant reconstructed wingspan (~1.0-1.1 m) at frames 0/24/48. At frame 0 (least foreshortened, dragon moving almost straight away, d=4.07 m) the nose-to-tail extent is 605 px straight / 674 px along the body, giving L = s*d/f ~ 0.56-0.63 m; answer 0.60 m.

Final message:
I measured the dragon's body length as **0.60 m**.

Method summary:
- **Scale**: The scene's mask centroid is dominated by wing-beat noise (±150 px), so I tracked a rigid body point (shoulder) by template matching, verified on frames 0/12/24/36/48. A constant-speed 3D reconstruction (|P₂₄| = 5.2108 m, |P₄₈| = 6.3261 m, step = 1.29/24 m) gives f ≈ 4400 px (range 4000–4700). Cross-check: the reconstruction's own chord between t=1 and t=2 is 1.196 m, which independently reproduces f ≈ 4585 px, and the reconstructed wingspan is constant (~1.0–1.1 m) at frames 0, 24 and 48.
- **Body length**: Frame 0 is the least-foreshortened view (normalised apparent length maximal; dragon moving almost straight away from the camera at d = 4.07 m). Nose-to-tail extent on the SAM mask is 605 px straight-line (674 px along the curved body), giving 0.56–0.63 m; I answered 0.60 m.
