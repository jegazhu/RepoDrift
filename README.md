# RepoDrift 🚀

*A Diagnostic Benchmark for API Deprecation Migration in Coding Agents*

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

RepoDrift is an open evaluation suite and diagnostic benchmark for measuring
how well coding agents perform long-horizon API deprecation migration across
real-world codebases without introducing functional regressions.

Submitted to the **Google Gemma 4 Developer Agent Paper Track**, 2026.

---

## 📊 Dataset Scale

RepoDrift v1.0 defines **14 API deprecation migration tasks** across **12 real-world
repositories**. Tasks are released in two tiers:

- **Runnable core set** — tasks executable within a standard Python environment.
  Validated end-to-end on `headroomlabs-ai/headroom` (57 and 66 baseline tests
  passing after migration).
- **Containerized task inventory** — tasks requiring per-repository Docker
  environments, provided as task specifications for community extension.

Repositories represented include:

| Repository | License | Deprecated API |
|---|---|---|
| `vllm-project/vllm` | Apache-2.0 | `asyncio.get_event_loop()` |
| `home-assistant/core` | Apache-2.0 | `asyncio.get_event_loop()` |
| `crewAIInc/crewAI` | MIT | `asyncio.get_event_loop()`, `datetime.utcnow()` |
| `scikit-learn/scikit-learn` | BSD-3-Clause | `collections.Mapping` |
| `apache/superset` | Apache-2.0 | `datetime.utcnow()` |
| `scrapy/scrapy` | BSD-3-Clause | `asyncio.get_event_loop()` |
| `bytedance/deer-flow` | MIT | `asyncio.get_event_loop()` |
| `zylon-ai/private-gpt` | Apache-2.0 | `asyncio.get_event_loop()` |
| `headroomlabs-ai/headroom` | MIT | `asyncio.get_event_loop()`, `datetime.utcnow()` |
| `FoundationAgents/MetaGPT` | MIT | `asyncio.get_event_loop()` |
| `FoundationAgents/OpenManus` | MIT | `asyncio.get_event_loop()` |
| `unclecode/crawl4ai` | Apache-2.0 | `asyncio.get_event_loop()` |

---

## 🛠️ The Three-Stage Evaluation Protocol

To prevent superficial patches and reward hacking, RepoDrift enforces a rigorous
validation pipeline:

1. **Stage 1 — Deprecation Audit (Static Verification):** Uses static analysis
   (AST parsing, grep, linters) to confirm that zero references to the deprecated
   API remain in the repository.
2. **Stage 2 — Behavioral Test Suite (Functional Correctness):** Runs the
   repository's native test suite to ensure observable behavior remains intact
   and no functional regressions are introduced.
3. **Stage 3 — Interface Contract Verification (Semantic Integrity):** Executes
   specialized contract tests to validate that the modern replacement API is
   invoked correctly.

An agent submission receives a definitive **PASS** only when it successfully
clears all three stages.

### Gold-Patch Validation Gate

Before any task is used to score an agent, RepoDrift requires that the task's
**correct reference migration** passes all three stages. If the gold patch fails
any stage, the task is flagged as invalid and removed from the benchmark.

---

## 📂 Repository Structure

```
RepoDrift/
├── harness/                # Three-stage evaluation logic
│   ├── stage1_audit.py
│   ├── stage2_behavioral.py
│   ├── stage3_contract.py
│   ├── gold_patch_gate.py
│   └── orchestrator.py
├── tasks/                  # 14 task definitions
│   ├── task_<repo>_<api>/
│   │   └── task_config.json
│   └── sample_deprecation_task.py
├── docs/
│   └── protocol.md
├── LICENSE                 # Apache-2.0
└── README.md
```

---

## 🚀 Getting Started

Clone the repository and explore the evaluation harness:

```bash
git clone https://github.com/jegazhu/RepoDrift.git
cd RepoDrift
```

Each task's `task_config.json` specifies the deprecated API, replacement API,
base commit, affected production files, and scoped test command. To evaluate
an agent:

1. Clone the target repository at the specified `base_commit`.
2. Run the agent to produce a migration patch.
3. Apply the patch and run the three-stage harness.

---

## 🧩 Extending RepoDrift

RepoDrift is designed for extension. To add a new task:

1. Select a repository with a documented API deprecation.
2. Identify the base commit and the correct migration.
3. Verify the repository's test suite passes before migration.
4. Add a `task_config.json` under `tasks/` following the schema in
   `tasks/sample_deprecation_task.py`.
5. Run the gold-patch validation gate to confirm the task is solvable.

To add a new language or refactoring class, adapt the Stage 1 audit
(static analysis) and Stage 3 contract verification (semantic tests)
for the target language.

---

## 📝 Citation

If you use RepoDrift in your research, please cite:

```bibtex
@misc{repodrift2026,
  title  = {RepoDrift: A Diagnostic Benchmark for API Deprecation Migration in Coding Agents},
  author = {Zhu, J.},
  year   = {2026},
  note   = {Gemma 4 Developer Agent Paper Track, Kaggle}
}
```

---

## 📄 License

This project is licensed under the Apache License 2.0 — see the [LICENSE](LICENSE) file for details.
