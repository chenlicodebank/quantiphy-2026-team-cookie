# q_1183: height of the walking person (simulation_0046)

**Answer: 1.88 m**

The file is 33 fps and question_fps is also 33, so t=1 s is frame 33 and t=2 s is frame 66.

## Method (3D, pinhole)
- **Prior.** The moving bicycle's wheel diameter is 0.65 m. Depths are given for the bike and the walker at t=1 and t=2.
- **Wheel diameter in pixels** (`wheelfit.py`). I took radial intensity profiles around each hub and found the outer edge of the dark tyre (the half-intensity crossing). I then fitted a circle and an axis-aligned ellipse to those edge points, in every second frame from f14 to f72.
  - The horizontal semi-axis is the cleanest value. I fitted it linearly over f24-72 (`final.py`).
  - Front wheel: 49.98 px at f33 and 46.12 px at f66.
  - Rear wheel: 51.19 px at f33 and 47.64 px at f66. The rear wheel is a little nearer the camera, because the bike recedes as it rides left.
  - Mean diameter (front and rear semi-axes added): **101.2 px at t=1 and 93.8 px at t=2**. This average stands for the bike origin, which sits between the wheels.
- **Focal length.** f = D_px · Zc / 0.65, with Zc = d / sqrt(1 + r²/f²) and the principal point at the image centre. This gives f = 1926 px at t=1 and 1861 px at t=2; the mean is 1894.
- **Walker height in pixels.** I used the scene record's head top to lowest shoe pixel, checked against bbox rows. I took mid-stance frames, where the legs are together and the walker stands tallest:
  - 246.5 px near f35 (t≈1)
  - 243.5 px near f68 (t≈2)
  - About 246.5 near f52 and 244.5 near f85 as well.
  - I treat the mid-stance walking height as the standing height.
- **Height.** H = h_px · Zc_walker / f:

  | time | with that time's own f | with the mean f |
  |---|---|---|
  | t=1 | 1.817 m | 1.846 m |
  | t=2 | 1.944 m | 1.912 m |

  The answer is the centre of these values: **1.88 m**.

## Second route and inconsistency
- **Pixel sizes do not change the way the depths predict.**
  - From t=1 to t=2, the bike's pixel size shrinks by a factor of 1.08-1.09. Three measures agree on this: wheel fits, wheelbase (1.076) and the record's template scale (1.074). The given depths predict only about 1.044.
  - The walker's pixel height shrinks by only about 1%, where the depths predict about 4.9%.
  - No choice of principal point fixes both objects together, because they would need shifts in opposite directions. So I averaged the two times instead of trusting just one.
- **Cross-check.** Using the t=1 focal length with the t=2 walker, or the reverse, gives about 1.87-1.91 m. That agrees with the answer.
- **Confidence.** The answer should be within about ±4% of the true value. The spread between the two times is the main source of uncertainty.
