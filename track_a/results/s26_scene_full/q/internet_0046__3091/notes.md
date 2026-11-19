# q3091 velocity of cup at 1.10 s
- t=1.10 s -> frame 33 (file fps = question fps = 30).
- Camera static (scene record; caps move <=3 px).
- Scale: cup body height rim-to-base = 570 px (scene record median 568-582; own gradient check frame 33: top 303, base ~869 -> 566). 10.5 cm / 570 px = 1.842e-4 m/px.
- Pixel motion frame 33->34 (forward difference, annotator convention): body centre 862.6->977.7 = 115.1 px; own left-edge 50% crossing 629.5->744.5 = 115.0 px; profile cross-correlation shift = 115 px. Three routes agree.
- v = 115 px * 30 /s * 1.842e-4 = 0.636 m/s. (Backward diff 111.6 px -> 0.617; central -> 0.626.)
- Confidence: good; main uncertainty is the height pixel count (+-2%).
