# q1680: length of the rock (m)

Prior: the boat moves at 4 m/s. depth_info: boat at 90.1103 m (t=1 s) and 90.4360 m (t=2 s). The question uses 24 fps, so t=1 s is frame 24 and t=2 s is frame 48. The file itself is 25 fps; I used the frame column of the track, not its seconds.

## Focal length (focal.py)
- I fitted the boat track (frames ≥ 3) with a quadratic and took the image positions at frames 24 and 48. Those rays were back-projected with the two given distances.
- The focal length was solved so that the boat's displacement over 1 s is 4 m.
- Result: f = 3501–3507 px across three reference points (bbox centre, centroid, hull/keel). That is a horizontal FOV of 15.6°.
- Check: hull length 390 px × 90.3 / 3502 = 10.1 m, a plausible fishing boat.

## Rock in pixels (rockprof.py, frame 72)
- Mask bbox x 329–954 (625 px wide, right tip not truncated), y 25–312.
- The centre row is about 168. The bottom boundary is a curved ellipse-like profile whose tips are at row ~160. There is a flat-cut, streaked base at rows 290–311.
- The rock is static.

## The rock's depth: the main uncertainty
No depth is given for the rock. I assumed it rests on the water plane, the same plane the boat floats on.
- **Camera pitch from the mast (mast.py).** The tilt of the mast changes steadily with image x as the boat crosses: dx/dy goes from −0.009 at u=+250 to +0.025 at u=−215. This comes from the vertical vanishing point and gives a pitch θ ≈ 15.3°.
- **Pitch from the boat's drift.** The boat drifts slightly up the image as its depth increases, which suggests θ ≈ 21–26°. That route is less reliable (only 5–7 px of drift).
- **Water plane.** The plane is anchored at the boat's waterline: row ~660 at camera depth 90.2 m, which gives a camera height of about 28 m for θ = 15°.
- **Ellipsoid model (rockdepth.py).** I modelled the rock as an ellipsoid resting on the water. Its centre must project to row 168, and its vertical semi-extent must be 144 px.
- **Result.** The rock centre comes out at camera depth Zc ≈ 117–137 m. The length 2a = 625 px × Zc / f comes to:
  - θ = 13.5°: 24.2–24.5 m
  - θ = 15.25°: 23.0–23.3 m
  - θ = 17°: 22.1–22.4 m
  - θ = 21°: 20.7–21.1 m

  This holds across depth-to-length ratios b/a of 0.5–1. A second route, the water-plane depth of the base's front edge at row 311 (Z = 130 m at θ = 15°), agrees: 625 × 130 / 3502 ≈ 23 m.

## Answer
23.0 m, the image x extent at the rock's estimated depth, which I take as the rock's longer horizontal extent.

## Alternatives and confidence
- If the rock were instead floating at the boat's depth (about 90 m), the length would be 625 × 90.3 / 3502 ≈ 16.1 m.
- If its depth extent were larger than its width, that would be the "length" instead. I can't tell from the video.
- Confidence: low to moderate (roughly ±20%), because the rock's depth is inferred, not given.
