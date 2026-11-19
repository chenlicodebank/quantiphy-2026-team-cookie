Motorcycle (right lane, southbound) tracked with SAM 3 over frames 0-122: linear fit 9.33 px/frame = 276.9 px/s, confirmed by an independent brightness-centroid fit (278.2 px/s, 0.5% agreement); camera verified static (background cross-correlation dy=0). 2D scale from the prior: the visible carriageway is 73 px wide (asphalt edges x~525-597 at all y), so 3.66 m / 73 px = 0.0501 m/px (this keeps the cars at ~1.5x3.4 m and speeds at ~45-50 km/h; the alternative one-lane reading would make the cars 2.9 m wide, >40% implausible). Average speed = 277.5 px/s x 0.0501 m/px = 13.9 m/s.

Final message:
**Answer: 13.9 m/s** (question 2035)

Method summary:
- **Object**: the small two-wheeler in the right lane travelling south (scene/ labelled it "cyclist"; SAM 3 "motorcycle" segments it cleanly — rider with helmet over a bike).
- **Pixel speed**: SAM 3 track over frames 0–122 gives 9.33 px/frame = 276.9 px/s (constant velocity); an independent brightness-centroid fit gives 278.2 px/s (0.5 % agreement). Camera confirmed static (background cross-correlation dy = 0).
- **Scale**: prior lane width 3.66 m. RGB cross-sections show the asphalt is only ~73 px wide (x≈525–597, centre line at x=560). Using 3.66 m / 73 px = 0.0501 m/px keeps the cars at ~1.5 × 3.4 m and speeds at ~45–50 km/h; the "one lane = half the road" reading would make the cars 2.9 m wide (>40 % implausible). UK 4 m/2 m centre-line dashes (90/44 px) independently give 0.044–0.046 m/px, bracketing the adopted value.
- **Result**: 277.5 px/s × 0.0501 m/px ≈ **13.9 m/s** (~50 km/h).
