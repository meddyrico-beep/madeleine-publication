# MADELEINE - Phase 10 DMO-005 Targeted Prior-Art Comparison v1

## 0. Provenance and status

POST-PUBLICATION TARGETED MATHEMATICAL AND METROLOGICAL COMPARISON

Date: 2026-10-26

Reference main:
14fceb3eaf6d6c684ef7544b7e255958e70a65ae

Frozen release:
v0.2.1

Frozen release commit:
fee2c31cfa17159a4075e1cbfbfa7e2fceba9c4b

Target:
DMO-005

Claim:
C026

Evidence classes:
F - Formal.
M - Methodological.

CORRECT != NOVEL != GENERAL != EXTERNALLY VALIDATED

No new experiment.
No frozen contract changes.
No calibration.
No modification of published evidence.

## 1. Inspected contract

For every internally valid reading L,
the frozen DMO-005 defines:

K(L)=(M,W,k,G,T).

Here:

M = metric schema;
W = window size;
k = history depth;
G = regime-gate version;
T = traceability schema.

The direct-comparison relation is:

L1 ~ L2

if and only if:

K(L1)=K(L2).

Direct componentwise subtraction
is admitted only under the
declared contract-matching rule.

This is a conservative
internal admission condition.

## 2. Formal equivalence result

The relation inherits the
properties of equality.

Reflexivity:

K(L)=K(L).

Symmetry:

K(L1)=K(L2)
implies K(L2)=K(L1).

Transitivity:

K(L1)=K(L2)
and K(L2)=K(L3)
imply K(L1)=K(L3).

Therefore the declared
relation is an equivalence
relation on valid readings.

Its equivalence classes
are the fibers of K.

VERDICT:

SURVIVES.

The mathematics is standard.

## 3. External comparator A

Source:
Encyclopedia of Mathematics.

Title:
Equivalence relation.

URL:
https://encyclopediaofmath.org/wiki/Equivalence

Relevant established result:

Given any function f,
the relation defined by:

f(x)=f(y)

is an equivalence relation.

Its equivalence classes
partition the domain.

The DMO-005 construction
is an instance of
this standard mechanism.

This comparison does not
prove equivalence of
scientific measurements.

## 4. Direct numerical differences

When the frozen gate accepts
a pair of compatible,
well-formed numerical readings,
the executable permits
componentwise subtraction.

If the value vectors are
denoted illustratively by:

V_A and V_B,

then:

Delta V_(B-A)=V_B-V_A.

Reversing the arguments gives:

Delta V_(A-B)=-Delta V_(B-A).

This is an arithmetic identity.

It is not independently
new mathematical theory.

The notation V is used
only to distinguish
numerical values from
the metric-schema field M.

## 5. External comparator B

Source:
Joint Committee for Guides
in Metrology.

Reference:
International Vocabulary
of Metrology, VIM3.

Entry:
2.46 - Metrological
comparability of
measurement results.

URL:
https://jcgm.bipm.org/vim/en/2.46.html

Relevant established concept:

Results for quantities
of a given kind are
metrologically comparable
when they are traceable
to the same reference.

This does not demand
identical complete
measurement procedures.

DMO-005 instead defines
a stricter internal rule
for direct subtraction.

The two notions have
different domains and
must not be equated.

DMO-005 is not proven
to implement complete
metrological traceability.

## 6. External comparator C

Source:
Joint Committee for Guides
in Metrology.

Reference:
VIM3.

Entry:
2.41 - Metrological
traceability.

URL:
https://jcgm.bipm.org/vim/en/2.41.html

Relevant established concept:

Traceability concerns
a measurement result
related to a reference
through a documented
unbroken calibration chain
with associated uncertainty.

A trace-field schema
is not that chain.

Equality of trace schemas
does not establish
metrological traceability.

This is an important
limitation of DMO-005.

## 7. External comparator D

Source:
Association for
Psychological Science.

Title:
Testing for Measurement
Invariance: Does Your
Measure Mean the Same Thing
for Different Participants?

URL:
https://www.psychologicalscience.org/observer/testing-for-measurement-invariance

Relevant established idea:

Comparability between groups
can require testing explicit
invariance conditions.

Different levels of
invariance support
different kinds of comparison.

This is an analogy at
the methodological level.

It is not a claim
that MADELEINE metrics
are psychometric scales.

No measurement-invariance
test is performed here
for the frozen lab metrics.

## 8. Metric-schema limitation

The frozen M field
identifies metric names
and their declared order.

Equality of identifiers
does not logically guarantee
identity of:

metric definitions;
units;
normalization;
implementation versions;
calibration;
measurement uncertainty.

A hypothetical example:

Two systems both store
a metric field called A0.

One interprets A0
in metres.

The other interprets A0
in kilometres.

If this difference is
not represented in K,
matching identifiers
could allow misleading
raw subtraction.

This is a logical
countermodel to a
universal sufficiency claim.

It is not an observed
defect in frozen
MADELEINE data.

## 9. Trace-schema limitation

The field T describes
the structure of a trace.

It does not mean all
trace values are equal.

Two valid readings
can share the fields:

seed;
parameters;
series_hash;
rule_version;

while their actual values
are different.

Different seeds and
series hashes can be
expected across
distinct experimental runs.

Therefore:

equal trace schema

does not imply:

equal provenance;

identical experiments;

or independent scientific
replication.

The distinction is
already identified by
the DMO-005 adversarial audit.

## 10. Contract equality is not
universal scientific sufficiency

Within DMO-005,
equality of K authorizes
comparison according to
the declared program rule.

However, even identical K
does not independently prove:

physical equivalence;
common real-world mechanism;
calibrated units;
measurement validity;
external generalization.

These are separate
scientific obligations.

The formal gate may be
correct while the physical
interpretation remains open.

## 11. Different contracts
can admit explicit bridges

Consider an illustrative
measurement transformation.

Let C denote a temperature
value on a Celsius scale.

Let Ktemp be the corresponding
Kelvin numerical value.

Their standard scale relation is:

Ktemp=C+273.15.

The numerical values have
different scale conventions.

Direct raw subtraction
as though they shared one
identical representation
would be inappropriate.

But the explicit map
relates their values.

For example:

0 degrees Celsius

corresponds to:

273.15 kelvin.

Thus different
representations can be
related by a declared bridge.

This example is external
to the frozen MADELEINE
DMO-005 executable.

It does not establish
a validated bridge
between MADELEINE contracts.

It shows why refusing
untranslated direct comparison
does not prove universal
incomparability.

## 12. Relationship to DMO-006

DMO-005 covers:

direct comparison
under matching K.

DMO-006 covers:

finite maps and their
fiber structures.

Neither result by itself
supplies a general,
validated bridge between
different measurement
contracts.

Even a bijection between
state sets does not
necessarily preserve
transition laws or
metric interpretations.

For declared dynamics:

f:X -> X

and:

g:Y -> Y,

a mapping B:X -> Y
preserves those dynamics
when:

B o f = g o B.

This is a standard
intertwining condition.

The frozen DMO-005
does not construct such
a map across K classes.

VERDICT:

CROSS-CONTRACT DYNAMIC
PRESERVATION NOT ESTABLISHED.

## 13. Minimality issue

DMO-005 requires equality
of five declared fields.

It has not proven that
all five are necessary
for every scientifically
legitimate comparison.

It also has not proven
that no additional field
would ever be required.

The implemented rule is:

a declared conservative
compatibility policy.

It is not:

a theorem of universal
minimal comparability.

## 14. Novelty assessment

Equivalence from function
equality:
STANDARD_OR_DERIVATIVE.

Partition into contract
classes:
STANDARD_OR_DERIVATIVE.

Vector difference
antisymmetry:
STANDARD_OR_DERIVATIVE.

Scientific comparability
through common references:
ESTABLISHED METROLOGY.

Measurement-invariance
methodology:
ESTABLISHED PRIOR WORK.

Specific K tuple and
implementation in MADELEINE:
SYSTEM-SPECIFIC.

Universal optimality
or minimality of K:
NOT ESTABLISHED.

External measurement validity:
NOT ESTABLISHED.

Cross-contract
structure-preserving bridge:
UNDERDETERMINED.

Integrated scientific novelty:
UNDERDETERMINED.

## 15. Seven-condition mapping

S - Scope:
DOCUMENTED.

E - Evidence classes:
F AND M DOCUMENTED.

A - Adversarial examination:
DOCUMENTED.

L - Prior-art comparison:
TARGETED SOURCES DOCUMENTED.

N - Novelty assessment:
STANDARD INGREDIENTS;
INTEGRATED NOVELTY OPEN.

V - Supported verdict:
SURVIVES_WITH_RESTRICTION
FOR DIRECT COMPARABILITY.

R - Residual limitations:
DOCUMENTED.

This is a focused
mathematical and
metrological comparison.

It is not an exhaustive
historical priority search.

It does not close
the overall Phase 10
scientific audit.

## 16. Residual obligations

R10-DMO005-01:
Restrict C026 to
direct comparison under
the declared contract.

R10-DMO005-02:
Distinguish trace schema
from actual provenance.

R10-DMO005-03:
Future versions may
include metric definition
versions, units or hashes.

R10-DMO005-04:
Do not assert K is
universally minimal
or scientifically sufficient.

R10-DMO005-05:
An explicit translation
between distinct contracts
requires separate validation.

R10-MAT-12:
The formal cross-level
bridge remains open.

No future version
is authorized by this
documentary step.

## 17. Final decision

DMO-005 equivalence:
SURVIVES.

Internal matching gate:
SURVIVES.

Direct comparability
under DMO-005:
SURVIVES_WITH_RESTRICTION.

Universal need for
literal equality of K:
NOT JUSTIFIED.

Scientific sufficiency
of identical K:
UNDERDETERMINED.

Cross-contract
preservation:
NOT ESTABLISHED.

Isolated mathematical novelty:
STANDARD_OR_DERIVATIVE.

System-level originality:
UNDERDETERMINED.

External physical validity:
EXTERNAL_VALIDATION_REQUIRED.

Full Phase 10 audit:
OPEN.

## 18. Preservation

No change to:

v0.2.1;
release tag;
published PDFs;
references.bib;
canonical ZIP;
snapshots;
frozen experimental results;
Zenodo deposit.

This is a post-publication
documentary comparison.

No commit or push occurs
during file creation.

STATUS:

PHASE10 DMO005 TARGETED PRIOR ART COMPARISON DOCUMENTED

DMO005 CROSS CONTRACT PRESERVATION REMAINS OPEN
