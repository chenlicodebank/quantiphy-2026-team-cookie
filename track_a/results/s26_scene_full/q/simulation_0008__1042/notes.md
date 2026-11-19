# Q1042 – height of the cabin floor above the ground (m)

The file's frame rate is 22.80 fps, but the question uses 24 fps, so t = 1 s is frame 24. The camera does not move.
This is a 3D scene with an unknown focal length, so the scale comes from depth_info.

## Focal length (focal.py)
- The boat moves sideways at a nearly constant depth Z: its apparent size stays the same to within about 2%.
- With d² = Z²(1 + r²/f²), I used the boat origin (scene/tracks/boat.csv ref_x/ref_y) at frame 0
  (u = 1314, v ≈ 686) with d = 7.452, and at frame 24 (u = 1060, v ≈ 690) with d = 6.655.
- Result: f ≈ 1000 px (978–1005 depending on the origin's x/y position ± 4 px), and Z_boat ≈ 5.86 m.
- Check against the 0.75 m boat height:
  - The stem-post top (y 620) sits about 120 px above the water level at the boat.
  - The water level comes from the midpoint between the bow gunwale and its reflection, at y ≈ 739.
  - So the post top is about 0.70 m above the water, which leaves about 0.05 m of keel below it. This is consistent.

## Cabin floor and ground (profile.py, frames/stairs.png, frame 0)
- The cabin wall ends and the floor's front fascia starts at y ≈ 521. I take this as the floor surface.
  - The underside of the floor platform (dark beam and shadow) runs from y 521 to y 534–540.
- The front stair posts run from y 541 down to the ground at y ≈ 586–592, so I take the stair foot (ground) as y ≈ 588.
  - The steps rise about 11 px each (treads at about 549, 560, 571, 581).
- The difference is Δv ≈ 67 px, at the stairs' depth of 17.62 m. The stairs are almost on the optical axis (u ≈ 547, v ≈ 560).

## Result
- Simple estimate: h = 67 × 17.62 / 1000 = 1.18 m.
- Perspective-corrected estimate:
  - Water-plane geometry: the cabin ridge (y 330) and its reflection apex (y ≈ 855) put the water level at the cabin at y ≈ 592.
  - Combined with the boat's water level, this puts the horizon at v_h ≈ 520–527.
  - Taking the stair foot at about 17.3 m and the floor edge at about 18 m gives 1.16 m.
- Answer: **1.17 m**. Sanity check: about 6 step rises of about 0.19 m each.

## Alternative readings
- Measured to the underside of the floor structure (y ≈ 530) instead, the height would be about 1.0 m.

## Uncertainty
- I'm moderately confident.
- f is uncertain by about ±3%, the ground point by about ±3 px (±5%), and the choice of floor surface adds some ambiguity.
- The pier's depth of 11.58 m doesn't fit well as the deck centre: the water-plane geometry puts the deck at about 7.5–12 m.
  - Its origin is probably not at the centre of the deck, so I didn't use it.
