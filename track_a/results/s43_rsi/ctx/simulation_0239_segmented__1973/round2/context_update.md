# Round 2 addendum for q1973 (house width)

## Verified (my_measure.py: new routes, i.e. a 5-frame median mask with direct eave-corner reads, and horse texture template matching)
- Round 1's proposal is reproduced.
  - The eave-level y extent is 618.0 px from direct corner reads and 618.1 px from the rake fit (round 1 had 619.6).
  - The eave-level x extent is 699 px (x 662-1361).
  - The ridge/eave ratio is 1.168, with the nadir at row 538.4, so the camera is top-down.
  - The cross-gable band is 805 px wide only at its ridge row y=380. At y=270 and y=520 it is flush with the main eaves
    (661/1362).
- Brown horse speed:
  - Template matching over one gait cycle gives 2.657 px/frame. The centroid gives 2.665 and the nose 2.636.
  - Adopted 2.65 px/frame, so the scale is 0.013742 m/px at the horse's body. Closure is within 0.6%.
  - The horse comes out 2.03 m long.
- W = 618 × 0.013742 = 8.49 m uncorrected. Correcting for eave height (single storey, Δh ≈ 1.5 m, pitch 35-45°,
  f ≈ 1700-2430 px) with k = 0.936-0.955 gives **7.95-8.11 m, central 8.05**.

## Ruled out
- 10.9-10.96 (C2/C3): a ridge-level extent along the longer side.
- The blend 8.94 carries 30% weight from that value.

## Open
- The eave height and focal length cannot be measured from the roof-only top-down view. This leaves ±2-3%. If the house
  were two-storey, W would be about 7.0-7.5, but nothing in the clip supports that.
- If the reference took "width" to be the x extent, the answer would be about 9.0-9.2. The convention (width is the shorter side)
  gives 8.05.
