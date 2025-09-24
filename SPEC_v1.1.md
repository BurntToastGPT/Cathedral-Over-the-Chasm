# Cathedral Over the Chasm — SPEC v1.1 (Proposed)
**Date:** 2025-09-20 18:07 UTC  
**Author:** Noah Scott (Independent Researcher)

## Goals
v1.1 hardens the benchmark to reduce spec‑gaming while preserving creativity. It enforces: (i) Curator salience; (ii) on‑line inference evidence; (iii) ablation integrity for the musical prior; (iv) sufficient world complexity; (v) reproducibility and openness.

## Evaluation Protocol
- **Containerized run:** A single `docker run` command must produce bit‑reproducible outputs on reviewer hardware. No external network calls.
- **Two‑phase holdout:** Submitters provide a container image + commit hash. Organizers generate **secret nonces** after submission and run the image against them.
- **Deliverables:** code, logs, verifier proofs, `THEME` artifact, and an ablation report. Provide a `MANIFEST.json` with file hashes.

## Mandatory Checks (Pass/Fail)
1. **Curator salience** — Randomize intervention period `K ∈ {10, 20, 40}`. Each successful run must contain **≥3** Curator interventions and **≥1** that materially changes the plan (log plan diff).  
   *Fail:* `{num_interventions < 3}` or all deltas negligible.
2. **Curator update diversity** — Entropy of Curator update sequences across holdout nonces must exceed **H ≥ 1.5 bits**.  
   *Fail:* patterned, templated updates below threshold.
3. **On‑line inference logs** — For each step, log `(observation, Δposterior-summary, top‑k actions + scores)`.  
   *Fail:* any run missing the triplets chain.
4. **Action‑sequence entropy** — Across 100 runs, **H(action path) ≥ 1.75 bits** unless sensors are byte‑identical (then document).  
   *Fail:* below threshold without justification.
5. **Ablation integrity** — Hold planner schedule constant between `with-theme` and `no-theme`. Require **≥10% median** step reduction and **≥70%** improved runs.  
   *Fail:* below either threshold.
6. **Prior robustness (anti‑steg)** — Perturb `THEME` (transpose ±2 semitones; tempo ±5%). Performance loss must be **<50%** vs unperturbed.  
   *Fail:* cliff behavior suggests steganography.
7. **W_Σ complexity witness** — EITHER (a) median positive Lyapunov exponent in passive trajectories, OR (b) baseline A* requires **>10,000 steps** on gauntlet tasks.  
   *Fail:* both easy.
8. **Fragility calibration** — Cumulative‑stress break model calibrated within **±10%** of empirical survival probabilities.  
   *Fail:* mis‑calibrated.
9. **Novelty meta‑verification** — Sample **3–5** verifier claims and re‑prove in an independent prover (e.g., Lean/Isabelle).  
   *Fail:* any sampled claim fails.
10. **Blow‑up baselines** — Compute against a fixed panel (e.g., PA, STLC, a ZFC fragment, simple category, MLTT fragment). Require **median ≥100×** blow‑up.  
    *Fail:* below threshold.
11. **Curator orthogonality** — Correlation between aesthetic score and stability margin must be **< 0.1** across successes.  
    *Fail:* ≥0.1.
12. **Component ablations** — Remove each axis (axioms / embodiment / adversary / music). Expect **≥20%** median performance drop per axis.  
    *Fail:* no drop.
13. **Open artifacts** — Release code/seeds/raw logs; or supply a minimal OSS “hello‑world” kit that reproduces a toy run.  
    *Fail:* neither provided.
14. **Container determinism** — All runs in the holdout driver must be deterministic given the same nonce. Provide PRNG seed discipline.  
    *Fail:* nondeterministic outcomes.
15. **MANIFEST** — SHA‑256 for every file in the artifact; list tool versions; include `run_eval.sh` entrypoint.  
    *Fail:* missing or mismatched hashes.

## Logging Schema (JSONL)
Each step line includes:
```json
{
  "t": 12,
  "obs": "...",
  "posterior_delta": {"taste_mode": "symmetry", "confidence": 0.62},
  "candidate_actions": [{"a":"brace", "score":0.71}, { "a":"shim", "score":0.41 }],
  "chosen_action": "brace",
  "energy": 3,
  "curator_event": null
}
```

## Ablation Protocol
- Freeze planner schedule, sampler seeds, and exploration budget.  
- Run `N=100` nonces with and without `THEME`; compute median delta and percent improved.  
- Robustness: apply controlled perturbations; compare relative loss.

## Reproducibility
- Provide `Dockerfile`, `run_eval.sh`, and `README_docker.md`.  
- No internet. All dependencies vendored or pinned.  
- Outputs archived to `out/` with `MANIFEST.json` and a `REPLAY.md` for re‑analysis.
