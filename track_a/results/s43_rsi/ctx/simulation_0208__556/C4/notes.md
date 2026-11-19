Scale from the free-fall prior: own centroid track over frames 0-9 fits cy=6.334 i^2 (rms 1.1 px) -> 7322 px/s^2, so A=747 px/m (1.339 mm/px); check: width 293 px = 0.39 m, a full-size typewriter. The render has real perspective (horizon at the image centre, camera 0.65 m above the desk), so the silhouette height at rest (175 px) is inflated by the visible top face. Measuring the extent where the object's centre crosses the horizon (142 px, SAM frame 7 vert_px=146) and correcting with the measured perspective term 2eps=D/z=0.083 gives h=0.188-0.194 m; second route (extent vs height fit, intercept 144.6 px) gives 0.194 m. Answered 0.20 m, a small hedge toward the flat-2D pixel-extent value (0.234 m).

Final message:
I measured the typewriter's height at **0.20 m**.

**Method summary:**
- **Scale from the prior:** my own silhouette track over the free-fall frames gives cy = 6.334 i² (rms 1.1 px) → 7322 px/s², so A = 747 px/m (1.339 mm/px). Cross-check: the typewriter's 293 px width → 0.39 m, a realistic full-size machine.
- **Camera geometry:** the desk's far edge is horizontal and the mat's depth-direction edge converges to the image centre, so the optical axis is horizontal (horizon y = 540) and the camera sits 0.65 m above the desk. The fall therefore doesn't change depth (width constant to <0.5 %).
- **Height:** because the camera looks down on the object, the rest silhouette (175 px) is inflated by the visible top face. Measuring the extent at the instant the object's centre crosses the horizon (142 px, confirmed by SAM at frame 7) removes that term → h = 0.190 m; an independent extent-vs-height fit gives 0.194 m, and the corrected rest extent gives 0.188 m.
- **Second route / caveat:** the naive flat-2D pixel extent × scale would give 0.234 m; the video plainly shows perspective (apparent height 127→175 px during the fall), so I used the perspective-corrected world-space value and hedged slightly to 0.20 m.
