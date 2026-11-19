# q_1706 — width of the boat (m)

File: 25 fps, 75 frames, 960x960. question_fps = 24, so t=1 s -> frame 24 and t=2 s -> frame 48 (I used the frame numbers, not the scene/ seconds).

## Scale / focal length
- Human (adult): median bbox height 73 px at 140 m. f = 73*140/(1.75*cos(pitch)), which gives f ≈ 5840–6100 px for a 1.75 m adult.
- Prior (person speed 1.3 m/s): the human's depth_info barely changes (139.95→139.98), so per the rules it describes the origin and not the walking
  body. The body moves 1.20 px/frame left and 0.59 px/frame down (hum.py). Treating the downward motion as
  walking toward the camera on the ground with the pitch below, 1.3 m/s needs f ≈ 6300–7300. But that makes the person 1.45–1.65 m tall,
  so I gave the human-height constraint more weight.
- Bird (eagle): wingspan 70 px at ~140 m, which gives 1.6 m at f = 6000 (plausible).
- Chosen value: f ≈ 6000 px, ±7 %. At t=0 (D ≈ 127.0 m): k0 = 47.3 px/m. At t=1 (D = 130.35 m): k1 = 46.0 px/m.

## Boat geometry (geom2.py)
- 3D boat velocity from the given distances (130.35 → 133.74 m) and the pixel track: about 4.0 m/s, moving away and left.
  - The camera pitch from "the boat moves horizontally" is α ≈ 13.5°.
  - The heading is ψ ≈ 32° from the line of sight (bow pointing away and left; stern and port side face the camera).
- Independent check: in the image, edges along the hull run at slope +0.35..0.5 and edges across the beam (cabin aft face, crane arm) at about −0.15.
  The model predicts +0.37 and −0.146, so the geometry is consistent.
- Unit image vectors: along the hull toward the stern (0.530, 0.198)k; beam toward starboard (0.848, −0.128)k; up (0, −0.97)k.

## Beam measurement (frame 0)
- Port gunwale (top of the white band above the red hull): about (200,789), (250,812), (300,828).
- Starboard bulwark top (seen against the background behind the cabin): (336,768), (366,788), (392,800).
- Matching the port and starboard gunwale at the same station (same height, so the offset between them lies along the beam vector):
  - Δx = 136 px at the cabin-aft station → B ≈ 3.4 m.
  - Δx = 125 px further aft → B ≈ 3.1 m. The hull narrows toward the round stern.
  - The widest beam is hidden behind the cabin; I estimate it at **≈ 3.5 m**.
- Cross-checks:
  - The cabin aft face is 62 px wide → 1.55 m wide cabin.
  - The hull's image width across the line of sight is 275 px = 5.8 m, consistent with L ≈ 8.5–9.5 m and B ≈ 3.3–3.6 m.
- Crane/davit: a post on the starboard gunwale with an arm pointing outboard along the beam, sticking out about 0.9 m past the gunwale (35–38 px).
  If the world bounding box includes it (one mesh), width ≈ 1.75 + 1.57 + 0.9 ≈ **4.2 m**.

## Answer
The hull beam is about 3.5 m; the bounding box including the crane arm is about 4.2 m. The reference uses the world-space bounding box,
which probably includes the crane, so I answered **4.0 m**, between the two readings and leaning toward the bounding box.

## Confidence
Moderate (±15 %):
- The focal length is uncertain by about 7 %.
- It is unclear whether the crane is part of the box.
- The widest station is hidden behind the cabin.
