# Round 2 addendum for q1680 (rock length)

## Verified (own code, a different extraction from round 1)
- **Pitch from the vertical vanishing point** (vp_edges.py). Sub-pixel half-level edge crossings on two dark verticals, 70 frames, u 265–778:
  - mast stripe: 18.17° (17.8–18.5);
  - thin post: 18.80° (17.9–19.6).
  - This confirms θ ≈ 18.5 ± 0.5°. C1's 15.25° is biased low. The split halves of the post scatter (25° and 18°), so a short window is unreliable.
- **Focal length** (closure2.py). f = 3496–3503 px. The 4 m/s prior closes within 0.04–0.24%. Boat hull: 10.1 m.
- **Front-waterline lower bound.** L ≥ 21.2–21.6 m for θ 18.2–18.8° and Zwl 88.5–89.5 m. The submitted 20.5 is below it.
- **Round 1's ellfeat.py solutions are partly unphysical.** For example, at b/a = 1 it gives zc > c, an ellipsoid floating clear of the water.
- **New outline fit** (ellfit2.py). Ellipsoid touching the water, free yaw, full per-column outline. At θ 18.2–18.8° and b/a 0.5–1.0: lateral AABB extent 21.8–22.7 m, rms 12.5–14.6 px.
- **Adopted: 22.0 m** (round 1 had 21.8).

## Ruled out
- **Rock at the boat's depth** (15.4–16.4 m): its waterline is 343 px higher and the camera looks down.
- **θ = 15.25°** (23–24 m).

## Still open
- **Front-to-back extent.** Fits elongated in depth (b/a 1.6–2.0) are worse (rms 14.8–16.3 px against 12.5–13.7) and need a 3–4 m flat slab. That is weak evidence that length is the lateral extent, not proof.
- **Pitch.** ±0.5° gives about ±1.5% in L.
