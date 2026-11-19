# QuantiPhy Challenge 2026: team Cookie

This repository holds the code, the method descriptions and the recorded model outputs behind our final submissions
to the [QuantiPhy Challenge](https://quantiphy.stanford.edu/competition/index.html) at NeurIPS 2026, one folder per
track. Each folder rebuilds its submission files byte for byte from the recorded per-question sessions, and contains
the pipeline that produced those sessions.

| folder | track | method |
|---|---|---|
| [`track_a/`](track_a/) | Track A (main track) | [`track_a/METHOD.md`](track_a/METHOD.md) |
| [`track_b/`](track_b/) | Track B (open-weight track) | [`track_b/METHOD.md`](track_b/METHOD.md) |

## The method in brief

Every answer is a measurement made in code by a coding agent, one question per session. A first session per video
writes a question-blind scene record (objects, tracks, timings, camera cues). Then a fresh session per question gets
the video, that record and the one question with its own prior and depth_info, measures in code and converts pixels to
metres.

- **Track B** uses open weights only: DeepSeek-V4.1-Flash-1017 in the DeepSeek Harness, with SAM 3 segmentation and
  tracking as tools. Each row is the median of 2 to 6 sessions of the same question.
- **Track A** uses Claude Opus in Claude Code as the agent and combines its answer, per question, with the Track B
  median.

In each folder, `METHOD.md` describes every step, `MODELS.md` every model and setting, and `STATEMENT.md` how every
prediction was produced from its own question's inputs, with the one exception in Track A and every choice we
disclose. `SUBMISSION.md` names the two uploads the folder rebuilds: the entry we put forward, and an alternative
with extra steps that we asked the organisers to rule on.

## Rebuild the submissions

Python 3.13. Track A takes under a minute, Track B about 2 minutes.

```sh
cd track_b            # or track_a
python3.13 -m venv .venv && . .venv/bin/activate
pip install -r requirements-rebuild.txt
./reproduce.sh
```

`reproduce.sh` runs our build scripts as they ran and prints the sha256 of every rebuilt file, with
`"byte_identical": true` when it equals the uploaded file (`SUBMISSION.json`). In Track A it then traces every value of
the answer lines to the per-question record it comes from. Model calls are not deterministic, so running the agents
again gives slightly different answers. The recorded answers are the exact inputs of the rebuild. Each folder's
`README.md` explains its layout and how to run the agents on new questions.

## Data and models

- `track_*/data/` holds the question rows of the QuantiPhy test split (revision of 2026-10-21) and of the validation
  split, from the Hugging Face datasets [`PaulineLi/QuantiPhy`](https://huggingface.co/datasets/PaulineLi/QuantiPhy)
  and [`PaulineLi/QuantiPhy-validation`](https://huggingface.co/datasets/PaulineLi/QuantiPhy-validation), released
  under CC BY 4.0 by the QuantiPhy authors. The videos are not included. They come from the same datasets.
- DeepSeek-V4.1-Flash-1017:
  [`deepseek-ai/DeepSeek-V4.1-Flash-1017`](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017), MIT license.
- SAM 3: [`facebook/sam3`](https://huggingface.co/facebook/sam3), gated access under Meta's license. Its weights are not
  included.

## Cost

To be added: what each track cost to run (model calls and compute), and the accuracy gained per unit of cost.

## Changes from our code packages of 28 October 2026

Only local paths, login names, internal references and archive owners differ. Every answer and every build step is
unchanged. [`CHANGES.md`](CHANGES.md) lists each change.

## License

MIT, see [`LICENSE`](LICENSE). The bundled QuantiPhy question rows keep their CC BY 4.0 license.

Team Cookie: Chen Li and Luhui Liu.
