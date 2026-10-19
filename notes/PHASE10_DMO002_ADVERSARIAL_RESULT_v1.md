# MADELEINE — PHASE 10 — DMO-002 ADVERSARIAL RESULT v1

## Target

Claim:

C014

Demo:

DMO-002

Frozen scientific target:

v0.2.1

Commit:

fee2c31cfa17159a4075e1cbfbfa7e2fceba9c4b

Evidence class:

F — Formal

---

## 1. Audited proposition

For a history

H = (x_0,...,x_n)

with:

x_0 = 0

and integer states:

x_i in {0,...,m},

DMO-002 defines:

delta(H) = sum |x_(i+1) - x_i|.

The principal proposition states:

Delta_n^(m) = {0,1,...,mn}.

Therefore:

|Delta_n^(m)| = mn + 1.

---

## 2. Domain clarification

The statement requires explicitly:

m,n in N

with:

m >= 1
n >= 1.

The published formulation uses the discrete set {0,...,m} and therefore already relies implicitly on m being an integer.

This is a notational/domain precision issue.

It does not defeat the proposition.

A future version should state the integer domain explicitly.

---

## 3. Independent logical attack

Let:

k in {0,...,mn}.

Write by Euclidean division:

k = qm + r,

with:

0 <= r < m.

Use q full jumps of length m, alternating between 0 and m.

They contribute:

qm.

If:

r = 0,

the remaining transitions may be zero-length stays.

If:

r > 0,

then from:

qm + r <= mn

and:

r > 0

it follows that:

q <= n - 1.

Therefore at least one transition remains available.

After q full jumps the current state is one of the two endpoints:

0 or m.

A residual jump of length r may therefore be taken as:

0 -> r

or:

m -> m-r.

Both endpoints belong to:

{0,...,m}.

All remaining transitions may be zero-length stays.

Thus every integer:

k in {0,...,mn}

is realizable.

The reverse inclusion follows because each of the n transitions has length at most m.

Therefore the proposition survives.

---

## 4. Boundary attacks

### k = 0

Use only zero-length stays.

SURVIVES.

### k = mn

Here:

q = n
r = 0.

Use n alternating full jumps of length m.

SURVIVES.

### n = 1

Possible total variations are exactly:

0,...,m.

SURVIVES.

### m = 1

Each transition contributes either 0 or 1.

Every total:

0,...,n

can be realized.

SURVIVES.

### residual case

For:

0 < r < m,

q <= n-1 guarantees the residual transition fits within the transition budget.

SURVIVES.

No logical counterexample was identified within the declared domain.

---

## 5. Corollary audit

### Fixed n does not determine delta

For fixed:

m >= 1
n >= 1,

the set Delta_n^(m) contains more than one value.

Therefore n alone does not determine delta.

SURVIVES.

### Delta does not determine n

The value:

delta = 1

can occur for every:

n >= 1

through:

0 -> 1

followed by zero-length stays.

Therefore delta alone does not determine n across histories of different lengths.

SURVIVES.

---

## 6. Strongest justified statement

The strongest statement currently justified is:

Within the discrete DMO-002 domain, the transition count n and accumulated variation delta are non-redundant coordinates: neither determines the other over the declared family of histories.

---

## 7. Stronger statements not justified

DMO-002 does not establish that:

- every possible notion of counting and measuring is irreducible;
- counting and measurement are universally independent;
- n and delta are statistically independent;
- n and delta are algebraically independent;
- the construction describes physical time or physical distance;
- the proposition constitutes a universal theory of measurement.

Any such extension requires additional definitions and evidence.

---

## 8. External mathematical positioning

The quantity:

sum |x_(i+1) - x_i|

belongs to the standard mathematical family of total-variation or path-variation constructions.

Classical bounded-variation theory uses sums of absolute consecutive increments.

Discrete optimization and signal-processing literature likewise uses adjacent absolute differences as discrete total-variation terms.

The DMO-002 proposition is therefore built from standard mathematical objects.

A first literature pass did not identify an exact source for the particular reachability statement:

Delta_n^(m) = {0,...,mn}.

Absence of such a source in the first pass is not evidence of novelty.

Because the proof is elementary and derives from standard discrete variation and Euclidean division, no independent theorem-level novelty is asserted at this stage.

---

## 9. Novelty assessment

Mathematical correctness:

SURVIVES.

Generality:

RESTRICTED TO THE DECLARED FINITE DISCRETE DOMAIN.

Provisional mathematical novelty:

STANDARD_OR_DERIVATIVE.

Potential MADELEINE-specific value:

the use of the double register as part of the wider architectural and methodological system may still carry structural relevance even if the isolated proposition is elementary.

That wider contribution is not established by DMO-002 alone.

---

## 10. Final adversarial verdict

Primary verdict:

SURVIVES_WITH_RESTRICTION.

Novelty verdict:

STANDARD_OR_DERIVATIVE.

Evidence class:

F — Formal.

External physical validation:

NOT APPLICABLE TO THE FINITE THEOREM ITSELF.

Any physical or universal interpretation:

EXTERNAL_VALIDATION_REQUIRED.

---

## 11. Residual issues

R10-DMO002-01:

The integer nature of m and n should be explicit in a future version.

R10-DMO002-02:

The term "irreducible" should not be used as a stronger synonym for non-determination unless a specific mathematical notion of irreducibility is defined.

R10-DMO002-03:

A deeper literature search is still required before making any claim of novelty for the exact reachability formula.

---

## 12. Preservation

This audit result is post-publication.

It does not modify:

v0.2.1

or its commit:

fee2c31cfa17159a4075e1cbfbfa7e2fceba9c4b.

Any scientific wording change resulting from this audit belongs to a later version.
