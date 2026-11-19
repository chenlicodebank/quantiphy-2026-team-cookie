"""Lab prop sizes from the QuantiPhy paper (2026-10-22, Track B session eac5885a; Series 28).

The paper's appendix B (tex/sec/appendix/b_collect.tex, Table "List of physical objects and their measured dimensions
used in our lab-captured videos") lists every prop of the lab captures with its hand-measured dimensions, and appendix C
says the lab static sizes are those manual measurements ("To obtain static priors such as object size, we manually
measure the shape and dimensions of each object"). On the labelled validation split 11 of the 12 lab size questions
about a listed prop carry exactly the table value (the twelfth, a notebook width 10.8 against the table's 8.8 x 18.6,
is a different notebook or a slip). This is knowledge of how the dataset was made, the same for every question
(challenge.md, per-question rule, reading (2)); no other question's prior or answer enters.

snap(question, value, video_source) moves a lab size answer to the nearest listed dimension of the prop the question
names, when the answer is already within --tol of it (the answer still decides which edge of a box is meant and
rejects a wrong match, such as an "orange ball" that is the basketball, not the 5.7 cm orange plastic ball).
"""
import math
import re

# name patterns -> dimensions in cm (the table's numbers). The table does not say which edge of a box is its length,
# width or height, so a name maps to the edges it can mean and a snap picks the one nearest the measured answer.
PROPS = [
    # (name pattern, {named dimension: cm}); "any" lists every edge for names the table cannot settle
    (r"ping ?pong", {"any": (4.0,)}),
    (r"tennis ball", {"any": (6.7,)}),
    (r"yoga ball|purple ball", {"any": (52.2,)}),
    (r"soccer ball|football", {"any": (17.5,)}),
    (r"basketball", {"any": (23.2,)}),
    (r"red (?:plastic )?ball", {"any": (7.0,)}),
    (r"orange (?:plastic )?ball", {"any": (5.7, 23.2)}),  # the plastic ball, or the orange basketball some clips name so
    (r"white ball", {"any": (4.0,)}),  # the white ping pong balls
    (r"green ball|pink ball", {"any": (6.7,)}),  # the coloured tennis balls
    (r"slope|small white ?board", {"length": (30.8,), "width": (23.2,), "thickness": (0.5,), "height": (0.5,),
                                   "any": (30.8, 23.2)}),
    (r"white ?board", {"thickness": (1.0,), "any": (81.0, 60.0)}),
    (r"trash ?bin|trash ?can", {"any": (34.5, 89.1, 59.9)}),
    (r"\btape\b", {"diameter": (10.1,), "width": (10.1, 4.8), "length": (10.1,), "height": (4.8,), "thickness": (4.8,),
                   "any": (10.1, 4.8)}),
    (r"food box|white box", {"length": (19.5,), "any": (19.5, 6.0, 7.2)}),
    (r"cookie", {"diameter": (8.0,), "width": (8.0,), "length": (8.0,), "thickness": (1.8,), "height": (1.8,),
                 "any": (8.0, 1.8)}),
    (r"cosmetic jar", {"diameter": (7.2,), "width": (7.2,), "height": (6.0,), "any": (7.2, 6.0)}),
    (r"glass jar", {"diameter": (6.8,), "width": (6.8,), "height": (8.5,), "any": (6.8, 8.5)}),
    (r"\bcup\b", {"diameter": (8.6,), "width": (8.6,), "height": (14.5,), "length": (14.5,), "any": (8.6, 14.5)}),
    (r"bottle", {"diameter": (6.7,), "width": (6.7,), "height": (19.5,), "length": (19.5,), "any": (6.7, 19.5)}),
    (r"marker", {"length": (13.5,), "diameter": (0.8,), "width": (0.8,), "any": (13.5, 0.8)}),
    (r"\bpen\b", {"length": (14.5,), "diameter": (1.2,), "width": (1.2,), "any": (14.5, 1.2)}),
    (r"note ?book", {"length": (18.6,), "width": (8.8,), "thickness": (1.5,), "height": (1.5,), "any": (18.6, 8.8, 1.5)}),
    (r"book", {"thickness": (2.2, 1.5), "width": (12.5, 8.8), "length": (19.5, 18.6), "height": (2.2, 1.5, 19.5),
               "any": (12.5, 19.5, 2.2, 18.6, 8.8, 1.5)}),  # either listed book (the green notebook too)
    (r"pencil (?:case|bag)", {"length": (21.0,), "height": (6.7, 7.2), "width": (6.7, 7.2), "any": (6.7, 7.2, 21.0)}),
    (r"credit card", {"length": (8.56,), "width": (5.398,), "any": (8.56, 5.398)}),
    (r"poker|deck of cards|playing cards", {"length": (9.8,), "width": (6.3,), "height": (1.8,), "thickness": (1.8,),
                                           "any": (9.8, 6.3, 1.8)}),
]
SIZE_Q = re.compile(r"\b(height|length|width|diameter|radius|size|thickness|depth|side)\b", re.I)
MOTION_Q = re.compile(r"veloc|speed|accelerat|displacement|distance|travel|between|from .* to|rebou|bounce|reach|"
                      r"maximum height|max height|highest|lowest|tower", re.I)  # a card tower is no prop
# Colour-named balls, books, bins, boards and boxes can be props the table does not list (captured_0054's "white ball"
# is about 7 cm, no ping pong ball): those move only when the answer is already within UNSURE_TOL of a listed value.
UNSURE = re.compile(r"book|trash|white ?board|box|(?:white|orange|red|green|pink) ball", re.I)
UNSURE_TOL = 1.35


def unit_factor(q):
    """cm -> the question's unit."""
    ql = q.lower()
    if re.search(r"\bin mm\b|\(mm\)|millimet", ql):
        return 10.0
    if re.search(r"\bin cm\b|\(cm\)|centimet", ql):
        return 1.0
    if re.search(r"\bin m\b|\bin meters?\b|\bin metres?\b|\(m\)", ql):
        return 0.01
    return 1.0


def prop_dims(q):
    """The listed dimensions (in the question's unit) of the prop a lab size question names, restricted to the
    dimension it names when the table settles that name, or None."""
    m = SIZE_Q.search(q)
    if not m or MOTION_Q.search(q):
        return None
    ql = q.lower()
    name = m.group(1).lower()
    name = {"radius": "diameter", "depth": "thickness", "size": "any", "side": "any"}.get(name, name)
    for pat, dims in PROPS:
        if re.search(pat, ql):
            k = unit_factor(q)
            out = [d * k for d in dims.get(name, dims["any"])]
            if re.search(r"\bradius\b", ql):
                out = [d / 2 for d in out]
            return out
    return None


def snap(q, value, source, tol=1.6):
    """(new value, matched dimension or None). A prop whose named dimension leaves one listed value takes it whatever
    the answer (a scale error does not change which pen it is); a name that leaves several, or a prop the table may
    not be the one meant (UNSURE), moves only when the answer is within tol of the nearest listed value."""
    if source != "lab" or value is None or not value > 0:
        return value, None
    dims = prop_dims(q)
    if not dims:
        return value, None
    best = min(dims, key=lambda d: abs(math.log(value / d)))
    gap = abs(math.log(value / best))
    if UNSURE.search(q):
        return (best, best) if gap <= math.log(UNSURE_TOL) else (value, None)
    if len(dims) == 1 or gap <= math.log(tol):
        return best, best
    return value, None
