# Q1097: fire hydrant height (m)

The prior gives the person's height as 1.87 m. The depths are: person 13.882 m (t=0) and 13.768 m (t=1); hydrant 12.565 m. This is a 3D render with a static camera. The file runs at 29.9966 fps and the question at 30 fps; time does not matter for this size question.

## Measurements (measure.py, code on frame 87 plus a median background)
- Hydrant: column profiles give the top cap at y≈753.5 and the bottom of the base flange at y≈890.5, just above the dark contact line at 891. That makes the height **137 px**, which agrees with the scene record (753-890).
- Person: the background-subtraction mask over frames 76-88 puts the head top at 650-653. The sole is at ≈868.5, where the shoe rows (width ~35) give way to the narrower reflection. That makes the height **≈218 px** (walking 215-219), which agrees with the record.

## Geometry (geom.py)
- Pinhole with a level camera and the principal point at the centre. For an upright object, pixel height = f·H/z, with z = d·f/√(f²+r²).
- Focal length from the person: f = 1535.8 (t=0, pelvis x≈84) and 1536.3 (t=1, x≈135). The two values agree within 0.03%.
- Hydrant origin taken as its centre (100, 822): z = 11.90 m, so H = 137·11.90/1536 = **1.061 m**.
- If the origin is at the base: H = 1.052 m.
- Second route, a simple ratio without the off-axis correction: 1.87·(137/218)·(12.565/13.882) = 1.064 m. This is consistent.

## Confidence
Uncertainty is about ±3%, mostly from the person's rest height in pixels (215-220 px) and from the ±1 px hydrant edges. Answer: 1.06 m.
