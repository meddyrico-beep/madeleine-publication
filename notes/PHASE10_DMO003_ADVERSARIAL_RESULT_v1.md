# MADELEINE — PHASE 10 — DMO-003 ADVERSARIAL RESULT v1

## Target

Claim:

C016

Demo:

DMO-003

Frozen scientific target:

v0.2.1

Commit:

fee2c31cfa17159a4075e1cbfbfa7e2fceba9c4b

Evidence class:

F — Formal

---

## 1. Audited construction

DMO-003 considers:

c = (x_+,x_-,y_+,y_-,z_+,z_-)

with integer channel values in:

{0,...,m}

and the projection:

P(c) =
(
x_+ - x_-,
y_+ - y_-,
z_+ - z_-
).

The audit treats:

m in N,
m >= 1.

---

## 2. Image audit

For one coordinate:

d = a-b

with:

a,b in {0,...,m}.

Every:

d in {-m,...,m}

is realizable.

For:

d >= 0,

choose:

(a,b) = (d,0).

For:

d < 0,

choose:

(a,b) = (0,-d).

Therefore the one-dimensional image is exactly:

{-m,...,m}.

By independence of the three coordinate pairs:

Im(P) = {-m,...,m}^3.

Thus:

|Im(P)| = (2m+1)^3.

SURVIVES.

---

## 3. Exact fiber audit

Fix one coordinate difference:

d = a-b.

If:

d >= 0,

all solutions are:

(a,b) = (d+s,s)

with:

s = 0,...,m-d.

Hence there are:

m-d+1

solutions.

If:

d < 0,

all solutions are:

(a,b) = (s,s-d)

with:

s = 0,...,m+d.

Hence there are:

m+d+1.

Both cases give:

|P_1^(-1)(d)| = m+1-|d|.

For:

v = (d_x,d_y,d_z),

the coordinate pairs are independent.

Therefore:

|P^(-1)(v)| =
(m+1-|d_x|)
(m+1-|d_y|)
(m+1-|d_z|).

SURVIVES.

---

## 4. Structural decomposition exposed by the audit

For each pair:

(a,b),

define:

d = a-b

and:

s = min(a,b).

Then the original pair is recovered uniquely from:

(d,s).

If:

d >= 0,

(a,b) = (d+s,s).

If:

d < 0,

(a,b) = (s,s-d).

The allowed range is:

0 <= s <= m-|d|.

Therefore the two-channel state is equivalently parameterized by:

(d,s)

subject to the declared bounds.

The projection:

(a,b) -> d

forgets exactly the coordinate:

s.

In MADELEINE language, s measures simultaneous common activation of the two opposed channels.

This is a mathematical description of the distinction removed by the net-difference projection.

It does not establish that this distinction has physical meaning.

---

## 5. Three-axis decomposition

Applying the previous result independently to the three axes gives the exact parameterization:

c
<->
(d_x,d_y,d_z,s_x,s_y,s_z)

where:

d_j in {-m,...,m}

and:

0 <= s_j <= m-|d_j|.

The Cartesian projection retains:

(d_x,d_y,d_z)

and removes:

(s_x,s_y,s_z).

Thus the nontrivial fibers are precisely the allowed common-mode coordinates compatible with a fixed net vector.

---

## 6. Non-injectivity attack

For every:

m >= 1,

the full-domain projection is not injective.

A uniform counterexample valid already at m=1 is:

(a,b) = (0,0)

and:

(a,b) = (1,1).

They are distinct states but:

a-b = 0

in both cases.

Therefore the one-axis projection is non-injective.

Embedding this pair in the six-channel state proves that P is non-injective.

SURVIVES.

---

## 7. Published-example defect

The published theorem also uses:

(1,0)

and:

(2,1)

as a non-injectivity example.

That example requires:

m >= 2.

It is therefore not a valid counterexample for the full stated range:

m >= 1.

This is a local proof-example defect.

It does not invalidate the non-injectivity result because:

(0,0)

and:

(1,1)

provide a valid counterexample for every m >= 1.

A future version should replace or qualify the published example.

---

## 8. Unique-fiber vectors

A three-dimensional fiber has cardinality one exactly when:

m+1-|d_x| = 1,
m+1-|d_y| = 1,
m+1-|d_z| = 1.

Therefore:

|d_x| = |d_y| = |d_z| = m.

For:

m >= 1,

there are exactly:

2^3 = 8

such vectors.

Thus the number of image vectors with multiple preimages is:

(2m+1)^3 - 8.

SURVIVES.

---

## 9. Zero-vector fiber

For:

(d_x,d_y,d_z) = (0,0,0),

the fiber cardinality is:

(m+1)^3.

Equivalently, the zero net vector permits:

s_x,s_y,s_z in {0,...,m}

independently.

SURVIVES.

---

## 10. Exclusivity audit

DMO-003 defines the exclusive domain through:

x_+ x_- = 0,
y_+ y_- = 0,
z_+ z_- = 0.

For one axis this forces:

s = min(a,b) = 0.

Therefore every net coordinate d has exactly one representation:

d >= 0 -> (d,0)

d < 0 -> (0,-d).

Hence the restricted projection is bijective onto:

{-m,...,m}^3.

SURVIVES.

---

## 11. External mathematical positioning

Representing an unrestricted signed quantity as:

x = x^+ - x^-

with:

x^+,x^- >= 0

is standard mathematics and a standard transformation in linear programming.

Without an additional restriction the representation is non-unique because the same nonnegative quantity can be added to both parts without changing their difference.

The canonical positive/negative-part decomposition removes that redundancy by ensuring that positive and negative parts do not coexist at a point.

DMO-003 therefore uses standard mathematical structure.

The exact finite-box fiber count is an elementary counting consequence of that structure.

No independent theorem-level novelty is asserted for these facts.

---

## 12. Strongest justified statement

The strongest formally justified statement is:

Within the declared finite six-channel domain, the net-difference projection loses exactly the common-mode degrees of freedom represented by s_j = min(x_j^+,x_j^-). If opposed channels are required to be exclusive, these degrees of freedom vanish and the representation becomes bijectively equivalent to the signed Cartesian vector.

---

## 13. Statements not justified

DMO-003 does not establish that:

- six channels define a new geometry;
- six channels are intrinsically richer than Cartesian coordinates under every admissible constraint;
- the common-mode coordinates s_j are physically observable;
- simultaneous activation of opposed channels occurs in nature;
- the removed distinctions are dynamically relevant;
- the six-channel representation is universally preferable;
- a new physical dimension has been discovered.

---

## 14. Novelty assessment

Fiber mathematics:

STANDARD_OR_DERIVATIVE.

Positive/negative channel splitting:

STANDARD_OR_DERIVATIVE.

Exact common-mode interpretation:

mathematically immediate from the fiber structure.

Potential MADELEINE-specific significance of retaining s_x,s_y,s_z:

UNDERDETERMINED.

Whether those coordinates participate essentially in later MADELEINE dynamics must be established separately.

---

## 15. Final adversarial verdict

Primary formal verdict:

SURVIVES_WITH_RESTRICTION.

Novelty verdict for the isolated mathematics:

STANDARD_OR_DERIVATIVE.

Evidence class:

F — Formal.

Meaning of the additional common-mode coordinates inside the larger MADELEINE architecture:

UNDERDETERMINED.

Geometric or physical interpretation:

EXTERNAL_VALIDATION_REQUIRED.

---

## 16. Residual issues

R10-DMO003-01:

State m as an integer explicitly in a future version.

R10-DMO003-02:

Replace or qualify the published (1,0)/(2,1) counterexample because it requires m >= 2.

R10-DMO003-03:

Prefer "distinctions removed by the projection" to an unqualified use of "additional information" unless an information measure is explicitly defined.

R10-DMO003-04:

Determine in a later phase whether the common-mode coordinates:

s_x,
s_y,
s_z

are used by MADELEINE dynamics or later canonical operators in a way that cannot be reconstructed from the projected vector alone.

That question is central to the possible system-level originality of the six-channel representation.

---

## 17. Preservation

This audit result is post-publication.

It does not modify:

v0.2.1

or its frozen commit:

fee2c31cfa17159a4075e1cbfbfa7e2fceba9c4b.

Any scientific wording or construction change belongs to a later version.
