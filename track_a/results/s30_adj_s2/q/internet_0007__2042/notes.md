# q2042 — length of the black car (internet_0007), prior lane width = 3.66 m

The video is a top-down drone shot with an almost static camera. The black car is the dark (blue-black) car in the left lane that drives toward the top of the image
(scene blue_car). The file runs at 29.943 fps and the question at 30 fps; that doesn't matter for a size.

## Where the candidates part ways
- C1 (7.0) treats the prior's "lane" as one half of the road (~38.5 px), which makes the car ~7 m long and ~2.7 m wide.
  That fails the car sanity check (3–7 m, and a sedan with L/W ≈ 2.7 should be ~4–5 m), and the convention says an
  unnamed "lane width" is the road surface curb to curb. So I reject C1.
- C2 (3.66) and C3 (3.42) both take the whole carriageway as 3.66 m (74–75 px). They differ only in the car's pixel length:
  C2 measures 74 px and C3 measures 70 px.

## My measurements (measure2.py)
- Road width, frame 200, with each edge at half contrast between the asphalt and the verge in grey level, over 30 row bands (excluding the SLOW marking):
  median 71.8 px, IQR 69.8–75.6. In the cleaner upper half (y 580–860) it is a steady 75.4–76.5 px. The outer edge
  including the dark worn band is ~80–83 px. I take ~75 px for the visible asphalt edge-to-edge.
- Car length, frames 0–80 every 5, by colour difference against frame 200 along the car's column, with each bumper at half contrast:
  median 75.6 px (range 73–78; one outlier of 59). The scene record's mask_len gives 73–75 px (median 74). Checked on a zoomed crop
  of frame 40, where the bumpers sit at y ≈ 1048–1122 (≈74 px). I take 74–75 px. C3's 70 px looks short.

## Answer
The car's pixel length ≈ the road width in pixels (74.5 / 75). Length = 3.66 × 74.5 / 75 ≈ **3.6 m**.
Sensitivity: road 72–76 px and car 74–76 px give 3.56–3.86 m.
Second route: the whole C2 measurement (road 74.2 px, car 74.2 px) agrees independently. The car's width of ~34 px gives ≈1.7 m, which is realistic.
I agree with C2, within 2 %.
Confidence: moderate-high on the convention, about ±4 % on the pixel measurements.
