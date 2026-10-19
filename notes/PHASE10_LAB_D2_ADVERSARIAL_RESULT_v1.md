# MADELEINE — PHASE 10 — LAB-D2 ADVERSARIAL RESULT v1

## Target

Experiment:

LAB-D2-v1

Frozen scientific target:

v0.2.1

Frozen release commit:

fee2c31cfa17159a4075e1cbfbfa7e2fceba9c4b

Evidence classes:

F — Formal

C — Computational

M — Methodological

---

## 1. Audit scope

LAB-D2 is not canonical D2.

It is the flexible second-order synthetic candidate of:

LAB-FEN-001-v1.

Its frozen local objective is simultaneous satisfaction of:

A1,
Delta_hist,
C_hist,
P_rel,
N,
U

under thresholds calibrated before LAB-D2 execution.

This audit does not execute new experiments.

---

## 2. Frozen provenance

Repository history records:

LAB-D2 specification:

cd0f30b433d7e65dfd11ff64862688d29ddf9a8a

initial frozen executable:

4d9e6772da2be6eb66fa81f431adcd6e4e5831ef

serialization-only correction:

3286cd6e92e94caeec2c7f924b7360cae88be025

recorded result:

3e984cdbc124b10f1ce503dda25585402d868f95

Therefore the scientific specification precedes the executable and the recorded result.

SURVIVES.

---

## 3. Serialization incident

The first complete numerical evaluation produced:

8/8 seed passes

before output serialization failed because dictionaries in the structural report contained tuple keys.

The later code modification changes only JSON serialization of:

family_sizes

and:

out_degrees

by replacing tuple keys with string keys.

The generator, metrics, thresholds, seeds and gate logic are unchanged in that diff.

Therefore the serialization repair does not constitute scientific retuning of LAB-D2.

SURVIVES.

---

## 4. Generator

For:

a=x_(t-1)

and:

b=x_t,

LAB-D2 defines:

h(a,b)
=
b+2a mod 5.

Allowed successors are:

S(a,b)
=
{
h(a,b),
h(a,b)+1,
h(a,b)+2
}
mod 5.

The next state is selected uniformly from these three values.

Thus:

P(c|a,b)
=
1/3

for:

c in S(a,b),

and zero otherwise.

The dependence on the previous state is explicit in the generator.

---

## 5. Second-order state graph

The natural causal state is:

z_t
=
(x_(t-1),x_t).

There are:

25

such pair states.

Every pair state has exactly:

3

outgoing transitions.

The frozen implementation verifies:

25 nodes,
75 edges,
75 allowed trigram transitions,
strong connectivity,
and the declared self-loops.

These structural checks survive.

---

## 6. Exact incoming degree

Consider a target pair:

(b,c).

A predecessor has the form:

(a,b).

Such a transition exists exactly when:

c
=
b+2a+k mod 5

for one of:

k in {0,1,2}.

For every fixed k:

2a
=
c-b-k mod 5.

Because 2 is invertible modulo 5, this congruence has exactly one solution a.

The three values of k produce three distinct predecessors.

Therefore every pair state also has:

3

incoming transitions.

Thus the pair-state graph is directed 3-regular.

---

## 7. Uniform stationary distribution

Transitions from each pair state assign probability:

1/3

to each outgoing edge.

Because every pair state has exactly three incoming edges, the uniform distribution:

pi(a,b)=1/25

is stationary.

The frozen graph is strongly connected.

It also contains self-loops.

Therefore the finite pair-state Markov chain is irreducible and aperiodic.

Consequently it possesses a unique stationary distribution, which is the uniform distribution above.

This formal structure explains much of the observed signature.

---

## 8. Historical dependence under stationarity

Under:

pi(a,b)=1/25,

the previous and current symbols are uniform across the 25 pairs.

For a known pair:

(a,b),

the next symbol is uniform over three allowed successors.

Therefore:

H(X_(t+1) | X_(t-1),X_t)
=
ln 3.

For a fixed present state b, the five possible previous states and three branch choices distribute the next state uniformly across all five symbols.

Thus:

P(c|b)=1/5

and:

H(X_(t+1)|X_t)
=
ln 5.

Therefore the exact conditional information is:

I(
X_(t-1);
X_(t+1)
|
X_t
)
=
ln(5/3).

Numerically this is approximately:

0.5108 nats.

---

## 9. Consequence for A1

The later observed A1 values are approximately:

0.507 to 0.509.

A1 subtracts the p95 Markov-1 null estimate from the observed conditional-information estimate.

Therefore the observed magnitude is consistent with the structural value:

ln(5/3)

minus a small finite-sample/null correction.

The positive A1 signal is real under the metric.

However its approximate magnitude is largely predictable from the frozen generator.

It is not an unexpected emergent quantity.

---

## 10. Consequence for Delta_hist

At the ideal stationary limit:

a first-order predictor conditioned only on the current state sees approximately:

P(c|b)=1/5.

Its optimal negative log-likelihood is therefore:

ln 5.

The second-order predictor sees:

P(c|a,b)=1/3

on the true successor.

Its optimal negative log-likelihood is:

ln 3.

Therefore the ideal predictive gain is:

Delta_hist
=
ln 5-ln 3
=
ln(5/3).

The observed values near:

0.508 to 0.510

are again consistent with the direct analytical consequence of the generator.

SURVIVES.

But the magnitude is not independent evidence of a new phenomenon.

---

## 11. Consequence for C_hist

For a given pair context, the second-order law is uniform on three states:

1/3,
1/3,
1/3,
0,
0

up to permutation.

The first-order law is uniform on all five:

1/5,
1/5,
1/5,
1/5,
1/5.

Their total-variation distance is:

TV
=
1/2
[
3 |1/3-1/5|
+
2 |0-1/5|
]
=
0.4.

The observed C_hist values are approximately:

0.3985 to 0.3988.

Thus the observed C_hist magnitude is almost exactly the structural prediction of the frozen generator.

SURVIVES.

Again, this is not an independent unexpected discovery.

---

## 12. Non-independence of the historical coordinates

A1,
Delta_hist,
and C_hist

all react to the same designed contrast:

the future is uniform over five states when only x_t is used,

but restricted to three states when:

(x_(t-1),x_t)

is used.

They are mathematically different summaries.

However in LAB-D2 they are not three independent sources of evidence for three independent phenomena.

They are multiple diagnostics of the same implanted second-order structure.

Therefore:

three historical coordinates PASS

must not be interpreted as:

three independent confirmations.

---

## 13. Exact trigram support

There are:

25

pair contexts.

Each admits exactly:

3

successors.

Therefore the support contains exactly:

75

allowed trigram states out of the:

125

possible trigrams over five symbols.

The frozen implementation verifies this value directly.

SURVIVES.

---

## 14. Stationary trigram distribution

Under the uniform pair-state stationary distribution:

P(a,b)=1/25.

Within a pair:

P(c|a,b)=1/3

for every allowed successor.

Therefore every allowed trigram has probability:

1/75.

Thus the stationary trigram distribution is uniform over the 75 allowed trigrams.

---

## 15. Consequence for N

For a uniform distribution over 75 trigram states:

H_3
=
ln 75.

Therefore:

D_3
=
exp(H_3)
=
75.

LAB-FEN-001 defines:

N
=
D_3/125.

Hence the structural stationary value is:

N
=
75/125
=
0.6.

The observed values are approximately:

0.5978 to 0.5985.

Thus LAB-D2 almost saturates the maximum diversity permitted by its explicitly constructed 75-trigram support.

The result:

N > T_N

SURVIVES.

But interpreting this as spontaneously emergent novelty is NOT JUSTIFIED.

It is primarily a measure of nearly uniform occupancy of the generator's declared support.

---

## 16. Meaning of novelty

In LAB-D2, N measures diversity of empirical trigram occupancy.

It does not demonstrate:

new information ex nihilo,
creative generation,
novel physical states,
or histories outside the predeclared support.

Every observed trigram belongs to a support explicitly determined before execution.

Therefore the safe wording is:

high normalized historical diversity inside the allowed support.

Not:

emergent novelty in an unrestricted sense.

---

## 17. Consequence for P_rel

P_rel is defined as:

1
-
D_within / D_null.

LAB-D2 is a homogeneous finite irreducible aperiodic Markov chain on pair states.

For sufficiently long windows, empirical trigram distributions from different windows converge toward the same stationary trigram distribution.

Therefore:

D_within

is expected to become small.

The Markov-1 surrogate lacks the designed pair-dependent trigram law, so:

D_null

remains positive.

Hence:

P_rel

is expected to be large and tends toward one in the long-window limit when the denominator remains positive.

The observed values:

approximately 0.914 to 0.941

are consistent with this mechanism.

---

## 18. Interpretation of persistence

The P_rel result survives operationally.

However a high P_rel in this experiment may largely express:

stationarity of one homogeneous Markov-2 law

plus:

distance from its Markov-1 surrogate.

It is therefore not automatically a distinct phenomenon of long-memory persistence.

Verdict:

SURVIVES_WITH_RESTRICTION.

Its independence from the historical contrast is UNDERDETERMINED.

---

## 19. Consequence for U

LAB-D2 has stochastic branching at every pair context.

Its pair-state graph is irreducible and contains self-loops, hence is aperiodic in the Markov-chain sense.

The frozen U detector additionally finds no dominant recurrence period in its tested finite lag range.

Observed:

U approximately 0.983 to 0.986.

This operational result:

SURVIVES.

However U-v1 examines only finite lags up to its declared cutoff.

It is not a proof of mathematical aperiodicity of every possible trajectory.

---

## 20. U is not specific to LAB-D2

LAB-D0 also produced a high U value.

Therefore high U distinguishes LAB-D2 from the rigid LAB-D1 endpoint but does not by itself distinguish D2 from an open first-order stochastic process.

The scientific role of LAB-D2 is the conjunction:

history plus high U,

not high U alone.

Thus U is an additional gate coordinate, not independent evidence for historical structure.

---

## 21. Second-order versus first-order on expanded state

Relative to the scalar observable:

x_t in S,

LAB-D2 is genuinely second order.

However define the expanded state:

z_t
=
(x_(t-1),x_t).

Then:

z_(t+1)
=
(x_t,x_(t+1))

depends probabilistically only on:

z_t.

Therefore LAB-D2 is a first-order Markov chain on:

S^2.

This is a standard state-space lifting of a finite higher-order Markov process.

---

## 22. Consequence for "irreducible history"

LAB-D2 cannot support an unrestricted statement:

"the process is irreducible to first order."

It is reducible to first order by expanding the state to the ordered pair.

A restricted statement may survive:

the process is not Markov-1 with respect to the original five-symbol observable x_t.

Therefore any future use of:

irreducible history

must specify the representation with respect to which reducibility is tested.

Absolute irreducibility:

FAILS.

Representation-relative non-Markov-1 structure:

SURVIVES.

---

## 23. Constructive versus emergent result

LAB-D2 was designed after:

the metric definitions,

D0/D1 calibration,

and the thresholds

were already known.

This is methodologically legitimate because the architecture was then frozen before execution.

However LAB-D2 is therefore a targeted construction designed to occupy the desired operational region.

Its PASS should be read primarily as a constructive existence result.

It is not equivalent to discovering an unanticipated regime in unconstrained data.

---

## 24. Threshold meaning

The frozen thresholds:

T_P,
T_N,
T_U

were derived from D0 and D1.

LAB-D2 exceeds all three with large margins.

This establishes an internal classification under the frozen decision rule.

But the thresholds are internal operational boundaries.

They are not universal phase-transition constants.

They were not estimated from external phenomena.

---

## 25. Seed evidence

Unlike deterministic LAB-D1, LAB-D2 uses pseudo-random branch choices throughout each trajectory.

Different seeds therefore generate different internal stochastic realizations of the same architecture.

The observed:

8/8

seed passes provide useful internal seed robustness.

They do not represent:

eight external experiments,
eight independent model classes,
or external replication.

---

## 26. Local candidate PASS

Every frozen seed satisfies simultaneously:

A1 > 0,

Delta_hist > 0 and its null gate,

C_hist > 0 and its null gate,

P_rel > T_P,

N > T_N,

U > T_U.

Therefore according to the frozen protocol:

LAB-D2-v1 LOCAL CANDIDATE PASS

SURVIVES.

The exact permitted label remains:

CANDIDATA INTERNA QUE SUPERA LA FIRMA LOCAL LAB-FEN-001-v1.

---

## 27. What is genuinely established

LAB-D2 establishes a constructive existence result:

there exists a finite frozen stochastic second-order architecture, under the declared LAB-FEN-001-v1 representation and metrics, that simultaneously occupies the desired operational region of:

historical dependence,
stable trigram statistics,
high trigram diversity,
and absence of dominant finite-lag periodicity.

This is stronger than either D0 or D1 alone.

It remains an internal synthetic result.

---

## 28. What is not established

LAB-D2 does not establish:

- spontaneous emergence of historical dependence;
- absolute irreducibility to first-order dynamics;
- independent evidential status of A1, Delta_hist and C_hist;
- emergent novelty from N;
- long-memory persistence distinct from stationarity;
- universal aperiodicity;
- a natural phase transition;
- universality of the thresholds;
- physical memory;
- geometry emergence;
- external empirical validation;
- a unique MADELEINE mechanism;
- inability of simpler alternative Markov constructions to satisfy the same signature.

---

## 29. Simpler-model challenge

The frozen process is itself a compact finite Markov chain on 25 pair states.

Therefore any claim that LAB-D2 demonstrates a fundamentally new class of stochastic dynamics is not supported by this experiment alone.

A critical future novelty question is:

does MADELEINE produce consequences not reproducible by ordinary finite-state Markov models with an augmented state representation?

This question remains open.

---

## 30. Novelty assessment

Finite second-order Markov construction:

STANDARD_OR_DERIVATIVE.

First-order lifting to pair states:

STANDARD_OR_DERIVATIVE.

Conditional-information signature:

STANDARD_OR_DERIVATIVE.

Entropy/effective diversity of finite trigram support:

STANDARD_OR_DERIVATIVE.

Finite-lag recurrence diagnostics:

STANDARD_OR_DERIVATIVE.

Specific conjunction, freezing discipline and audit architecture inside LAB-FEN-001:

SYSTEM-SPECIFIC.

Scientific novelty of LAB-D2 as an isolated dynamical mechanism:

NOT ESTABLISHED.

---

## 31. Final adversarial verdict

Frozen specification-before-result ordering:

SURVIVES.

Serialization correction as non-scientific repair:

SURVIVES.

Structural 25-node / 75-edge architecture:

SURVIVES.

Historical detector PASS:

SURVIVES.

P_rel gate:

SURVIVES_WITH_RESTRICTION.

N gate:

SURVIVES_WITH_RESTRICTION.

U gate:

SURVIVES_WITH_RESTRICTION.

Joint 8/8 local candidate PASS:

SURVIVES.

Interpretation of historical coordinates as independent confirmations:

NOT JUSTIFIED.

Interpretation of N as emergent novelty:

NOT JUSTIFIED.

Interpretation of P_rel as independent long-memory evidence:

UNDERDETERMINED.

Absolute irreducibility to first order:

FAILS.

Non-Markov-1 character relative to x_t alone:

SURVIVES.

Emergent-regime interpretation:

NOT ESTABLISHED.

External physical interpretation:

EXTERNAL_VALIDATION_REQUIRED.

---

## 32. Residual issues

R10-LABD2-01:

Qualify irreducibility explicitly relative to the declared observable/state representation.

R10-LABD2-02:

Do not count A1, Delta_hist and C_hist as statistically independent confirmations of distinct mechanisms.

R10-LABD2-03:

Record that the stationary architecture predicts approximately:

A1 raw scale ~ ln(5/3),

Delta_hist ~ ln(5/3),

C_hist ~ 0.4,

N ~ 0.6.

R10-LABD2-04:

Interpret high N as diversity inside the predeclared 75-trigram support.

R10-LABD2-05:

Determine whether P_rel measures something beyond stationarity plus separation from a Markov-1 surrogate.

R10-LABD2-06:

Keep U restricted to absence of dominant periodicity inside its finite declared lag range.

R10-LABD2-07:

Do not promote midpoint D0/D1 thresholds to universal boundaries.

R10-LABD2-08:

Future scientific versions should compare against simpler augmented-state Markov competitors.

R10-LABD2-09:

Keep synthetic internal seed robustness separate from external replication.

---

## 33. Consequence for the next audit

The local LAB-D2 result survives.

The central scientific question now shifts from:

"does LAB-D2 pass the six-coordinate gate?"

to:

"which parts of that PASS survive when the generator is causally damaged, simplified or replaced?"

Therefore the next adversarial evidence must come from the already frozen:

ABLATIONS-v1

followed by:

ATLAS-v1.

No new experiments are authorized in PHASE 10.

---

## 34. Preservation

This audit result is post-publication.

It does not modify:

v0.2.1

or its frozen commit:

fee2c31cfa17159a4075e1cbfbfa7e2fceba9c4b.

No new experiment was executed.

No threshold was changed.

No metric was recalibrated.

Any new competitor, new null family or new experiment belongs to a future scientific version.
