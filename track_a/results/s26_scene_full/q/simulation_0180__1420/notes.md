# Q1420 – height of the entrance gate (incl. frame)

The video file and the question both run at 24 fps. Static camera, 3D Blender render.
The gate is the glass door with its wooden frame at the far left of the image (scene.json: "entrance_door").

## Focal length (fitf.py)
- Prior: trolley (shopping cart) acceleration 1.507 m/s², starting from rest at frame 0 (pixel steps 0,1,2 px in frames 1-3).
- Model: P(t) = P0 + ½·a·t²·D. P0 = 12.589 m along the ray of the cart reference pixel at frame 0. D is a unit 3D direction.
  Fitted f and D to the whole 60-frame pixel track, with the given depth 12.513 m at t=0.5 s (frame 12) as a constraint.
- Results: bbox centre f=2697, bottom point 2678, wheel centroid 2668, frames 0-39 only 2690-2708. RMS residual 0.4-0.6 px.
  Adopted f ≈ 2690 px (HFOV ≈ 39°). The given depth at t=0.5 is reproduced (12.509).

## Floor plane and camera height (tiles.py, geom.py)
- Hough lines on the floor tiles: the receding tile seams meet at a vanishing point of (1569, 213) px, with a median residual of 1.6 px.
- Floor normal = (that direction) × (fitted cart direction D). The two directions are 89.4° apart, which matches a square
  tile grid with the cart moving along it. Horizon v ≈ 214 px, pitch 6.9° down, roll 0.1°.
- Camera height: the cart's floor-contact centre is at pixel (384, 941), the mean of the 4 wheel bottoms read at 3× zoom:
  near wheels 948 and 957, far wheels 923 and 937. It sits at the cart's depth (Z = 12.25 m), which gives h = 3.28 m.

## Gate
- Measured at 5× zoom on frame 58 (the cart is away from the door). The wooden post (x 81-136) stands on the floor at
  v ≈ 807. The top edge of the wooden header is at v ≈ 80.
- Ray through (108, 807) intersected with the floor gives the gate base at a depth of 15.0 m (15.8 m from the camera).
- Vertical segment from the base, solved so that its top projects to v = 80: **H = 4.01 m**.
  The predicted image tilt of the vertical (u 108 → 79) matches the slant of the post.

## Checks and sensitivity
- Horizon-ratio route: H ≈ h_cam·(v_bot − v_top)/(v_bot − v_hor) = 3.28·727/593 = 4.02 m.
- f from 2630 to 2740 px gives H = 4.10 to 3.94 m.
- A contact-point v of ±9 px gives H ±0.05 m.
- Sanity check: the cart is about 1.29 m tall in this scene (283 px at Z 12.25 m), so the gate is 3.1 cart heights.
  That is plausible for an entrance with a header frame, and the scene is about 1.3× real scale.
- Confidence: moderate-good, ±4%.

Answer: 4.0 m
