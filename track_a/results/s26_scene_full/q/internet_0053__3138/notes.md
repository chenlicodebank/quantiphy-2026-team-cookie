# q3138: scooter height (m)

- Prior: the rider's average speed is 4.46 m/s. fps = question_fps = 30, so no re-timing.
- Camera is static (drift of 2 px or less). Mean per-frame pixel speed over frames 0-80: 539.9 px/s for the scooter
  midpoint (scene track) and 538.2 px/s for the rider's upper body (an independent track). Scale = 4.46/539.9 = 0.00826 m/px.
- Scooter height, from the handlebar top (hands rest on it) to where the wheel touches the ground, read on 4x zooms with
  a grid (frames/h0, h40, h70.png): 207.5 px at frame 0, 198 px at frame 40 and 197.5 px at frame 70. The path is slightly
  oblique, so sizes shrink about 12% across the clip. I used the mid-clip value of 198 px, which matches the scale of the
  clip-average speed.
- Height = 198 x 0.00826 = **1.64 m** (frame 0 gives 1.71 m, frame 70 gives 1.63 m).
- Check: the two independent speed tracks agree within 0.3%. Caveat: real-world knowledge suggests the prior's scale is
  large (the rider would come out at about 2.7 m), but the benchmark convention scales everything with the prior, so I follow it.
- Confidence: moderate. The hands hide the top of the handlebar, so the reading is uncertain by ±3 px, and the
  answer depends on which frame is used (up to 5%).
