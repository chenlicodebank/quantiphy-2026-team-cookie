# q1680: length of the rock (m). Answer: 21.0 m

Prior: the boat moves at 4 m/s. depth_info: boat at 90.11 m (t=1 s) and 90.44 m (t=2 s). question_fps is 24, so t=1 s is frame 24 and t=2 s is frame 48. The file runs at 25 fps; I used frame indices.
The rock is static and has no depth of its own. Its silhouette (frame 72, largest component) spans x 329–954, which is 625 px, the right tip just inside the image, and y 25–312.

## Where the candidates part ways
- **C2, C3, C4 (16.0–16.4 m)** put the rock at the boat's depth, about 90 m. Nothing supports that. The rock's bottom is a flat, streaky cut, which is its waterline, and it sits about 340 px above the boat's waterline. A rock on the sea surface must therefore be well behind the boat. I reject 16 m.
- **C1 (23.0 m)** put the rock on the water plane, which is right. It took a camera pitch of 15.3° from an intensity-weighted fit of the pale mast. The pitch is the step that sets the answer: the rock's depth comes from the horizon row, which is cy − f·tanθ.

## My measurements
- **Focal length.** The boat moves at 6.44 px/frame. At 4 m/s and 24 fps that is 0.1667 m/frame, at Z ≈ 90 m, so f ≈ 3490 px. The boat's hull is then about 10 m, which is realistic.
- **The boat moves parallel to the image plane** (vscale.py). Its vertical apparent size, from roof top to hull bottom (179 px), changes by only −0.17% over 66 frames. A boat receding as depth_info suggests would shrink by about 1.2%. ECC registration also gives a vertical scale of 1.000.
  The roof and the keel both drift up by the same −0.25 px/frame. With no receding, that drift must be a camera roll of about 2.2°, not perspective. So the "drift" route to the pitch (about 22°) is not valid evidence.
  The growth in depth_info then implies that the boat's origin is offset left of the hull. That barely changes f.
- **Pitch from the vertical vanishing point** (stripe.py). I used sub-pixel left and right edges of two high-contrast vertical features on the boat, tracked over 70 frames as the boat crosses the frame (u 280–780), and fitted the slope dx/dy against u, where the slope variation is −1/(v_vp − v).
  - Black stripe on the mast: rms 0.05 px, θ = 18.2° (bootstrap 17.8–18.5).
  - Black post aft of the wheelhouse: θ = 21.6° (20.5–22.8).
  - Both give the same constant offset (−0.013), which is consistent with both being truly vertical.
  - My earlier, cruder threshold fits of the pale mast (11–13°), and C1's 15.3°, had 0.7–1.2 px residuals and were biased low.
  - I take θ ≈ 20° ± 2°.
  - Cross-check: the deck is clearly visible. The far gunwale is about 50 px above the near one. For a beam of about 3.6 m, the expected gap is about 54 px at a 23° depression and about 36 px at 15°.
- **Rock depth** (rockdepth2.py). I anchored the water plane at the boat's near-side waterline: row 655.5 at u ≈ 650, the same column as the rock base, so the roll cancels. That point is at Z ≈ 88.2–90 m, the origin depth less half a beam. The rock base at row 312 then lies at Z ≈ 113–122 m.
  I also used C1's ellipsoid-on-water model (centre at row 168, with b/a from 0.5 to 1):

  | θ | L |
  |---|---|
  | 18° | 21.3–22.1 m |
  | 20° | 20.6–21.4 m |
  | 22° | 20.0–20.9 m |

  The length is the x extent: the footprint looks elongated left to right.

## Answer
21.0 m (θ = 20°, near-waterline Z ≈ 88.3 m).
Range over the plausible pitch is 20.2–22.1 m. If the rock floated at the boat's depth instead, the answer would be 16.1 m, but the waterline cut rules that out.
Confidence: moderate, about ±8%.
I agree with C1's geometry but not its pitch.
