# Q303 – length of the white airplane

The video is a 2D top-down view. The file rate and question_fps are both 24 fps. The "car" in the prior is the tug towing the plane, the only vehicle that moves.

- **Pixel speed.** `measure.py` tracks templates of the nose and the tug from frame 71 back to frames 2, 50 and 60. The motion is a constant 5.247–5.249 px/frame, which matches scene/ (5.247). The tug and the plane move together.
- **Scale.** 11.155 / (5.2475 × 24) = 0.08857 m/px.
- **Plane length at frame 71.** I read the intensity profile along the fuselage axis (x ≈ 475) and a zoomed grid crop. The nose edge is at y ≈ 542.5 and the tail tip at y ≈ 966, so the length is ≈ 423 px, the same as scene/.
- **Answer.** 423 × 0.08857 = **37.47 m**.

**Plausibility check.**
- The wingspan is 386.5 px, or 34.2 m.
- Together, a 37.5 m length and a 34.2 m wingspan are about the size of an A320-class airliner (37.6 m long, 35.8 m span), so the scale is realistic.
- The tug body is 4.3 m long (6.3 m with the prongs), which is also plausible.

**Confidence.** High, about ±2 %.
