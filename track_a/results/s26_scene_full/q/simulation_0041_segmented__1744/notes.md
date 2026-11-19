# q_1744 — height of the boat (prior: person height 1.75 m)

fps 24 = question_fps (no re-timing issue; time not needed for a size).

## Geometry
- The view is oblique from above, so the boat's vertical extent cannot be read straight off the bbox (234 px is
  mast top plus deck/hull depth foreshortening). The reference is the world AABB z-extent (keel to mast top).
- Perspective is weak: rigid-boat ECC scale change only ~1.5 % per 100 px of vertical image motion
  (`boat_ecc.py`, `boat_scale.py`), so f ≈ 6000 px (narrow FOV). Close to orthographic.
- Camera elevation at the boat from rectangular deck hatches (`frames/bow.png`, `frames/aft.png`): heading edges
  slope 0.21, beam edges x/y ≈ 0.35–0.44 → tanα·sinψ = 0.21, tanα/sinψ ≈ 0.38 → ψ ≈ 48° ± 4°, α ≈ 16°.
  Teal hatch aspect (39/49) agrees with a square hatch at that angle.
- Person (`person.py`, mask = 255 − min RGB > 40; > 12 gives mean 46.9): bbox height 39–51 px, mean 45.8 px, width ~19 px.
  Projected extent model: head top 1.65cosψ + 0.1 + mean forward toe offset 0.25 sinψ, with ψ ≈ 43° at the person
  (5° shallower than at the boat because of the perspective).
  → vertical px per metre ≈ 22.6 at the person. Perspective scale and cosψ changes almost cancel
  (sin2ψ is near 1 around 45°), so ≈ 22.3–22.6 px/m at the boat. This is insensitive to ψ (21–22.7 for ψ 43–55°).

## Boat height
- Mast top: y = 843 (frame 0). Centreline deck point under the mast: cabin near-face bottom ≈ 1010 minus half cabin
  width (24 px/m beam projection), cross-checked with near sheer ≈ 1027 minus half beam (B ≈ 3 m) → ≈ 991–995.
  → mast top above deck ≈ (995 − 843)/22.6 ≈ 6.7 m (cabin ≈ 2.2 m + mast above roof ≈ 4.2 m).
- Keel is hidden. Deck-to-keel depth is estimated from the visible near-side hull band (15–22 px below the sheer) with
  box-shaped vs elliptical cross-section bounds 0.8–1.85 m → ≈ 1.0–1.2 m.
- H ≈ 6.7 + 1.0 ≈ 7.7 m.

## Checks
- Boat length along the heading ≈ 10.3 m, beam ≈ 3 m. H/L ≈ 0.75 is plausible for a fishing boat with a mast.
- Under the naive 2D convention (bbox 234 px / person 45.8 px × 1.75) the result would be 8.9 m. That includes
  deck-depth foreshortening, so it is an upper bound.
- Person walking speed implied ≈ 1.2–1.7 m/s (plausible).

Confidence: moderate (~±12 %). The main uncertainties are the hidden hull depth below the deck and the person's
projected-height model.
