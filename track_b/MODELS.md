# Models, weights and generation settings (Track B, team Cookie)

Every value in both files is the median of DeepSeek-V4.1-Flash-1017 sessions of that question, times at most one
deterministic factor computed without a model; in the alternative (#222), some rows take a validation value or a value
from the paper's prop table instead (`STATEMENT.md`). No model was fine-tuned, so there are no checkpoints.

| model | weights (public) | how it was called | role |
|---|---|---|---|
| DeepSeek-V4.1-Flash-1017 | [`deepseek-ai/DeepSeek-V4.1-Flash-1017`](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017), MIT, not gated (Hugging Face API read 2026-10-22) | DeepSeek Harness 0.2.1, through OpenRouter as `deepseek/deepseek-v4.1-flash-1017`, pinned to DeepInfra's fp8 deployment | every answer: 568 scene records, 8,800 per-question sessions |
| SAM 3 | [`facebook/sam3`](https://huggingface.co/facebook/sam3), public with gated access (access on request; Hugging Face lists the license as `other`, Meta's own terms) | our server on a Lambda GH200 (`scripts/sam3_server.py`, `transformers` 5.14.1) | `segment` and `track` tools the agent calls; question-agnostic |

## DeepSeek sessions (`scripts/dsh_scene.py`; launchers `scripts/run_29_5.sh`, `scripts/run_37_*.sh`)

- Reasoning effort `medium`, temperature 0.3, top_p the provider default, `max_tokens` 16,384 a request; caps of 60
  calls, 200,000 output tokens, 30 images, 40 minutes and $0.30 a session; the last 3 calls of a question session can
  only submit the answer. API keys came from an environment file on the GPU box, which this package does not include.
- Serving: OpenRouter with `provider.only` set to DeepInfra fp8 (`deepinfra/fp8`, and from Series 37 its flex,
  standard and priority price tiers of the same deployment), no fallback. Every run record keeps its `provider_pin`
  and the provider that answered each request: DeepInfra for 279,278 requests, unrecorded for 53.
- Harness tools: `run_python` (sandboxed Python with OpenCV, NumPy, SciPy, PyAV), `video_frames`, `view_image`,
  `finish_answers`, and the SAM 3 `segment` / `track` calls (score threshold 0.3, at most 8 instances).
- Phase 1 writes one question-blind scene record per video; phase 2 runs one session per question with that record,
  the video and the question's own `inputs.json`.
- The same code calls any OpenAI-compatible server (the bridge `baseURL`), so a self-hosted server of the public
  weights replaces the hosted one without code changes. We did not run that path during the competition.

## Where to check

Each compacted run record in `records.tar.xz` (`results/s37_test_repeats/q/<video>__<id>/r<k>.json`, and
`results/s37_physcheck/q/...` for the physical-scale sessions) holds the model id, provider pin, reasoning setting,
finish reason, the session's inputs, its notes, its final answer and its cost. The raw event streams (about 12 GB) and
the code each session wrote are kept on our side and available on request.
