# Q794 – length of the horse at the back (m)

Prior: speed of the horse at the back = 0.874 m/s. No depth_info. fps = question_fps = 24.

Object: "horse at the back" = the brown (chestnut) horse. It trails the white horse in the walking direction (+x)
and is the upper/farther one in the overhead view. Both readings point to the same horse.

Method (2D, one m/px scale from the prior):
- Pixel speed of the brown horse over frames 0–48 (frame 49 is an animation loop reset and is excluded):
  - torso-block template match (frame-0 template, sub-pixel): 2.618 px/frame (slope), 2.634 (net/48)
  - nose (mask bbox right edge, low residual 0.7 px): 2.667 px/frame
  - mask centroid 2.69, eroded torso centroid 2.51 (noisy, pose-dependent)
  - adopted 2.64 px/frame = 63.4 px/s -> scale = 0.874 / 63.4 = 0.01379 m/px
- Pixel length nose-to-rump: 142–144 px in most frames (median mask length 144; zoom at frame 0: x ≈695–838).
  It grows to 150–164 px only while a hind leg is stretched back (frames 27–32, 46–48). Used 144 px.
- Length = 144 x 0.01379 = 1.99 m.

Second route: speed from the nose track (2.667 px/frame) gives 1.97 m; from the torso template (2.618) 2.00 m.
The speed and length are both measured on the body top, so they are at the same depth and perspective cancels.
If the leg-stretched maximum extent (~150 px) were used, the result would be ~2.07 m.

Confidence: moderate-high (±4 %). The main uncertainty is which pose/frame the reference bounding box used.
