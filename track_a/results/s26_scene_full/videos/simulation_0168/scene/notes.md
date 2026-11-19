# simulation_0168 – measurement record (pixels / seconds only)

Video: 1920x1080, 24 fps, 80 frames (t = frame/24, frame 0 = t 0, frame 79 = 3.292 s). Blender render, 3D street
scene at night. **Static camera** (facade phase correlation vs frame 0: shift < 0.02 px in all frames).

## Scene content
Two moving objects, both moving the whole clip, both visible in all 80 frames:
* **cyclist** – cartoon delivery rider (orange/light-blue round helmet, grey faceless head, green jacket + backpack,
  orange trousers, yellow parcel on the front rack) on a lilac bicycle with white-spoked wheels. Always the left-most
  mover and closer to the camera than the van. Rides from the right edge (bbox centre x≈1836, frame 0) toward the
  camera and left (x≈783, frame 79). Never occluded.
* **police_van** – white VW-Transporter-style police van, 'Police' lettering, blue chevrons on the side, plate
  "1-MWS-002", roof light bar with flashing blue beacons. Drives toward the camera and left, close behind/right of the
  cyclist. Frames 0-38: its right part is beyond the right border (only front-left corner visible at frame 0);
  fully in frame from 39. Frames 42-79: its front-left corner is hidden behind the cyclist.
* No other people, animals, vehicles or loose props move. Static objects (lamp/signal pole, fence, bunting, building,
  signs, road lines, kerbs) are listed with frame-0 pixel boxes in scene.json.

No discrete events (no start/stop, contact, bounce). Notable: the cyclist's image motion is slow in frames 0-8
(~4 px/frame) and faster later; the cyclist starts overlapping the van in the image at frame 42 (image overlap only –
they are at different depths; no contact seen). Both still moving at the last frame.

## Files
* `scene.json` – inventory, static objects, camera/perspective cues, events, apparent-size summary.
* `tracks/cyclist.csv` – every frame: `left,top,right,bottom` (bbox), `width_px,height_px`, `cx,cy` (bbox centre),
  `ground_x,ground_y` (= bbox centre x, bbox bottom = front-wheel ground contact), `hip_x,hip_y` (pelvis estimate,
  top of the orange trousers at the saddle), `occluded` (always 0).
* `tracks/van.csv` – every frame: bbox (top = top of roof light bar, bottom = lowest tyre contact = image-right front
  tyre), `width_px,height_px`, `cx,cy`, `ground_x,ground_y`, `plate_x,plate_y` (licence-plate centre),
  `wheelFR/RR/FL_x,_y` (tyre ground contacts: FR = front wheel on the image-right, visible flank; RR = rear wheel on
  that flank; FL = other front wheel), `right_in_frame` (0 for frames 0-38), `occluded` (1 for frames 42-79), `note`.
* `scripts/` – `common.py` (decoding), `survey.py` (camera check, raw extents), `zoom.py`/`zoomc.py` (gridded /
  contrast-stretched crops used for hand reading), `keyframes.json` (all hand measurements), `klt.py` → `klt.json`
  (frame-to-frame similarity fits per object), `propagate.py` → `propagated.json`, `make_tracks.py` (CSVs + overlay
  check images), `road_lines.py` (road-line fit / vanishing point), `fgmask.py`/`seg.py` (background-difference
  masks – tried, not used for the final numbers, see below).

## Method
1. Hand measurements at keyframes 0,10,20,…,70,79 from zoomed gridded crops (bbox edges, cyclist hip, van plate,
   van tyre contacts at 40-79 read on contrast-stretched crops).
2. KLT feature tracking on each object (features on foreground, cyclist box excluded from the van; only the left 70 %
   of the cyclist box after frame 40) → per-frame scale + translation (rotation discarded).
3. Every hand point is pushed forward from the previous keyframe and backward from the next one with these
   per-frame motions and the two are blended linearly in time, so tracks pass exactly through the hand values and
   follow the tracked motion in between. Forward-prediction vs hand mismatch at the next keyframe (drift check):
   van bottom ≤ 6 px, van plate ≤ 5 px (11 px for 70→79), van top ≤ 10 px (16 px 70→79), van left/right up to
   20-27 px after frame 50 (the van turns its flank into view, so its width grows faster than the KLT scale);
   cyclist edges mostly ≤ 8 px, right edge up to 16 px after frame 50.
4. Overlays (bbox, centres, plate, wheel contacts) were drawn on frames 5,12,35,40,45,65,75,79 and inspected: the
   boxes hug both objects.

Background-difference masks were tried but rejected for the extents: the flashing blue beacon glow lights up the
facade above the van, the van and cyclist cast dark shadows on the road (masks bleed below the tyres), and the white
van has low contrast against the grey building – hence hand keyframes + tracking.

## Reliability
* Cyclist bbox edges: ±3 px at keyframes, ±5 px between. Height (helmet top to front-wheel contact) 177 px (f0) →
  207 (f20) → 253 (f40) → 313 (f60) → 419 px (f79). The rider is bent forward over the bars; this is riding height,
  not standing height. The bbox centre x oscillates with the pedalling sway (period ≈ 19 frames, ±2-3 px/frame in
  the per-frame differences) – smooth/fit before differentiating.
* Cyclist hip (pelvis): ±10-15 px; hidden partly by arms/parcel; prefer bbox centre / ground point for kinematics.
* Van top/bottom: ±3 px at keyframes (top = light-bar top, not the glow; white light-ray streaks above the bar are a
  render effect, ignored). Height 170 (f0) → 210 (f20) → 258 (f40) → 326 (f60) → 439 px (f79).
* Van right edge frames 0-38 and therefore its width/centre there: **extrapolated** (outside the image) by tracking
  scale – rough (±20 px). Van left edge frames 42-79: **estimated** behind the cyclist (±15 px). Van frame 0 top
  (468) is uncertain (±8 px).
* Van per-frame motion is very smooth (centre x step grows steadily from −4.8 to −25 px/frame; ground y step from
  +0.7 to +4.6 px/frame) – consistent with steady driving toward the camera.
* Plate centre: ±3 px (visible all clip from frame ~15; earlier it is outside/at the border, values extrapolated).
  Wheel contacts: x ±8 px (tyre seen obliquely), y ±3 px; hand-anchored only in 40-79 (FL 40-60); values outside
  those ranges are tracking extrapolations (FL behind the cyclist after ~62, FR/RR partly outside the frame before ~38).

## 3D / perspective notes
* Ground plane: road. Yellow solid centre line y = −0.1933x + 1053.2, right white edge line ≈ y = −0.40x + 1627;
  they meet at ≈ (2777, 516) → horizon roughly y ≈ 515-530 (assuming no roll; ±30 px).
* Both objects approach the camera: apparent height grows ×2.37 (cyclist) and ×2.58 (van) from frame 0 to 79,
  so their depths shrink accordingly; the van is behind (farther than) the cyclist throughout.
* Origins: van root/centre is not directly visible – bbox centre (`cx,cy`) or the ground point / mean of tyre
  contacts are the available proxies; for the cyclist the pelvis ≈ `hip_x,hip_y` (or bbox centre, which lies
  ~20-35 px to its left/below). Focal length unknown – derive it from given depths and a known size.
