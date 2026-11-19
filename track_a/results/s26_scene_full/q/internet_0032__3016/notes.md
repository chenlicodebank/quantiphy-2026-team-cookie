# Q3016: average speed of the boat from 0 s to 2 s (m/s)

The prior is boat length = 3.5 m. This is an internet video with a static camera (background shift < 0.2 px), and the boat is seen side-on moving right to left.

## Time base
The file runs at 29.85 fps and the question at 30 fps, which is effectively the same rate. t = 2 s is frame 60, so the interval covers frames 0 to 60 = 2.0 s.

## Measurements
- **Record (scene/tracks/boat.csv):** I checked the hull tips on zoomed frames 0 and 60 and they match. At f0 the bow is at 761 and the stern at 972. At f60 they are at 673 and 896.
  - Hull-centre x goes from 866.5 to 784.5, a net 82 px.
  - The motion is a straight line at a steady rate, so the path length equals the net displacement.
- **Independent re-segmentation (measure.py):** I thresholded the hull band (rows 520-537) myself. This gives centre x 869 to 787.5, a net 81.5 px, and the path length after Savitzky-Golay smoothing is 82.0 px. This band cuts off the thin bow tip, so its lengths come out about 5 px short (206 to 217).
- **Boat length in pixels:** the record gives 212 (f0) to 224 (f60), a mean of about 218 px over the interval. The boat grows slightly because it is approaching the camera.

## Result
- Scale = 3.5 / 218 = 0.01606 m/px.
- Speed = 82 px × 0.01606 / 2.0 s = **0.658 m/s**.

## Sensitivity
- Taking the scale from frame 0 only (212 px) gives 0.677 m/s.
- Taking it from frame 60 only (224 px) gives 0.641 m/s.
- Using the file fps (60 frames = 2.01 s) gives 0.655 m/s.

Confidence: good, about ±4%. The main uncertainty is which frame the annotators used for the prior's pixel length.
