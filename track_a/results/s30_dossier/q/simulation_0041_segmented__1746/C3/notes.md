2D scene, one scale from the person: 1.75 m / 47 px = 0.0372 m/px (person walks 1.34 m/s, boat 5.3 m/s, both realistic). Boat hull axis at -159 deg; deck beam perpendicular to it (far gunwale to near gunwale, mast excluded) = 94 px, hull perpendicular extent ~117 px. Correcting the projected beam for the ~40-50 deg camera elevation and ~30 deg yaw (foreshortening ~0.78) gives a true beam of ~4.4 m (13.3 m projected length, L/B ~3, a normal fishing boat). Raw PCA width (197.7 px) and bbox height (234 px) include the vertical mast and would give an implausible 7-9 m beam, so they were rejected.

Final message:
I measured the boat's width in the segmented 2D scene.

**Method:**
- **Scale:** The person's bbox height is ~47 px (mean over 72 frames), giving 1.75 m / 47 px = 0.0372 m/px. This scale checks out: the person walks at 1.34 m/s and the boat moves at 5.3 m/s (~10 knots), both realistic.
- **Boat width:** The boat is a 3D fishing-boat model viewed from above/side, with its hull axis at −159°. The deck beam perpendicular to the hull (far gunwale to near gunwale, excluding the vertical mast) is ~94 px; the hull's perpendicular extent is ~117 px.
- **Foreshortening:** From the visible freeboard and cabin wall, the camera elevation is ~40–50°, and with the hull yaw (~30°) the beam foreshortening factor is ~0.78. This gives a true beam of ~4.4 m (projected length 13.3 m, L/B ≈ 3, a normal fishing boat).
- The raw PCA width (197.7 px → 7.4 m) and bbox height (234 px → 8.7 m) include the vertical mast and would imply an implausible beam, so they were rejected.

**Answer: 4.4 m** (confidence moderate; the foreshortening correction is the main uncertainty, roughly ±10%).
