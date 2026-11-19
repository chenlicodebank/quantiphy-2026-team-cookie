# q6 — body length of the bird (m); prior: bird speed = 6 m/s

2D top-down (nadir) scene, static camera, the bird flies straight toward +x. Body length and speed are measured
in the same plane (the bird's height stays constant: its length stays ~130 px all clip), so
length = 6 m/s x length_px / speed_px_per_s does not depend on depth.

File fps 22.925 (61 frames); question_fps 24. The file skips one source frame before file frames 19 and 43
(double steps there, also a likely third skip in 50-58). Steps between adjacent non-skipped file frames are one
source frame = 1/24 s. Script: `measure.py` (uses scene/tracks/bird.csv frame column; skips accounted for).

Measurements
- Body length (beak tip to tail tip), clean frames (no shadow contamination, frames < 46): median 130 px
  (mean 130.5, n = 35); checked by eye on a gridded crop of frame 32 (~128-133 px).
- Speed profile: accelerates (frames 0-17), cruises at a constant speed (frames 19-45), decelerates (46-60).
  Cruise, fitted on beak and tail: 19.7-20.4 px/frame -> 478-485 px/s at 24 fps.
- Body length with 6 m/s = cruise speed: 1.61-1.63 m -> answer 1.62 m.

Second route / alternative reading
- Tail-tip track gives the same cruise speed (20.2 px/frame for 20-42) -> same answer.
- If 6 m/s were the clip-average speed (net 965 px over 63 source frames = 374 px/s), length would be 2.09 m.
  I took the cruise (constant-phase) speed as the designed "speed of the bird"; it is also the less implausible one.

Plausibility: 1.6 m is very large for a crow/raven-like bird (real ~0.6 m); the ground props (barrel ~77 px)
also suggest the bird/prior pair is not at real scale relative to the props. The answer follows the exact prior,
which is the only metric scale given. Confidence: moderate (main risk is which speed the prior refers to).
