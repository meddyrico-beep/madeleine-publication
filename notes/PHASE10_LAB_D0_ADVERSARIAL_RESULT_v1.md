# MADELEINE — PHASE 10 — LAB-D0 ADVERSARIAL RESULT v1

## Target

Experiment:

LAB-D0-v1

Role:

negative first-order causal control

Frozen scientific target:

v0.2.1

Frozen release commit:

fee2c31cfa17159a4075e1cbfbfa7e2fceba9c4b

Evidence classes:

C — Computational

M — Methodological

---

## 1. Audit scope

LAB-D0 is not canonical D0.

It is the negative laboratory control of LAB-FEN-001-v1.

Its purpose is to test whether the historical detection block produces a robust false positive on a process whose next-state law is explicitly first order.

The relevant quantities are:

Delta_hist

and:

C_hist.

Later metric calibration also evaluates LAB-D0 with A1, P_rel, N and U, but the original LAB-D0 gate concerns the historical block.

---

## 2. Frozen provenance

Repository history records the following order:

LAB-D0 specification:

1f9f11056c48164229178077164c35e172b68b24

LAB-D0 executable:

d4e6a91d39ba6260e14ebe34d3733b31d88ecae9

LAB-D0 result:

0910669c6eac16e51ff16768220a13f15ff86407

Therefore the specification precedes the executable and the executable precedes the recorded result.

This ordering supports the claim that the declared rule was frozen before the result.

SURVIVES.

This is provenance evidence.

It is not evidence that the chosen experimental design is optimal.

---

## 3. Structural null

The frozen generator implements:

x_t -> x_(t+1)

with transition probabilities determined solely by the current state.

The executable function is:

sample_next(current, rng)

and does not receive x_(t-1).

Therefore the generative law satisfies, by construction:

P(x_(t+1) | x_t,x_(t-1))
=
P(x_(t+1) | x_t).

The structural Markov-1 property of LAB-D0 survives direct code inspection.

SURVIVES.

---

## 4. Important distinction: truth by construction versus detector evidence

The statement:

LAB-D0 is first order

is true because of how the generator was constructed.

It is not discovered by Delta_hist or C_hist.

The scientific role of the metrics is different:

given data generated from that known first-order process, do the instruments incorrectly report robust second-order history?

Therefore LAB-D0 is a detector sanity check.

It is not evidence for the existence of historical structure.

---

## 5. Delta_hist result

Across the eight frozen seeds:

Delta_hist > p95(null)

occurred:

0/8.

Also:

Delta_hist > 0

occurred:

0/8.

All observed Delta_hist values were negative.

Therefore the second-order predictor did not improve out-of-sample prediction relative to the first-order predictor in any of the eight realizations.

SURVIVES.

The negative sign is compatible with additional estimation complexity in M2 without useful historical information.

It should not be promoted to a universal theorem about overfitting.

---

## 6. C_hist result

Across the eight frozen seeds:

C_hist > p95(null)

occurred:

0/8.

C_hist itself remained positive because the empirically fitted M1 and M2 distributions are not expected to coincide exactly at finite sample size.

The use of a null reference therefore prevents:

C_hist > 0

from being interpreted automatically as historical dependence.

Within this control:

SURVIVES.

---

## 7. Frozen gate

LAB-D0 requires:

Delta hits <= 1/8,

C_hist hits <= 1/8,

no consistent historical signal across seeds,

and confirmation that the generator is first order.

Observed:

Delta hits = 0/8,

C_hist hits = 0/8,

consistent Delta signal = NO,

consistent C_hist signal = NO,

generator uses previous state = NO.

Therefore the frozen gate returns:

LAB-D0-v1 PASS.

SURVIVES.

---

## 8. Non-independence of gate clauses

The four LAB-D0 gate clauses should not be interpreted as four independent confirmations.

In particular:

generator does not use x_(t-1)

is a structural property of the code known by construction.

The Delta_hist and C_hist clauses are detector outputs from the same generated trajectories.

The cross-seed consistency clause is also derived from those same metric outcomes.

Therefore the gate combines:

implementation verification

and:

statistical diagnostic evidence.

It does not contain four independent experiments.

---

## 9. Scope of the negative control

LAB-D0 tests one specific first-order family.

Its frozen configuration contains:

5 states,

a fixed circulant transition rule,

8 seeds,

1000 burn-in steps,

30000 useful transitions per seed,

18000 training transitions,

12000 test transitions,

Dirichlet smoothing alpha = 0.5,

64 conditional null permutations.

This is a legitimate negative control.

It is not an exhaustive test of the class of all first-order processes.

---

## 10. Friendly-control limitation

The LAB-D0 transition kernel has broad support and a large sample relative to its five-state alphabet.

Therefore state and transition contexts are comparatively well populated.

The audit has not shown that the same false-positive behavior persists for first-order processes that are:

sparse,

strongly imbalanced,

nearly deterministic,

metastable,

larger-alphabet,

or poorly sampled.

Thus:

"LAB-D0-v1 did not trigger falsely"

SURVIVES.

But:

"Delta_hist and C_hist are calibrated for arbitrary Markov-1 systems"

is NOT ESTABLISHED.

---

## 11. Conditional permutation null

For the historical null, x_(t-1) is permuted among observations sharing the same x_t.

This preserves the observed present-state grouping while breaking association between:

x_(t-1)

and:

x_(t+1)

conditional on x_t.

Conceptually this targets the intended null relation.

However the input examples come from overlapping triples in a serial trajectory.

They are therefore not ordinary independent observations.

After permutation, the collection of triples need not itself correspond to one dynamically consistent Markov trajectory.

Consequently the permutation distribution is an operational conditional null for LAB-FEN-001-v1.

The current evidence does not establish that it is an exact finite-sample permutation test with universally controlled type-I error.

Verdict:

UNDERDETERMINED as a general inferential guarantee.

---

## 12. What 0/8 establishes

The observed:

0/8 Delta hits

and:

0/8 C_hist hits

are stronger than the maximum allowed by the frozen gate.

They establish that no gross false historical signal appeared in these eight realizations.

They do not estimate a universal false-positive rate with high precision.

Eight realizations are insufficient to characterize the full tail behavior of the detector across the class of possible first-order generators.

---

## 13. Seed interpretation

The eight seeds provide repeated realizations of the same stochastic architecture.

They are useful for testing whether the result depends on one random realization.

They are not:

eight different physical systems,

eight independent external laboratories,

or eight different model classes.

Therefore cross-seed agreement is internal reproducibility evidence.

It is not external replication.

---

## 14. Calibration versus validation

LAB-D0 is subsequently reused, together with LAB-D1, to calibrate:

T_P,
T_N,
T_U

for LAB-D2.

This is methodologically legitimate under the frozen protocol.

However it means LAB-D0 and LAB-D1 are calibration controls for those thresholds.

Their successful separation should not later be counted again as independent validation of the thresholds that were derived from them.

A later independent test set would be needed for independent calibration validation.

---

## 15. Metric-layer consequence

The later METRICS-v1 calibration reports for LAB-D0:

A1 positive:

0/8,

relatively high N,

high U,

and low P_rel relative to LAB-D1.

This is consistent with the intended D0 control role.

However those additional values were used as part of the D0/D1 calibration that generated the D2 thresholds.

They therefore remain calibration evidence rather than external validation.

---

## 16. Causal language

Because the data generator is known exactly, the absence of second-order dependence in LAB-D0 is structurally guaranteed.

Thus statements about the control itself may use causal-generator language internally.

But the fact that the detector behaves correctly on this synthetic generator does not imply that a positive detector value on an unknown external process identifies physical causality.

The inference:

metric positive
->
physical historical cause

is not established by LAB-D0.

---

## 17. Strongest justified statement

The strongest justified statement is:

Under the frozen LAB-D0-v1 first-order generator, the predeclared historical detector produced no robust false positive across the eight frozen realizations: Delta_hist and C_hist generated zero p95 hits, and the second-order predictor did not improve out-of-sample loss in any seed. This supports the use of LAB-D0 as the specific negative control of LAB-FEN-001-v1.

---

## 18. Statements not justified

LAB-D0 does not establish that:

- Delta_hist is universally calibrated for every Markov-1 process;
- C_hist is universally calibrated for every Markov-1 process;
- the conditional permutation p95 has exact universal type-I error control;
- eight seeds determine the detector's full false-positive distribution;
- all first-order generators would pass the same gate;
- the metrics identify physical causality;
- a future positive LAB-D1 or LAB-D2 result must represent irreducible history;
- the D0/D1-derived thresholds are independently validated by the same controls used to construct them.

---

## 19. Novelty assessment

Use of a negative synthetic control:

STANDARD_OR_DERIVATIVE.

Out-of-sample comparison of first- and second-order predictors:

STANDARD_OR_DERIVATIVE.

Conditional permutation as a null-building strategy:

STANDARD_OR_DERIVATIVE in general methodological character.

Specific frozen integration into LAB-FEN-001:

SYSTEM-SPECIFIC.

Scientific novelty of the isolated LAB-D0 control:

NOT ESTABLISHED.

---

## 20. Final adversarial verdict

Structural Markov-1 property:

SURVIVES.

Freeze ordering:

SURVIVES.

Observed 0/8 historical hits:

SURVIVES.

LAB-D0 as the declared negative control:

SURVIVES_WITH_RESTRICTION.

General calibration of Delta_hist and C_hist over arbitrary first-order systems:

NOT ESTABLISHED.

Exact inferential validity of the serial conditional-permutation null:

UNDERDETERMINED.

Internal reproducibility:

SUPPORTED.

External validation:

NOT ESTABLISHED.

---

## 21. Residual issues

R10-LABD0-01:

Do not convert successful performance on one frozen Markov-1 kernel into universal calibration of the detector.

R10-LABD0-02:

Treat the generator-control clause as implementation verification rather than independent statistical evidence.

R10-LABD0-03:

A future version may test a deliberately heterogeneous family of first-order null generators, including sparse and near-deterministic cases.

R10-LABD0-04:

If exact inferential claims are desired, justify the conditional permutation procedure under serially dependent overlapping triples or replace it with a null procedure whose sampling validity is explicitly established.

R10-LABD0-05:

Keep calibration controls separate from later independent validation evidence.

R10-LABD0-06:

Do not infer external physical causality from successful synthetic-control behavior.

---

## 22. Preservation

This audit result is post-publication.

It does not modify:

v0.2.1

or its frozen commit:

fee2c31cfa17159a4075e1cbfbfa7e2fceba9c4b.

No new experiment was executed.

Any new null family, new seed family, recalibration or metric change belongs to a future scientific version.
