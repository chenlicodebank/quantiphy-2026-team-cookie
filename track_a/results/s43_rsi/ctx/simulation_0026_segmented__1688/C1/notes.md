# q1688 – length of the boat (m)

The file runs at 25 fps, but question_fps is 24, so t=1 s is frame 24 and t=2 s is frame 48 (I used the frame
column from scene/ tracks).

## Focal length (from the prior)
I measured the human mask myself (human.py, thresholds 10/20/40). Head top to feet is 50–51 px at T10 and 48–49 px
at T20 (frames 0–74). The head is faint and the person is walking, so I take the rest height as about 51.5 px
(range 49–53). With the human at 114.83 m: f = 51.5·114.83/1.75 ≈ 3380 px (HFOV ≈ 16°).

## Boat geometry
- The boat is in a 3/4 view. Using f and the given depths (103.157 m at t=1, 106.091 m at t=2), the origin moves
  ΔX ≈ −3.0 m and ΔZ ≈ +2.8 m in that second. This puts the heading (bow first) about 42–43° from the image plane,
  with the bow pointing away (solve2.py, heading.py).
- First check on the heading: the apparent extent shrinks faster (251→239 px) than 1/depth alone would explain.
  A rigid boat reproduces this best at a heading of about 40° over frames 24–48 (35–38° using all frames, which
  relies on extrapolated depths). The cabin's face widths (side 50 px, back 25 px) also fit about 40°.
- Bow tip (stem, on the centreline) is at x ≈ 195 (frame 24) and 110 (frame 48). The rightmost silhouette point
  (x ≈ 444.5 / 348) is the far quarter of the rounded stern, not the aft end of the centreline. I put the aft
  centreline point about 10 px (range 8–16) inside it, based on the rudder position and a rounded-stern model.
- L = distance between the points where the bow and stern pixel rays meet the boat's 3D centreline (passing through
  the origin along the heading). This is full pinhole geometry.

## Results (frames 24–48)
- off=10 px, h=51.5 px: L ≈ 10.4–10.5 m.
- Spread: off 8→16 px gives 10.6→10.3 m; h 49→53 px changes L by about ∓2%; using the full silhouette (off=0)
  gives 10.95 m; a 40° heading instead of 42.8° gives about 10.0 m.
- The two heading estimates (motion and size change) agree to within about 3°.

Answer: 10.4 m. Confidence: moderate (±6%). The main uncertainties are the aft-point offset and the heading.
