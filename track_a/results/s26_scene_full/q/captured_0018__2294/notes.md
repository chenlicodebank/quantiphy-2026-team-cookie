# q_2294 — height of the right person (cm)

The right person is the nearer one (black cap, dark shirt). depth_info gives near_person = 2.002 m. The question fps
and the file fps are both 24. The person stands still for the whole clip, so the frame does not matter.

## Measurements (headtop.py, crops.py; frames 0–48)
- Head top: first dark row in the head region is y = 103–104 with the cap on (frames 0–44) and 107 without the cap
  (frame 48, hair). I used 104.
- Feet: the rear shoe's sole is at y = 666. The front (nearer) shoe's top is at y = 695 and its sole is cut off by the
  image bottom (about 720–725). The body centre's floor contact lies between the two, at about 694.
- Ground-plane check: the far person's soles are at 575 at 3.130 m and the horizon is at 342, which gives a camera
  height of about 0.956 m. At 2.002 m the floor row is then 342 + 763·0.956/2.002 ≈ 706. I took the foot row as
  700 ± 8.
- Pixel height = 700 − 104 = 596 px.

## Method card
f = 0.5959·1280 = 763 px. H = 2.002 × 596 / 763 = 1.564 m (range 1.55–1.58 for a foot row of 694–706).

## Second route (horizon ratio)
H = h_cam·(v_foot − v_head)/(v_foot − v_horizon) = 0.956 × 596/358 = 1.59 m (1.58 with a foot row of 706).

## Answer
157 cm (between the two routes, which give 156–159). Confidence is moderate. The main uncertainties are the cut-off
front foot and whether depth_info is the Z-depth or the Euclidean distance. If the distance were Euclidean and
converted to Z for x ≈ 990, the height would come out about 9 % lower. That conversion was not applied, following the
card.
