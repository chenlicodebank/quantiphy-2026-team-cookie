# q_1751 — average speed of the boat (m/s)

Prior: boat length = 10 m. depth_info: 173.71 m at t=1 s, 174.55 m at t=2 s, so the boat moves away from the camera at
0.842 m/s. File fps = question_fps = 24.

## Method (ratio of image speed to image length along the same 3D direction)
- The boat moves bow-first along its own long axis. The image motion direction is -163.8 deg, and the bow-to-stern image
  direction is about 16-18 deg, so the two are parallel. Because the motion and the length point the same way in 3D,
  both are foreshortened by the same factor (|u_perp|). The camera is ~174 m away and the boat is 10 m long, so weak
  perspective holds. That gives v = L * (pixel speed) / (pixel length).
- Pixel speed (`speed.py`, linear fits to scene/tracks/boat.csv frames 1-71): centroid 88.4, bow tip 87.6,
  bbox centre 88.2, bbox-left/bottom 87.7 px/s. First half 88.0-88.9, second half 87.0-87.8 (the boat recedes slightly).
  I use 88.0 px/s at mid-clip (frame 36).
- Pixel length at frame 36 (`ends.py`, `zoom.py`): bow tip at deck level (211, 871); aftmost point of the stern at
  deck/gunwale level about (412-414, 925-928). Projected on the motion direction, that is 210-211 px. The full
  silhouette extent along the motion direction is 218 px, but that includes the hull height (the hull bottom at the
  stern projects further along the axis). The bow is probably a bit higher than the stern deck, which would make the
  same-height length about 2 px shorter. I take L_pix = 210 px (range 208-218).
- v = 10 * 88.0 / 210 = **4.19 m/s** (range 4.04-4.23 for L_pix 218-208).
- Speed is constant (no events), so the mean of the per-frame speeds equals the fitted speed.

## Consistency checks
- Radial speed from depth_info is 0.842 m/s, so the transverse speed is sqrt(4.19^2 - 0.84^2) = 4.10 m/s. That implies a
  focal length f = 88 * 174 / 4.10 = 3730 px (hFOV about 16.5 deg), which is plausible.
- The expected shrink in apparent size from the depth change over frames 5-66 is about 1.2%. The measured mask_length
  shrink is 1.16% (224.3 -> 221.6 px), which agrees with the depth_info.
- The focal length cannot be estimated independently (no other object of known size), so the ratio route is the main
  measurement.

Confidence: moderate-high. The main uncertainty (about 2-3%) is where the stern endpoint of the 10 m length sits in the
image.
