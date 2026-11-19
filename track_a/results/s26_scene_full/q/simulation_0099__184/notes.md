# q184: shark speed at 1.0 s (frame 24)
2D video at 24 fps (file fps = question_fps), static camera.
Scale: boat length = 10 m. At frame 0 the boat spans x 231-1087 px (my own threshold on hull rows 360-560), so 857 px; the scene record gives 228-1087 (851-860 depending on the edge definition). That makes 0.011669 m/px.
Shark speed: the scene record's ref_x gives 573.56 -> 562.72 = 10.84 px/frame (frame 23->24), and the whole run is constant at -10.76 px/frame.
My own template match: 10.78 (frames 23->24), 10.83 (22->26), 10.83 (20->28). I used 10.80 px/frame.
Speed = 10.80 * 24 * 10/857 = 3.02 m/s.
Second route: the motion is constant, so the global fit (10.76 px/frame) gives 3.01 m/s. Confidence: high (about 2 pct), assuming the boat length = the hull bbox extent.
