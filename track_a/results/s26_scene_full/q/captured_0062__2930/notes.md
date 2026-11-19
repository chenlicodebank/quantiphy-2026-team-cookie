# q_2930: height of the trashbin (cm), captured_0062

The object is the blue patterned waste bin at the back left (bbox about x 289-379, y 104-208 px; static). Frame for t=1.4 s is round(1.4x24) = 34. The file rate and question_fps are both 24.
Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).

## Pixel measurements (frame 34; binmask.py, V-profiles)
- Back rim top: y about 110-111.
- Front rim (lip highlight) at the centre line: y about 134-136 (x 328-350).
- Bottom front edge: y about 207-208 (x 325-340).
- Top width is about 90 px and bottom width about 66 px, so the bin tapers.
- Full image extent is about 97-104 px; the scene bbox of 107 includes a little of the white bag behind.

## Camera tilt (vp.py)
- The right-wall panel seams, which are vertical lines (11 Hough segments), meet at a vertical vanishing point (464, 1351). From that, world up in camera coordinates is (0.140, -0.785, -0.604), which puts the optical axis about 37 deg below horizontal.
- The board's own plane normal, from its corner vanishing points, agrees within 2.7 deg.

## Problem: the given bin distance (2.303 m) is not consistent with the scene
- With the given depths of the floor objects, the implied camera height is: board 1.81, bag 1.73, box 1.58, toy 1.73 m (median 1.73).
- Placing the bin at 2.303 m along its ray puts its base about 0.7 m above the floor. The bin also stands far beyond the board, whose distance is 2.815 m, so it must be farther than 2.8 m.
- If the 2.303 m is taken at face value, the bin height would be 0.22 m with the tilt geometry, or 0.32 m with the naive card (107 px x 2.303 / f). I consider this depth reading wrong.

## Method used (height_floor.py)
- Floor plane: the seam up-vector and a camera height of 1.73 m.
- The bottom front edge pixel's ray meets the floor at 3.77 m.
- A vertical, tapered front face (taper about 9 px per side, about 4.5 cm) is intersected with the front rim ray, then the back rim ray.
- Results by camera height:
  - h = 1.73 m: H = 0.358 m (0.340 m without the taper correction)
  - h = 1.70 m: H = 0.352 m
  - h = 1.80 m: H = 0.373 m
  - h = 1.60 m: H = 0.331 m

## Independent checks
1. **Basketball beside and behind the bin.** The floor geometry places it at about 4.0 m. A 24 cm ball there should appear 46.0 px across, and the measured diameter is 44-48 px. This confirms the scale near the bin.
2. **Prior.** The board speed from floor-plane back-projection at frame 34 is 1.94 m/s, as a 5-frame central difference over frames 32-36, which includes the frame 35-36 jump. The single steps are about 1.5 m/s. The prior is 1.934 m/s, so the floor scale is consistent with it.

## Answer
H is about 0.35 m. Confidence is moderate: the uncertainty is about ±6%, from the camera height and the taper. The other risk is that the reference instead used the inconsistent 2.303 m depth.
