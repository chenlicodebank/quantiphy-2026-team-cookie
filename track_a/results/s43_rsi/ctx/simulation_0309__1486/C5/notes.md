Focal length f=3886 px from the prior speed 1.29 m/s plus depth_info (5.2108->6.3261 m over 1 s, radial 1.115 m/s, lateral 0.648 m/s, head-tip pixel displacement 383 px/s). Nose-to-tail-tip pixel lengths measured on zoomed frames: 563 px (f0, depth ~4.05), 317 px (f24, 5.21 m), 331 px (f48, 6.33 m). The dragon flies away at ~60 deg from the image plane (cos theta ~0.5, confirmed by the constant projected wingspan ~1.07 m while the body is foreshortened), so L = L_px*depth/(f*cos theta) gives 1.17/0.85/1.07 m; the independent route L = L_px*v/v_px (f cancels) gives 1.34/1.03/1.07 m. Both agree at ~1.05-1.1 m; answer 1.08 m.

Final message:
I measured the dragon's body length at ~1.08 m.

**Method summary:**
- **Scale:** depth_info gives a radial rate of 1.115 m/s (5.2108 → 6.3261 m over 1 s). With the prior speed of 1.29 m/s, the lateral speed is 0.648 m/s. Combining this with the measured head-tip pixel displacement (383 px/s between t=1 and t=2) gives a focal length of f ≈ 3886 px, cross-checked against the mask-area ratio and the constant projected wingspan.
- **Body length:** nose-to-tail-tip pixel lengths measured on 3× zoomed frames: 563 px (frame 0, depth ≈ 4.05 m), 317 px (frame 24, 5.21 m), 331 px (frame 48, 6.33 m).
- **Foreshortening:** the dragon flies away at ~60° from the image plane (cos θ ≈ 0.5), confirmed by the wingspan staying constant (~1.07 m) while the body is strongly foreshortened.
- **Two independent routes** (L = L_px·depth/(f·cos θ) and L = L_px·v/v_px, in which f cancels) both converge on ~1.05–1.1 m.
