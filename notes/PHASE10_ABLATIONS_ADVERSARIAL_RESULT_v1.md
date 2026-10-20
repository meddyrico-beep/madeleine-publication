# MADELEINE — PHASE 10 — ABLATIONS ADVERSARIAL RESULT v1

## Target

Experiment:

LAB-D2-ABLATIONS-v1

Reference candidate:

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

The frozen ablation battery intervenes on LAB-D2-v1 through:

NO_PAST,

RANDOMIZED_PAST,

DETERMINISTIC_CHOICE,

and:

DELAYED_PAST.

Its purpose is not to improve LAB-D2.

Its purpose is to test whether selected parts of the local signature disappear when specific generative ingredients are removed, misaligned or rigidified.

No new experiment is executed in this audit.

---

## 2. Frozen provenance

Repository history records:

ablation specification:

58274a0471d99a7e5c4d77e3a41f48abcb00dc61

decision gate:

df3b7a976638dfe6954364ead09252fb00687145

executable:

e7eeca433239bdb9897d1a5f0e4ee80062d413c8

recorded result:

79d047f955ecfa6ad44de7cfb98963c5e09491d3

Thus:

specification
->
gate
->
executable
->
result

is preserved.

SURVIVES.

---

## 3. Frozen primary result

The recorded battery reports:

NO_PAST:

PASS.

RANDOMIZED_PAST:

PASS.

DETERMINISTIC_CHOICE:

PASS.

DELAYED_PAST:

DIAGNOSTIC ONLY.

Overall:

ABLATION BATTERY v1 PASS.

This result survives literal application of the frozen gate.

SURVIVES.

---

## 4. Meaning of an ablation PASS

An ablation PASS does not mean that a universal causal law has been discovered.

It means that, under a predeclared intervention inside the synthetic generator, the measured response changed in the predeclared direction.

The evidence is therefore mechanistic within the constructed model.

It is not external causal validation.

---

# PART I — NO_PAST

## 5. NO_PAST intervention

NO_PAST replaces the D2 historical family by:

S_0(b)
=
{
b,
b+1,
b+2
}
mod 5.

Thus the next-state law depends only on:

x_t=b.

The process is Markov-1 by construction relative to the original five-symbol observable.

---

## 6. NO_PAST historical prediction

Because:

x_(t-1)

does not enter the transition law once x_t is known, the population-level immediate historical information is zero:

I(
X_(t-1);
X_(t+1)
|
X_t
)
=
0.

Therefore the observed loss of:

A1,
Delta_hist,
C_hist

is structurally expected.

The recorded result:

A1 positive = 0/8,

Delta hit = 0/8,

C hit = 0/8,

historical joint = 0/8,

seed pass = 0/8

SURVIVES.

This validates detector behavior on this particular intervention.

It does not establish general detector calibration over every Markov-1 process.

---

## 7. NO_PAST stationary structure

The transition kernel is circulant.

For every current state b there are exactly three equiprobable successors.

The uniform state distribution:

pi(b)=1/5

is stationary.

At stationarity every allowed transition has probability:

1/15.

An allowed trigram requires:

a -> b

and:

b -> c,

with three choices at each transition.

Therefore the number of allowed trigram states is:

5 * 3 * 3
=
45.

---

## 8. Exact NO_PAST novelty prediction

Under the uniform stationary distribution each allowed trigram has probability:

1/45.

Therefore:

H_3
=
ln 45,

D_3
=
45,

and:

N
=
45/125
=
0.36.

The recorded values are approximately:

N ~ 0.359.

Thus the measured novelty of NO_PAST is almost exactly the structural value predicted by the ablated generator.

This is not an emergent quantity.

---

## 9. NO_PAST U prediction

NO_PAST contains self-transition with probability:

1/3.

Under the uniform marginal:

B
=
sum_s pi_s^2
=
1/5.

At lag one:

R(1)
=
1/3

in the stationary idealization.

Therefore:

E(1)
=
(
1/3 - 1/5
)
/
(
1 - 1/5
)
=
1/6.

If this is the dominant recurrence scale:

U
approximately
1 - 1/6
=
5/6
approximately
0.8333.

The observed values near:

0.831 to 0.836

are consistent with this prediction.

Again, much of the metric vector is analytically explained by the generator.

---

## 10. NO_PAST interpretation

NO_PAST supports the restricted statement:

the immediate historical coordinates of LAB-D2 depend on actual use of the previous symbol by the generator.

SURVIVES_WITH_RESTRICTION.

It does not show that every historical architecture requires exactly the D2 formula.

It does not establish uniqueness of the mechanism.

---

# PART II — RANDOMIZED_PAST

## 11. RANDOMIZED_PAST intervention

RANDOMIZED_PAST replaces the actual previous symbol with:

a_tilde
~
Uniform(S)

independently of the real trajectory history.

The successor family remains:

c
=
b
+
2 a_tilde
+
k
mod 5,

where:

k in {0,1,2}

is selected uniformly.

---

## 12. Exact marginalization of RANDOMIZED_PAST

Fix any present symbol b and any candidate successor c.

There are:

5 * 3
=
15

equally weighted pairs:

(a_tilde,k).

For each fixed k, because 2 is invertible modulo 5, the equation:

2 a_tilde
=
c-b-k
mod 5

has exactly one solution.

Therefore exactly three of the 15 pairs produce any specified c.

Hence:

P(c|b)
=
3/15
=
1/5.

This does not depend on b.

Thus after marginalizing the artificial past signal, the effective one-step transition law is uniform over all five symbols.

---

## 13. Consequence of RANDOMIZED_PAST

The randomized intervention does more than merely weaken historical alignment.

At the observable transition level it collapses the generator to:

P(
X_(t+1)=c
|
X_t=b
)
=
1/5

for every b and c.

Thus the observable process is the maximally open first-order endpoint of this five-symbol family.

This explains why historical coordinates disappear.

---

## 14. RANDOMIZED_PAST diversity

For the uniform observable process, stationary trigram probabilities approach:

1/125

over all:

125

possible trigrams.

Therefore:

H_3
=
ln 125,

D_3
=
125,

N
=
1

in the ideal limit.

The recorded battery reports approximately:

N ~ 0.995.

This is exactly compatible with the analytically induced uniform process.

---

## 15. RANDOMIZED_PAST aperiodicity

An approximately i.i.d. uniform sequence has no designed dominant recurrence lag.

Therefore U is expected to remain high under the finite-lag detector.

The recorded result:

U ~ 0.985

is consistent with that expectation.

High diversity and high U in RANDOMIZED_PAST therefore do not preserve the D2 phenomenon.

They show that these two coordinates can remain high even after the aligned historical mechanism has been removed.

---

## 16. Isolated hits

RANDOMIZED_PAST records:

A1 positive = 1/8,

Delta hit = 1/8,

C hit = 1/8,

but:

historical joint = 0/8.

The isolated hits do not form a coherent joint historical signal.

Their existence is compatible with finite-sample threshold crossings.

Given the limitations already identified for the null procedures, they should not be promoted either as anomalies or as precise frequentist error-rate estimates.

---

## 17. RANDOMIZED_PAST interpretation

The result supports:

alignment with the real past matters for the immediate historical signature.

SURVIVES_WITH_RESTRICTION.

However RANDOMIZED_PAST is an extreme intervention because its observable marginal dynamics become uniform.

Therefore it does not quantify sensitivity to partial historical corruption.

It does not determine how much alignment is necessary.

---

# PART III — DETERMINISTIC_CHOICE

## 18. Deterministic intervention

DETERMINISTIC_CHOICE keeps:

h(a,b)
=
b+2a
mod 5

but removes branching.

The recurrence is:

x_(t+1)
=
x_t
+
2 x_(t-1)
mod 5.

---

## 19. Pair-state matrix

Define:

z_t
=
[
x_(t-1),
x_t
]^T.

Then:

z_(t+1)
=
M z_t

with:

M
=
[
[0,1],
[2,1]
]

over the field modulo 5.

---

## 20. Exact cycle identity

Direct multiplication modulo 5 gives:

M^2
=
[
[2,1],
[2,3]
],

M^3
=
[
[2,3],
[1,0]
],

and:

M^4
=
I.

Therefore every pair-state trajectory has period dividing:

4.

No stochastic or asymptotic argument is required.

The short-period collapse is an exact algebraic property of the chosen deterministic ablation.

---

## 21. Consequence for U

Because every orbit has exact period at most four, and the U detector searches lags far beyond that scale:

U=0

is structurally forced after the periodic regime is represented.

The recorded result:

U=0

for:

8/8

seeds therefore SURVIVES.

But it is not an unexpected experimental discovery.

It is the direct consequence of the selected deterministic recurrence.

---

## 22. Consequence for N

A period-two or period-four trajectory occupies only a tiny set of trigrams.

The recorded values:

N=0.016

or:

N=0.032

correspond to effective supports of approximately:

2

or:

4

histories out of 125.

This is again consistent with the exact short cycles generated by:

M^4=I.

---

## 23. Historical signal under determinization

The battery reports:

A1 positive = 5/8,

Delta hit = 5/8,

C hit = 5/8,

historical joint = 5/8.

Thus historical dependence can remain detectable after local stochastic choice is removed.

But:

seed passes = 0/8

because the full signature collapses, especially through U and N.

This distinction is important:

history survives in some deterministic trajectories,

while flexible, high-diversity, high-U behavior does not.

---

## 24. What DETERMINISTIC_CHOICE does and does not establish

It supports:

the specific stochastic branching of LAB-D2 prevents the particular short-cycle crystallization produced by this deterministic replacement.

SURVIVES_WITH_RESTRICTION.

It does not establish:

all deterministic mechanisms fail,
stochasticity is universally necessary,
or the D2 branching is the unique mechanism able to avoid crystallization.

Moreover any deterministic finite-state autonomous system eventually becomes periodic.

Therefore a finite-lag anti-periodicity gate naturally favors stochastic branching over finite deterministic dynamics.

This methodological asymmetry must remain explicit.

---

# PART IV — DELAYED_PAST

## 25. DELAYED_PAST intervention

DELAYED_PAST uses:

x_(t-2)

instead of:

x_(t-1)

to construct the successor family.

Thus the generator contains genuine historical dependence.

But that dependence is deeper than the immediate order-two detector is designed to target.

---

## 26. Expanded causal state

The natural state for DELAYED_PAST is:

(
x_(t-2),
x_(t-1),
x_t
).

There are:

5^3
=
125

possible states.

The frozen structural report records:

125 nodes,

375 edges,

and out-degree:

3.

Thus the ablation is a deeper-history stochastic process.

It is not a no-history control.

---

## 27. Immediate detector result

The immediate detector reports:

A1 positive = 0/8,

Delta hit = 0/8,

C hit = 0/8,

historical joint = 0/8.

This does not imply absence of historical dependence.

It means the dependence implanted at lag two is not detected by the immediate:

(x_(t-1),x_t)

instrument.

This was correctly predeclared as diagnostic only.

---

## 28. Why immediate history can disappear

For fixed:

x_(t-1)=b

and:

x_t=c,

the hidden historical input:

a=x_(t-2)

is not part of the immediate predictor.

When its distribution is approximately uniform, marginalizing over a and the three branch choices distributes the next state approximately uniformly over the five symbols.

Therefore the order-two observable can appear nearly Markov-1 even though the generator uses deeper history.

This is a representation-depth effect.

---

## 29. DELAYED_PAST diversity

The recorded result gives approximately:

N ~ 0.995

and full trigram coverage.

This is compatible with an almost uniform immediate trigram distribution after the deeper historical coordinate has been marginalized.

Thus high N here coexists with a genuine deeper causal dependency that is invisible to the immediate detector.

---

## 30. Critical detector lesson

DELAYED_PAST supplies a counterexample to the unrestricted inference:

no immediate historical signal
->
no historical dependence.

That inference FAILS.

The valid statement is only:

no dependence detected at the tested historical depth and representation.

This finding makes an explicit history-depth audit scientifically necessary.

---

# PART V — BATTERY AS A WHOLE

## 31. What the battery genuinely strengthens

Relative to the frozen LAB-D2 baseline:

NO_PAST removes immediate history and the historical signature disappears.

RANDOMIZED_PAST destroys alignment with the real past and the joint historical signature disappears.

DETERMINISTIC_CHOICE preserves part of the historical dependence but collapses diversity and finite-lag aperiodicity.

DELAYED_PAST preserves deeper history while escaping the immediate detector.

Together these interventions give genuine mechanistic information about what the six-coordinate signature is responding to.

---

## 32. Non-independence of outcomes

The ablation metrics are not six independent causal witnesses.

A1,
Delta_hist,
and C_hist

remain multiple diagnostics of historical dependence.

N and U are often strongly predictable from the support and periodic structure of the ablated generator.

P_rel is influenced by stationarity and by distance from its Markov-1 surrogate.

Therefore the battery should be interpreted at the level of intervention patterns rather than as a count of independent positive metrics.

---

## 33. Extremity of the interventions

The three primary ablative controls are deliberately strong.

NO_PAST exactly removes lag-one dependence.

RANDOMIZED_PAST induces an effectively uniform observable transition law.

DETERMINISTIC_CHOICE produces a recurrence satisfying:

M^4=I.

These are useful falsification controls.

They do not map a graded causal response curve around the baseline architecture.

Thus the battery establishes qualitative intervention specificity.

It does not estimate quantitative necessity.

---

## 34. Causal wording

Because the generator is fully known and explicitly intervened upon, mechanistic causal language is justified inside this synthetic model.

For example:

removing the past term removes the immediate historical signature

is justified for the declared intervention.

But the battery does not establish causal relations in an external physical system.

Nor does it prove that the same intervention semantics transfer outside the synthetic generator.

---

## 35. Strongest justified statement

The strongest justified statement is:

Within the frozen LAB-FEN-001-v1 synthetic system, the complete LAB-D2 local signature is intervention-sensitive. Removing or decorrelating the immediate historical input destroys the joint immediate-history signal, while replacing stochastic branching by the frozen deterministic recurrence produces short-period crystallization and destroys the complete candidate gate. These results support a restricted mechanistic interpretation of LAB-D2 based on aligned immediate history plus stochastic branching under the interventions actually tested.

---

## 36. Statements not justified

The ablation battery does not establish that:

- the LAB-D2 mechanism is unique;
- aligned lag-one history is universally necessary;
- stochastic branching is universally necessary;
- every deterministic competitor must fail an appropriately defined richness criterion;
- the six metrics provide independent causal confirmations;
- no simpler augmented-state Markov model can reproduce the signature;
- failure of the immediate detector means absence of deeper history;
- the mechanism corresponds to physical memory;
- the ablation PASS proves an external causal law;
- the battery establishes a new universal dynamical class.

---

## 37. Novelty assessment

Synthetic ablation methodology:

STANDARD_OR_DERIVATIVE.

Removal of a causal input:

STANDARD_OR_DERIVATIVE.

Randomization of an input:

STANDARD_OR_DERIVATIVE.

Determinization of a stochastic transition:

STANDARD_OR_DERIVATIVE.

Lag-misalignment diagnostic:

STANDARD_OR_DERIVATIVE.

Specific coordinated battery inside LAB-FEN-001:

SYSTEM-SPECIFIC.

Scientific novelty of the isolated ablation methodology:

NOT ESTABLISHED.

---

## 38. Final adversarial verdict

Frozen provenance:

SURVIVES.

Primary battery PASS:

SURVIVES.

NO_PAST immediate-history falsification:

SURVIVES_WITH_RESTRICTION.

RANDOMIZED_PAST alignment falsification:

SURVIVES_WITH_RESTRICTION.

DETERMINISTIC_CHOICE crystallization result:

SURVIVES_WITH_RESTRICTION.

DELAYED_PAST diagnostic:

SURVIVES.

Claim that immediate detector measures arbitrary historical dependence:

FAILS.

Restricted claim that it detects the aligned lag-one dependency used by LAB-D2:

SURVIVES.

Claim that the full D2 signature depends on aligned history plus stochastic branching under these tested interventions:

SURVIVES_WITH_RESTRICTION.

Universal necessity of those ingredients:

NOT ESTABLISHED.

Uniqueness of the LAB-D2 mechanism:

NOT ESTABLISHED.

External physical causality:

EXTERNAL_VALIDATION_REQUIRED.

---

## 39. Residual issues

R10-ABL-01:

Do not treat the three historical coordinates as independent causal confirmations.

R10-ABL-02:

Record the analytical NO_PAST predictions:

trigram support = 45,

N = 0.36,

and approximately:

U = 5/6

from the lag-one recurrence.

R10-ABL-03:

Record that RANDOMIZED_PAST marginalizes to:

P(c|b)=1/5,

which explains:

N approximately 1

and high U.

R10-ABL-04:

Record that the frozen deterministic recurrence satisfies:

M^4=I,

so its crystallization is algebraically forced.

R10-ABL-05:

Do not infer universal necessity of stochastic branching from one deterministic finite-state replacement.

R10-ABL-06:

Use DELAYED_PAST as evidence that historical detection is depth-specific.

R10-ABL-07:

Reserve claims of deeper-memory detection for the separate HISTORY-DEPTH audit.

R10-ABL-08:

Keep intervention evidence internal to the synthetic generator distinct from external causal validation.

---

## 40. Consequence for ATLAS-v1

The battery survives its frozen primary gate.

Therefore the next frozen evidence may address the question it was designed to precede:

does the LAB-D2 local candidate occupy a neighborhood of architectures rather than one isolated hand-selected point?

The next adversarial target is:

LAB-D2-ATLAS-v1.

No new experiment is authorized in PHASE 10.

---

## 41. Preservation

This audit result is post-publication.

It does not modify:

v0.2.1

or its frozen commit:

fee2c31cfa17159a4075e1cbfbfa7e2fceba9c4b.

No new trajectory was generated.

No metric was changed.

No threshold was recalibrated.

Any graded intervention family, alternative deterministic competitor or new causal test belongs to a future scientific version.
