# MADELEINE — PHASE 10 — DMO-005 ADVERSARIAL RESULT v1

## Target

Claim:

C026

Demo:

DMO-005

Frozen scientific target:

v0.2.1

Commit:

fee2c31cfa17159a4075e1cbfbfa7e2fceba9c4b

Evidence classes:

F — Formal

M — Methodological

---

## 1. Audited definition

For every valid reading L, DMO-005 defines:

K(L) = (M,W,k,G,T)

where:

M = metric schema,
W = window size,
k = history depth,
G = regime-gate version,
T = traceability schema.

Direct comparability is defined by:

L1 ~ L2

if and only if:

K(L1) = K(L2).

The comparison:

Delta M = M_B - M_A

is enabled only inside the same contract class.

---

## 2. Formal equivalence-relation audit

The relation:

L1 ~ L2
iff
K(L1) = K(L2)

inherits the elementary properties of equality.

Reflexivity:

K(L) = K(L).

Therefore:

L ~ L.

Symmetry:

K(L1) = K(L2)

implies:

K(L2) = K(L1).

Therefore:

L1 ~ L2
implies
L2 ~ L1.

Transitivity:

K(L1) = K(L2)

and:

K(L2) = K(L3)

imply:

K(L1) = K(L3).

Therefore:

L1 ~ L2
and
L2 ~ L3

imply:

L1 ~ L3.

The formal result survives.

SURVIVES.

However, the result follows immediately from equality of K.

It is not an independent theorem-level novelty.

---

## 3. Equivalence classes

Because the relation is equality under the map K, it partitions valid readings into fibers:

[L] = {L' : K(L') = K(L)}.

This is mathematically correct.

The classes are exactly the inverse images of contract values under K.

SURVIVES.

The construction is standard.

---

## 4. Difference antisymmetry

For comparable readings:

Delta M_(B-A) = M_B - M_A.

Reversing order gives:

Delta M_(A-B) = M_A - M_B.

Therefore:

Delta M_(B-A) = -Delta M_(A-B).

SURVIVES.

This is an elementary arithmetic identity and does not constitute independent mathematical novelty.

---

## 5. Gate implementation

The executable rejects direct comparison when the readings differ in:

metric schema,
window size,
history depth,
regime-gate version,
or trace schema.

It also rejects internally malformed readings.

For identical contracts it enables componentwise subtraction.

The executable therefore implements the declared rule consistently.

SURVIVES.

---

## 6. Central adversarial distinction

DMO-005 defines a conservative rule for direct comparison:

same K
->
direct componentwise comparison allowed.

This does not establish the converse scientific statement:

scientifically comparable
->
same K required.

Different measurement or observation contracts can in principle become comparable through:

calibration,
traceability to a common reference,
explicit transformations,
validated mappings,
measurement invariance,
or other bridges.

Therefore equality of K is a sufficient condition inside the DMO-005 rule.

It has not been demonstrated to be a universally necessary condition for scientific comparability.

---

## 7. C026 wording audit

C026 currently states, in general form, that two readings are comparable only when they share minimum criteria.

The strongest audited formulation should be narrower:

Under DMO-005, direct componentwise comparison is permitted only between internally valid readings that share the declared reading contract K.

This formulation survives.

A universal reading of:

only identical contracts can ever be compared

is not justified.

SURVIVES_WITH_RESTRICTION.

---

## 8. Metric-schema weakness

In the executable, M is represented by metric names:

for example:

A0,
A1,
P_rel,
N,
U.

Equality of names and order does not independently verify equality of:

mathematical definition,
implementation version,
normalization,
units,
calibration,
or code.

Therefore two readings could satisfy:

metric_schema_A = metric_schema_B

while the meaning of a metric has changed outside the structure represented by the tuple.

The current repository may prevent such changes procedurally, but DMO-005 itself does not encode that guarantee.

Thus metric-schema equality is a structural compatibility check.

It is not by itself proof of measurement equivalence.

---

## 9. Trace-schema weakness

T is represented in the executable as a tuple of field names such as:

rule_version,
seed,
parameters,
window,
series_hash.

DMO-005 compares the schema:

which trace fields exist.

It does not compare the actual trace values.

Therefore two readings can have:

T_A = T_B

while possessing different:

rule versions,
seeds,
parameters,
or series hashes.

This is not necessarily an error.

Different runs often need different provenance values in order to be compared.

But the exact meaning must remain:

compatible trace schema,

not:

identical provenance.

---

## 10. Regime-gate equality

DMO-005 requires the same regime-gate version.

This is a defensible conservative rule for direct comparison.

However, two different gate versions might later be shown equivalent or explicitly translatable.

DMO-005 does not provide such a translation.

Therefore rejection of differing gate versions means:

not directly comparable under DMO-005.

It does not mean:

scientifically incomparable under every possible bridge.

---

## 11. Window and history depth

DMO-005 requires exact equality of:

W

and:

k.

This prevents naive componentwise comparison across different observation scales or historical depths.

That restriction is methodologically conservative.

It is not demonstrated to be mathematically necessary in all cases.

A later transformation might relate measurements across:

different windows,
different resolutions,
or different history-depth conventions.

Such a bridge is outside DMO-005.

---

## 12. External metrological positioning

Established metrology distinguishes comparability from identity of complete measurement procedures.

Metrological comparability is based on measurement results being traceable to the same reference.

Thus exact equality of every procedural detail is not a universal definition of comparability.

DMO-005 should therefore be interpreted as a stronger internal compatibility rule for direct comparison, not as a replacement for general metrological comparability theory.

---

## 13. External measurement-invariance positioning

Other scientific fields likewise treat comparability through explicitly tested invariance conditions.

Comparability may be justified after establishing appropriate levels of measurement invariance rather than requiring literal identity of the entire observational procedure.

This again shows that:

K(L1) = K(L2)

is one conservative construction of direct comparability.

It is not established as the unique possible construction.

---

## 14. Necessary versus sufficient conditions

Within DMO-005:

K(L1) = K(L2)

is necessary by definition for the relation:

L1 ~ L2.

But this is definitional necessity.

It is not evidence that exact K equality is necessary for every scientifically legitimate comparison.

Similarly, same K permits the numerical subtraction implemented by the demo.

But same K alone has not been demonstrated to guarantee that:

the metrics are externally valid,
the quantities have the same physical meaning,
or the observed systems instantiate the same phenomenon.

Therefore the scientific sufficiency of K is:

UNDERDETERMINED.

---

## 15. Strongest justified statement

The strongest justified statement is:

DMO-005 defines an auditable equivalence relation of direct comparability among internally valid MADELEINE readings by requiring exact equality of the declared reading contract K. Within a single contract class, componentwise differences can be computed without simultaneously changing the represented metric schema, window size, history depth, regime-gate version or trace schema.

---

## 16. Statements not justified

DMO-005 does not establish that:

- exact contract equality is universally necessary for comparison;
- exact contract equality is sufficient for physical equivalence;
- the selected coordinates of K are the unique minimal comparability criteria;
- equal metric names imply identical metric definitions;
- equal trace schemas imply equal provenance;
- readings from different contracts can never be translated;
- a small Delta M implies physical similarity;
- a large Delta M implies scientifically meaningful difference;
- the metrics themselves are universally valid.

---

## 17. Novelty assessment

Equality-based equivalence relation:

STANDARD_OR_DERIVATIVE.

Partition into equality classes:

STANDARD_OR_DERIVATIVE.

Antisymmetry of vector differences:

STANDARD_OR_DERIVATIVE.

General idea of controlling comparability through common measurement conditions and traceability:

STANDARD_OR_DERIVATIVE.

Specific contract:

K = (M,W,k,G,T)

and its integration into MADELEINE:

SYSTEM-SPECIFIC.

Whether this exact contract is minimal, sufficient or generally useful beyond the current system:

UNDERDETERMINED.

---

## 18. Final adversarial verdict

Formal equivalence relation:

SURVIVES.

Executable gate:

SURVIVES.

Direct componentwise comparability under identical K:

SURVIVES_WITH_RESTRICTION.

Universal necessity of identical K:

NOT JUSTIFIED.

Scientific sufficiency of K:

UNDERDETERMINED.

Mathematical novelty of the isolated result:

STANDARD_OR_DERIVATIVE.

System-specific methodological architecture:

PRESERVED AS A POSSIBLE MADELEINE CONTRIBUTION.

External physical equivalence:

NOT ESTABLISHED.

---

## 19. Future strengthening

A later version could strengthen K by versioning or hashing the actual definitions behind its components.

For example:

M* =
(
metric identifiers,
metric versions,
definition or implementation hashes,
units or normalization contracts
).

Likewise, traceability could distinguish explicitly between:

trace schema compatibility

and:

trace content/provenance.

A future translation object:

J(K1,K2)

could define when two different contracts are legitimately comparable after a declared transformation.

That would extend DMO-005 without modifying its frozen v0.2.1 meaning.

---

## 20. Residual issues

R10-DMO005-01:

Narrow C026 from universal comparability to direct comparability under the declared MADELEINE contract.

R10-DMO005-02:

Distinguish trace-schema equality from provenance equality.

R10-DMO005-03:

Version or hash metric definitions in a future contract if cross-version comparison becomes important.

R10-DMO005-04:

Do not describe equality of K as a proven minimal or universal set of comparability requirements.

R10-DMO005-05:

Use DMO-006 or a later explicit bridge to study comparability across different contracts.

---

## 21. Preservation

This audit result is post-publication.

It does not modify:

v0.2.1

or its frozen commit:

fee2c31cfa17159a4075e1cbfbfa7e2fceba9c4b.

Any scientific wording or contract change resulting from this audit belongs to a later version.
