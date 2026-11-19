# Q548 – height of the typewriter (m)

Prior: typewriter falls at 9.8 m/s^2 before 0.45 s (frames 0-10 free fall, impact between 10 and 11).
question_fps = file fps = 24. No depth_info -> scale from the free-fall pixel acceleration.

## Pixel acceleration (features.py, chained template tracking, frames 0-10, quadratic fits)
- carriage middle (back of machine): 6944 px/s^2 (rms 0.1 px); left paper-guide plate (back): 6890
- logo dot on body side: 7230; keyboard (front): 7380
Features at different depths have different pixel accelerations (a_px = f g / Z): ~6.5 % front-to-back
spread, so the scale must be taken at the depth of the edges that define the height.
The scene record's bbox-centre value (~7085) is a mix of these edges.

## Pixel height (height.py)
Low-threshold (diff > 8-10) silhouette vs clean background, column profiles:
frame 0 top 190-191, bottom 314-315 -> 124 px; frames 1-3: 125, 125, 123 px (constant).
(The scene record's 113 px used threshold 30 and missed the faint carriage top.)
The desk side edges converge to a horizon near y ~ 470, so in frames 0-3 the camera is level with or below
the typewriter: the silhouette then runs from the top of the carriage to the bottom of the base at
the back of the machine (no top surface showing), i.e. the true height at the back-plane depth. Later frames
show the top surface (camera above) and the height grows to ~170 px, so they are not used.

## Result
Scale at back depth = 9.8 / ~6920 px/s^2 = 1.416 mm/px -> H = 124 x 1.416 = 0.176 m.
Check: H_px rescaled to the mid depth (124 x 7150/6920 = 128 px) with the mid-depth scale (9.8/7150)
gives the same value. If the mid-depth scale were applied to the unscaled 124 px: 0.170 m.
Plausibility: width 291 px -> ~0.39-0.41 m; a 0.39 x ~0.18 m vintage typewriter is realistic.
Answer 0.175 m. Confidence: moderate-good (+-5 %); the main uncertainties are which depth the silhouette
edges lie at (+-3 %) and the faint carriage-top edge (+-2 px).
