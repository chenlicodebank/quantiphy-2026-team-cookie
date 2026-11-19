# q_3064 – width of the bridge (m)

Prior: white car length = 4.572 m. Static size question, so the frame rate does not matter.
Near-nadir drone view; the camera is static in frames 0-23. Scale is taken near the white car's rows (y ≈ 100-600)
to limit the perspective effect, since ground scale grows about 12 % from the top of the frame to the bottom.

- White car length (bumper to bumper, frame 14, measured in code with measure.py): 451 px with a brightness threshold;
  457 px in the scene record (frames 11-17). Used 455 px, so scale = 4.572/455 = 0.01005 m/px.
- Bridge outer edges (outer edge of the white side girders/walkways), from edge.py row profiles at y = 250 and 400,
  frame 14: left ≈ 458 px, right ≈ 1952 px, giving 1495 px → **15.0 m**.
- Road deck between the inner kerbs at the same rows: ≈ 1320 px → **13.3 m** (the scene record gives
  1317-1332 px at y = 100-400, which agrees).
- Second check: the inner width from my profiles (1314-1328 px) matches the scene record's road_width_vs_y.csv.
  In that record, frame 20 has the same deck width as frame 0. At frame 43 it is about 2.6 % smaller, which fits the
  2.4 % zoom-out. I did not re-measure frames 20 and 43 myself.

Ambiguity: "bridge width" could mean the full structure (15.0 m) or only the carriageway (13.3 m). I answered 14.8 m,
leaning toward the full width while hedging toward the carriageway reading.
Confidence: moderate. Scale is good to about ±2 %, and the main uncertainty is which of the two definitions was meant.
