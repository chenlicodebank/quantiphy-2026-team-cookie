# Q89 – length of the black-and-white car (prior: yellow car length = 5.67 m)

This is a 2D top-down scene. Two pickups of the same model drive side by side in −x. The camera is slightly
perspective: a truck's pixel length shrinks about 3% from right to left. So I compared the two trucks at the
same image x position.

Method (`measure.py`, output in `lengths.csv`): the mask is min channel < 100, max channel > 172, or saturation > 50.
For each truck I took the front and rear x in the core rows (yellow rows 375–430, white rows 515–580), using the
extreme columns of the mask.

- Route 1, same position: in frame 0 both trucks have their fronts at x = 1432. Yellow is 314 px long and white
  312 px, a ratio of 0.9936.
- Route 2, position-matched: each white frame is paired with the yellow frame whose centre is within 6 px.
  Over 52 pairs the median ratio is 0.9934. Near the image centre: white 302 px (frame 40), yellow 304 px (frame 55).
- These agree with the scene record (304/302 px near the centre, 314/312 px at frame 0).

Length = 5.67 × 0.9935 ≈ **5.63 m**. Confidence: high. The ±1 px edge jitter is about 0.3%.
