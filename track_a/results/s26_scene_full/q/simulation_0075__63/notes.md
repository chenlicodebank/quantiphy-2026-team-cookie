# Q63: width of the white car (m); prior: its length = 6 m

The "white car" is the white van in the near-top-down 2D view (vertical road, x≈831). Time base is 24 fps (the same in the file and the question; time does not matter for a size).

Method (measure.py): I made a brightness mask (|grey − asphalt| > 25) around the van's track centre at frames 10–71.
- Width = the column span where more than 50% of the central rows are masked. It is 86 px (cols 789–874) in every frame
  where the van is clear. At f71 the cyclist merges into the mask, so I excluded that frame.
- Length = the row span along the van's centre strip. It is 232–235 px in mid frames and 240–244 px in early and late frames,
  where the shadow or bumper halo is included.
- Record cross-check: vehicle_sizes.json thr25 gives 236×93 (f0), 233×88 (f36) and 236×87 (f71). A zoomed grid crop at f36 reads
  about 788–876 × 620–852 px.

Scale: 6 m / ~234 px = 0.0256 m/px. Width: 86–88 px gives 2.20–2.26 m. Answer: **2.22 m**.
Second route: the record's thr25 sizes at f36 and f71 give 88/233×6 = 2.27 and 87/236×6 = 2.21. They agree within about 2%.
No mirrors stick out visibly in the render. Confidence: good (about ±4%).
