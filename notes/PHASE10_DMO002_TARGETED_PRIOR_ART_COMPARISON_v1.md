# MADELEINE - Phase 10 DMO-002 Targeted Prior-Art Comparison v1

## 0. Status

POST-PUBLICATION TARGETED MATHEMATICAL COMPARISON

Date: 2026-10-24

Reference main:
ed9e66cd2e30820e843dfe1cd66c54c4b0db3bf7

Frozen scientific release:
v0.2.1

Frozen scientific commit:
fee2c31cfa17159a4075e1cbfbfa7e2fceba9c4b

Target:
DMO-002

Associated claim:
C014

Evidence class:
F - Formal.

CORRECT != NOVEL != GENERAL != EXTERNALLY VALIDATED

No new experiment.
No recalibration.
No frozen source modification.

## 1. Exact frozen mathematical domain

Let:

m,n be integers with m,n >= 1.

Consider histories:

H=(x_0,...,x_n)

with:

x_0=0

and:

x_i in {0,...,m}.

Stationary successive states
are permitted.

Define:

n(H)=n

and:

delta(H)
=sum_(i=0)^(n-1) |x_(i+1)-x_i|.

The frozen proposition states:

Delta_n^(m)={0,...,mn}.

Its cardinality is:

mn+1.

## 2. Status of the finite theorem

Every transition changes
the state by at most m.

Consequently:

0 <= delta(H) <= mn.

For any integer k
in the declared range,
Euclidean division gives:

k=qm+r

with:

0 <= r < m.

Use q full jumps of length m,
alternating between 0 and m.

If r>0, then q<n,
so a residual transition
of length r is available.

All remaining steps
may be stationary.

Therefore every k
in {0,...,mn} is reached.

The construction proves
the finite reachability formula
under the stated domain.

VERDICT:

SURVIVES.

This note does not assert
that the proof is a new
mathematical invention.

## 3. External source A

Title:
Variation of a function.

Source:
Encyclopedia of Mathematics.

URL:
https://encyclopediaofmath.org/wiki/Variation_of_a_function

Relevant antecedent:

Total variation uses sums
of absolute increments
over ordered partitions,
followed by a supremum
over admissible partitions.

The DMO-002 sum is a
fixed finite-path variation.

It uses a standard
absolute-increment operation.

A finite-path sum and the
supremum over all partitions
must not be conflated.

The source establishes
the mathematical family
of the construction.

It does not independently
prove the exact DMO-002
reachability formula.

## 4. External source B

Title:
Pairing Function.

Author:
Eric W. Weisstein,
with contributors.

Source:
Wolfram MathWorld.

URL:
https://mathworld.wolfram.com/PairingFunction.html

Relevant antecedent:

Known pairing functions
encode pairs of nonnegative
integers reversibly as
single nonnegative integers.

They demonstrate that
two integer coordinates
do not necessarily require
two separate scalar fields
for lossless representation.

This is a comparator
for representation claims.

It does not establish
equivalence of all downstream
MADELEINE operations.

## 5. Exact non-redundancy examples

Fix m=1.

Consider:

H_1=(0,0).

Then:

n(H_1)=1;
delta(H_1)=0.

Consider:

H_2=(0,1).

Then:

n(H_2)=1;
delta(H_2)=1.

Thus n alone does not
determine delta.

Now compare:

H_2=(0,1)

and:

H_3=(0,1,1).

Both have:

delta=1.

But their transition
counts are respectively:

1 and 2.

Thus delta alone does not
determine n across histories
with varying lengths.

These examples use
stationary steps permitted
by the frozen domain.

VERDICT:

FINITE COORDINATE
NON-REDUNDANCY SURVIVES.

## 6. Strict-step countermodel

Consider an additional rule
that was not imposed
by frozen DMO-002:

x_(i+1) != x_i.

Use the binary alphabet:

{0,1}.

Every permitted transition
must change the state
by exactly one.

Therefore:

delta(H)=n(H).

On this restricted subdomain,
the two coordinates are
functionally dependent.

This does not refute
the original theorem.

It demonstrates that
non-redundancy depends
on the admissible histories
and counting convention.

## 7. Reversible scalar encoding

Suppose:

1 <= n <= N

and:

0 <= delta <= mN

for fixed positive integers
m and N.

Define:

J(n,delta)
=(mN+1)*n+delta.

For this bounded domain,
J is injective.

Indeed, different n values
produce disjoint integer
blocks of length mN+1,
and delta identifies a
position within its block.

Therefore:

(n,delta)

can be represented
losslessly by one integer.

More generally, standard
pairing functions provide
reversible encodings
without this finite bound.

VERDICT:

UNIVERSAL IMPOSSIBILITY
OF SCALAR ENCODING FAILS.

This does not eliminate
the usefulness of retaining
two semantically distinct
coordinates.

## 8. Canonical bridge limitation

The inspected sources use
three related constructions.

A. Base Axiomática:

M=(n,delta),

where delta is an
internal subphase.

B. Tomo I:

M(X;W)=(n_T,delta_E),

using count and
declared extension.

C. DMO-002:

(n(H),delta(H)),

where delta is accumulated
discrete total variation.

Shared notation and
conceptual motivation
do not prove formal identity.

A bridge would need:

- domains;
- explicit mappings;
- compatible update rules;
- window and resolution rules;
- preserved observables.

VERDICT:

CANONICAL-EDITORIAL-DEMO
EQUIVALENCE NOT ESTABLISHED.

## 9. Downstream necessity

A meaningful system-level
necessity argument must
identify a specific
already defined operation O.

To prove that n alone
cannot support O,
one needs histories H,H'
with the same n but
different O outputs.

To prove that delta alone
cannot support O,
one needs histories H,H'
with the same delta but
different O outputs.

Choosing O=(n,delta)
would merely repeat
representational distinctions.

It would not establish
a new downstream capability.

The inspected sources
have not established
a nontrivial canonical
operation that requires
both demo coordinates.

VERDICT:

DOWNSTREAM NECESSITY
UNDERDETERMINED.

## 10. Novelty assessment

Absolute-increment variation:
STANDARD MATHEMATICS.

Transition counts:
STANDARD MATHEMATICS.

Finite reachability formula:
CORRECT UNDER DECLARED DOMAIN.

An exact independent
historical antecedent for
this particular formula
has not been established
by this limited review.

Absence of a located
identical formula is
not evidence of novelty.

Lossless integer-pair encoding:
STANDARD MATHEMATICS.

Non-redundancy under
individual projections:
SURVIVES WITH RESTRICTION.

Canonical formal equivalence:
NOT ESTABLISHED.

Integrated scientific novelty:
UNDERDETERMINED.

Physical measurement theory:
NOT ESTABLISHED.

## 11. Seven-condition mapping

S - Scope:
DOCUMENTED.

E - Evidence class:
F, DOCUMENTED.

A - Adversarial examination:
DOCUMENTED.

L - Literature comparison:
TARGETED COMPARISON DOCUMENTED,
NOT AN EXHAUSTIVE PRIORITY SEARCH.

N - Novelty assessment:
STANDARD INGREDIENTS;
EXACT PRIORITY NOT CERTIFIED.

V - Supported verdict:
SURVIVES_WITH_RESTRICTION.

R - Residual limitations:
DOCUMENTED.

This improves the
DMO-002 literature record.

It does not close
all Phase 10 obligations.

## 12. Strongest justified statement

Under the declared finite
discrete DMO-002 domain,
the transition count n
and accumulated variation
delta do not determine
one another over
the full family of histories.

The reachability set
for fixed n and m is:

{0,...,mn}.

The result is correct.

It does not prove
universal irreducibility,
a novel theory of measurement,
or necessary use of both
registers in every
MADELEINE representation.

## 13. Remaining obligations

R10-DMO002-01:
Keep m,n explicitly integer.

R10-DMO002-02:
Distinguish non-redundancy
from absolute irreducibility.

R10-DMO002-03:
Treat exact historical
novelty as unresolved
without a sufficient search.

R10-MAT-12:
Specify a formal bridge
between register versions.

R10-CROSS-07:
Demonstrate or refute
nontrivial downstream
necessity of both coordinates.

No frozen definition
is changed here.

## 14. Final decision

DMO-002 finite result:
SURVIVES.

Coordinate non-redundancy:
SURVIVES_WITH_RESTRICTION.

Known mathematical ingredients:
STANDARD_OR_DERIVATIVE.

Exact theorem priority:
NOT INDEPENDENTLY CERTIFIED.

Scalar recoding impossibility:
NOT SUPPORTED.

Canonical bridge:
NOT ESTABLISHED.

Downstream necessity:
UNDERDETERMINED.

Integrated originality:
NOT ESTABLISHED.

Full Phase 10 audit:
OPEN.

## 15. Preservation

Do not modify:

v0.2.1;
release tag;
published PDFs;
references.bib;
canonical ZIP;
snapshots;
frozen experimental evidence;
Zenodo deposit.

This is a post-publication
interpretive comparison.

No commit or push occurs
during file creation.

STATUS:

PHASE10 DMO002 TARGETED PRIOR ART COMPARISON DOCUMENTED

DMO002 CANONICAL BRIDGE AND NECESSITY REMAIN OPEN
