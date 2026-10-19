# MADELEINE — PHASE 10 — DMO-006 ADVERSARIAL RESULT v1

## Target

Claim:

C030

Demo:

DMO-006

Frozen scientific target:

v0.2.1

Commit:

fee2c31cfa17159a4075e1cbfbfa7e2fceba9c4b

Evidence classes:

F — Formal

M — Methodological

---

## 1. Audited construction

Let:

T : X -> Y

with finite declared sets X and Y.

For every:

y in T(X)

define the fiber:

T^(-1)(y)
=
{x in X : T(x)=y}.

DMO-006 defines:

E(T) = |X| - |T(X)|,

P(T) =
sum_y binom(|T^(-1)(y)|,2),

and:

U(T) = |Y| - |T(X)|.

---

## 2. Fiber identity for E(T)

The nonempty fibers partition X.

Therefore:

|X|
=
sum_{y in T(X)}
|T^(-1)(y)|.

Since the number of nonempty fibers is:

|T(X)|,

we obtain:

|X|-|T(X)|
=
sum_{y in T(X)}
(
|T^(-1)(y)|-1
).

Therefore:

E(T)
=
sum_{y in T(X)}
(
|T^(-1)(y)|-1
).

SURVIVES.

---

## 3. Injectivity audit

A map is injective exactly when every nonempty fiber has cardinality one.

Therefore, for finite X:

E(T)=0

if and only if:

T is injective.

Likewise:

P(T)=0

if and only if every fiber contains at most one element.

Thus:

P(T)=0

if and only if:

T is injective.

SURVIVES.

---

## 4. Surjectivity audit

By definition:

U(T)
=
|Y|-|T(X)|.

For finite sets:

U(T)=0

if and only if:

|T(X)|=|Y|.

Because:

T(X) subseteq Y,

this occurs exactly when:

T(X)=Y.

Therefore:

U(T)=0

if and only if T is surjective.

SURVIVES.

---

## 5. Bijection audit

Within the finite declared domain:

T is bijective

if and only if:

T is injective and surjective.

Therefore:

T bijective
iff
E(T)=0 and U(T)=0.

Equivalently:

T bijective
iff
P(T)=0 and U(T)=0.

SURVIVES.

This establishes equivalence only at the level of the declared sets.

---

## 6. Dependence between E(T) and U(T)

From the definitions:

E(T)=|X|-|T(X)|

and:

U(T)=|Y|-|T(X)|.

Subtracting gives:

E(T)-U(T)
=
|X|-|Y|.

Therefore, when the source and target sets are fixed:

E(T)

and:

U(T)

are not numerically independent quantities.

Knowing one of them together with:

|X|

and:

|Y|

determines the other.

Their interpretations remain different:

E describes collapsed source distinctions,

while:

U describes declared target states outside the image.

But they should not be interpreted as independent evidence.

---

## 7. P(T) is distinct from E(T)

For a fiber of size n:

its contribution to E is:

n-1.

Its contribution to P is:

n(n-1)/2.

For n=3:

E contribution = 2,

P contribution = 3.

Therefore E and P are distinct summaries.

SURVIVES.

---

## 8. Adversarial completeness attack

The triple:

(E,P,U)

does not uniquely determine the fiber structure.

Consider:

|X|=9

and:

|Y|=3,

with a surjective map.

Translation A has fiber sizes:

(5,2,2).

Then:

E_A
=
(5-1)+(2-1)+(2-1)
=
6.

Also:

P_A
=
binom(5,2)
+
binom(2,2)
+
binom(2,2)
=
10+1+1
=
12.

And:

U_A=0.

Now consider Translation B with fiber sizes:

(4,4,1).

Then:

E_B
=
(4-1)+(4-1)+(1-1)
=
6.

Also:

P_B
=
binom(4,2)
+
binom(4,2)
+
binom(1,2)
=
6+6+0
=
12.

And:

U_B=0.

Therefore:

(E_A,P_A,U_A)
=
(E_B,P_B,U_B)
=
(6,12,0),

while the fiber structures are different.

Thus:

(E,P,U)

is not a complete invariant of a translation.

This does not invalidate DMO-006 because the executable also records the fiber sizes.

It restricts how strongly the three scalar summaries may be interpreted.

---

## 9. Importance of the fibers

The fundamental structure induced by T is the partition:

x ~_T x'

if and only if:

T(x)=T(x').

The equivalence classes are exactly the fibers of T.

A non-injective translation identifies multiple source states inside the same class.

Therefore the full fiber partition contains structural information not recoverable in general from:

E,
P,
U

alone.

The strongest audit architecture is therefore:

T
->
fiber partition
->
derived summaries E,P,U.

Not:

T
->
E,P,U
->
complete reconstruction of T.

---

## 10. Case 1 — bijective relabeling

For a one-to-one and onto relabeling:

E=0,
P=0,
U=0.

The map is bijective.

SURVIVES.

The correct statement is:

the two declared sets are in one-to-one correspondence.

No additional algebraic, dynamical, geometric or physical equivalence follows automatically.

---

## 11. Case 2 — coarse-graining

For the parity map from four source states to two target classes:

fiber sizes are:

(2,2).

Therefore:

E=2,

P=2,

U=0.

The map is surjective but not injective.

Distinct source states become indistinguishable after applying T.

SURVIVES.

---

## 12. Case 3 — derived representation

The map:

x -> (x, x mod 2)

is injective.

The second coordinate is a deterministic function of x.

Therefore it introduces no additional independent degree of freedom relative to x.

The target set declared by DMO-006 is larger than the image.

Thus:

U>0.

SURVIVES.

However, the expression:

"no independent information"

should be interpreted structurally unless an explicit information-theoretic quantity is defined.

DMO-006 does not compute:

entropy,
mutual information,
channel capacity,
or physical information.

---

## 13. Case 4 and DMO-003

For:

T(a,b)=a-b

on:

{0,1}^2,

the states:

(0,0)

and:

(1,1)

share the image:

0.

Therefore T is non-injective.

The result agrees with the DMO-003 fiber analysis.

SURVIVES.

---

## 14. Case 5 — exclusivity

Restricting the source to:

(0,0),
(1,0),
(0,1)

makes:

T(a,b)=a-b

bijective onto:

{-1,0,1}.

Therefore the presence or absence of collapse depends on the declared source domain.

SURVIVES.

This reinforces the Phase 10 DMO-003 result:

projection loss is not a property of the symbolic formula alone.

It depends on which source states are admissible.

---

## 15. Meaning of "loss"

DMO-006 establishes loss in the following restricted sense:

two or more distinct elements of X may become unrecoverable from T(x) alone because they share the same image.

This is loss of source distinctions under the mapping.

It is not automatically:

Shannon-information loss,
physical-information loss,
thermodynamic entropy production,
semantic loss,
or experimental uncertainty.

Those notions require additional structures and definitions.

---

## 16. Meaning of "gain"

A larger representation space does not by itself establish independent new information.

The derived-coordinate example demonstrates this correctly.

However:

U(T)

is a measure of unreachable declared target states.

It is not a general measure of informational gain.

DMO-006 currently has no scalar:

G(T)

that quantifies independent gained information.

Therefore wording about "gain" must remain representational rather than information-theoretic.

---

## 17. External mathematical positioning

The mathematics used by DMO-006 belongs to standard set theory.

Fibers of a function determine a partition of the source.

Injectivity means distinct source elements have distinct images.

Surjectivity means the image equals the codomain.

Bijection means simultaneous injectivity and surjectivity.

A bijection establishes one-to-one correspondence of sets.

Consequently the isolated mathematical identities of DMO-006 are not treated as new theorem-level results.

---

## 18. Strongest justified statement

The strongest justified statement is:

For a finite declared translation T:X->Y, the fiber structure determines exactly which source states become identified by the translation. E(T), P(T), and U(T) provide useful scalar summaries of source collapse, pairwise collisions, and unreachable targets, but they do not completely characterize the translation or its fiber partition. Bijection guarantees only set-level one-to-one correspondence unless preservation of additional structure is separately demonstrated.

---

## 19. Statements not justified

DMO-006 does not establish that:

- E, P and U uniquely characterize a translation;
- E, P and U are statistically independent;
- U measures informational gain;
- E measures Shannon-information loss;
- a bijection preserves dynamics;
- a bijection preserves algebraic structure;
- a bijection preserves geometry;
- a bijection establishes physical equivalence;
- all relevant MADELEINE translations are finite;
- every cross-level translation can be reduced to these three scalars.

---

## 20. Novelty assessment

Injectivity and surjectivity criteria:

STANDARD_OR_DERIVATIVE.

Fiber partition:

STANDARD_OR_DERIVATIVE.

Finite cardinality identities:

STANDARD_OR_DERIVATIVE.

Collision-pair counting:

STANDARD_OR_DERIVATIVE.

Bijection as set-level equivalence:

STANDARD_OR_DERIVATIVE.

Specific organization of:

fibers,
E(T),
P(T),
U(T)

as a MADELEINE translation-audit protocol:

SYSTEM-SPECIFIC.

Broader novelty or utility of that exact audit vector:

UNDERDETERMINED.

---

## 21. Final adversarial verdict

Finite mathematical identities:

SURVIVES.

Six implemented examples:

SURVIVE within their declared finite domains.

Use of fibers as translation accounting:

SURVIVES.

Use of E,P,U as diagnostic summaries:

SURVIVES_WITH_RESTRICTION.

Interpretation of E,P,U as a complete translation invariant:

NOT JUSTIFIED.

Interpretation of E and U as independent evidence:

NOT JUSTIFIED.

Mathematical novelty of the isolated results:

STANDARD_OR_DERIVATIVE.

MADELEINE-specific audit organization:

PRESERVED AS A POSSIBLE SYSTEM-LEVEL CONTRIBUTION.

Dynamic, geometric or physical equivalence:

EXTERNAL_VALIDATION_REQUIRED.

---

## 22. Residual issues

R10-DMO006-01:

Future wording should distinguish:

fiber structure

from:

scalar summaries E,P,U.

R10-DMO006-02:

Record explicitly the identity:

E(T)-U(T)=|X|-|Y|.

R10-DMO006-03:

Do not describe U(T) as informational gain.

It counts declared target states outside the image.

R10-DMO006-04:

Use "loss of source distinctions under T" rather than unqualified "information loss" unless an information measure is defined.

R10-DMO006-05:

If translation between richer structures is required, define the preservation conditions explicitly.

Examples may include preservation of:

operations,
transition laws,
metric structure,
topology,
order,
or probability law.

R10-DMO006-06:

Do not use E,P,U alone to classify translations as equivalent.

Different fiber profiles can share the same triple.

---

## 23. Consequence for C030

The core caution in C030 survives:

translation must not be treated as automatic equivalence.

The strongest future wording should emphasize:

- source distinctions identified by fibers;
- image reachability;
- representation changes;
- explicit preservation requirements for any additional structure.

A stronger assertion that E,P,U form a complete theory of translation is not justified.

---

## 24. Preservation

This audit result is post-publication.

It does not modify:

v0.2.1

or its frozen commit:

fee2c31cfa17159a4075e1cbfbfa7e2fceba9c4b.

Any scientific wording, metric or translation change resulting from this audit belongs to a later version.
