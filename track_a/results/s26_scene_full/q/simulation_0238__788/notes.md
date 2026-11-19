# q788 – width of the house (m)

Prior: speed of the horse at the back = 0.874 m/s. 2D clip (static camera, 24 fps, and question_fps is 24 too), so one m/px scale.

## Which horse
"At the back" = the trailing (left) chestnut horse (`horse_brown`). Check: with this scale the horses come out at
2.1 m (brown) and 2.6 m (tan) nose to tail, which is plausible. If the prior were the tan horse, the horses would be
~1.3 m long and the house ~4.1 m wide, which is implausible.

## Pixel speed (match.py)
I template-matched the brown horse's torso (chestnut-coat mask that leaves out the brick, limited to the torso rows)
from frame 0 against every frame, searching over x shifts. The shift grows linearly: 76 px at frame 24 and 154 px at
frame 48, so 3.21 px/frame = 77.0 px/s (first half 3.17, second half 3.25). Frame 49 matches frame 0 at shift -1,
which is the animation loop reset, so I left it out.
Cross-check with the scene record: ref_x gives 151.4/48 = 3.15 px/frame and the rump edge gives 149/48 = 3.10
(both noisier). I used 3.21.
Scale = 0.874 / 77.0 = 0.01135 m/px.

## House width (house.py, eave.py, frame 49)
Horizontal extent of the facade (the house's world bounding box seen face-on):
- widest, at the gable eave / barge-board tips (y ~620): x 176-904, which is **729 px**, giving 8.27 m (answer)
- jettied upper storey: 200-881 = 682 px, giving 7.74 m
- brick ground floor: 251-830 = 580 px, giving 6.58 m

The answer is the full extent (729 px × 0.01135 = 8.27 m).
The front-to-back depth of the house can't be seen in this frontal view.

Confidence: moderate. The pixel speed is good to about 3%. The main uncertainties are whether the reference uses the
full extent including the eaves (8.27 m) or the wall (7.7 m), and a small depth difference between the horses' path
and the facade.
