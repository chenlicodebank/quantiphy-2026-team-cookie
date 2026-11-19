# Q93 – speed of the yellow car at 1.0 s (m/s)

- 2D top-down Blender render, 24 fps (file fps = question_fps, no retiming). t = 1.0 s -> frame 24.
- Yellow truck (upper lane) moves in pure -x at constant velocity from frame 1->2 to the end.
- Scale from prior: length 5.67 m. Pixel length measured in code (measure.py, core band rows 375-430,
  saturation>50 or dark mask): 308 px at frame 24 (also the clip median; 302-314 over the clip because of mild
  perspective). Checked visually on frames/f24.png (front ~1174, rear ~1481). -> 0.01841 m/px.
- Pixel speed at frame 24: column-profile cross-correlation 11.46 px/frame at f24, 11.41 mean over f20-28,
  11.42 over the whole clip; bbox edges/centre in scene record 11.26-11.41. Used 11.37 px/frame.
- Speed = 11.37 x 24 x 5.67/308 = 5.02 m/s (range 4.97-5.06 over the pixel-rate and length spreads).
- Second route: scene record's cx_xcorr track (11.40 px/frame) and length 310 at f24 -> 4.98 m/s. Agrees.
- Confidence: high (likely 5.0 m/s true value).
