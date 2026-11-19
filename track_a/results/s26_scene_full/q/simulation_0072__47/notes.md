# Q47: speed of the walking pedestrian at 1.0 s (m/s)

The view is top-down and 2D (the ground plane faces the camera), so one metres-per-pixel scale comes from the prior
(bicycle speed 5.33 m/s). The file fps and question_fps are both 24, so t = 1.0 s is frame 24.

## Method (measure.py)
- Re-tracked both movers myself. For each one I cropped a region of interest, took the median background over all
  72 frames, kept pixels where |diff| > 25, applied an opening, and used the mask centroid as the reference point.
- Bicycle (lane x ≈ 918): linear fit of y over frames 2–71 gives -8.927 px/frame. The mean per-frame step is
  8.916 px, and the top and bottom box edges give 8.87 and 8.89 px/frame. The speed is constant.
  Scale = 5.33 / (8.92 × 24) = 0.0249 m/px.
- Pedestrian (sidewalk at y ≈ 842, walking +x): the per-frame centroid steps are noisy because of the gait, so I
  used windowed linear fits around frame 24:
  - frames 18–30: 2.019 px/frame
  - frames 14–34: 2.086 px/frame
  - frames 12–36: 2.090 px/frame
  - whole clip (frames 2–71): 2.031 px/frame
  - box edges x0 and x1: 2.06 and 2.02 px/frame
  
  Vertical drift is about 0.04 px/frame, which is negligible. Best estimate: 2.05 ± 0.04 px/frame.
- Speed = 2.05 / 8.92 × 5.33 = 1.22 m/s. The windows give a range of 1.21 to 1.25 m/s, which is a plausible
  walking speed.

## Check
This agrees with scene/ (bicycle ≈ 8.9 px/frame, pedestrian ≈ 2.0 px/frame), and the bounding-box edge slopes give
the same ratio. Confidence: good (about ±3%).
