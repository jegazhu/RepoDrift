# RepoDrift 🚀
*A Diagnostic Benchmark for API Deprecation Migration in Coding Agents*

RepoDrift is an open evaluation suite and diagnostic benchmark designed to measure how well coding agents perform long-horizon API deprecation migration across real-world codebases without introducing functional regressions.

---

## 🛠️ The Three-Stage Evaluation Protocol

To prevent superficial patches and reward hacking, RepoDrift enforces a rigorous validation pipeline:

1. **Deprecation Audit (Static Verification):** Uses static analysis (AST parsing, grep, linters) to confirm that zero references to the deprecated API remain in the repository.
2. **Behavioral Test Suite (Functional Correctness):** Runs the repository's native test suite to ensure observable behavior remains intact and no functional regressions are introduced.
3. **Interface Contract Verification (Semantic Integrity):** Executes specialized contract tests to validate that the modern replacement API is invoked correctly.

An agent submission receives a definitive **PASS** only when it successfully clears all three stages.

---

## 📂 Repository Structure

- `harness/`: Contains the evaluation logic, static auditing tools, and test runners.
- `tasks/`: Houses the curated benchmark tasks representing real-world API deprecations.

---

## 🚀 Getting Started

Clone the repository and explore the evaluation harness:
```bash
git clone [https://github.com/jegazhu/RepoDrift.git](https://github.com/jegazhu/RepoDrift.git)
cd RepoDrift
