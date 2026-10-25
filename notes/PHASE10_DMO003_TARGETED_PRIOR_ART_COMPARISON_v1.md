# MADELEINE - Phase 10 DMO-003 Targeted Prior-Art Comparison v1

## 0. Status

POST-PUBLICATION TARGETED MATHEMATICAL COMPARISON

Date: 2026-10-26

Reference main:
93109eaedc7bc1f336d5cf9a031dbc3636fec71d

Frozen scientific release:
v0.2.1

Frozen scientific commit:
fee2c31cfa17159a4075e1cbfbfa7e2fceba9c4b

Target:
DMO-003

Associated claim:
C016

Evidence class:
F - Formal.

CORRECT != NOVEL != GENERAL != EXTERNALLY VALIDATED

No new simulation.
No recalibration.
No change to frozen results.

## 1. Inspected finite construction

Let m be an integer, m >= 1.

Define the six-channel state:

c=(xp,xm,yp,ym,zp,zm)

with each channel in:

{0,...,m}.

Define its signed projection:

P(c)=(xp-xm,yp-ym,zp-zm).

The image is exactly:

{-m,...,m}^3.

The cardinality of the image is:

(2m+1)^3.

These results survive within
the declared finite domain.

## 2. Exact fiber calculation

For one opposed pair:

(a,b) in {0,...,m}^2

let:

d=a-b.

For fixed d, the number
of admissible pairs is:

m+1-|d|.

For three independent pairs:

|P^(-1)(dx,dy,dz)|
=(m+1-|dx|)
 (m+1-|dy|)
 (m+1-|dz|).

This exact finite count survives.

The calculation is an elementary
property of signed differences
under finite bounds.

## 3. Common-mode decomposition

Define:

s=min(a,b).

Then:

a=max(d,0)+s

and:

b=max(-d,0)+s.

The admissible range is:

0 <= s <= m-|d|.

Therefore:

(a,b) <-> (d,s)

is a reversible parameterization
on the declared bounded domain.

For the full state:

c <-> (dx,dy,dz,sx,sy,sz).

The projection P keeps d
and forgets s.

This describes exactly
the distinctions removed
by the projection.

It does not establish
a physical information measure.

## 4. External comparator A

Source:
Carnegie Mellon University.

Title:
Linear Programs in Standard Form.

URL:
https://mat.tepper.cmu.edu/classes/QUANT/NOTES/chap7/node3.html

Relevant established method:

An unrestricted signed variable
can be replaced with the
difference of two nonnegative
variables.

The two-variable representation
is not unique without
additional constraints.

Comparison:

The use of opposed nonnegative
components is standard.

DMO-003 adds an explicit
finite-box domain and
counts its fibers.

This comparator does not
establish that all MADELEINE
six-channel operations
are equivalent to
linear programming.

## 5. External comparator B

Source:
Encyclopedia of Mathematics.

Title:
Disjunctive elements.

URL:
https://encyclopediaofmath.org/wiki/Disjunctive_elements

Relevant established construction:

For a scalar x, its
canonical positive and
negative parts are:

xplus=max(x,0)

xminus=max(-x,0).

They do not have
simultaneous positive values.

Their difference recovers x.

This is an antecedent for
an exclusive signed
representation.

The comparison concerns
the decomposition only,
not a full dynamic theory.

## 6. Exclusivity boundary

DMO-003 also considers
the exclusive constraint:

xp*xm=0,
yp*ym=0,
zp*zm=0.

Under this condition:

sx=sy=sz=0.

The six-channel state
is uniquely recovered
from its signed projection.

Thus P becomes bijective
on the exclusive domain.

VERDICT:

EXCLUSIVE REPRESENTATION
IS MATHEMATICALLY EQUIVALENT
TO THE THREE SIGNED COORDINATES.

Without exclusivity, P has
nontrivial fibers.

The distinction depends
on the permitted states.

## 7. Universal counterexample

For every integer m >= 1:

c0=(0,0,0,0,0,0)

and:

c1=(1,1,0,0,0,0)

are both admissible.

They are different states.

But:

P(c0)=P(c1)=(0,0,0).

Hence P is non-injective
throughout the declared
parameter range.

The published example:

(1,0) and (2,1)

requires m >= 2.

That example does not cover
the m=1 boundary.

The general theorem survives
using c0 and c1.

This note does not modify
the published example.

## 8. Projection factorization

Let O be any defined
observable on the
six-channel state space.

A function F exists with:

O=F o P

if and only if:

P(c)=P(c')
implies O(c)=O(c')

for all admissible states.

This is an elementary
fiber-factorization criterion.

Its proof constructs F
from the common O value
on each fiber.

Therefore representational
loss is relevant to O
only if O distinguishes
states with the same P value.

## 9. Auxiliary distinguishing observable

For comparison only,
define a hypothetical observable:

Q(c)=xp+xm+yp+ym+zp+zm.

Then:

Q(c0)=0

and:

Q(c1)=2,

although:

P(c0)=P(c1).

Thus Q does not factor
through P on the
unrestricted six-channel domain.

Equivalently, for one pair:

a+b=|d|+2s.

This example shows how
a specified observable
can depend on the forgotten
common-mode coordinate.

However, Q is introduced
here as an auxiliary
mathematical comparator.

This note does not claim
that Q is a frozen
canonical MADELEINE operator
or a proved physical observable.

It cannot by itself
establish system-level
six-channel necessity.

## 10. Involution

The documented canonical
involution exchanges
each opposed pair.

On the (d,s) representation:

I(d,s)=(-d,s).

Therefore:

P(I(c))=-P(c).

The projected effect
of this involution
depends only on P(c).

This example does not show
that the common-mode
coordinates are required
for projected behavior.

VERDICT:
STANDARD_OR_DERIVATIVE.

## 11. Dynamic necessity criterion

Suppose a deterministic
six-channel transition T
has been fully specified.

A projected transition F
satisfying:

P o T=F o P

exists if and only if:

P(c)=P(c')
implies
P(T(c))=P(T(c'))

for all admissible c,c'.

A counterexample to
this implication would
show that the projected
current state is insufficient
for that specific T.

The inspected frozen sources
have not established
a complete T together
with such a counterexample.

Therefore:

DYNAMIC NECESSITY
UNDERDETERMINED.

No new T is silently
introduced by this note.

## 12. Canonical versus laboratory evidence

The LAB-D2 generator uses
a five-symbol categorical
state space.

It is not an executable
six-channel transition law.

Its successful frozen
internal metrics do not
demonstrate that sx,sy,sz
are necessary for
canonical MADELEINE dynamics.

The common D-labels
do not prove a mathematical
identity between the layers.

## 13. Novelty assessment

Signed-variable splitting:
STANDARD_OR_DERIVATIVE.

Exclusive positive-negative
representation:
STANDARD_OR_DERIVATIVE.

Finite fiber counts:
ELEMENTARY FINITE COUNTING.

Non-injectivity of P:
SURVIVES.

Exact common-mode recovery
with (d,s):
SURVIVES.

Nontrivial canonical
observable using s:
NOT ESTABLISHED.

Indispensable canonical
six-channel dynamics:
UNDERDETERMINED.

Novel six-channel
physical geometry:
NOT ESTABLISHED.

System-level originality:
UNDERDETERMINED.

An exhaustive independent
historical priority search
has not been completed.

## 14. Seven-condition mapping

S - Exact scope:
DOCUMENTED.

E - Evidence class:
F, DOCUMENTED.

A - Adversarial examination:
DOCUMENTED.

L - External mathematics:
TARGETED COMPARISON DOCUMENTED
WITH DECLARED LIMITS.

N - Novelty assessment:
STANDARD MATHEMATICAL
INGREDIENTS; GLOBAL
NOVELTY NOT ESTABLISHED.

V - Final verdict:
SURVIVES_WITH_RESTRICTION.

R - Residual limitations:
DOCUMENTED.

The review improves
the DMO-003 literature record.

It does not certify
universal novelty or
full Phase 10 closure.

## 15. Remaining obligations

R10-DMO003-01:
Make the integer domain
of m explicit.

R10-DMO003-02:
Qualify the published
non-injectivity example.

R10-DMO003-03:
Distinguish lost
representational states
from measured information.

R10-DMO003-04:
Identify an actual
frozen or future
canonical downstream operator
that uses the common modes.

Specify the admissible
state space and dynamics.

Test factorization
under declared conditions.

Do not promote a
hypothetical auxiliary
observable to a
validated MADELEINE law.

## 16. Final decision

DMO-003 finite theorem:
SURVIVES_WITH_RESTRICTION.

Known signed-splitting
and exclusive decomposition:
STANDARD_OR_DERIVATIVE.

Loss of common modes
under net projection:
PROVED IN THE FINITE DOMAIN.

Canonical dynamic necessity:
NOT ESTABLISHED.

Independent integrated novelty:
NOT ESTABLISHED.

External physical interpretation:
EXTERNAL_VALIDATION_REQUIRED.

Full Phase 10 audit:
OPEN.

## 17. Preservation

Do not modify:

v0.2.1;
release tag;
published PDFs;
references.bib;
canonical ZIP;
snapshots;
frozen laboratory data;
Zenodo deposit.

This is a post-publication
interpretive comparison.

No commit or push occurs
during file creation.

STATUS:

PHASE10 DMO003 TARGETED PRIOR ART COMPARISON DOCUMENTED

DMO003 DYNAMIC NECESSITY REMAINS OPEN
