# q_831: length of the antelope (kudu)

- This is a 2D top-down Blender render at 30 fps. The file rate and question_fps agree. The kudu walks in +x along a straight path.
- **Scale from the prior** (speed 1.277 m/s): I ran `measure.py` on `scene/tracks/kudu.csv`. Mean per-frame pixel speed by reference point:
  - core: 9.09 px/frame
  - trunk: 9.46
  - whole mask: 9.37
  - nose: 9.42
  - The pelvis lies between the rump and the core, so I took 9.27 px/frame = 278 px/s.
  - Scale: 1.277 / 278 = 0.00459 m/px.
- **Length** is the world AABB's longer horizontal extent, from snout to tail tip, which is the x extent of the bounding box. At frame 45, a gridded crop confirms nose x ≈ 1375 and tail tip x ≈ 702. The tail swing makes this extent vary from 612 to 732 px over the clip, with median 674 and mean 674.
  - 674 px × 0.00459 = **3.10 m**.
  - Alternatives: body without the tail (~495 px) gives 2.27 m; the per-frame extremes give 2.8–3.4 m.
- **Second route:** with the slowest and fastest reference speeds (9.09 and 9.46 px/frame) the length is 2.98–3.15 m. A real kudu is ~2.0–2.5 m of body plus ~0.4 m of tail, so the answer is plausible.
- **Confidence:** moderate. The main uncertainty is which frame or pose defines the reference bounding box.
