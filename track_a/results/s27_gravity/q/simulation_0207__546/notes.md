# Q546 — length of the table (desk), metres

Prior: typewriter falls with a = 9.8 m/s^2 before 0.45 s (frames 0-10). No depth_info. question_fps = file fps = 24.

## Scale from the fall (feat.py)
Template-tracked typewriter features, quadratic fit of y(frame), frames 0-9:
carriage plates (back) 11.83 / 11.91 px/frame^2, side knob (mid) 12.52, keyboard (front) 12.71;
bbox centre 12.6, bbox top 11.85, bbox bottom 13.39. Back/front differ by ~7 % (perspective depth
of the typewriter). Origin (body centre) taken as mid-depth: a = 12.35 +- 0.3 px/frame^2
-> s = 9.8 / (12.35 * 576) = 1.378 mm/px at the typewriter's depth (typewriter width 291 px -> 0.40 m, plausible).

## Desk geometry (edges.py)
Camera is level (horizon y = 544 from the vanishing point of the two desk side edges, VP x = 1066 = image centre).
Side edges (top surface silhouettes): dx/dy = -1.972 (left), +1.814 (right) -> desk length = 3.786 * h,
h = camera height above the desk top. Check: back edge y = 946, width there 1521 px, 1521/(946-544) = 3.784. Consistent.

## Linking scale to the desk
h = s * (y_desk_under_typewriter_centre - 544). Typewriter front-bottom contact line y ~ 1026 (482 px below horizon;
frames 11 and 24). Centre is ~D/2 ~ 0.16 m behind the front edge at Z ~ 2.6 m (Z from the 7 % back/front
acceleration ratio), so the centre's desk point is ~452 px below horizon (cross-check: rest footprint back corner
read at y ~ 958 gives a footprint centre at ~445 px).
h = 452 * 1.378 mm = 0.623 m; length = 3.786 * 0.623 = 2.36 m (route via back-corner reading: 2.32 m).
Implied camera: f ~ 1880 px (HFOV ~ 59 deg), desk back edge ~2.9 m away.

## Checks / confidence
Other objects at this scale: alarm clock ~0.14 m, typewriter 0.40 m wide, lamp shade ~0.38 m: somewhat large but
within ~40 %, so the prior scale is kept. Uncertainty ~ +-5 % (acceleration choice of origin depth, contact-line position).
Answer: 2.36 m.
