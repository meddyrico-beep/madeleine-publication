# MADELEINE — PHASE 10 — DMO-004 ADVERSARIAL RESULT v1

## Target

Claim:

C020

Demo:

DMO-004

Associated laboratory audit:

LAB-D2-DMO004-AUDIT-v1

Frozen scientific target:

v0.2.1

Commit:

fee2c31cfa17159a4075e1cbfbfa7e2fceba9c4b

Evidence classes:

M — Methodological

C — Computational

---

## 1. Audit distinction

DMO-004 contains two logically different layers.

Layer A:

the abstract Boolean gate.

Layer B:

the application of that gate to previously frozen LAB-FEN-001 evidence.

These layers must not be conflated.

The first tests implementation of a declared decision rule.

The second asks whether LAB-D2 satisfies that declared rule.

---

## 2. Boolean gate

The declared rule is:

G(R) =
R_region
AND
R_seeds
AND
R_nulls
AND
R_failure
AND
R_non_reducible
AND
R_frozen
AND
R_trace.

Acceptance occurs if and only if all seven Boolean criteria are true.

This rule is internally unambiguous.

SURVIVES.

---

## 3. Exhaustive 128-state sweep

Seven Boolean inputs produce:

2^7 = 128

possible configurations.

Because acceptance is defined as conjunction of all seven criteria, exactly one configuration must be accepted:

(True,True,True,True,True,True,True).

The implementation reports:

1 accepted,
127 rejected.

This confirms that the program implements the declared conjunction correctly.

SURVIVES.

However, this result is logically implied by the gate definition.

It is therefore an implementation verification.

It is not independent evidence that the seven substantive criteria are scientifically necessary.

---

## 4. Clause-ablation audit

DMO-004 disables each criterion individually.

Every single-clause ablation changes the output from:

ACCEPTED_AS_REGIME

to:

NOT_ACCEPTED_AS_REGIME.

This establishes that no input is ignored by the implementation.

It does not establish that each criterion is independently necessary for a universal scientific concept of regime.

The demonstrated necessity is:

necessity relative to the declared decision rule.

It is not:

epistemic necessity,
physical necessity,
or universal methodological necessity.

---

## 5. Application to LAB-D2

LAB-D2-DMO004-AUDIT-v1 does not merely hard-code seven True values.

It consumes frozen artifacts from:

LAB-D0,
LAB-D1,
LAB-D2,
ABLATIONS-v1,
ATLAS-v1,

and repository provenance.

The audit evaluates:

region_parametric,
seed_agreement,
null_separation,
explicit_failure_criterion,
non_reducible,
frozen_rule,
complete_trace.

The recorded result is:

7/7 PASS.

Within the declared contract this result is reproducible and internally valid.

SURVIVES_WITH_RESTRICTION.

---

## 6. REGION_PARAMETRIC

The region criterion consumes the predeclared 3x3 core of ATLAS-v1.

Required result:

9/9 POINT PASS.

Observed result:

9/9 POINT PASS.

The basal point is included.

The core was specified before its result.

Therefore the statement:

LAB-D2 is not an isolated PASS point inside the declared local perturbation core

is supported.

SURVIVES.

This does not locate an external boundary and does not establish global robustness.

---

## 7. SEED_AGREEMENT

A POINT PASS already requires:

at least 7/8 seed passes.

The DMO-004 seed criterion separately checks that every core point satisfies at least:

7/8.

Observed:

8/8

throughout the tested core.

SURVIVES.

However, this criterion is not evidentially independent of REGION_PARAMETRIC because POINT PASS itself already contains the seed threshold.

Therefore:

REGION_PARAMETRIC PASS

and:

SEED_AGREEMENT PASS

must not be interpreted as two statistically independent confirmations.

---

## 8. NULL_SEPARATION

The per-seed LAB-D2 gate already contains:

A1 > 0,
Delta_hist > 0,
Delta hit,
C_hist > 0,
C hit,

together with the other frozen thresholds.

The DMO-004 audit checks those historical-separation conditions again on the seed records contributing to PASS.

SURVIVES.

This provides an explicit audit trail.

But it also means NULL_SEPARATION shares evidence with the seed-level and point-level gates.

It is not an independent replicate of the experiment.

---

## 9. Dependence among criteria

The seven DMO-004 criteria are conceptually distinct requirements.

They are not seven independent random experiments.

In particular:

REGION_PARAMETRIC,
SEED_AGREEMENT,
and
NULL_SEPARATION

partly reuse the same atlas and seed-level evidence.

Likewise:

EXPLICIT_FAILURE_CRITERION,
FROZEN_RULE,
and
COMPLETE_TRACE

all use aspects of experimental provenance and repository history, although they test different procedural properties.

Therefore:

7/7 PASS

means:

all seven declared requirements are satisfied.

It does not mean:

seven independent confirmations,
seven independent likelihood factors,
or seven statistically independent pieces of evidence.

---

## 10. EXPLICIT_FAILURE_CRITERION

The audit verifies that failure-producing rules existed before the relevant results.

These include:

thresholds,
7/8 seed gates,
ablation failure criteria,
POINT FAIL,
and the 9/9 regional gate.

This materially limits retrospective redefinition of success.

SURVIVES.

Its importance is methodological rather than theorem-like.

---

## 11. FROZEN_RULE

The audit uses Git history to verify ordering between:

specifications,
executables,
and results.

Within the repository history inspected by the auditor, relevant rules precede their corresponding results.

SURVIVES.

This supports procedural integrity.

It does not prove that every scientific design choice was optimal.

---

## 12. COMPLETE_TRACE

The auditor checks:

required files,
shared seed contracts,
shared lengths,
embedded SHA256 values,
result hashes,
artifact presence,
commit presence,
and repository cleanliness before audit output.

This is substantial provenance evidence for internal reproducibility.

SURVIVES.

It does not constitute an independent reproduction by another research group.

---

## 13. NON_REDUCIBLE

This criterion has deliberately restricted scope.

The frozen claim is not:

UNIVERSALLY IRREDUCIBLE.

It is:

NO REDUCIBLE A LOS LIMITES INTERNOS ENSAYADOS EN LAB-FEN-001-v1.

The supporting controls include:

LAB-D0,
LAB-D1,
NO_PAST,
RANDOMIZED_PAST,
DETERMINISTIC_CHOICE.

Observed ablation outcomes include:

NO_PAST:
0/8 complete passes.

RANDOMIZED_PAST:
0/8 complete passes.

DETERMINISTIC_CHOICE:
0/8 complete passes,

with U <= T_U in 8/8.

Within this control set, the restricted statement survives.

SURVIVES_WITH_RESTRICTION.

The experiment does not establish uniqueness of LAB-D2 or exclude all simpler alternative mechanisms.

---

## 14. Scientific force of the gate

DMO-004 does not create the upstream evidence.

Its scientific function is to control promotion.

The evidence comes from:

controls,
metrics,
ablations,
atlas,
frozen protocols,
and preserved traces.

DMO-004 asks whether that evidence satisfies a predeclared admission contract.

Therefore the strongest interpretation is:

evidence
->
predeclared checks
->
internal admission label.

Not:

gate PASS
->
external truth.

---

## 15. External methodological positioning

Pre-specifying methods and decision criteria before outcomes are known is an established methodological principle associated with preregistration and Registered Reports.

Those practices aim to distinguish confirmatory from exploratory analysis and reduce opportunities for outcome-driven changes or selective reporting.

DMO-004 shares this general methodological logic.

Therefore predeclaration, freezing and explicit failure criteria are not claimed as novel methodological inventions of MADELEINE.

MADELEINE's specific integration of these ideas into its internal regime-admission architecture may be system-specific.

That system-level contribution is distinct from claiming invention of preregistration or reproducibility methodology.

---

## 16. Important distinction from external preregistration

The MADELEINE protocols were internally frozen before their relevant executions.

However, DMO-004 was not independently peer-reviewed before results in the manner of a formal external Registered Report.

Therefore the correct description is:

internally preregistered/frozen procedural structure.

It should not be represented as equivalent to independent pre-study peer review.

---

## 17. Status of the regime label

The label:

REGIMEN INTERNO ADMITIDO BAJO LAB-FEN-001-v1 Y DMO-004

is legitimate as a defined internal status.

Its meaning is exactly:

the candidate satisfied the frozen internal admission contract.

The word "regime" must travel with this qualification.

Without the qualification, readers could incorrectly interpret the label as:

physical regime,
natural regime,
universal dynamical regime,
or independently validated phenomenon.

Those stronger readings are not justified.

---

## 18. Strongest justified statement

The strongest statement supported by DMO-004 is:

LAB-D2 satisfies all seven requirements of the predeclared DMO-004 internal admission contract, using the frozen evidence preserved in LAB-FEN-001-v1.

This supports the internal label:

REGIMEN INTERNO ADMITIDO BAJO LAB-FEN-001-v1 Y DMO-004.

---

## 19. Statements not justified

DMO-004 does not establish that:

- the seven criteria are universal axioms of scientific validity;
- the seven criteria are statistically independent;
- 7/7 represents seven independent confirmations;
- LAB-D2 is the unique mechanism producing the observed signature;
- all simpler mechanisms have been excluded;
- the admitted regime is physically real;
- the admitted regime occurs in natural data;
- the gate validates the metrics themselves;
- internal admission implies external validation.

---

## 20. Novelty assessment

Boolean conjunction gate:

STANDARD_OR_DERIVATIVE.

Exhaustive Boolean sweep:

implementation verification,
not theorem-level novelty.

Predeclaration and freezing principles:

STANDARD_OR_DERIVATIVE as general methodology.

Traceability integration:

methodologically useful but not independently novel on current evidence.

Specific MADELEINE admission architecture:

SYSTEM-SPECIFIC,
with broader novelty still to be assessed.

---

## 21. Final adversarial verdict

Gate implementation:

SURVIVES.

Application to frozen LAB-D2 evidence:

SURVIVES_WITH_RESTRICTION.

Evidence classes:

M — Methodological.
C — Computational.

Novelty of the isolated methodology:

STANDARD_OR_DERIVATIVE.

Interpretation of 7/7 as independent evidence:

NOT JUSTIFIED.

Internal regime label:

SURVIVES_WITH_RESTRICTION.

External physical interpretation:

EXTERNAL_VALIDATION_REQUIRED.

---

## 22. Residual issues

R10-DMO004-01:

Future documentation should explicitly state that 7/7 means satisfaction of seven requirements, not seven independent confirmations.

R10-DMO004-02:

The phrase "no clause is redundant" should be understood as non-redundancy in the Boolean decision rule, not as proof of independent scientific necessity.

R10-DMO004-03:

Keep the restricted wording:

NO REDUCIBLE A LOS LIMITES INTERNOS ENSAYADOS EN LAB-FEN-001-v1.

Do not shorten it to universal irreducibility.

R10-DMO004-04:

A later phase should test alternative mechanism families capable of producing the same accepted signature.

R10-DMO004-05:

Independent reproduction or external application remains required before treating the regime label as evidence beyond the MADELEINE laboratory.

---

## 23. Preservation

This audit result is post-publication.

It does not modify:

v0.2.1

or its frozen commit:

fee2c31cfa17159a4075e1cbfbfa7e2fceba9c4b.

Any scientific wording or methodological change resulting from this audit belongs to a later version.
