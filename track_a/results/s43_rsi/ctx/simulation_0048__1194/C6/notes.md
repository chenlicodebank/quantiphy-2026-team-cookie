# Measurement notes

Question 1194: bicycle height from the handlebar to the bottom of its wheels.

Answer: **1.06 m**.

## Inputs and frame selection

- Exact scale prior: walking person's height is 1.8 m.
- File fps and question fps both equal 33. Frame 33 is 1 s; frame 66 is 2 s.
- Inspected both specified times, plus frames 0 and 50. The bicycle's front wheel is partly outside the image at frame 66, so complete height measurements use frames 0, 33, and 50.
- All processing reads individual frames; no high-resolution video dump was made.

## Camera geometry and scale

A simple image-height ratio with the supplied distances is unreliable here. Architectural verticals and the bicycle's rigid-feature trajectories provide a separate camera calibration. Fitting 19 architectural edges gives a vertical vanishing point near (969.4, 7935.7). Tracked bicycle features give a travel-direction vanishing point near (1778.0, -118.8). Assuming the principal point is the image center (960, 383), orthogonality gives a focal length of 1944.8 pixels. Independent pairs of rigid handlebar/stem trajectories give 1902.6 and 1987.3 pixels, supporting this calibration.

The metric scale is then obtained from the exact 1.8 m human prior. The crown and the planted-foot ground level define a vertical segment. Its base is placed on the image line through the crown and the vertical vanishing point to reduce lateral gait error. Solving the two endpoint rays for a 1.8 m vertical segment determines the ground-plane distance from the camera.

The visible human at 1 s is considerably farther from the camera under this calibration than its supplied 11.9259 m origin distance. Consequently, that origin distance is not assigned to the visible body's center. Animated body/root offsets are a material issue here. No assumed standard human, wheel, or bicycle size was substituted for the exact prior.

For the bicycle, back-project the front tire's ground contact onto the calibrated ground plane. Solve each handlebar grip ray as that ground point plus a vertical height and a lateral displacement perpendicular to bicycle travel. This handles the different projected heights of the left and right grips. It approximates the handlebar's longitudinal position by the front axle's position; the remaining fore/aft offset is a small uncertainty.

## Key measurements

Coordinates are in original 1920 x 766 pixels.

| Frame | Human crown | Planted-foot level y | Front tire bottom | Left grip | Right grip | Height estimate |
|---|---|---:|---|---|---|---:|
| 0 | (1542, 236) | 417 | (1727, 417) | (1711, 307) | (1758, 315) | 1.0618 m |
| 33 | (1532, 252) | 449 | (1712, 558) | (1697, 424) | (1755, 430) | 1.0277 m |
| 50 | (1524, 262) | 465 | (1701, 674) | (1684, 514) | (1750, 522) | 1.0535 m |

The camera height above the person's sidewalk inferred from these frames is 5.091, 4.947, and 4.930 m. Variation reflects gait, landmark uncertainty, and the distinction between standing height and the animated silhouette. Applying the sidewalk ground plane to the slightly lower road also modestly underestimates bicycle height.

## Independent check

At frame 33, placing the front-wheel contact ray at the supplied bicycle-origin range of 16.4919 m gives grip-height estimates of 1.0751 and 1.0710 m. Their mean is 1.0730 m. This is an approximate upper check: a bicycle rig root behind the front wheel can be farther from the camera than that contact point. The human-scaled front-wheel range is 15.795 m, compatible with a root located farther back on the bicycle.

The independent frame results and depth check support approximately 1.05–1.07 m. The final estimate is 1.06 m. Confidence is moderate to good, with roughly 5–7% practical uncertainty from the handlebar-to-axle offset, sidewalk elevation, gait, and root-position ambiguity.

## Reproducibility

- `measure.py`: architectural edge detection and inspection crops.
- `geometry.py`: architectural vertical calibration and an exploratory curb-line calculation. The curb pair was ill-conditioned and was not used for the final focal length.
- `track.py`: sequential optical-flow tracking of bicycle features and travel vanishing-point estimation. Individual tracks can drift; independent rigid-feature pairs provide the calibration check.
- `estimate.py`: pinhole reconstruction, height calculations, depth check, annotated measurement frames, and answer writing.
- `measurements.json`: numeric reconstruction results.
- `frames/annotated0.png`, `frames/annotated33.png`, `frames/annotated50.png`: measurement points and the human vertical segment for visual confirmation.
