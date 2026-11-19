# Q1039 – minimum distance, outer end of pier → boat, t = 3 s (round 3)

**Answer: 2.15 m. Decision: new (own value; it verifies round 2's proposed 2.23 within 4 %).** Confidence: medium.

## Inputs and time base
- Prior: boat height 0.75 m. Boat distance 7.452 m at t=0 (frame 0) and 6.655 m at t=1 (frame 24). Pier 11.579 m.
  Stairs 17.623 m.
- File rate 22.80 fps with 66 frames. question_fps is 24, so t = 3 s is frame 72, seven frames past the end. The boat
  position there is extrapolated from a linear fit to the bow track. Unit: metres.

## Crux
Which two points the distance runs between:
- pier origin → boat origin (C1/C2, 5.68, submitted);
- pier front edge → boat origin (C3/C9/DeepSeek runs, 2.2–3.9);
- pier front face → nearest boat surface (round 2, 2.23).

Numerically, the only open quantity is the depth of the pier front, Z_pf.

## Verification of round 2 (own code: measure.py, measure2.py, pier_axis.py, stern_axis.py, stem_view.py)
1. **Boat.** I used a constant-depth pinhole with the principal point at (540, 540) and the origin at bow + 324 px.
   - It gives f = 1002.5 px and Z_b = 5.858 m. Origin variants give f 986–1016 and Z_b 5.80–5.92.
   - Linear bow fit at frame 72: 247.6 px, so the origin is at u = 571.6 and X = 0.18 m.
   - Boat length 3.79 m, speed 1.42 m/s.
   - These reproduce round 2 and C1/C3.
2. **Pier-front water row** (`pier_axis.py`, frame 0, no boat):
   - The mirror correlation over a 40-row span (front beam plus its reflection) gives 675–676 in every column from
     470 to 630, so ap = 675.5. This reproduces round 2 exactly.
   - The front is square to the camera: the axis does not vary across the width.
   - Shorter spans lock onto leg detail and scatter between 662 and 690. I did not use them.
3. **Water row at the boat centreline**, by a route round 2 did not use: mirror axes at the two centreline ends.
   - Stem post and its reflection: 738 at frame 65 (11 columns), 739 at frame 63, 739–740 at frame 50.
   - Stern end: 740–745 in its valid columns.
   - Round 2's planform fit gave 744 ± 2; C3 got 740–747.
   - Best a_c = 742 ± 2.
4. **Horizon.** The deck side edges, through corners (462,630)→(495,592) and (637,630)→(603,592), meet at
   y ≈ 531. C3 got 531–535 and round 2 got 533–534. I used y_h = 533 (bracket 531–537). The camera is 1.23 m above
   the water.
5. **Half-beam** (`measure.py` profile, frame 65, midship columns):
   - Far rail top at 663.5: a dark-to-bright step from 56 to 105.
   - Near gunwale white band top at 692.5: a step from 133 to 206. The overlay shows this band runs from stem to
     stern.
   - b = Z_b(dn − df)/(dn + df) = 0.586 m (0.578–0.602 over y_h), so the beam is 1.17 m.
6. **Results:**
   - Z_pf = Z_b(a_c − y_h)/(ap − y_h) = 5.858·209/142.5 = **8.59 m**.
   - Gap = 8.59 − 5.858 − 0.586 = **2.15 m**. The range is 1.98–2.31 over a_c 738–746 and y_h 531–537. Round 2's
     a_c = 744 gives 2.23.
   - The rail is 0.39 m above the water and the pier front beam spans 0.25–0.38 m, so the closest points face each
     other in depth. The boat (X −1.70…2.08) covers the pier front (X −0.70…0.84) at frame 72.
   - Other readings with the same geometry: front-face centre → boat origin is 2.73 m; origins is 5.68 m.

## Rechecks
a. **Closure.**
   - Post top (row 620) to the centreline water row (742) is 122 px, which is 0.713 m at Z_b. Against the 0.75 m
     bbox height that is −4.9 % with zero draft. A few cm of keel below the water closes it.
   - The given distances are reproduced exactly, but that is by construction.
   - The constant hull height of 88 ± 2 px over the whole clip confirms the constant-depth model.
b. **Plausibility.** Boat length 3.79 m, beam 1.17 m, freeboard 0.39 m, speed 1.42 m/s. Pier 1.50 m wide (175 px at
   8.59 m), deck 0.38 m above the water, about 5.5 m long. Camera 1.23 m above the water. All are realistic.
c. **Units and time base.** Metres. t = 3 s is frame 72 at 24 fps. At the file rate it would be frame 68.4; the boat
   is still in front of the pier and the gap is unchanged (pure depth gap).
d. **Fault proof.**
   - C1/C2 (5.68): they measure to the pier origin. At y_h ≤ 537 that origin lies at Z ≈ 11.5 m, the deck centre.
     The outer end is at Z_pf = 8.59 m. For the origin to sit at the front, the horizon would have to be at row
     ≈ 607, below the boathouse base (≈ 590), which is impossible. So 5.68 is not a distance from the outer end.
     It is also origin to origin, not a minimum (surface) gap (LESSONS #13).
   - C3 (2.75) and C9 (3.34): they measure to the boat origin, not to its surface, which adds 0.59 m. C9's Z_pf of
     9.29 also disagrees with the mirror-axis 8.59.
   - C7 (2.21): its Z_pf of 8.00 is too shallow and it measures to the origin. The two errors cancel.
   - C4/C5/C6/C8 (2.8–3.9): edge-to-origin readings with scattered front depths.
   - Round 2 (2.23): no fault. Its centreline water row (744) is 2 px above my 742, which accounts for the 0.08 m
     difference.

## Decision
The submitted 5.68 has a proven fault: its endpoint is the pier origin at the deck centre, not the outer end, and it
is not a minimum distance. Round 2's measurement reproduces, with ap 675.5 identical and my gap within 4 %. I answer
with my own value, **2.15 m**. The remaining risk is the reading: if the reference measures front edge to boat
origin, the answer would be about 2.7 m.
