"""37_3 (2026-10-24, Track B, session 05e6b3c8): the per-question physical-scale check on internet questions.

On the dataset authors' self-filmed internet clips the reference answers sit on the scene's physical scale when the
stated motion prior contradicts it (Track A board #196: D2 +.018 on 43 rows with Claude's question-blind scene records;
the public VihanAggarwal repo's PHYSB reads +.009 / +.006). The Track B answers (B7) are still on the prior's scale there
(internet_0053: a 2.56 m scooter rider), and a session given the 28_6 --physical-internet card switches unevenly within
one clip. So here the open model only MEASURES and code decides: each internet question gets one more dsh_scene session
in r1's configuration plus SCALE_CHECK below, which keeps the answer on the prior's scale and records, in a fenced
scale_check block, whether the clip is self-filmed footage and the implied size of standard objects (an adult person,
regulation balls) under that question's own prior. scripts/s37_final_b.py applies the rule fixed before any read
(k = standard / implied, adult persons first, when the session calls the clip self-filmed and |ln k| > ln 1.15).
Everything comes from the question's own video, prior and session; the reference sizes are dataset-construction
knowledge (26_52's 1.65 m cap-to-soles adult, 24.3 cm basketball, 4.0 cm table-tennis ball).

Same arguments as dsh_scene.py; the card goes into every question session's prompt before "Method:".
"""
import dsh_scene as runner

SCALE_CHECK = """Scale check (this run): answer the question at the prior's scale as usual, and also check that scale against
standard objects in view. After you have the metres-per-pixel scale from the prior, measure on a clear frame each of
these that is fully visible, from the segment tool's mask: an adult person standing, walking or riding upright (crown
to soles; reference 1.65 m), a basketball (24.3 cm), a soccer ball (22 cm), a tennis ball (6.7 cm), a table-tennis
ball (4.0 cm). Measure them in the same plane as the prior's object where you can (in a 2D scene the scale holds in
that plane). Then write in notes.md one fenced block

```scale_check
{"self_filmed": true, "objects": [{"name": "adult person", "pixel_size": 412.0, "implied_m": 2.56, "standard_m": 1.65}]}
```

with "self_filmed" true only for everyday footage its makers filmed themselves (people riding, walking or playing in a
street, car park, room or court, from a handheld or tripod phone camera) and false for broadcast, dashcam, sports TV,
film, animation or lab footage; "implied_m" is the object's size in metres under the prior's scale; "objects" is an
empty list when no such object is fully visible. Do not change your answer because of this check.

"""


def main():
    original = runner.session

    def session(a, ws, inputs, system, prompt, rec_path):
        if inputs.get("questions"):
            assert system.count("Method:\n") >= 1
            system = system.replace("Method:\n", SCALE_CHECK + "Method:\n", 1)
        return original(a, ws, inputs, system, prompt, rec_path)

    runner.session = session
    runner.main()


if __name__ == "__main__":
    main()
