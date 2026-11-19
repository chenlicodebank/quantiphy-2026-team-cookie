# q_290: length of the bike (prior: bike speed = 24 m/s)

2D top-down render. The camera is fixed. fps = question_fps = 24, so the time base is not in question.
The "bike" is the cyclist, the only bicycle in the clip; it rides in −x at constant speed.

Method (one m/px scale from the prior, because length and speed are measured in the same plane):
- `tips.py`: median background over all frames, then |frame − bg| along the bike's frame line (row y≈593–596).
  The front and rear tips are found at the half-maximum crossings, with sub-pixel precision. The rider and handlebar
  can break the line, so gaps of up to 12 px are bridged. Output goes to `tips_out.txt`.
- `fit.py`: frames 16–46, which have clean background and both tips found (21 frames).
  - Bike length: **85.0 px** (median 85.1, std 1.2).
  - Pixel speed from linear fits of the tips: front −31.34, rear −31.29, so **31.32 px/frame = 751.6 px/s**.
- Scale: 24 / 751.6 = 0.03193 m/px, so length = 85.0 × 0.03193 = **2.71 m**.

Check (second route): the scene record's rider-tracked step of 31.64 px/frame with its 85 px tip-to-tip length
gives 2.69 m. The rider sits higher than the bike line, so perspective makes its step about 0.5% larger.
The two routes agree within 1%.

Confidence: good (±3%). The main uncertainty is where the blurred thin tips end (±1–2 px).
Rendered scale is not real scale, so the large bike length is expected given the 24 m/s prior.
