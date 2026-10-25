# MADELEINE - Phase 10 DMO-004 Targeted Prior-Art Comparison v1

## 0. Provenance and status

POST-PUBLICATION TARGETED METHODOLOGICAL COMPARISON

Date: 2026-10-26

Reference main:
08f67831c13c01ecd705bc28f30d790d958a89cc

Frozen release:
v0.2.1

Frozen release commit:
fee2c31cfa17159a4075e1cbfbfa7e2fceba9c4b

Target:
DMO-004

Claim:
C020

Evidence classes:
M - Methodological.
C - Computational.

CORRECT != NOVEL != GENERAL != EXTERNALLY VALIDATED

No new experiment.
No recalibration.
No alteration of frozen evidence.

## 1. Exact decision rule

The DMO-004 Boolean admission gate is:

G(R) =
R_region
AND R_seeds
AND R_nulls
AND R_failure
AND R_non_reducible
AND R_frozen
AND R_trace.

The gate accepts a candidate
only when all seven clauses
are true.

This is an internally
unambiguous conjunction.

Its implementation survives
the frozen DMO-004 audit.

## 2. Exhaustive finite truth table

There are seven Boolean inputs.

The total number of
input combinations is:

2^7 = 128.

Exactly one assignment
makes the conjunction true.

The reported frozen sweep has:

1 accepted;
127 rejected.

This is correct behavior
for the declared gate.

VERDICT:
BOOLEAN IMPLEMENTATION SURVIVES.

It establishes the behavior
of the decision implementation.

It does not establish that
all seven chosen scientific
criteria are universally necessary.

## 3. Single-clause ablation

Begin with seven true clauses.

Set exactly one clause to false.

The result changes from
accepted to rejected.

Repeat for each of
the seven clauses.

The frozen audit reports
this behavior.

It demonstrates that each
input is operative in the
declared Boolean rule.

It does not prove each
clause is an independently
necessary law of science.

## 4. External comparator A: MC/DC

Source:
NASA Software Engineering Handbook.

Title:
7.21 - Multi-condition Software Requirements.

URL:
https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695692/7.21%2B-%2BMulti-condition%2BSoftware%2BRequirements

Relevant established method:

Modified Condition/Decision
Coverage, MC/DC, requires
showing that individual
Boolean conditions can affect
the overall decision outcome
when other conditions
are appropriately controlled.

For an unmodified seven-input
conjunction, the all-true
assignment and seven
single-false assignments
are an elementary set of
condition-effect witnesses.

DMO-004's full 128-state
truth-table sweep is
exhaustive at the abstract
Boolean-input level.

The conceptual similarity is:

verification of decision
logic and individual
condition influence.

NOT ESTABLISHED:

that the complete
DMO-004 executable meets
a formal safety-critical
MC/DC certification standard;

that scientific input
criteria are statistically
independent;

that passing software
logic tests establishes
external scientific truth.

## 5. External comparator B: preregistration

Source:
Center for Open Science.

Title:
Preregistration.

URL:
https://www.cos.io/initiatives/prereg

Relevant established method:

A research plan is specified
before the relevant study
or analysis and submitted
to a registry.

This separates planned work
from exploratory decisions.

DMO-004 shares the
general methodological goal
of predeclaring success
and failure criteria.

MADELEINE's checked repository
history supports internal
ordering of declared rules
before the frozen outcomes.

It does not alone establish
that those protocols were
registered with an external
preregistration service.

Preregistration itself is
not a new MADELEINE invention.

## 6. External comparator C: Registered Reports

Source:
Nature Communications.

Title:
Registered Reports.

URL:
https://www.nature.com/ncomms/submit/registered-reports

Relevant established method:

Registered Reports undergo
peer review of the study
protocol before outcomes
are available, followed
by later review of results.

Internally frozen
MADELEINE protocols
are not equivalent to
independent Stage 1
Registered Report review.

Both approaches value
predeclared methods.

Their assurance levels
must not be conflated.

## 7. External comparator D: provenance

Source:
World Wide Web Consortium.

Title:
PROV-O: The PROV Ontology.

W3C Recommendation:
30 April 2013.

URL:
https://www.w3.org/TR/prov-o/

Relevant established method:

PROV-O represents
provenance information
using standardized entities,
activities, agents and
their relationships.

MADELEINE preserves
commit history, file hashes,
artifacts and dependencies.

This is a useful internal
provenance architecture.

The present comparison
does not demonstrate a
formal translation from
MADELEINE provenance
to PROV-O.

Generic traceability
is established prior art.

## 8. Frozen LAB-D2 gate application

The associated frozen audit
reports satisfaction of:

REGION_PARAMETRIC;
SEED_AGREEMENT;
NULL_SEPARATION;
EXPLICIT_FAILURE_CRITERION;
NON_REDUCIBLE;
FROZEN_RULE;
COMPLETE_TRACE.

Recorded result:

7/7 PASS.

The region condition uses
the predeclared 3x3 atlas core:

9/9 POINT PASS.

Seed records satisfy
the declared thresholds.

Provenance conditions
use preserved protocols,
commits and artifacts.

VERDICT:
INTERNAL GATE APPLICATION
SURVIVES_WITH_RESTRICTION.

This is a contract result,
not external validation.

## 9. Evidence dependence

The seven clauses are
logically distinct inputs.

Their supporting data are
not seven independent
scientific replications.

REGION_PARAMETRIC includes
point-level joint decisions.

Those already depend
on seed-level PASS criteria.

SEED_AGREEMENT examines
overlapping seed records.

NULL_SEPARATION rechecks
historical criteria used
inside seed-level results.

FROZEN_RULE and COMPLETE_TRACE
inspect related aspects
of a shared provenance chain.

The remaining clauses have
different procedural roles,
but distinct roles are not
equivalent to statistical
independence.

VERDICT:
SEVEN REQUIREMENTS PASSED,
NOT SEVEN INDEPENDENT
SCIENTIFIC CONFIRMATIONS.

## 10. Non-reducibility scope

The frozen non-reducibility
clause uses a restricted
set of synthetic controls.

Relevant comparisons include:

LAB-D0;
LAB-D1;
NO_PAST;
RANDOMIZED_PAST;
DETERMINISTIC_CHOICE.

It does not eliminate
every alternative model.

The supported wording is:

NO REDUCIBLE A LOS LIMITES
INTERNOS ENSAYADOS EN
LAB-FEN-001-v1.

Do not replace it with:

UNIVERSALLY IRREDUCIBLE.

## 11. Admission versus truth

DMO-004 implements a rule:

evidence
-> declared requirements
-> internal admission.

Passing the gate permits
the internal label:

REGIMEN INTERNO ADMITIDO
BAJO LAB-FEN-001-v1 Y DMO-004.

It does not imply:

a new physical regime;
a unique underlying mechanism;
a universal mathematical law;
independent external replication.

The admission label
must retain its qualifier.

## 12. Novelty assessment

Boolean conjunction:
STANDARD_OR_DERIVATIVE.

Exhaustive truth-table checks:
STANDARD SOFTWARE-LOGIC TESTING.

Single-clause influence:
RELATED TO KNOWN
CONDITION-DECISION TESTING.

Predeclared success criteria:
ESTABLISHED RESEARCH PRACTICE.

Traceable research artifacts:
ESTABLISHED PRIOR METHODOLOGY.

Specific MADELEINE
integration and terminology:
SYSTEM-SPECIFIC.

Demonstrated advantage over
independent baseline workflows:
NOT ESTABLISHED.

General claim-soundness theorem:
NOT ESTABLISHED.

Scientific originality of
the integrated architecture:
UNDERDETERMINED.

## 13. Seven-condition audit mapping

S - Exact claim scope:
DOCUMENTED.

E - Evidence classes:
M AND C DOCUMENTED.

A - Adversarial tests:
128-STATE SWEEP,
CLAUSE ABLATIONS,
LAB-D2 ADMISSION AUDIT.

L - Literature comparison:
TARGETED EXTERNAL
COMPARATORS DOCUMENTED.

N - Novelty assessment:
STANDARD INGREDIENTS;
SYSTEM-LEVEL NOVELTY OPEN.

V - Final verdict:
SURVIVES_WITH_RESTRICTION.

R - Residual limitations:
DOCUMENTED.

This is a focused
comparison, not an
exhaustive priority search.

It does not close the
entire Phase 10 gate.

## 14. Remaining obligations

R10-DMO004-01:
Never count 7/7 as seven
independent confirmations.

R10-DMO004-02:
Interpret clause necessity
relative to the declared gate.

R10-DMO004-03:
Retain the restricted
internal non-reducibility
formulation.

R10-DMO004-04:
Compare against alternative
mechanism families in an
appropriately predeclared
future scientific version.

R10-DMO004-05:
Require independent
external evaluation before
promoting the regime label.

R10-INTEGRATED-01:
No established comparative
advantage against known
research workflows.

R10-INTEGRATED-02:
No general formal guarantee
that gate PASS entails
an arbitrary stronger claim.

Any future executable
or empirical evaluation
belongs to a new version.

## 15. Final decision

DMO-004 implementation:
SURVIVES.

Frozen LAB-D2 application:
SURVIVES_WITH_RESTRICTION.

Methodological ingredients:
STANDARD_OR_DERIVATIVE.

Seven independent
scientific confirmations:
NOT JUSTIFIED.

Internal regime admission:
SUPPORTED UNDER CONTRACT.

Universal necessity
of the seven conditions:
NOT ESTABLISHED.

Integrated scientific novelty:
NOT ESTABLISHED.

External physical validity:
EXTERNAL_VALIDATION_REQUIRED.

Full Phase 10 audit:
OPEN.

## 16. Preservation

Do not modify:

v0.2.1;
release tag;
published PDFs;
references.bib;
canonical ZIP;
snapshots;
frozen experiments;
Zenodo deposit.

This note is post-publication
documentary analysis only.

No commit or push
during file creation.

STATUS:

PHASE10 DMO004 TARGETED PRIOR ART COMPARISON DOCUMENTED

DMO004 INDEPENDENCE AND SYSTEM NOVELTY REMAIN OPEN
