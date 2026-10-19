# MADELEINE — PHASE 10 — LAB-D1 ADVERSARIAL RESULT v1

## Target

Experiment:

LAB-D1-v1

Role:

positive deterministic second-order control

Frozen scientific target:

v0.2.1

Frozen release commit:

fee2c31cfa17159a4075e1cbfbfa7e2fceba9c4b

Evidence classes:

C — Computational

M — Methodological

---

## 1. Audit scope

LAB-D1 is not canonical D1.

It is the positive historical control of LAB-FEN-001-v1.

Its immediate purpose is to test whether the same historical detector used in LAB-D0 responds positively when second-order dependence is explicitly introduced into the generator.

LAB-D1 is also deliberately rigid and periodic.

It is not the target phenomenology.

---

## 2. Frozen provenance

Repository history records:

LAB-D1 specification:

709f24959d7c207609bc4490a5d86fe8f965f16c

LAB-D1 executable:

24a45176e5fea89f8ede94e3724746f00e4ae435

LAB-D1 result:

41dfb0a0f92e91265152a7b75863aac33c3973d0

Therefore:

specification
->
executable
->
result

appears in the correct frozen order.

SURVIVES.

This supports procedural provenance.

It does not establish that the control is representative of all second-order processes.

---

## 3. Structural second-order dependence

LAB-D1 defines:

x_(t+1)
=
F(x_(t-1),x_t).

The transition table contains all:

5^2 = 25

ordered contexts.

For every current state:

x_t=b,

different previous states generate different successors.

The executable verifies that each present state has:

5

distinct successors across the five possible previous states.

Therefore the present state alone does not determine the next state.

The previous state is structurally required by the declared generator.

SURVIVES.

---

## 4. Determinism and period

For each ordered pair:

(prev,current)

there is exactly one successor.

Thus the second-order rule is deterministic.

The frozen context cycle contains:

25

distinct ordered pairs and has minimal declared period:

25.

The useful trajectory, training segment and test segment all contain integer numbers of full periods.

Therefore the control is exactly periodic under its declared construction.

SURVIVES.

---

## 5. Truth by construction versus detector evidence

The statement:

LAB-D1 contains second-order dependence

is true from direct inspection of the generator.

Delta_hist and C_hist do not discover that structural fact.

Their role is instead:

given data from a known strong second-order process, does the detector recognize the implanted dependence?

This distinction is essential.

LAB-D1 is a positive detector control.

It is not evidence that historical dependence emerged spontaneously.

---

## 6. Delta_hist result

Across the eight declared seeds:

Delta_hist > p95(null)

occurred:

8/8.

Also:

Delta_hist > 0

occurred:

8/8.

The observed value is the same in every seed:

approximately:

1.606666.

Therefore the second-order predictor strongly outperforms the first-order predictor on this constructed control.

SURVIVES.

---

## 7. C_hist result

Across the eight declared seeds:

C_hist > p95(null)

occurred:

8/8.

The observed C_hist value is identical across seeds:

approximately:

0.797232.

The null p95 values are much smaller.

Therefore the fitted second-order conditional distributions are strongly separated from the corresponding first-order distributions in this control.

SURVIVES.

---

## 8. Why the separation is expected to be extreme

The construction deliberately maximizes the relevance of the previous state.

For every fixed present state:

the five possible previous states produce the five possible successors.

Thus conditioning only on the present mixes together five successor outcomes.

Conditioning on:

(previous,present)

identifies the successor deterministically.

Consequently LAB-D1 is an especially strong positive second-order control.

This makes it useful for detecting gross false negatives.

It does not establish sensitivity to weak second-order structure.

---

## 9. Seed structure

The eight seeds do not generate eight independent stochastic dynamics.

Each seed selects only an initial phase of the same deterministic period-25 cycle.

After phase selection there is no stochastic transition choice.

The transition law is identical.

The orbit structure is identical.

The empirical full-cycle distribution is identical.

Therefore the eight seeds are phase-shifted realizations of one deterministic construction.

---

## 10. Full-cycle cuts remove most phase variability

The frozen lengths satisfy:

30000 / 25 = 1200,

18000 / 25 = 720,

12000 / 25 = 480.

Thus:

the useful segment,
the training segment,
and the test segment

all contain exact integer numbers of complete cycles.

This means phase choice does not alter the empirical context frequencies over those complete segments.

This explains why the observed:

Delta_hist

and:

C_hist

are exactly identical across all eight seeds.

---

## 11. Consequence for the 8/8 interpretation

The observed:

8/8

agreement is real as a repository result.

However it must not be interpreted as eight independent confirmations.

The seeds are not eight distinct model classes.

They are not eight independent laboratories.

They are not eight independent stochastic transition realizations.

They are phase choices of the same deterministic periodic orbit.

Therefore:

8/8

means phase-robustness of this particular construction.

It does not mean eight independent replications of the scientific claim.

---

## 12. Consequence for the 7/8 binomial argument

The specification records:

P(X >= 7 | n=8,p=0.5)
=
9/256
approximately 0.0352.

That calculation is mathematically correct for eight independent Bernoulli trials under p=0.5.

However LAB-D1 seed outcomes do not satisfy the ordinary interpretation of eight independent Bernoulli trials.

Because the eight trajectories are deterministic phase shifts of the same cycle, the statistical independence required for that inferential interpretation is absent.

Therefore the rule:

at least 7/8

remains a frozen operational consistency gate.

But the numerical sign-test probability should not be interpreted as a valid p-value for LAB-D1 phase replicates.

Verdict:

NOT JUSTIFIED as an inferential significance claim for this control.

---

## 13. Positive-control difficulty

A detector may perform well on an extremely separated positive control while failing on weaker alternatives.

LAB-D1 contains:

complete second-order context coverage,

deterministic successor selection,

maximal differentiation of successor by previous state,

long trajectories,

and exact repeated cycles.

The present audit therefore establishes detector response to a strong positive case.

It does not establish a power curve.

It does not establish the minimum detectable historical dependence.

It does not establish robustness under noise.

---

## 14. Conditional null

The historical null permutes previous states within groups sharing the same present state.

The current-next empirical relation is therefore retained while the extra association between:

previous

and:

next

conditional on current

is broken.

This is conceptually aligned with the detector target.

As already noted in the LAB-D0 adversarial audit, the examples arise from overlapping serial triples.

The permutation output need not correspond to one dynamically consistent trajectory.

Therefore the null remains an operational LAB-FEN-001 null.

General exact finite-sample inferential validity remains:

UNDERDETERMINED.

---

## 15. The null does what is needed operationally here

For this strong constructed second-order control, the permutation null removes the decisive previous-next association.

Observed Delta_hist and C_hist remain far above their null p95 values.

Therefore the null is sufficient to demonstrate strong separation inside this frozen example.

SURVIVES_WITH_RESTRICTION.

This should not be generalized automatically to arbitrary serial processes.

---

## 16. Later A1 calibration

The later metric calibration reports for LAB-D1:

I2 approximately ln(5)

and:

A1 approximately 1.605

for all seeds.

This is consistent with the generator.

Given the present state alone, the successor remains distributed across the five possibilities.

Given the previous-present pair, the successor is determined.

Thus the strong conditional-information signal is primarily a designed property of the control.

It is not an emergent discovery.

---

## 17. Later persistence calibration

The later calibration reports:

P_rel = 1

for LAB-D1.

Because the trajectory is an exact repeated period-25 cycle and the analysis windows contain repeated copies of the same pattern, within-trajectory window variation collapses to the limiting rigid case.

This is appropriate for a rigidity control.

It is not evidence of flexible persistence.

---

## 18. Later novelty calibration

The later calibration reports:

N = 0.2.

The frozen cycle visits only a restricted set of trigram histories relative to the 125 possible trigram states.

Thus the reduced novelty score is consistent with deliberate crystallization.

Again this is a designed endpoint of the calibration.

---

## 19. Later aperiodicity calibration

The later metric layer reports:

U = 0

and:

p* = 25

for every seed.

This is exactly what the frozen period-25 construction should produce.

Therefore U recognizes the deliberately implanted periodicity.

SURVIVES.

This does not by itself establish sensitivity to weak, intermittent or very long periodic components.

---

## 20. Calibration endpoint issue

LAB-D0 and LAB-D1 later define the two calibration endpoints from which:

T_P,
T_N,
T_U

are constructed.

This is procedurally valid under the frozen protocol.

However the threshold values are partly consequences of the chosen endpoint controls.

In particular LAB-D1 is intentionally extreme:

rigid,
deterministic,
periodic,
historically maximally separated.

Therefore midpoint thresholds between D0 and D1 should be interpreted as:

internal operational decision boundaries.

They are not independently estimated universal phase boundaries.

---

## 21. Reuse of calibration evidence

Once D0 and D1 are used to derive the D2 thresholds, their separation cannot also be counted as independent validation of those same thresholds.

The same evidence cannot simultaneously serve as:

training/calibration data

and:

independent validation data

without qualification.

Independent validation would require evidence not used to construct the thresholds.

---

## 22. Causal language

Inside the synthetic generator, the previous state is mechanically used to determine the next state.

Therefore it is legitimate to say:

the generator contains a direct historical dependency by construction.

However LAB-D1 does not establish:

emergent memory,

physical memory,

natural historical causality,

or a novel causal principle.

Those stronger interpretations do not follow from a deliberately coded second-order rule.

---

## 23. History is not aperiodicity

LAB-D1 is a useful counterexample to the implication:

historical dependence
->
aperiodicity.

It has strong second-order dependence and exact periodicity.

Therefore, within the constructed domain:

history alone does not imply aperiodic dynamics.

SURVIVES.

This is conceptually useful but mathematically unsurprising.

---

## 24. Instrument inheritance

LAB-D1 imports the instrumental layer from:

LAB-FEN-001_D0.py.

Within frozen tag v0.2.1 this dependency is stable because the entire repository state is frozen.

However the import is file-based rather than content-hash-pinned inside the executable itself.

A future version could strengthen reproducibility by recording and checking the expected source hash of the inherited instrument.

This is a provenance-hardening issue, not a failure of the frozen release.

---

## 25. Strongest justified statement

The strongest justified statement is:

Under the frozen LAB-D1-v1 deterministic period-25 second-order generator, the historical detector strongly recognizes the explicitly implanted dependence on the previous state. Delta_hist and C_hist exceed their operational null references for every declared phase seed. This establishes LAB-D1 as a strong positive control of the LAB-FEN-001 historical detector, not as evidence of emergent or externally validated memory.

---

## 26. Statements not justified

LAB-D1 does not establish that:

- eight seeds are eight independent replications;
- the 7/8 binomial probability is a valid inferential p-value for these phase seeds;
- every second-order process is detectable;
- weak historical dependencies are detectable;
- noisy second-order dependencies are detectable;
- Delta_hist has known general statistical power;
- C_hist has known general statistical power;
- the conditional permutation null has universal exact validity;
- strong historical detection demonstrates emergent memory;
- strong historical detection demonstrates physical causality;
- period-25 behavior is itself scientifically novel;
- the D0/D1-derived thresholds are universal boundaries.

---

## 27. Novelty assessment

Deterministic second-order finite-state rule:

STANDARD_OR_DERIVATIVE.

de Bruijn-type full context cycle:

STANDARD_OR_DERIVATIVE.

Out-of-sample first-order versus second-order prediction:

STANDARD_OR_DERIVATIVE.

Positive synthetic control:

STANDARD_OR_DERIVATIVE.

Specific integration into LAB-FEN-001:

SYSTEM-SPECIFIC.

Scientific novelty of isolated LAB-D1:

NOT ESTABLISHED.

---

## 28. Final adversarial verdict

Frozen provenance:

SURVIVES.

Structural second-order dependence:

SURVIVES.

Context coverage 25/25:

SURVIVES.

Period-25 rigidity:

SURVIVES.

Observed 8/8 detector hits:

SURVIVES.

LAB-D1 as a strong positive control:

SURVIVES_WITH_RESTRICTION.

Interpretation of eight seeds as independent replications:

NOT JUSTIFIED.

Inferential interpretation of the 7/8 binomial calculation:

NOT JUSTIFIED for this deterministic phase ensemble.

General sensitivity to arbitrary second-order dependence:

NOT ESTABLISHED.

Emergent-memory interpretation:

NOT ESTABLISHED.

External physical interpretation:

EXTERNAL_VALIDATION_REQUIRED.

---

## 29. Residual issues

R10-LABD1-01:

Describe the eight seeds as phase robustness for LAB-D1, not eight independent stochastic replications.

R10-LABD1-02:

Do not use the 9/256 sign-test quantity as an inferential p-value for the deterministic phase ensemble.

R10-LABD1-03:

Treat LAB-D1 as a strong positive endpoint, not as evidence of detector sensitivity near the boundary of second-order dependence.

R10-LABD1-04:

Keep the distinction between implanted historical dependence and emergent memory explicit.

R10-LABD1-05:

Keep D0/D1 calibration evidence separate from independent validation evidence.

R10-LABD1-06:

A future scientific version may evaluate graded, noisy and partial second-order alternatives to estimate detector sensitivity.

R10-LABD1-07:

A future executable may pin the hash of the inherited D0 instrumental implementation.

---

## 30. Preservation

This audit result is post-publication.

It does not modify:

v0.2.1

or its frozen commit:

fee2c31cfa17159a4075e1cbfbfa7e2fceba9c4b.

No new experiment was executed.

No metric was recalibrated.

Any sensitivity study, alternative positive control or revised inferential procedure belongs to a future scientific version.
