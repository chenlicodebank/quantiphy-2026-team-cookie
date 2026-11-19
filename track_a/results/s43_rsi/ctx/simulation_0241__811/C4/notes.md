2D scene, one scale from the prior: the horse at the back is the trailing brown quadruped, whose pixel speed I re-measured at 63.5 px/s (centroid fit 63.0, trailing-edge fit 63.1, template 63.7-64.4), giving 0.874/63.5 = 0.01376 m/px. SAM 3 mask of the house (frames 20 and 40) gives a full horizontal extent of 805-806 px, so width = 805 x 0.01376 = 11.08 m. Check: the white animal then measures 2.27 m (cow-sized) and the brown 1.86 m, while the alternative scale (white = horse) would make both implausibly small.

Final message:
**Answer: 11.1 m** (question 811).

Method summary:
- **Scale**: the prior's "horse at the back" is the trailing brown quadruped (behind and farther from camera). Its pixel speed was re-measured several ways (colour-mask centroid fit 63.0 px/s, background-subtraction trailing-edge fit 63.1 px/s with 1.4 px rms, subpixel template matching 63.7–64.4 px/s) → adopted 63.5 px/s, so **0.01376 m/px**.
- **Plausibility check**: with this scale the white animal is 2.27 m long (cow-sized) and the brown one 1.86 m; the alternative (white = horse) would make both far too small, confirming the choice.
- **House width**: SAM 3 masks on frames 20 and 40 give a full horizontal extent of 805–806 px (widest at the flared middle tier, edges verified against the shadow on zoomed crops) → **805 × 0.01376 ≈ 11.08 m**, with a second-route check at frame 40 (806 px → 11.09 m) and a consistent 9.9 m height.
