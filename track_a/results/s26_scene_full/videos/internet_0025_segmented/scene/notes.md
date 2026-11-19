# internet_0025_segmented – measurement notes

**Scene.** Segmentation video (internet footage with the background replaced by pure white), 2D, 1280x720,
29.970629 fps, 305 frames (0–304, t = frame/fps). The only content is one long wooden boat (orange-brown, side-on,
square stern on the LEFT, pointed upturned bow on the RIGHT, dark cargo mid-deck). One person in dark clothing stands
at the stern holding a pole/paddle. No water, ground, or other objects are visible, so there are no static objects.

**Files.**
- `scene.json`: inventory, summary sizes, positions, events, camera.
- `tracks/boat.csv` (305 rows): frame, time_s, cx/cy = centre of the bounding box of the whole foreground mask
  (boat plus person), mask_cx/mask_cy = mask centroid, bbox_x0..y1, hull_x0 = stern end, hull_x1 = bow tip,
  hull_len_px = stern-to-bow length, hull_top_y (approximate gunwale line) / hull_bot_y (keel),
  length_main_axis_px / width_across_px from PCA of the mask, height_px, axis_angle_deg, area_px, occluded.
- `tracks/person.csv` (305 rows): bbox from the top of the head down to the gunwale line, cx/cy,
  height_above_deck_px, width_px. occluded=1 because the lower body is inside the boat.
- `scripts/track.py`: foreground = pixels with min(RGB) < 200, opened with a 2x2 kernel, blobs of 20 px or more.
  `scripts/check.py`: summary and overlay (frames/check.png, checked visually at frames 0, 100, 200 and 304).
  The boxes cover the boat from stern to bow tip.

**Key numbers (pixels).**
- Boat length, stern to bow tip: median 234 px (range 230–237, ±2 px of segmentation jitter, no trend, so there is
  no visible change in depth or zoom). Total bbox height including the person: about 50 px. Hull alone: about 20 px.
- Person height above the gunwale: about 30 px (range 26–33).
- Motion: steadily to the right. cx goes from 584.5 (frame 0) to 739.5 (frame 304), a net +155 px. The stern goes
  468→624 (+156 px) and the bow 701→855 (+154 px). The mean is 0.51 px/frame, about 15.3 px/s. Per 30-frame window:
  15, 13.5, 14, 14.5, 16, 14.5, 18, 17, 16.5, 14 px, so the boat speeds up slightly around frames 180–270. Vertical
  drift is about −3 px (slightly upward). The motion is roughly uniform, and the boat is already moving at frame 0
  and still moving at the last frame. There are no bounces, stops or direction changes.

**Reliability and ambiguity.**
- The camera cannot be checked because the background is white. The positions are image coordinates. If the
  original footage panned, image displacement would not be true displacement. The boat's constant size suggests a
  steady side-on view.
- The per-frame pixel steps are 0–1 px because of quantisation. Differentiate over windows of at least 10 frames.
  Use hull_x0 or hull_x1 (stern or bow) or cx as the reference point. The three agree within about 2 px.
- For a length prior ("boat length"), use hull_len_px, about 234 px, measured bow to stern along the main horizontal
  motion direction.
- The person's bbox width sometimes includes the paddle (13–36 px). The person's height is only above the gunwale.
