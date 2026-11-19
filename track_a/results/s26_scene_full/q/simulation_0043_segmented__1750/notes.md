# q_1750 — width of the boat (prior: length = 10 m; depths 173.7093 m at t=1 s, 174.5515 m at t=2 s)

Answer: **3.05 m** (beam, horizontal extent across the hull).

File fps 24 = question_fps 24, so t=1 s is frame 24 and t=2 s is frame 48.

## Method (3D pinhole, zero roll)
1. Boat image motion (linear fit of the scene/ centroid track): (-3.534, -1.024) px/frame, 88.3 px/s, at 16.2 deg above
   leftward. Bow is on the left and the boat moves bow first.
2. Hull length in pixels along that axis, measured on the mask (`lengthpx.py`): 222 px at frame 24, from the bow tip
   (251,883) to the lowest stern point. I took off ~3 px because the stern point sits lower than the bow tip:
   l = 219 px.
3. `solve.py`: back-project the centroid at frames 24 and 48 with the given depths (as a function of f). Assume the
   motion is horizontal along the hull axis and the camera has zero roll. That gives the pitch from the motion
   vector; matching the 10 m length to l then gives f.
   Result: f = 3856 px (hfov 15.9 deg), pitch 54.9 deg, ray to the boat 60.5 deg below horizontal, speed 4.05 m/s.
   This fit was **checked against measurements it did not use**:
   - Predicted image direction of the beam: 112.0 deg (y down). Measured: 109-114 deg, from the edges of the green deck
     hatch and the rear edge of the cabin roof (`hatch.py`, `roof.py`).
   - Predicted lean of vertical lines: 4.5 deg, top to the left. Measured: 2.7-4.3 deg on the cabin's rear vertical
     corner (`cabedge.py`). The mast leans the other way by ~6.6 deg, which fits a mast raked aft (not used).
4. `rectify.py` / `width_frames.py`: map two edges onto a horizontal plane in boat coordinates (X along the axis, Y
   across it). The far edge is the top of the silhouette; the near edge is the white gunwale line on top of the red
   hull stripe. Both edges are at gunwale height, so the choice of plane height cancels in the chord.
   - Widths amidships (X = -1.25 to +0.25 m from the origin): 2.86-3.00 m, averaged over 7 frames (4 to 68).
   - The near edge reaches its maximum Y of 1.46-1.50 m at X ~ +1 m, where the far side is hidden by the cabin.
     Assuming the hull is symmetric about the amidships midline (Y ~ -0.06 to -0.1), the maximum beam is ~3.08-3.16 m.
   - Forward deck (X = 2.75 m): 2.7-3.3 m, narrowing towards the bow, as it should.
   - Taking the measured chord (~2.97 m) and the symmetric maximum (~3.1 m) together: **W ≈ 3.05 m**.

## Second route / consistency
- The result repeats across frames 4-68 within ±0.1 m.
- The beam direction and vertical lean predicted by the solve match the image independently (see step 3).
- Sanity check: L/W = 3.3, normal for a 10 m fishing boat.

## Uncertainty
- About ±4%. The main sources are which edges mark the extreme beam (the far gunwale amidships sits behind the cabin
  and a dark deckhouse) and ±1.5% from the pixel length l.
- Notes on the scene/ record: its mask_width (~117 px) includes the cabin and mast and is foreshortened, so I did not
  use it.
