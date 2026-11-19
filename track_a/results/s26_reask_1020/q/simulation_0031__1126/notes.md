# Q1126 – width (beam) of the boat — answer 2.7 m

The file runs at 25 fps, but times use question_fps = 24, so t=1 s is frame 24 and t=2 s is frame 48. The camera is static.

## Orientation
- The bow is the high white end at the upper left. The stern, with its rail and a narrow dark-red transom, is at the lower right.
- The boat moves bow-first, up and to the left, away from the camera.
- The image direction of the sheer line (slope ~0.42) matches the motion direction (slope 0.46), so the boat moves along its own axis.
- The camera sees the port side and the deck. The starboard gunwale is seen as the far bulwark top against the water.

## Camera (calib.py, beam.py)
- **Focal length.** The person's origin depth barely changes (139.95 → 139.98 m), so their origin stays put while the body walks. That makes the 1.3 m/s prior unusable for scale here:
  - On flat ground, the speed route would need f > 8000 px, which makes the person 1.3 m tall.
  - The beach slope is unknown, so the walking direction cannot be pinned down.
- I took f from the person's height instead: 77 px (head top to lowest foot, mean over frames) at ~140 m. A 1.75–1.80 m adult gives f = 5990–6160 px; I used f ≈ 6050 px (HFOV ≈ 9°).
- **Check with the eagle.** Peak image wingspan is 70–75 px at depth 132–147 m, which is 1.7 m in the image plane. Allowing for its flight at ~55° to the image plane, the true span is ≈ 2.05 m, a plausible eagle.
- **Pitch.** From the boat's depth change of 3.394 m/s (given) and its image motion between frames 24 and 48, assuming the boat moves horizontally: pitch ≈ 12.6°, boat speed ≈ 4.0 m/s.

## Beam measurement (frame 24, boat depth 130.35 m)
- 1 m of horizontal beam, perpendicular to the boat's axis, projects to (40.6, −6.3) px.
- **Check of that direction.** The cabin's roof edge and aft wall lie along this direction: their measured slope is −0.13, against −0.155 predicted.
- I traced both gunwales on 4× overlays (`overlay.py`, frames/b24a.png, frames/b24b.png):
  - port gunwale: the near deck edge;
  - starboard gunwale: the far bulwark top behind the cabin.
- At each starboard point I found the port point that is offset by W × the beam vector.
- Beam per station, from just aft of the cabin to the stern: 2.62, 2.59, 2.42, 2.17, 1.11 m. The hull is widest at the cabin and narrows to a ~1.3 m transom; the stern rail is 52 px ≈ 1.3 m.
- If the port gunwale's outer edge sits 3 px lower than traced, the maximum becomes 2.73 m. Across f = 5900–6200 px the maximum ranges 2.57–2.78 m.
- The widest section may sit partly hidden under the cabin, so I answered slightly above the largest visible value: **2.7 m**.

## Checks
- **Cabin.** 1.51 m wide and ~1.8 m long, with 0.55 m side decks: consistent.
- **Hull length.** Roughly 9.5 m, giving a length-to-beam ratio of ~3.5, typical for a small fishing boat.

**Confidence:** moderate, about ±10%. The main uncertainties are the focal length (taken from the assumed person height, since the speed prior gave no usable scale) and where exactly the gunwale edges lie.
