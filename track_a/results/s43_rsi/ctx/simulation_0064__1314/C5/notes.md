Near foreground traffic light: pole base y=568 px, top of the 3-lens head y=160 px (408 px tall). Camera calibrated from depth_info + ground plane (v_bottom = y_h + (h_cam/H)*h_px): y_h=11.4 px, A=f*h_cam=11120 px*m, giving its ground distance D=11120/556.6=20.0 m. Focal length from standard objects (1.44 m sedan -> f=3026 px; 2.15 m van -> f=2874 px; pedestrian -> 2780 px). H = 408*20.0/f = 2.84-2.90 m; second route (taxi alone at f38) gives 2.90 m, and the proportion check H/H_van=1.32 gives 2.84 m.

Final message:
I measured the traffic light's height as **2.9 m**.

**Method summary:**
- The prominent foreground traffic light (left; the right one is identical) spans from pole base y=568 px to the top of the 3-lens head y=160 px → 408 px tall.
- Calibrated the camera from the given depth_info using the ground-plane relation `v_bottom = y_h + (h_cam/H)·h_px`, fitted on the clean front-facing white van at t=0.58 s and t=1.58 s: y_h = 11.4 px, A = f·h_cam = 11120 px·m.
- Focal length from standard real-world objects: 1.44 m sedan → f = 3026 px; 2.15 m van → f = 2874 px; pedestrian → 2780 px.
- Traffic light ground distance D = 11120/556.6 = 20.0 m → H = 408 × 20.0 / f = 2.84–2.90 m.
- Second route (taxi alone at f38) gives 2.90 m; proportion check against the van gives 2.84 m.
