# Lessons library, harness v3 (v2 plus what rounds 1-2 learned about re-asks; procedure only, no question values)

1. A segmentation clip keeps the original scene's answers: if the object the question names was removed with the
   background, the answer is still about that object; never re-read the question as being about another visible
   object, and a measured substitute far outside the asked object's plausible range is wrong.
2. Agreement is weak evidence. Sessions of one model share its readings, and the open-weight agent's repeated runs share
   its errors; on held-out scores the Claude sessions are usually the more accurate measurers, but not always.
3. When one candidate's answer is close to a constant multiple of another's, the difference is almost always one scale
   step (pixel scale, focal length, which point the depth refers to, which object served as the scale, a unit). Decide
   it by closure on the question's own prior, never by which candidate looks more self-consistent; a mislabelled scale
   object gives a consistent but wrong constant-factor answer.
4. The submitted answer may carry a fixed convention factor or a fixed-rule blend validated on held-out scores for its
   whole population (CONTEXT.md names it). When the candidates differ from it by exactly that factor, the factor is the
   convention, not a fault; only a fault in a measurement step justifies a change.
5. In a 3D scene, a focal length from two references at nearly the same depth, or from a short baseline, is
   ill-conditioned. When given depths imply inconsistent geometry, calibrate the focal length from vanishing points of
   level scene lines plus verticals and trust the depth that calibration reproduces.
6. A speed or acceleration asked at a time is a short-window derivative around that time. Locate velocity steps first
   and confine every fit to its own smooth segment; for motion easing in or out, a local cubic or ease-curve model beats
   a long quadratic; the backward-difference second difference is centred one frame before the asked time.
7. For an acceleration between two time windows of real footage, take each window's average speed from its endpoint
   positions (forward differences), not from in-window line fits, which shrink the change when motion is uneven.
8. Animated characters: before trusting a near-constant given distance for a walker, check its facing (frontal vs
   profile silhouette), whether its feet stay planted in stance, and whether the given distances move with the body.
   Root motion on the hip carries the gait surge into one-frame derivatives.
9. Depth rates from apparent size are biased by pose, yaw, lean and motion blur: prefer the vertical scale of a rigid
   part over long baselines, or a vanishing point that many long scene lines share; pose changes (straightening, a
   planted foot at a fixed image row) must not drive the radial velocity.
10. When the asked object changes depth during the clip, its pixel extent and its depth must be read at the same frame.
11. Identify the asked object by its role, on zoomed frames: on foot versus on a vehicle, the struck object versus the
    hand-held strikers; when several objects of the asked kind appear, measure each and check which the submitted
    answer fits.
12. Named dimensions follow the conventions above. In real footage, a reading that makes a standard object unrealistic
    signals a misread dimension; in a rendered scene, a uniformly oversized scene under an unrealistic prior is a
    legitimately scaled scene, not a reason to re-read the prior's dimension.
13. A question that names a part of an object while depth_info gives the object's origin: first establish whether the
    origin can lie at that part. A minimum distance at an instant is a surface-to-surface gap, not origin to origin.
    An object standing on the floor with no other support includes its stand or pedestal.
14. An earlier answer that substituted a typical real-world value for a measurement is a guess; prefer a measurement
    that passes closure, and keep the guess only when nothing in the clip can be measured.
15. When the submitted answer comes from a re-ask under a named convention (objects at real-world scale, a prior whose
    motion the clip never shows), that convention was validated on held-out scores for its whole population.
    Returning to the reading the re-ask replaced needs a measured fault in the re-ask's own measurement, not a
    preference for the earlier scale or agreement with other candidates that share the earlier reading.
