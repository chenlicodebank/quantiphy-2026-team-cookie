# q_2504 – width of the table (cm)

Width means the table top's shorter horizontal extent, i.e. its front-to-back depth. File fps and question_fps are both 24.

## Method (lab pinhole camera: f = 0.5959*1280 = 762.8 px, principal point (640,360))
1. `table_edges.py`: fitted lines to the table-top outline in code. The back edge comes from the top of the mask in
   frame 0, where the ball is away at the front right. The left and right side edges come from frame 45. The front
   top edge (top surface against the darker front face) comes from the strongest vertical gradient in frame 45.
   Each fit has 0.3-0.8 px rms residual, and the overlay (`frames/edges.png`) sits on the edges.
   Corners: BL (449.8,448.6), BR (918.2,467.6), FL (210.8,535.9), FR (1140.6,587.3).
2. `table3d.py`: vanishing points: side edges meet at (708.0,354.4) and front/back edges at (-6298,176). The two
   back-projected directions are 88.8 deg apart, close to the 90 deg a rectangle should give. Plane normal = their
   cross product.
3. Scale: the ball centre comes from back-projecting the depth_info distances: frame 30 (t=1.24, 1.144 m) and frame
   38 (t=1.6, 1.027 m), with the ball centres from scene/tracks/ball.csv. The table plane lies one ball radius
   (3.35 cm) below the plane through the ball centre, which puts the camera 0.159-0.162 m above the table top. The
   corner rays were then intersected with the table plane.
   - Scale from frame 30: width 58.0 cm on both sides, length 71.5 cm.
   - Scale from frame 38: width 59.0 cm, length 72.7 cm.
   - Mean: width ≈ 58.5 cm.
4. Consistency check: the rolling ball (frames 29-48, depth from its size scaled to the given distances) stays
   2.8-3.3 cm above the fitted plane, which matches a 3.35 cm radius.

## Second route
I also built the plane normal from the rolling ball's 3D path direction crossed with a table edge direction.
- Path × side direction: 56-61 cm.
- Path × front/back direction: 61-63 cm.
- Moving the side vanishing point ±2 px vertically gives 57.5-59.8 cm.

All routes fall between 56 and 63 cm. The vanishing-point route is the best constrained.

## Side notes
- Ball size gives depths about 7% larger than depth_info (for example 1.234 vs 1.144 m at frame 30). The given
  distances were used for the scale, as the instructions say.
- Length reading (the long side, left-right): about 72 cm.

Answer: 58.5 cm. Confidence: moderate-good (about ±4%).
