# q_285: horizontal distance between the two mallet handles

- 2D top-down view of an air-hockey table, 24 fps. The file fps and question_fps match, and no time is involved.
- "Horizontal distance" = the image-x separation of the two mallets. The top mallet moves only vertically (its x stays at 531.5–531.6 px in every frame), so this distance is constant through the clip. The full in-plane distance changes over time, which is why I read the question as asking for the x separation.
- Mallet x (measure.py, frames 10/48/71):
  - disk centres from the colour mask (scene track): 531.6 and 713.3 → 181.7 px
  - Hough knob/handle circles: 531.5 and 713.5–715.5 → 182–184 px
  - Hough outer disk: 531.5 and 711.5 → 180 px
  - Adopted value: 182 px.
- Scale: puck diameter 0.074 m. The puck's bbox is 64 px (the scene record gives 63–64; the equal-area diameter including the antialiased edge is 64.5–65). Adopted 64 px → 1.156e-3 m/px.
- Answer: 182 × 0.074 / 64 = 0.2104 m, reported as 0.211.
- Check: the range of plausible pixel values (180–184 px for the distance, 63.5–65 px for the puck) gives 0.205–0.214 m, within ±3% of the answer.
- Confidence: good. The main remaining doubts are the interpretation of "horizontal" and small perspective effects, since the handles stand higher above the table than the puck.
