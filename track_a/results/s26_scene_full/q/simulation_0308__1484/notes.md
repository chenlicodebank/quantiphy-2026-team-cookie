# q1484 – length of the whale (m)

Prior: whale speed 1.67 m/s. depth_info: d(t=1)=33.7307 m, d(t=2)=35.1624 m. question_fps = file fps = 24.
3D Blender scene, static camera, one whale swimming up-left (away from the camera) over a flat floor, casting a crisp shadow.

## Camera model (model3d.py, fit_ft.py)
- I assume a pinhole camera with its principal point at the image centre and zero roll. The camera is pitched down by th. The whale origin moves horizontally at 1.67 m/s with heading psi, and |O(t=2)| must equal 35.1624 m given |O(t=1)| = 33.7307 m.
- The blowhole is a sharp rigid feature, so I used it as the motion reference (track3.py). The skin texture is unusable: it does not move with the body (DIS flow on the back is about 0). The blowhole moves (1105.6,367.3)->(1053.9,338.7) between f24 and f48.
- Solving with origin pixel guesses (1230..1350, 600..700) and blowhole height 0-2 m above the origin plane gives f = 3100-3800 px (HFOV 37-45°), pitch 18-21°, heading -25..-27°. The horizon then sits at y ≈ -450..-650. A floor-texture anisotropy check puts the horizon at about -540..-800, which agrees.
- Check: the shadow's motion on the floor plane points along the solved heading to within a degree for every camera. The shadow front stays a constant 4.9-5.1 m ahead of the origin in all frames.

## Main route: whale shadow on the floor (shadow_series.py, robust_cam.py, front_speed.py)
- A horizontal body casts a shadow from directional light that is congruent to its top-view outline. It is exact for the length whenever the snout and fluke are at the same height (tail at mid-stroke).
- Floor scale: the shadow translates at the whale's horizontal speed (1.67 m/s). Its front moves 0.109-0.121 floor-units/s, which puts the floor h_f = 13.8-15.0 m below the camera (14.4 m from the f12-66 fit). The whale origin is about 10.8 m below the camera.
- Shadow length from front to fluke rear, in metres:
  - f48 / f54: 18.9 (only just cut by the bottom edge), mid-stroke.
  - f60: 18.7 (cut).
  - f66: 17.8 (tail raised).
  - f71: 16.9 (tail raised).
- Across very different camera solutions (f 2600-4200, pitch 17-28°) the mid-stroke length stays at 18.6-19.6 m. The route is insensitive to the camera because the length and the speed are measured on the same plane.
- Range from the h_f spread: 18.0-19.6 m.

## Second route: whale body mapped to the horizontal plane through the origin (body_f0.py, length_plane.py)
- Frame 0: the fluke lobe tips are about 2 m behind the fluke notch and the fluke span is 5.0-5.5 m.
- Notch to blowhole is 14.6-19.4 m, depending on how far the blowhole sits above the axis (0-2 m). The snout is hidden beyond the head crest, about 2-3 m ahead of the blowhole.
- Total 18.6-24 m. This agrees with the shadow route if the blowhole is about 2 m above the axis, which is plausible for a whale about 19 m long. The route depends on heights, so it is only a consistency check.

## Answer
L ≈ 19.0 m. This is the shadow length at mid-stroke, taken as the whale's longest horizontal extent; the reference is the world-space bounding box. I assumed the whale's heading runs along a world axis; if it doesn't, the bounding box would be longer. The raised-tail pose gives about 17-18 m.

Confidence: moderate (about ±10%). The main uncertainty is the floor scale h_f (±4%), whether the cut fluke extends a little further, and the light/thickness effect on the shadow front.
The record in scene/ had no metric scale. Its head_top track is fine. I did not use the 'head' patch (track2) or the texture-based patches, because they lock onto features that do not move with the body.
