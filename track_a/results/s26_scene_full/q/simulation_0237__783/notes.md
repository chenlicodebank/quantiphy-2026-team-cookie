# q783 — width of the house (m)

Prior: horse speed 0.874 m/s. No depth_info. File fps 24 = question_fps 24; I used 24.

## Scene
Top-down camera over a gabled house (two parallel wings plus a cross-wing). The camera is static. One horse
walks right just below the house. "Horse at the back" = the only horse in the clip.

## Scale from the prior
The scene/ track gives the horse's trunk point a net displacement of 129.4 px over 49 frames, so about 2.645 px/frame
(the mean per-frame step of 2.658 is slightly inflated by noise). That is 63.5 px/s, so
**0.01377 m/px at the height of the horse's back**.

## House pixel extents (edges.py: roof mask plus row/column edge profiles, frame 0)
- The gable ends of the main wings run in the image-vertical direction. The eave corners are at y ≈ 96 (top) and y ≈ 717 (bottom),
  so the world extent is **621 px at eave scale**. The ridge ends stick out further (y 24 and 745) only because
  of perspective: the ridge is closer to the camera.
- Perspective check: with the ridge and eave corners at the same world Y, the principal point is cy = 543 and the
  ridge-to-eave magnification is k = 1.161, the same at both ends. The main ridge (x≈1021) against the eave midpoint
  (1011.8) gives cx ≈ 954. Both are consistent with the image centre, and the camera points straight down.
- Image-horizontal direction: the cross-wing eave corners are at x 648 to 1381, so 733 px (the main wings span 701 px).
- The shorter horizontal extent is therefore the image-vertical one, 621 px. So "width" = 621 px; the length would be ~733 px.

## Perspective correction
The roof eaves sit above the ground, closer to the camera than the horse's back, so their pixels are larger than
the horse-scale pixels. W = 621 × 0.01377 × (H − z_eave)/(H − h_back).
The camera height H is not observable directly: the focal length is unknown and no depth_info is given. I put
plausible bounds on it with roof pitches (main-roof tan(pitch) = 3.95e-4·f):
- f = 1500–2667 px gives H ≈ 22–38 m.
- With a one-storey eave height of ~2.7 m and a back height of ~1.2 m, the factor is 0.93–0.96, so W ≈ 7.9–8.2 m.
- With a two-storey eave height (~5 m), W ≈ 7.4 m.

Without any perspective correction, 621 × 0.01377 = 8.55 m. The record's naive whole-roof bbox, 724 px × scale,
gives 9.97 m, but that overstates it because it includes the perspective-shifted ridge ends.

## Answer
**8.0 m** (house width = shorter horizontal footprint, eave to eave). Under the other reading, length (image-x,
733 px), the answer would be ~9.5 m.

Confidence: moderate. The main uncertainty (~±8 %) is the unknown camera height and eave height. The second route
(the uncorrected planar scale) gives 8.55 m, an upper bound.
