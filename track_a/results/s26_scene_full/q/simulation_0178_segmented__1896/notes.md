# q1896: displacement of the small elephant (m)

- 2D side-view clip, 24 fps (file and question fps match), 60 frames. Both elephants walk steadily to the right. Checked on a contact sheet (frames 0/20/39/59): the calf is on the left and the adult on the right. scene/ tracks cover the right animals.
- m.py fits the scene/ tracks (mask centroid, bbox edges, body-span edges).
  - Adult x speed: centroid fit 7.008 px/frame; rump and head edges 6.95–6.96; net centroid 416.3/59 = 7.06. I used **7.0 px/frame = 168 px/s**.
  - Scale = 2.313 / 168 = 0.01377 m/px.
- Calf displacement from frame 0 to frame 59: centroid net 361.2 px, centroid fit 360.3, head edge 363/361. Vertical change is about 3 px, so negligible. I used **360 px**.
- Displacement = 360 × 0.01377 = **4.96 m**.
- Check by ratio: 2.313 × (59/24) × (calf/adult px motion 361/416) = 4.93 m. That agrees to within 1%.
- Confidence: high. Uncertainty is about ±2%, from the choice of reference point.
