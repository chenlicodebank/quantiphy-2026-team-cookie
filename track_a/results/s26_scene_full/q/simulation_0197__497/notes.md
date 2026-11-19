# Q497 — diameter of the plunge tube (glass pipette), metres

Prior: horizontal width of the "skynova" text on the bottle = 0.00188 m. No depth_info. fps 30 = question_fps.

## Scale (measure.py)
The brand text runs vertically (rotated 90°) on the left of the bottle label; only "NOVA" is in frame. Its horizontal
on-screen extent is the letter height. Threshold for white, low-saturation pixels in x 1050–1300, y 1950–2560:
letters V, V(A), O, N each span x 1106/1108 → 1184/1186, so 78–80 px per letter and 80 px for the union. Results are
the same at thresholds 180 and 190. Width used: 79.5 px, so the scale is 0.00188 / 79.5 = 2.365e-5 m/px.
Sanity check: the bottle body (~1160 px) comes out at ~27 mm wide, which is plausible for a serum bottle.

## Tube diameter (tube5.py; tube4.py draws the edges for a visual check)
I rotated the frame by 31.5° so the tube axis is horizontal, then took column-averaged profiles across the
liquid-filled section. Edges are half-max crossings: the top is where the background drops to the dark outer wall,
and the bottom is where the bright lower glass wall drops to the background. The outer diameter is 216.1 px
(std 0.5 px over 12 positions). Frames 0, 24 and 49 give the same value, and the edge lines overlaid on the original
frame follow the outer glass surface.
The scene record's estimate of "~145 px" for the outer diameter was a rough grid reading and is wrong. The tube is
about 216 px wide.

## Answer
D = 216.1 × 2.365e-5 = 0.00511 m (about 5.1 mm).
Second check: the ratio of tube to bottle body (216/1160 ≈ 0.19) fits a ~5 mm pipette in a ~27 mm bottle.
Main uncertainty: the text and pipette may sit at slightly different depths. I used a single planar scale, following
the 2D convention.
Confidence: moderate-high (±5%).
