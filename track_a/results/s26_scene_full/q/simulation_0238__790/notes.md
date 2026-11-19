# Q790 – width of each glass window (m)

Prior: speed of the horse at the back = 0.874 m/s. 2D video, 24 fps (file fps = question fps, no re-timing).

## Prior object
"Horse at the back" = the chestnut/brown horse: it trails (left, behind the tan horse in walking direction) and is
the slower one. Both horses walk along the foot of the brick wall (hooves at y ≈ 1043-1048, the same as the wall base at y ≈ 1045),
so they are at essentially the same depth as the windows. That means one metres-per-pixel scale applies (2D convention).

## Brown horse pixel speed (frames 0-48; frame 49 is an animation loop reset)
- Masked template matching of the chestnut-coloured body (track_brown.py), using templates from frames 12, 24 and 36
  and two body windows: slope 3.18-3.23 px/frame, mean of per-frame differences 3.08-3.27. I take **3.21 px/frame
  = 77.0 px/s**.
- Second route: the scene record's torso reference point gives a linear-fit slope of 3.24 and an end-to-end value of 3.15 px/frame.
- Scale = 0.874 / 77.0 = 0.01135 m/px.

## Window width (window.py, plus a zoomed visual check frames/winR.png)
Outer frame extent at the half-max of the blue-minus-red contrast, at rows 875-945:
right window (frame 0) 64.0-65.9 px, middle window (frame 48) 62-66 px, left window (upper rows) 64-65.7 px.
Visual check: right window outer frame x ≈ 744.4 to 809.6 → 65 px. Width = **65 px**. Height is about 107 px.

## Answer
65 px × 0.01135 m/px = **0.74 m**. Using the 3.15 px/frame speed instead gives 0.75 m, and 3.26 px/frame gives
0.73 m. Confidence: moderate-high (±4%). The main uncertainty is the horse's pixel speed, because of gait jitter.
