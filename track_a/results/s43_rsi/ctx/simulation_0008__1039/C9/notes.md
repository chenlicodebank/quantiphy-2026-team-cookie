# Measurement notes

Question 1039: minimum distance from the outer end of the pier to the boat at t = 3 s.

Answer: 3.34 m. I use the supplied benchmark convention that the boat position is its object origin. The nearest point along the pier's outer edge is opposite the boat at the requested time.

## Time and observations

The file contains 66 frames at 22.802381 fps. All question times use 24 fps: t = 1 s is frame 24, and t = 3 s would be frame 72. Frame 72 is absent. I extrapolate seven frames from frame 65 using the late observed motion. Template matching over all frames gives approximately -10.01 pixels/frame over frames 48–65. This extrapolation puts the boat origin within the horizontal extent of the pier, so modest horizontal extrapolation error has little effect on the minimum distance.

## Measurements and geometry

Scripts: measure.py tracks a hull patch, writes tracking.csv and draws the measured points and deck polygon in frames/measurements.png. geometry.py computes both calibrations. Frames are decoded sequentially and discarded.

At frame 65, the raised boat stem spans approximately y = 620 to 744. Its 124-pixel height and exact 0.75 m prior give 0.00604839 m/pixel at the boat. The boat's image length is about 635 pixels, corresponding to 3.84 m, a plausible full-size rowboat.

The tracked patch moves 672 pixels from frame 0 to frame 65 and 416 pixels from frame 24 to frame 65. Assuming predominantly lateral translation at fixed optical depth, the two exact radial distances, 7.452 and 6.655 m, constrain the boat origin's horizontal coordinate and the focal length. With the height scale, the result is f = 982.4 pixels and boat optical depth = 5.942 m. Both radial distances are reproduced numerically. The origin can differ from the silhouette midpoint; this fit places it approximately 50 pixels left of that midpoint.

The pier's top has front corners (459,633), (637,633) and rear corners (489,591), (609,591). Front and rear widths are 178 and 120 pixels. For a rectangular deck, inverse-width depth ratios and the supplied 11.579 m distance to its central origin give an outer-edge optical depth of 9.286 m. A small radial-to-optical correction uses the pier's projected centre. The closest 3D distance to the boat origin is 3.344 m. The stairs are farther back and are consistent with the given ordering of camera distances; their unknown root location prevents an additional precise calibration.

## Independent check

Taking the boat's geometric silhouette midpoint as its origin, and deriving scale from the two radial distances instead, yields f = 1008.2 pixels, a predicted stem height of 0.720 m, boat length 3.69 m, and distance 3.431 m. The distance differs by 2.6%. The final answer uses the height-based route because the height prior is exact. This route comparison also bounds sensitivity to the unknown asset origin.

## Limitations and confidence

Confidence: moderate. The main uncertainties are the asset origins, exact deck endpoints, and the absent requested frame. The model assumes the pier origin is at its geometric longitudinal centre and the boat's depth stays nearly constant. The observed late motion supports a short extrapolation.

The answer follows the requested origin convention. A literal shortest clearance to the boat's physical hull would be smaller, roughly 2.7–2.9 m after allowing for the far half-width; the footage does not uniquely constrain that surface clearance. It is not the submitted interpretation.
