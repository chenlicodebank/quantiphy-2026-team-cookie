# q3123: height of the left basketball backboard

**Prior.** The scooter rider's average speed is 2.9 m/s. The video is 30 fps and question_fps is also 30, so no re-timing.

## Scale
I used the rider track in `scene/tracks/rider.csv`, in stabilised coordinates. The camera drift is under 1 %.
- **Mean of per-frame speeds:**
  - bbox centre: 476.3 px/s
  - front wheel: 475.8 px/s
  - rear end: 476.8 px/s
- The motion is monotonic, so the mean speed equals the net speed. The three reference points agree to 0.1 %.
- Scale = 2.9 / 476.3 = **0.006089 m/px**.

## Backboard pixel height (`measure.py`, `bottom.py`, frame 0)
- **Top edge:** the sky-to-dark-frame edge is at y 524-525 in columns 450, 520, 600 and 640.
- **Bottom edge:** the bottom frame band (grey-dark, values about 70-80) covers rows 699-703, and the trees begin at row 704. That puts the outer bottom edge at about 703.5.
- **Outer height:** about **178 px**. The scene record read 175 px by eye.
- **Width (horizontal):** x 415.5-670, about 255 px.

## Answer
178 px × 0.006089 = **1.08 m**. Reading 175 px instead gives 1.066 m.

**Sanity check:** regulation backboards are 1.07 m tall (42 in), which is consistent.

**Confidence:** good, ±3 %.
