# q_281 — height of the person (m)

2D render (camera static, man walks parallel to the facade). fps = question_fps = 24, no re-timing issue.
Scale from prior: speed 1.22 m/s.

## Pixel speed (measure.py: median background subtraction, own mask)
- Head-top x line fit: 5.574 px/frame; mask centroid fit: 5.591; head endpoints 5.516; scene pelvis_x_smooth endpoints
  (363.0 -> 749.8)/70 = 5.526. Adopted 5.56 px/frame = 133.4 px/s -> 0.00915 m/px.

## Pixel height
- Head top y = 656-662 (656 at f14-18, f48-52, f66-69).
- Mask bottom of 875-878 in many frames is the soft shadow/reflection on the deck, not the shoe: zoomed crops
  (frames/feet18b.png, feet61.png) show the soles ending at y≈867-868, the same as the mask bottom (868) in frames
  where no shadow is picked up.
- Height ≈ 868 - 656 + 1 ≈ 211-212 px (≈210 at f61: 659->868).

## Answer
212 px x 0.00915 = 1.94; 211 px -> 1.93. Answer 1.93 m.
Check: the record's raw heights (210-223 px) give 1.92-2.04 m; the upper values include the shadow. Using the record's
pelvis speed alone (5.526 px/f) gives 1.95 m. Confidence: moderate-high (±4%), mostly from the pixel speed (gait
variation) and the head-top/sole definition.
