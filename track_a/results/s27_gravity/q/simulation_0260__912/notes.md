# Q912: width of the iPhone to the right of the plant

The clip is a static-camera render. A mug falls in a plane parallel to the image and lands on the table next to the phone, so a single metres-per-pixel scale applies. The file is 30 fps and question_fps is also 30.

## Scale from the prior (mug acceleration 9.8 m/s² before 0.5 s)
`measure.py` re-segments the mug and fits a parabola over the free-fall frames 3/5-15, before the impact at frame 16:
- scene ref_y, frames 5-15: 6155 px/s² (rms 0.5 px)
- my own mask bottom edge, frames 3-15: 6198 px/s²; frames 5-15: 6208 px/s² (rms 0.5 px)
- top rim, frames 5-15: 6078 px/s² (rms 1.2 px; less reliable because the bottom-ellipse view changes)
- Adopted value: 6180 px/s², which gives a scale of 9.8/6180 = 1.586 mm/px.

## Phone
The black phone lies flat on the table at x ≈ 1141.5-1192 px, between the plant and the mug. I measured its horizontal extent row by row, using half-maximum crossings on frame 0 and rows 866-870. It is 49.1-50.0 px wide, and up to about 51 px if you include the small raised corner at the right end. I adopted 50.5 px.

The camera sits at table height, so only the phone's horizontal extent across the image is visible. That extent is 50.5 × 1.586 = 80 mm. This is an iPhone width (71-78 mm), not a length (about 147-160 mm), so the phone lies with its long axis pointing toward the camera. The visible horizontal extent is therefore its width. Depth difference from the mug's fall plane is a few cm out of several metres, which is negligible.

## Check
The same scale gives realistic sizes for other objects:
- mug: 89 mm tall, 76 mm body
- coffee cup: 101 mm
- camera bag: 354 mm

Changing the acceleration fit within 6150-6210 px/s² moves the answer by only ±0.5 %.

**Answer: 0.080 m.** Confidence is moderate to high. The main risk is the phone's orientation, i.e. whether the reference counts this horizontal extent as its "width".
