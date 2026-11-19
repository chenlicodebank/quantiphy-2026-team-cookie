# Q1747: average speed of the boat (m/s)

The file runs at 24 fps and question_fps is also 24, so t = frame/24. The prior is a person height of 1.75 m. No depth_info. The clip is labelled 2D, so I used one m/px scale taken from the person.

## Scale (person)
- `person_crops.py`: the person mask (min RGB < 215) gives a bbox height for every frame. Frames 0–1 are the static rest pose at **42 px** (y 367–408). While walking the height swings between 39 and 51 px. Because the view is oblique from above, a stride lengthens the figure on screen, so walking heights are not the standing height.
- SAM 3 "person" at frame 0: box 365.8–408.4, so **42.6 px** (its vert_px count is 44). My 42 px is 1.4% off from that, so they agree. I used 42.3 px, which gives a scale of 1.75/42.3 = 0.04137 m/px.

## Boat motion
- `boat_track.py`: template-matched the frame-0 stern part, which stays in frame the whole time (the bow touches the left edge from frame 63), with sub-pixel refinement. Net movement from frame 1 to 71 is (−396.3, −111.1) px, i.e. **5.88 px/frame**. A linear fit gives 5.89. Single-frame steps alternate between about 5.2 and 6.4 px (render/encode jitter). The step from frame 0 to 1 is about 0 because motion starts at frame 1.
- Second route: SAM 3 track of "boat" (`tracks/boat_0.csv`; the overlay was checked and covers the whole boat). Its net speed over frames 1→62 is 5.864 px/frame against my 5.928, about 1% apart. The SAM box at frame 40 (128–461, 780–1010) matches my mask bbox (128–462, 779–1010). The slopes of the mask's right and bottom edges give 5.64 and −1.60 px/frame, which is also consistent.
- Mean of the per-frame speeds over frames 1..71, counting the zero first step: 5.88 × 70/71 = 5.797 px/frame.

## Answer
5.797 px/frame × 24 × 0.04137 m/px = **5.76 m/s**. Without the zero first step it would be 5.84.

Sanity check: at this scale the boat is about 360 px × 0.041 ≈ 15 m long and the person walks about 1.5 m/s. Both are plausible.

## Confidence
Moderate. The main uncertainty is the person's pixel height. The camera looks down obliquely, so the person is foreshortened and the true ground scale could differ. If I had used the walking median height (46.5 px) instead, the answer would be 5.24 m/s.
