# q_1582 — width of the paper next to the typewriter (m)

The file and the question both use 24 fps. The scene is a 3D Blender render with a static camera.
Answer: **0.19 m**

## Object
I took "the paper next to the typewriter" to be the flat cream sheet lying just in front of and to the left of the
resting typewriter (scene.json `front_paper_sheet`). It is the only paper that is clearly next to the typewriter
after it lands. The other papers are the slip under the revolver and the paper with keys, which the typewriter covers.
I segmented the sheet in code on frame 0 (gray > 150, largest component; overlay in `frames/papermask.png`).
The mask is a clean quadrilateral with corners (1056,693), (1157,740), (1257,719), (1151,673) px (`paper.py`).

## Camera (principal point at the image centre; three routes)
1. **Vanishing points** (`lines.py`, `vp.py`, `vp2.py`). I detected lines with LSD on the desk:
   - 5 lines along the front edge, 5 along the left edge, and 10 vertical leg lines.
   - The vertical vanishing point is at (1064, 11734). That means zero roll, and f/tan(pitch) = 11194 px.
   - Requiring the front-edge and left-edge directions to be orthogonal on the horizon gives f ≈ 2840 px, pitch 14.2°. A spurious second root near 1870 px is ruled out by route 2.
2. **Gravity fall** (`fit2.py`, `fit3.py`, `final.py`). P0 is the frame-0 pixel back-projected at the given 4.32 m. I fitted P(t) = P0 − ½·9.8·t²·up to frames 2-9 (rms about 2.1 px).
   - With the pitch free, the best f is about 2800-2900 px, the start time is ≈ 0 and the pitch is ≈ 14-16°.
   - With the vanishing-point pitch fixed, the best f is ≈ 2800-2840.
   - At f = 2840 the drop from the t=0 point (4.32 m) to the t=0.5 resting point (4.501 m) is 0.87 m and nearly vertical (0.03 m horizontal). That implies impact at 0.42 s, which matches the frame 10→11 contact.
3. **Desk-plane consistency**. With the depths given for the near desk corner (3.593 m) and the gun (4.704 m), both lie on the same horizontal plane (gun origin about 1.5 cm above it) for f ≈ 2750-2840.
   - The resting typewriter origin is then about 7 cm above the desk, which is plausible.
   - The "far right corner" (5.009 m) could not be located reliably: it is hidden near the phone, so I did not use it.

I adopted f ≈ 2820 px (HFOV ≈ 41°), pitch 14.1°, roll 0, and desk plane ≈ 1.28 m below the camera.
Scale sanity checks: alarm clock ≈ 0.14 m wide, picture frame ≈ 0.15 m tall, lamp ≈ 0.47 m tall. All are plausible.

## Paper measurement (`paper3d.py`)
I intersected the corner rays (expanded by half a pixel) with the desk plane.

| f (px) | 2700 | 2800 | 2840 | 2900 |
|---|---|---|---|---|
| short edge (m, along the desk front) | 0.192 | 0.184 | 0.181 | 0.176 |
| long edge (m, front-to-back) | 0.299 | 0.284 | 0.279 | 0.271 |
| desk-aligned AABB, short side (m) | 0.204 | 0.199 | 0.197 | 0.195 |

The sheet is turned about 5-6° relative to the desk edges. Its aspect ratio is ≈ 1.54, so it is not a standard A4 or Letter sheet.

## Ambiguity and answer
- If "width" means the sheet's own short side, it is ≈ 0.181 m.
- If it means the world AABB with world axes along the desk, it is ≈ 0.198 m.
- The world axes themselves are unknown.

I answered 0.19 m, which is within about 5% of both readings.
Confidence: moderate. The focal-length uncertainty (2750-2900) gives about ±4%, on top of the AABB-versus-edge ambiguity.
