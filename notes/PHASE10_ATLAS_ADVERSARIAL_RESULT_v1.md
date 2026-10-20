# PHASE 10 — LAB-D2-ATLAS-v1 adversarial audit

## 0. Status and scope

Audit of frozen LAB-D2-ATLAS-v1 evidence.

Reference main:
9d9139631d17052a0ee3801fd2158143b536fe92

Frozen release:
v0.2.1

Release commit:
fee2c31cfa17159a4075e1cbfbfa7e2fceba9c4b

No new experiments are authorized in Phase 10.
No frozen scientific artifacts are modified.

Epistemic rule:

CORRECT != NOVEL != GENERAL != EXTERNALLY VALIDATED

## 1. Frozen evidence

Primary sources:

- lab/LAB-FEN-001_D2_ATLAS_SPEC_v1.md
- lab/LAB-FEN-001_D2_ATLAS.py
- lab/LAB-FEN-001_D2_ATLAS_RESULT_v1.md
- lab/results/LAB-FEN-001_D2_ATLAS_v1_results.json

The narrative report and executable were inspected.

The complete structured per-seed JSON was not independently
recomputed during this review. Fine-grained gate margins
therefore remain subject to documentary verification.

## 2. Predeclared experimental contract

The atlas retains the D2 causal base:

h(a,b) = (b + 2a) mod 5.

The three historical successors are:

h, h+1, h+2 mod 5.

Parameters:

beta in {-0.10,-0.05,0,+0.05,+0.10}

epsilon in {0,0.05,0.10,0.15}

Unmixed successor weights:

w0 = 1/3 + beta
w1 = 1/3
w2 = 1/3 - beta

With probability epsilon, the successor is sampled
uniformly from the full five-state alphabet.

The complete grid contains 20 points.

The predeclared primary core contains nine points:

beta in {-0.05,0,+0.05}

epsilon in {0,0.05,0.10}

POINT PASS requires at least 7/8 joint seed passes.

REGION PASS requires 9/9 core POINT PASS.

The extended 11 points do not determine the primary boolean.

Frozen seeds:
11,23,37,51,79,101,131,173.

Burn-in: 1000.
Useful transitions: 30000.
Train: 18000.
Test: 12000.

Thresholds and null instruments remain unchanged.

## 3. Reported empirical outcome

Primary core: 9/9 POINT PASS.

Full grid: 20/20 POINT PASS.

All 19 newly simulated points: 8/8 seed passes.

Frozen imported baseline: 8/8 seed passes.

Baseline-connected PASS component: 20/20 points.

No POINT FAIL was reported within the explored grid.

The reported primary contractual outcome survives.

VERDICT: SURVIVES.

This does not establish an external boundary of failure.

## 4. Baseline qualification

The baseline (0,0) was imported from the frozen
LAB-D2-v1 result, not resimulated as a twentieth
new experimental point.

Thus the atlas comprises 19 new simulations
plus one previously frozen baseline record.

The primary criterion explicitly permits this.

Its inclusion does not independently replicate
the baseline using the atlas sampling implementation.

VERDICT: SURVIVES_WITH_RESTRICTION.

## 5. Architecture-preserving perturbations

Every atlas point retains:

- alphabet size five;
- the same historical base h(a,b);
- a second-order conditional transition law;
- the same three preferred successor offsets;
- the same metric definitions and evaluation procedure.

Only probability weights and uniform leakage change.

The 20 points are not 20 independent causal
architectures or 20 independent mechanism discoveries.

They form a finite grid inside one predefined
two-parameter Markov-2 family.

The result supports local parameter tolerance
within this fixed architecture.

It does not establish general architecture robustness.

VERDICT: SURVIVES_WITH_RESTRICTION.

## 6. Ordinary Markov representation

The observable process is Markov-2 with respect
to the scalar state x_t.

Define:

z_t = (x_(t-1), x_t).

Then z_t is an ordinary finite-state Markov-1 chain
on at most 25 ordered-pair states.

Therefore absolute irreducibility to Markov-1
does not follow.

The only relevant non-Markov-1 claim is relative
to the chosen five-state scalar observable.

VERDICT: STANDARD_OR_DERIVATIVE for Markov order.

## 7. Stationary structure

For fixed b, the mapping

a -> (b + 2a) mod 5

permutes all five residues.

For every beta and epsilon in the atlas:

sum_a P(c|a,b) = 1

for each fixed b and c.

Consequently, uniform probability over the
25 ordered pairs is stationary.

At that stationary distribution:

P(c|b) = 1/5

while the conditional transition P(c|a,b)
retains historical dependence.

This property is imposed by the chosen algebraic
family and is not a new empirical phenomenon.

The empirical record may have finite-sample deviations.

## 8. Information-theoretic explanation

Let p=(p0,p1,p2,p3,p4) denote the five
conditional successor probabilities for a context.

Their entropy is:

H(p) = -sum_j p_j ln(p_j).

In the stationary pair-uniform regime:

I(X_(t-1);X_(t+1)|X_t) = ln(5) - H(p).

The trigram distribution consists of 25
translated copies of that conditional law,
each weighted by 1/25.

Consequently:

H3 = ln(25) + H(p).

The frozen metric implementation defines:

N = exp(H3)/125.

Therefore its stationary theoretical value is:

N = exp(H(p))/5.

And hence:

N = exp(-I).

These identities explain a substantial part of
the dependence between historical information
and the effective trigram diversity metric.

They are analytic properties of this generator,
not additional independent experimental validations.

Finite-sample estimators need not satisfy
these identities exactly.

VERDICT: STANDARD_OR_DERIVATIVE.

## 9. Trigram support and leakage

For epsilon=0, all three preferred successors
have strictly positive probability throughout
the declared beta range.

There are exactly:

25 * 3 = 75

structurally possible trigram types out of 125.

For epsilon>0, all five successors have
positive probability for each historical pair.

The theoretical trigram support becomes 125/125.

However, N measures effective entropy-normalized
diversity, not just observed support coverage.

Full mathematical support does not imply N=1.

The diversity pattern is substantially generated
by the transition probabilities themselves.

Calling N independent emergent novelty
is not justified.

VERDICT: FAILS for an independent novelty claim.

## 10. Metric redundancy and gates

A1 and historical prediction metrics diagnose
related aspects of the planted second-order
dependence.

N is analytically constrained by the same
conditional transition distribution.

P_rel may primarily measure stationarity of
a common law and separation from a Markov-1
surrogate, rather than a new causal mechanism.

U tests absence of strong measured recurrence
over a finite prescribed lag range.

Joint gate satisfaction does not turn these
coordinates into independent causal evidence.

The thresholds were frozen before the atlas,
which limits retrospective tuning.

But their calibration against earlier D0/D1
conditions is not independent external validation.

No gate should be promoted to universal necessity
on the basis of this atlas.

VERDICT: SURVIVES_WITH_RESTRICTION.

## 11. Seed and point dependence

Every new point uses the same eight seed values.

The RNG is reinitialized for each seed and point.

Thus parameter comparisons have common-seed
coupling and are not independent cross-point
statistical replications.

The same generator family, metrics, surrogate
machinery and thresholds are shared throughout.

Eight seed passes per point support finite
within-point reproducibility under this design.

They do not imply twenty independent validations
of a proposed general mechanism.

VERDICT: SURVIVES_WITH_RESTRICTION.

## 12. No observed boundary

All 20 tested grid points reportedly pass.

Therefore no failure boundary is localized
within the tested discrete grid.

This is compatible with the explored parameter
window lying inside a broader PASS set.

It is also compatible with thresholds that are
insufficiently discriminating within that window.

No exact continuous PASS boundary follows from
the finite grid.

The explored rectangle must not be silently
promoted to a fully verified continuum.

VERDICT: UNDERDETERMINED for exterior boundaries.

## 13. Missing margin analysis

The report records universal PASS counts, but
the scalar gate margins are needed to determine
which constraints are close to failing.

Relevant quantities include:

A1
delta_hist
delta_hit
c_hist
c_hit
P_rel
N
U

Also relevant are:

- distances to frozen thresholds;
- seedwise extrema;
- dependence on beta and epsilon;
- comparison of near-neighbor points;
- surrogate null distributions;
- empirical versus analytic metric variation.

Without complete documentary inspection of
the saved pointwise data, no specific bottleneck
gate or safety margin is established here.

No new simulation is proposed.

VERDICT: UNDERDETERMINED for the active bottleneck.

## 14. Relation to the ablations

The atlas and ABLATIONS-v1 answer distinct questions.

The ablations alter or remove selected structural
features of the original mechanism.

The atlas retains the historical architecture
and perturbs its transition probabilities.

The conjunction supports a restricted statement:

the observed diagnostic signature is sensitive
to some architectural modifications and tolerant
of the specified quantitative perturbations.

It does not establish that the architecture is
unique, necessary or physically causal.

DELAYED_PAST already demonstrates that absence
of the immediate-depth signal does not imply
absence of historical dependence.

VERDICT: SURVIVES_WITH_RESTRICTION.

## 15. Adversarial claims ledger

CLAIM: predeclared 9/9 core PASS.
VERDICT: SURVIVES.

CLAIM: reported 20/20 full grid PASS.
VERDICT: SURVIVES.

CLAIM: basal is not isolated in tested grid.
VERDICT: SURVIVES_WITH_RESTRICTION.

CLAIM: local tolerance to declared parameter changes.
VERDICT: SURVIVES_WITH_RESTRICTION.

CLAIM: general architecture robustness.
VERDICT: UNDERDETERMINED.

CLAIM: irreducible novel non-Markovian physics.
VERDICT: FAILS as established by this atlas.

CLAIM: ordinary expanded-state Markov representation.
VERDICT: STANDARD_OR_DERIVATIVE.

CLAIM: independent emergence of N.
VERDICT: FAILS as an independent claim.

CLAIM: causal independence of diagnostic gates.
VERDICT: FAILS as a strong claim.

CLAIM: exterior failure boundary determined.
VERDICT: UNDERDETERMINED.

CLAIM: universal necessity or uniqueness.
VERDICT: UNDERDETERMINED.

CLAIM: physical realization or general external relevance.
VERDICT: EXTERNAL_VALIDATION_REQUIRED.

## 16. Final scientific decision

PRIMARY CONTRACT:
SURVIVES.

INTERNAL PARAMETRIC ROBUSTNESS:
SURVIVES_WITH_RESTRICTION.

ARCHITECTURAL NOVELTY:
NOT ESTABLISHED.

UNIVERSAL NECESSITY:
NOT ESTABLISHED.

INDEPENDENT PHYSICAL CAUSALITY:
EXTERNAL_VALIDATION_REQUIRED.

The atlas is a valid constructive internal result
under its predefined finite experimental contract.

It does not demonstrate a universal physical regime,
unique mechanism or new law of nature.

Its strongest defensible contribution is a
reproducible local PASS region within a predefined
finite-state Markov-2 family.

## 17. Phase 10 handling

This note is an adversarial interpretation only.

It does not modify:

- frozen release v0.2.1;
- published PDFs;
- canonical ZIP;
- snapshots;
- Zenodo records;
- frozen experiment data.

No commit or push is authorized by this document.

STATUS:
PHASE10 ATLAS ADVERSARIAL AUDIT — DOCUMENTED
