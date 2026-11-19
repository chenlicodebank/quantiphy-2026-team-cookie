# q1704 — height of the boat (m)

The file runs at 25 fps, but the question uses 24 fps, so t=1 s is frame 24 and t=2 s is frame 48.

## Measurements (measure.py, human.py, geom.py)
- Boat image height (own mask, min(RGB)<240): 441 px at frame 24 (D=130.35 m) and 430 px at frame 48 (D=133.74 m).
  The products px*D are 57484 and 57508. They agree to 0.04 pct, so the boat depths are consistent with its apparent size.
- Human: the median mask height is 75 px. Over the clip, p90 is 78 px and the maximum is 80 px. The pale head blends
  into the background, so I take the standing-equivalent height as about 77 px. Body depth is about 139.97 m.
- Human image motion over the clip: -1.20 px/frame in x and +0.59 px/frame in y (moving down the image). There is no
  clear change in apparent size.

## Scale: the speed prior assumed sideways gives an impossible scene, so the scale comes from the human
- If all 1.3 m/s were sideways motion (32 px/s at 140 m), f would be about 3500 px. The human would then be 2.9 m
  tall, the eagle's projected wingspan 2.7 m, and the wheelhouse door about 3.5 m. That is rejected.
- I took the scale from the standard object: a 1.75 m adult at 77 px and 139.97 m gives f ≈ 6160 px.
- Checks at f=6160:
  - The eagle's maximum projected wingspan is 1.55 m. That is plausible, since the true span is at least this.
  - The wheelhouse door is about 2.0 m.
  - The boat's speed is about 4 m/s.
- Reconciling the speed prior: if the boat moves on a horizontal plane, the camera pitch comes out at about 13-14°.
  The human's downward image motion then means they are walking toward the camera at about 1.3 m/s along the ground.
  Combined with the 0.67 m/s sideways motion, that gives about 1.45 m/s, within about 12 pct of the 1.3 m/s prior.
  Without the sideways-only assumption, the prior and a real-size human roughly agree.

## Boat height
- Image extent in metres: 57496 / 6160 = 9.34 m.
- Correction for the downward view: the line of sight is about 15° below horizontal. The lowest image point is the
  hull bottom at the stern, which is about 1.5 m nearer the camera than the mast top. So
  H = (9.34 - 1.5 sin15°) / cos15° ≈ 9.25 m. Taking 20° instead gives about 9.3 m.
- Answer: **9.2 m**.

## Confidence
Medium. The main uncertainty is the human's true height, which was assumed to be 1.75 m (±5 pct).
