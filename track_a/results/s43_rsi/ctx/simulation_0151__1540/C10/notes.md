# Measurement notes

- Question 1540: scalar acceleration of the blue car at 1 second, in m/s^2.
- The video and question both use 24 fps. The target is frame 24. The reference acceleration is the difference of the speeds for 23-to-24 and 22-to-23, multiplied by 24; its central trajectory time is frame 23, or 0.958333 s.
- All measurements use only this video, the exact tire diameters (blue 0.369 m, yellow 0.764 m), and the yellow front tire's 11.38 m camera distance at frame 12.

## Tracking and time dependence

The camera is fixed. The vehicles move horizontally, with constant wheel heights and essentially constant tire sizes. The blue vehicle has changing acceleration, so a constant-acceleration fit over the whole clip would be inappropriate.

The upper rear roof tip remains visible despite the yellow car's occlusion of the blue body. `tip_track.py` measures its horizontal translation by normalized template matching and a subpixel peak fit, decoding frames sequentially. A fourth-degree fit to frames 16-41 has a 0.303 px RMS residual. Applying the exact discrete second difference gives 289.473 px/s^2. A cubic fit to frames 16-34 gives 294.879 px/s^2, and a cubic fit to 18-30 gives 292.652 px/s^2. These agree within about 2% with the adopted fit.

The blue car moves left and its speed is increasing at the queried time, so its scalar acceleration is positive.

## Scale and perspective

`check_scale.py` samples radial image gradients on visible tire silhouettes and robustly fits circles to the lower and side arcs. Blue tire diameters are 73.259 px (rear, frame 34), 72.762 px (front, frame 34), and 72.997 px (rear, frame 41). Their mean is 73.006 px. Annotated circle fits and sampled boundary points are in `frames/*_fit.png`.

The rear wheel centre moves 218.471 px between frames 34 and 41; the tracked roof tip moves 214.029 px. Thus the roof feature is slightly farther from the camera. The measured translation ratio, 1.02075, corrects its scale without assuming that the tire and roof have identical depth. The final roof scale is 0.00515927 metres per pixel.

As a 3D consistency check, the yellow tire's fitted diameter is 191.390 px and its centre at frame 12 is (1649.47, 789.54). With principal point (960,540), the given Euclidean camera distance and tire diameter imply a focal length of approximately 2754.9 px and yellow optical depth 10.997 m. Back-projecting the tire centre reproduces 11.38 m. The blue tire scale then implies an optical depth of 13.924 m; the roof tip's depth is about 14.213 m. This is consistent with the blue vehicle being behind the yellow vehicle. There is only one supplied absolute camera distance, so a second independent absolute focal calibration is unavailable; the answer instead uses the blue tire's exact metric scale directly and the independently measured roof-to-wheel translation ratio. Focal length cancels from that result.

The same scale gives the yellow car a length of about 4.6 m and the small blue cart a height of about 1.55 m, consistent with their visible models.

## Independent checks and limitations

`edge_check.py` independently locates the roof-tip silhouette using blue-channel edge gradients rather than template correlation. The clear, well-lit frames 23-37 give 298.232 px/s^2 with 0.399 px RMS residual, equivalent to about 1.539 m/s^2. Earlier edge thresholds are affected by the vehicle passing from shadow into light, explaining their less stable estimates. The adopted template fit and multiple frame-window checks are more stable.

Initial front-roof color segmentation, unconstrained optical flow, and front/corner template checks were rejected because illumination changes and yellow-car occlusion moved the detected feature; their larger fit residuals are recorded by the scripts. They are not used in the answer. The successful tip and wheel annotations are retained for inspection.

Final answer: 1.4935 m/s^2. Confidence: moderately high, with an estimated uncertainty of about 5-8%, principally from subpixel trajectory curvature and the tire silhouette.
