# MADELEINE — PHASE 10 ADVERSARIAL SCIENTIFIC AUDIT v1

## Status

Audit target:

v0.2.1

Frozen scientific commit:

fee2c31cfa17159a4075e1cbfbfa7e2fceba9c4b

The audit is post-publication.

It does not modify the frozen v0.2.1 object.

It does not introduce new experiments.

---

## 1. Purpose

The purpose of PHASE 10 is to evaluate MADELEINE v0.2.1 as if it had been submitted by an unrelated author.

No claim receives credit from terminology, architectural coherence, previous internal PASS labels, publication status, DOI assignment, download counts or author intent.

Every claim must survive independent scrutiny.

---

## 2. Fundamental rule

CORRECT != NOVEL != GENERAL != EXTERNALLY VALIDATED

A result may be correct while elementary or known.

A computational observation may be reproducible while restricted to the tested generator.

A methodological rule may be useful without being a mathematical theorem.

An internal regime may be robust without constituting a physical regime.

These categories must never be merged.

---

## 3. Audit dimensions

Every priority claim will be evaluated on:

1. exact formulation;
2. domain and assumptions;
3. logical correctness;
4. reproducibility;
5. dependence on definitions chosen by MADELEINE;
6. strength of falsification attempts;
7. generality;
8. comparison with established literature;
9. mathematical novelty;
10. methodological novelty;
11. empirical/external support;
12. residual risk.

---

## 4. Evidence classes

### F — Formal

A proposition or theorem with an independently checkable derivation.

### C — Computational

A result established by frozen executable procedures over declared data or generated series.

### M — Methodological

A rule, gate, protocol or policy whose validity is procedural rather than a theorem about an external system.

### E — External

Evidence obtained from an independent empirical, observational or externally supplied system.

No evidence may be promoted from one class to another without an explicit bridge.

---

## 5. Adversarial verdicts

### SURVIVES

The exact claim survives the attempted objection within its declared domain.

### SURVIVES_WITH_RESTRICTION

The core result survives but the wording, domain or interpretation must remain narrower than a stronger reading.

### STANDARD_OR_DERIVATIVE

The claim is correct but appears to follow from standard mathematics or established methodology and cannot currently be treated as a new theorem by itself.

### UNDERDETERMINED

The available evidence does not distinguish the claim from relevant alternatives.

### FAILS

A valid counterexample, logical defect, reproducibility failure or contradiction defeats the exact claim.

### EXTERNAL_VALIDATION_REQUIRED

The internal result may stand, but the external interpretation has not been established.

---

## 6. Priority audit set

The first adversarial pass will examine:

- C012 / DMO-001 — canonical origin sub_0;
- C014 / DMO-002 — double register;
- C016 / DMO-003 — six-channel projection;
- C020 / DMO-004 — regime gate;
- C026 / DMO-005 — comparability;
- C030 / DMO-006 — translation accounting;
- LAB-D0;
- LAB-D1;
- LAB-D2;
- ABLATIONS-v1;
- ATLAS-v1;
- HISTORY-DEPTH-v1;
- HISTORY-DEPTH-ATLAS-v1.

---

## 7. Required adversarial question for every claim

For every claim we must answer:

- What exactly is proved or observed?
- What would falsify it?
- Is the conclusion stronger than its premises?
- Does it follow trivially from the definitions?
- Is the result already standard?
- Could a simpler model reproduce the same evidence?
- Does the numerical result depend materially on thresholds or protocol choices?
- Has the claim been tested outside the system that generated it?
- Which statement is the strongest one currently justified?
- Which tempting stronger statement is explicitly not justified?

---

## 8. Known audit alerts at entry

The audit begins with the following non-scientific consistency alerts:

A10-001:
CLAIMS_TABLE contains historical placeholder rows C001-C003 followed by later substantive reuse of the same identifiers.

A10-002:
Some historical next-step statements are stale relative to the final v0.2.1 state.

A10-003:
DEMO_CLAIM_MAP still lists DMO-007 as under construction.

These alerts do not invalidate scientific results.

They are retained because an adversarial audit must distinguish documentation debt from scientific failure.

---

## 9. Experimental freeze

PHASE 10 does not authorize:

- recalibration;
- new seeds;
- new parameter sweeps;
- new candidate selection;
- threshold changes;
- new phenomenological experiments.

If an adversarial objection requires new data, the result must be recorded as an open question for a later version.

It must not be repaired retrospectively inside v0.2.1.

---

## 10. External comparison rule

External literature will be used to determine:

- prior existence of equivalent mathematics;
- standard terminology;
- known stronger theorems;
- methodological precedents;
- differences that may constitute genuine MADELEINE contributions.

Similarity to prior work is not treated as failure.

It changes the novelty classification.

---

## 11. Success condition for PHASE 10

PHASE 10 succeeds even if claims fail.

The audit succeeds when every priority claim has:

- an exact scope;
- an evidence class;
- an adversarial test;
- a literature comparison;
- a novelty assessment;
- a final verdict;
- an explicit residual limitation.

The objective is not to maximize the number of PASS results.

The objective is to identify the strongest statements that remain true after hostile scrutiny.

---

## 12. Preservation rule

The frozen release:

v0.2.1

and its commit:

fee2c31cfa17159a4075e1cbfbfa7e2fceba9c4b

must remain unchanged.

All PHASE 10 documents belong to post-publication main or a later development version.

Any scientific modification resulting from this audit requires a new version.
