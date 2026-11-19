# q2963: speedboat length (prior: sailboat length = 12 m)

Video: 960x540. The file runs at 24 fps and question_fps is 30, but the answer is a size, so the time base does not matter.
The "speedboat" is the small dark object near the bottom edge (scene/'s `bottom_object`). It enters at frame 179 and is fully in view from frame 184 to frame 239.

## Method (measure.py)
- Mask = min(RGB) < 200, with the watermark excluded. Connected components: the largest is the sailboat, and the component below y=495 is the speedboat.
- Horizontal pixel extent on each frame:
  - Sailboat: bbox length has median 100 px (range 98-105), and the hull (bottom 13 rows) has median 98 px.
  - Speedboat (frames 184-239): 39-43 px. Frames 184-209 give about 40 px. Frames 210-239, which are sharper and fully clear, give about 41.5 px.
- Scale = 12 m / 100 px = 0.12 m/px. Speedboat length = 41.5 x 0.12 = 4.98 m (40 px gives 4.8 m; using the 98 px hull gives 5.08 m).

## SAM 3 check
- Frame 230, phrase "small dark boat": the speedboat is 40 px horizontally (my mask: 42 px) and the sailboat is 100 px (my mask: 101 px). That is within about 5% for the speedboat and 1% for the sailboat. The 1-2 px difference is the speedboat's blurry edge pixels. A box-prompted "boat" mask on the same frame gives 43 px. The SAM ratio 40/100 x 12 = 4.8 m.
- Frame 210, box prompt: the SAM mask was bloated (68 px) and took in white background around the blob. The overlay confirms this, so I rejected it.

## Answer
About 5.0 m, from a speedboat/sailboat pixel ratio of 0.40-0.42. Results range from 4.8 to 5.1 m depending on the frame and mask. Confidence: moderate. The speedboat is small and blurry, so ±1-2 px (±4%) of jitter remains. It sits lower in the frame (possibly nearer the camera), but I applied the annotators' single-scale convention without perspective correction.
