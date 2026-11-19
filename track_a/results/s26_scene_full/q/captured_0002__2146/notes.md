# q_2146 – size (diameter) of the ball in mm

Lab video, 24 fps (file fps = question_fps = 24), 1280x720, f = 0.5959 x 1280 = 763 px, principal point (640, 360).
depth_info: t=1.0 s (frame 24) ball at 1.779 m; t=1.3 s (frame 31) 1.736 m. Prior (acceleration 4.05 m/s^2) not
needed for a size.

## Method (lab method card)
size = depth x pixel diameter / f.
- At t=1.0 (frame 24) the ball rests on the top edge of the white board, against the uniform green background on
  left, right and top: clean edges. Bottom edge merges with board/shadow (board top edge may hide a little of it),
  so the horizontal extent is used.
- `measure3.py`: luminance rows 277-287, sub-pixel half-max crossings left and right (bg Y~71, ball ~160-200);
  diameter = max chord per frame. Frames 0-26: median 25.23 px, mean 25.33, sd 0.31; frame 24: 25.06 px.
  `measure2.py` printed the luminance map (frames 18-26 averaged): left edge x~603.5, right edge x~628.5 -> ~25.1 px.
- scene/ record: bbox 25-26 px, area ~515 px -> equivalent diameter 25.6 px (threshold mask, slightly generous).
- Adopted 25.2 px -> D = 1.779 x 25.2 / 763 = 0.0588 m = **58.8 mm**.
  (Range 25.06-25.6 px -> 58.4-59.7 mm.)

## Second route
Frame 31 (t=1.3, depth 1.736 m): ball falling in front of the white board, faint, chroma-subsampled and blurred;
chroma (R+G)/2-B half-max chords 16 px, full extent ~22-23 px (expected 25.8 px for a 58.8 mm ball). This route
underestimates (low contrast, shading; noted in scene/notes.md too) and is not used, but its full extent
(~23 px -> 52 mm) is in the same range and does not contradict the rest-frame measurement.

## Confidence
Good: clean static edges, ±0.5 px on 25 px (~2%) plus depth/edge-definition uncertainty -> ~±3%.
