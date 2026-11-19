# internet_0072 — measurement notes

**Scene:** internet video, 2D, 2160x3840 px, 39 frames at 26.846729 fps (t = frame/fps, 0 to 1.415 s). A pink wall is lit by a round soft spotlight. A hand moves a red/pink credit card (it reads "CREDIT CARD" and has a gold chip and "0000 0000 0000 0000") from the dark bottom-right corner up and to the left into the spotlight. The card slows down steadily and stops near the spot's centre. The camera is static.

## Files
- `scene.json`: inventory, pixel sizes, events, camera and file index.
- `tracks/card.csv`: one row per frame with frame, time_s, `source` (`mask` or `by_eye`), the visible centre (cx, cy), the bbox, the minAreaRect `length_px`/`width_px`/angle (mask frames only), area, `step_px` (the distance the centre moved since the previous frame) and an occlusion note.
- `tracks/card_raw.csv`: the raw mask output for every frame. Frames 0–7 there are partial or missing because those frames are too dark, so do not use them.
- `tracks/spotlight.csv`: the half-max disc of the spotlight in each frame, used to check the camera.
- `scripts/`: `track_card.py` builds the mask track, spotlight track and overlays. `early_strip.py` makes brightened crops of frames 0–9 used for the by-eye estimates. `finalize.py` merges the two into card.csv and draws the track. `probe*.py` are colour probes.

## How it was measured
- **Card mask (frames 8–38):** a pixel counts as card if its hue is 170–179 or 0–4, its saturation is more than 35 above the same pixel in frame 0 (the wall has S≈95, the card S≈150), and it is no darker than 0.8× the frame-0 brightness (this excludes the cast shadows). The mask is then opened and closed, the largest component kept and holes filled. The reference point is the mask centroid. I checked overlays for frames 9, 18 and 36: they cover the whole card and exclude the shadow and the hand.
- **Frames 0–7:** the card is in the dark vignette and blurred by motion. Centres and boxes were read by eye from the gamma-brightened grid crops, to about ±30 px. Frame 8's mask matches the by-eye path, and so does frame 9 (by eye 1564,2739 vs mask 1555,2730).
- **Camera:** the spotlight disc's half-max bbox stays the same in every frame (x 100–2040, y 1092–3008). Its centroid moves 10–25 px only because the arm covers part of it. No pan or shake, so image coordinates are world coordinates up to one scale.

## Key numbers (px)
- **Card at rest (frames 33–38):** long axis about horizontal (tilt ~1–2°). Length from the left edge (x≈929) to the right edge (x≈1362) is **≈432 px** (range 430–435). Height (short axis) is **≈300 px**; the mask gives 294–316, and the bottom edge is a few px soft. The aspect is 1.44 rather than an ISO card's 1.586, so the card is probably slightly turned. For a size-based scale, use 432 px for the long side and ~300 px for the short side.
- **Apparent length over time:** about 380 px in frames 8–13, about 412 px in frames 14–23 and about 432 px in frames 30–38. This could be changing tilt or distance to the camera, or motion blur and edge softness early on. With one planar scale, use the rest-frame value unless the question names a time.
- **Path:** (1855,3685) at frame 0 → (1589,2801) at frame 8 → (1135,2058) at frame 38. The card moves up and to the left. The path curves slightly: steep at first, then about 45° up-left. Per-frame steps are roughly 100–135 px over frames 1–8, ~75 at 9–10, ~60 at 11–14, ~45 at 16–18, ~25 at 20–23, ~12–20 at 25–31, and under 7 from frame 32. The deceleration is monotonic and there is no reversal.
- **Spotlight:** at frame 0 its centre is at (1064, 2042) and its half-max diameter is 1932 (x) × 1908 (y) px. The edge is soft, so the diameter depends on the threshold.
- **Card shadow:** about 105 px to the left of the card's left edge at frame 38. It moves with the card.

## Events
The card is already moving at frame 0, so its motion starts before the clip. It enters the bright area at about frame 8 (0.298 s). It is essentially at rest from frame 36 (1.341 s); steps are under 7 px from frame 32 on. The clip ends at frame 38 (1.415 s). There is no release, bounce or impact, and the hand holds the card throughout.

## Reliability and ambiguities
- Mask centres for frames 9–38: ±3–5 px. Frame 8: ±10 px, because it is blurred. Frames 0–7 (by eye): ±30 px. Frame-to-frame differences there are noisy, so fit over several frames.
- Mask height jitters by up to ~20 px (296–316) because the bottom edge is soft and sometimes picks up a little shadow. Length is steadier.
- The thumb covers the top-right part of the card's right end in every frame. The card's corners are still visible, so the length is the full length.
- The hand/arm and the card's shadow move with the card. Only the card is tracked. Use it for the hand as well.
- There is only one card and no other moving object, so nothing can be confused with it.
