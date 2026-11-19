# q_2352 – diameter of the white jar (cm)

The "white jar" is the object scene/ calls `white_ball`: a small white cylindrical jar with a lid. In frames 0-8 its round lid
can be seen in left_person's hand. The file rate and question_fps are both 24, so t = 0.60 s is frame 14.
depth_info: jar at 1.9735 m at t = 0.60 s. f = 0.5959 x 1280 = 763 px.

## Method
- `profile.py`: for each flight frame, I rotate the crop so the motion direction (from the track) is vertical. Then I
  take the brightness profile across the motion, averaged over the central rows. I use its FWHM (half-way between the
  background and the jar's brightness), because that direction has no motion blur.
- Perpendicular FWHM: f13 29.3 px, **f14 27.3 px**, f15 21.6, f16 26.9, f17 28.8, f18 30.1, f19 26.7. The jar
  tumbles, and in f13-17 it is seen roughly side-on (elongated about 35-50 px along the motion).
- Diameter at f14 = 27.3 x 1.9735 / 763 = 7.06 cm. At f13 (depth about 1.88 m, extrapolated) it is 29.3 x 1.88 / 763 = 7.2 cm.
- Which dimension is the diameter: at f17 the motion blur is small (the f21-22 shapes show that the exposure is short), and
  the shape is about 29 x 35-40 px. The short side, across the motion, matches the size of the lid circle seen in the hand.

## Second route
In f3-f5 the lid circle in the hand has a major axis of about 31 px (core mask, from the record) to 34-36 px (with the soft
edge). At about the near person's depth (1.58 m) that gives 6.4-7.4 cm, which agrees.

`crops.py`, `crops2.py`, `measure.py`, `perp.py` and `profile.py` hold the measurements; the overlays are in frames/.

Answer: **7.1 cm**. Confidence: moderate (about ±10%), because of the edge definition under the SAM2 halo and the jar's tumbling.
