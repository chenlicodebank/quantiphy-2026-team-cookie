# Q784 — length of the house (m). Prior: horse speed = 0.874 m/s. No depth_info. fps 24 (= question_fps).

## Scale from the horse
Only one horse in the clip (the record's track is correct: it walks steadily +x below the house, frames 0-49).
Net displacement 129.4 px over 49 frames = 2.641 px/frame; path length 130.3 px = 2.659 px/frame (includes noise).
Using ~2.65 px/frame = 63.6 px/s gives 0.874 / 63.6 = 0.01377 m/px at the depth of the horse's back (the tracked
surface). Sanity check: horse nose-to-rump 145 px = 2.0 m, so the scene is close to real-world scale.

## House pixel extents (edges.py, frame 0, measured with gradient profiles)
- Main block: left eave x = 660.5, right eave x = 1362.5, so **701 px** across x (the same at all rows).
  Gable ends: corners at y ≈ 95 / 716, apexes at y ≈ 20 / 745.5.
- Cross-wing: gable corners x ≈ 645 / 1386 (741 px), apexes x ≈ 615.5 / ~1425, eaves y ≈ 270 / 520.
- The bbox in the record (809 x 724 px) mixes edges that sit at different heights.

## Perspective (the camera looks straight down, but it is not 2D)
The gable apexes project farther from the image centre than the eave corners, by a factor of 1.168 for the main
block and 1.09 for the cross-wing. Both values are consistent at the top and bottom ends, and between the x and y
directions, so the gable ends are vertical. The cross-wing therefore sits higher, nearer the camera. The main ridge
meets the cross roof at y = 350 and y = 415, which puts the main ridge at about 1.022 times the cross-ridge depth.
In depth units of the cross ridge, the extents work out as follows:
- Main block x extent = 701 px x 1.194 = 837.
- Cross-wing x extent = 741 x 1.09 = 808.
- Main y extent = 621 x 1.194 = 741.

So the longest horizontal extent is the main block's x span, 701 px at the main-eave depth.
The main eave is above the ground, so it is nearer the camera than the horse's back. That means the horse's m/px
over-scales the house by z_back / z_eave. The focal length is unknown and there are no depths. For plausible lenses
(f = 1490-2670 px, giving roof pitches of about 31-48 deg) and an eave height of about 3-5 m:
z_eave / z_back is about 0.86-0.96, with a central value of about 0.93.

## Result
- Plain 2D answer: 701 x 0.01377 = 9.65 m (upper bound).
- Perspective-corrected: about 8.3-9.2 m.
- **Answer: 9.0 m.**

Second route: the y extent (621 px) gives 8.55 m in 2D, or about 8.0 m corrected. That is the width, not the length,
and it confirms that x is the long side. Using the horse's net speed instead of its mean step changes the scale by
less than 0.5 %.

Confidence: moderate. The main uncertainty (about ±7 %) is the eave-to-horse depth ratio, because no depth_info or
focal length is given.
