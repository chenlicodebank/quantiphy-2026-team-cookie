# Q452 – height of the truck (m)

2D simulation, 30 fps (file and question agree). Prior: truck acceleration = 10.757 m/s^2.

## Scale from acceleration
- fit.py: quadratic fits to scene/tracks/truck.csv ref_x (rigid horizontal translation):
  frames 14-50 a = 2.036, 20-54 2.045, 36-50 (high reliability) 2.042, 14-35 2.033 px/frame^2.
- check.py (independent): frame-to-frame SSD matching of the truck band (rows 380-880) -> per-frame shifts;
  the clean early part increments 2.04-2.05 px/frame per frame; linear fits over noisier ranges 1.99-2.02
  (later frames, template partly off-screen at the right).
- Adopted a = 2.04 px/frame^2 = 1836 px/s^2 -> scale = 10.757 / 1836 = 0.005859 m/px.

## Height
- Frame 42: foreground mask top row (railing top) = 352; tyre bottom 939 (record; wheel centre 862 + tyre
  radius ~75 = 937; bottom sits in the floor shadow, ±3 px). Height = 587 px (AABB incl. cab-top railing).
- Height = 587 x 0.005859 = 3.44 m (box-top reading would be 536 px -> 3.14 m; AABB reading used).

## Confidence
Acceleration known to ~±1 %, height px ±1 %; answer 3.44 m, likely within ~3 %. Sanity: ~3.4 m for a catering
high-loader with railings is realistic.
