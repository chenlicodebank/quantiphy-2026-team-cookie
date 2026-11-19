# q_2829: distance between white cup and book (m)

Lab clip, 24 fps (file and question rate agree), 1280x720, f = 0.5959*1280 = 762.8 px, principal point (640, 360).
Both objects are static, so the trashbin velocity prior is not needed for scale; depth_info gives cup 2.516 m, book 2.082 m.

Method (measure.py): non-green mask (HSV key, 25 px closing) on frames 10 (t=0.4 s), 0 and 47; centroid of each object.
- cup centroid (564.3, 423.8), bbox 552-577 x 403-447
- book centroid (664.5, 614.6), bbox 630-701 x 577-653
Back-projection: unit ray x Euclidean camera distance (depth = distance to the centre), then the 3D distance:
- Euclidean-range reading: 0.756 m (frames 0/10/47: 0.7558 / 0.7557 / 0.7551)
- if the depth were taken as z instead: 0.724 m
Check: the bbox centres (564.5, 425) and (665.5, 615) give the same result within 1 mm; the scene/ record's centroids agree.
Answer 0.756 m (Euclidean-range convention). Confidence: good. The main uncertainty is where the centre was clicked on the book.
