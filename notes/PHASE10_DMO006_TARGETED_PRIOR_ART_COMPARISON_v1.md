# MADELEINE - Phase 10 DMO-006 Targeted Prior-Art Comparison v1

## 0. Provenance and status

POST-PUBLICATION TARGETED MATHEMATICAL COMPARISON

Date: 2026-10-26

Reference main:
e59a0bfb17062d5010d99cc81f79ed3af03040d5

Frozen release:
v0.2.1

Frozen release commit:
fee2c31cfa17159a4075e1cbfbfa7e2fceba9c4b

Target:
DMO-006

Claim:
C030

Evidence classes:
F - Formal.
M - Methodological.

CORRECT != NOVEL != GENERAL != EXTERNALLY VALIDATED

No new scientific experiment.
No recalibration.
No change to released theory.
No modification of frozen evidence.

## 1. Exact construction

Let X and Y be finite
declared sets.

Let:

B:X -> Y

be a function.

For y in B(X), define
the nonempty fiber:

B^(-1)(y)
={x in X : B(x)=y}.

DMO-006 defines:

E(B)=|X|-|B(X)|

P(B)=sum_y binom(|B^(-1)(y)|,2)

U(B)=|Y|-|B(X)|.

The sum for P runs
over nonempty fibers.

The three quantities
describe different aspects
of a finite mapping.

They are not general
measurements of physical
or Shannon information.

## 2. Fiber decomposition

The nonempty fibers
partition the source X.

Therefore:

|X| =
sum_y |B^(-1)(y)|.

Subtracting the number
of nonempty fibers gives:

E(B) =
sum_y (|B^(-1)(y)|-1).

This identity survives
on the declared finite domain.

The quantity E counts
the excess number of source
elements within fibers
beyond one representative
per nonempty fiber.

## 3. Exact injectivity test

The mapping B is injective
if and only if every
nonempty fiber has size one.

Hence:

E(B)=0

if and only if:

B is injective.

Likewise:

P(B)=0

if and only if:

B is injective.

A collision pair contributes
to P exactly when two
distinct source elements
share one image.

VERDICT:

FINITE INJECTIVITY
CRITERIA SURVIVE.

## 4. Surjectivity and bijection

By definition:

U(B)=|Y|-|B(X)|.

Therefore:

U(B)=0

if and only if:

B is surjective.

Consequently:

B is bijective

if and only if:

E(B)=0 and U(B)=0.

Equivalently:

B is bijective

if and only if:

P(B)=0 and U(B)=0.

This is a set-theoretic
correspondence result.

It does not establish
preservation of any
additional operation.

## 5. External comparator A

Source:
Wolfram MathWorld.

Title:
Fiber.

Author:
Eric W. Weisstein.

URL:
https://mathworld.wolfram.com/Fiber.html

Relevant established concept:

A fiber of a mapping
is the preimage of an
individual target point.

Fibers are standard
objects of mathematics.

DMO-006 specializes
their counting to
a declared finite domain.

The comparator does not
validate the entire
MADELEINE architecture.

## 6. External comparator B

Source:
Abstract Math.

Title:
The Quotient of a Function.

URL:
https://abstractmath.org/MM/MMFuncQuotient.htm

Relevant established concept:

Any function induces
an equivalence relation
on its source:

x ~ x'

if and only if:

B(x)=B(x').

The classes are
the fibers of B.

The quotient X/~ can be
identified bijectively
with B(X).

Thus:

source set
-> fiber partition
-> image

is a standard
set-theoretic construction.

The MADELEINE audit may
organize this information
for its own purposes.

That organization alone
does not establish
new mathematical theory.

## 7. Dependence among summaries

By direct subtraction:

E(B)-U(B)
=
|X|-|Y|.

For fixed finite
source and target sizes,
E and U cannot vary
independently.

They have different
interpretations.

But numerically,
knowing either one
determines the other
when |X| and |Y|
are held fixed.

VERDICT:

DEPENDENCE PROVED.

Do not count E and U
as independent evidence
of two mechanisms.

## 8. Collision-pair diagnostic

For a fiber with
cardinality n:

E contribution=n-1.

P contribution=n(n-1)/2.

For n=3:

E contribution=2.

P contribution=3.

Thus E and P encode
different summaries
of the fiber sizes.

However, their joint
values need not determine
the full fiber profile.

## 9. Explicit incompleteness example

Let:

|X|=9

and:

|Y|=3.

Consider a surjective
mapping A with fibers:

(5,2,2).

Then:

E(A)=6.

P(A)=10+1+1=12.

U(A)=0.

Now consider a surjective
mapping B with fibers:

(4,4,1).

Then:

E(B)=6.

P(B)=6+6+0=12.

U(B)=0.

Both mappings have:

(E,P,U)=(6,12,0).

But their fiber-size
profiles are different.

Therefore the triple
(E,P,U) is not a
complete invariant
of the fiber partition.

This is a mathematical
counterexample.

It does not refute
the frozen DMO-006
implementation because
the demo also records
fiber information.

## 10. Distinction between
fiber profiles and mappings

Even identical fiber-size
profiles do not necessarily
identify the exact function B.

The source elements assigned
to each fiber may differ.

The target labels associated
with the fibers may also differ.

Therefore one should distinguish:

full mapping B;

fiber partition of X;

fiber cardinality profile;

summaries E,P,U.

These describe
progressively less of
the original mapping.

They are not interchangeable
without further assumptions.

## 11. Meaning of source loss

A non-injective B identifies
distinct source elements.

After observing only B(x),
some source distinctions
cannot be recovered uniquely.

This is a precise
set-theoretic meaning
of loss under translation.

It is not automatically
a numerical measure of:

Shannon entropy;

thermodynamic entropy;

physical information loss;

semantic equivalence;

measurement uncertainty.

Such claims need
additional defined structures.

## 12. Meaning of target reachability

The quantity U(B)
counts elements of Y
that are outside B(X).

It measures unreachable
declared target states.

It is not a general
measure of informational gain.

For example, an injective
derived-coordinate map
may have a larger
target representation
without introducing
independent source data.

Calling the larger
target an information
gain would be unjustified.

## 13. External comparator C

Source:
Wolfram MathWorld.

Title:
Injection.

Author:
Eric W. Weisstein.

URL:
https://mathworld.wolfram.com/Injection.html

Relevant established fact:

Injectivity means that
distinct inputs have
distinct outputs.

A bijection is both
injective and surjective.

These notions are
standard set theory.

DMO-006's finite zero
criteria are derived
tests for these properties.

No independent novelty
is inferred from them.

## 14. External comparator D

Source:
Scholarpedia.

Title:
Conjugate maps.

Author:
Yuri A. Kuznetsov.

Year:
2007.

URL:
https://www.scholarpedia.org/article/Topologically_equivalent

Relevant established concept:

A conjugacy relates
dynamical maps through
a suitable invertible
change of representation.

The dynamical relation
requires a commuting
composition equation.

For declared finite
set-based dynamics,
the algebraic condition is:

B o f = g o B.

Topological conjugacy
additionally requires
appropriate topological
hypotheses such as a
homeomorphism.

DMO-006 does not
establish these conditions
for its general mapping.

## 15. Explicit dynamic counterexample

Let:

X=Y={0,1}.

Define:

B(x)=x.

This is a bijection.

Hence:

E(B)=0.

P(B)=0.

U(B)=0.

Define source dynamics:

f(x)=1-x.

Define target dynamics:

g(x)=x.

At x=0:

B(f(0))=1.

But:

g(B(0))=0.

Therefore:

B o f != g o B.

The mapping is bijective
but does not preserve
these declared dynamics.

This counterexample
is elementary mathematics.

It is not a new
MADELEINE experiment.

## 16. Necessary structural bridge

To claim preservation
between two declared
dynamical systems,
one must specify:

source state space X;

target state space Y;

source update f;

target update g;

candidate bridge B;

admissible states;

which properties are
required to survive.

For deterministic dynamics,
a relevant test is:

B(f(x))=g(B(x))

for every admitted x.

A valid relation may
be established for
specific systems.

No general cross-level
MADELEINE construction
meeting this requirement
has been established
by the inspected
frozen demos.

VERDICT:

DYNAMIC PRESERVATION
UNDERDETERMINED.

## 17. Connection with DMO-003

DMO-003 studies a
six-to-three-channel
net-difference projection.

Its fibers reveal
common-mode distinctions.

DMO-006 provides
general finite
fiber-accounting language.

This relationship is
mathematically coherent.

But agreement of the
two fiber descriptions
does not prove a
structure-preserving
dynamic translation.

## 18. Connection with DMO-005

DMO-005 checks
direct comparability
when reading contracts
are identical.

DMO-006 analyzes
finite mappings and
their fiber structures.

A bridge between
different reading
contracts still needs
an explicit mapping
with preservation
and failure conditions.

A future symbol J(K1,K2)
would not, by itself,
establish such a bridge.

The missing object
is a validated
construction, not
merely a new name.

## 19. Novelty assessment

Fibers and inverse images:
STANDARD_OR_DERIVATIVE.

Equivalence classes
and quotient sets:
STANDARD_OR_DERIVATIVE.

Injectivity and
surjectivity criteria:
STANDARD_OR_DERIVATIVE.

Finite collision counting:
STANDARD_OR_DERIVATIVE.

The E,P,U combination:
SYSTEM-SPECIFIC
DIAGNOSTIC ORGANIZATION.

Exact historical novelty
of that diagnostic bundle:
NOT INDEPENDENTLY CERTIFIED.

Complete mapping invariant:
NOT ESTABLISHED.

Structure-preserving
cross-level translation:
NOT ESTABLISHED.

Integrated theoretical
originality:
UNDERDETERMINED.

External physical validity:
EXTERNAL_VALIDATION_REQUIRED.

## 20. Seven-condition mapping

S - Exact scope:
DOCUMENTED.

E - Evidence classes:
F AND M DOCUMENTED.

A - Adversarial tests:
DOCUMENTED.

L - External comparisons:
TARGETED MATHEMATICAL
COMPARATORS DOCUMENTED.

N - Novelty assessment:
STANDARD MATHEMATICAL
INGREDIENTS; SYSTEM-LEVEL
NOVELTY STILL OPEN.

V - Supported verdict:
SURVIVES_WITH_RESTRICTION.

R - Residual limitations:
DOCUMENTED.

This comparison is focused,
not an exhaustive
historical priority search.

It does not close
the full Phase 10
scientific audit.

## 21. Remaining obligations

R10-DMO006-01:
Retain full fiber
information rather
than only E,P,U.

R10-DMO006-02:
Preserve the identity
E-U=|X|-|Y|.

R10-DMO006-03:
Do not interpret U
as independent
information gain.

R10-DMO006-04:
Use precise language
for source distinctions
lost under a mapping.

R10-DMO006-05:
Specify preservation
conditions for any
richer structure.

R10-DMO006-06:
Do not interpret
equal summary triples
as equivalent
translations.

R10-MAT-12:
Formal cross-level
preservation remains
an open obligation.

No new scientific
experiment is authorized
by this comparison.

## 22. Strongest justified statement

For a declared finite map
B:X->Y, its fibers
identify exactly which
source states share
a target image.

The diagnostics E,P,U
summarize source collapse,
collision pairs and
unreached target states.

These diagnostics
survive mathematically
within the finite domain.

They neither reconstruct
the full mapping nor
establish equivalence
of additional dynamics,
geometries or physics.

## 23. Final decision

DMO-006 finite identities:
SURVIVES.

Finite implemented examples:
SURVIVE UNDER DECLARED DOMAIN.

Fiber accounting:
SURVIVES.

Scalar diagnostic interpretation:
SURVIVES_WITH_RESTRICTION.

Complete invariant claim:
NOT JUSTIFIED.

Independent E and U evidence:
NOT JUSTIFIED.

Set bijection as dynamic
equivalence:
NOT JUSTIFIED.

Cross-level dynamic bridge:
NOT ESTABLISHED.

System-level originality:
UNDERDETERMINED.

Full Phase 10 audit:
OPEN.

## 24. Preservation

Do not modify:

v0.2.1;
release tag;
published PDFs;
references.bib;
canonical ZIP;
snapshots;
frozen experimental data;
Zenodo deposit.

This is a post-publication
interpretive comparison.

No commit or push
during document creation.

STATUS:

PHASE10 DMO006 TARGETED PRIOR ART COMPARISON DOCUMENTED

DMO006 CROSS LEVEL PRESERVATION REMAINS OPEN
