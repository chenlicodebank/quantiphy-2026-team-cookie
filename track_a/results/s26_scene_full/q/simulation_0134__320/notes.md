# Q320: length of the toast (m). Prior: toaster height = 0.166 m. 2D scene, 24 fps (file rate = question rate)

Scale (measure.py, frame 0): the toaster's vertical extent runs from the top lip at y = 1120 down to the lowest
point of the cream base at y ≈ 1398 (the black band at y 1389-1395 is a recessed shadow under the base; the base
corner reaches 1398). That is 278 px (±3), so 0.166 / 278 = 5.97e-4 m/px. (The record's 276 px agrees.)

Toast (toast.py, frame 43, when the toast is fully out of the slot): it spans x 406-601, so 196 px wide; the mask
reaches 616 in the lower rows, but that extra part is the brown shadow, not crust. It spans y 839-1070, so 232 px
tall. Both match the scene record.

Interpretation: the prior calls the vertical extent of the toaster its "height" (Z), so I took the toast's "length"
to be its horizontal extent (the X extent of its world bounding box): 196 px × 5.97e-4 = 0.117 m.
Using 276 px for the toaster height instead gives 0.118 m.
Other reading: if "length" means the longest dimension (the vertical 232 px), the answer would be 0.139 m.

Confidence: the measurement is good to about ±2%. The main risk is how "length" is defined.
