# q3137: wheel-to-wheel width of the scooter (m)

- The rate is 30 fps, and the file and question_fps agree. The camera is static: drift is 2 px or less, and I subtracted it anyway.
- Scale from the prior (average speed 4.46 m/s). I took the mean per-frame pixel speed over the whole clip (frames 0-80). It is 543.5 px/s for the rear-wheel centre and 538.3 px/s for the upper-body track, so I used their mean, 540.9 px/s. Scale = 0.008245 m/px.
- Reading the name: the view is a side view of a single-track scooter, so its lateral width cannot be seen. I took "wheel-to-wheel" as the extent from wheel to wheel along the scooter, from the back of the rear wheel to the front of the front wheel. This works like bumper to bumper on a car.
  - Outer extent: the mean over frames 0-73 (fully visible) is 193.7 px, which gives **1.60 m**. My hand check at frame 40 (frames/f40.png) shows about 1160 to 1350, or roughly 190 px. The record has 192.5 px, which gives 1.59 m.
  - Other reading (axle centre to axle centre, the wheelbase): 152.9 px, which gives 1.26 m.
- Perspective: the scooter shrinks about 12% across the clip (207 to 180 px). Using the clip mean matches the whole-clip speed scale.
- Sanity check: the result is large for a real e-scooter, and the rider would also scale to about 2.5 m. So the prior's speed seems inflated, but the convention is to follow the prior.
- Confidence: moderate. The scale is solid (two tracks agree within 1%). The main uncertainty is whether "wheel-to-wheel" means the outer extent or the centres.
