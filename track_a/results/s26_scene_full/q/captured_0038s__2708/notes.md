# q2708 white cup rim diameter
Method (lab card): f = 0.5959*1280 = 762.75 px; depth of white cup = 0.874 m (t=1.4 s).
Cup is a tapered tumbler, widest at the rim (top, rows ~380-396). Rim horizontal pixel width measured in code
(subpix.py: half-max crossings of min(B,G,R) profile vs green background) on frames 5, 20, 45: 71.0-71.5 px per row,
peak ~71.4, mean 71.0-71.1 -> used 71.2 px (measure.py threshold mask gives 71 px, cols 724-794).
Diameter = 0.874*71.2/762.75 = 8.16 cm.
Check: credit card (0.6867 m) far edge spans ~94 px (frames/card.png), predicted 763*0.0856/0.6867 = 95.1 px -> focal/scale consistent within ~1%%.
Confidence: high (+-3%%). File fps = question fps = 24.
