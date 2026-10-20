# PHASE 10 - HISTORY-DEPTH adversarial audit v1

## 0. Status

Scientific adversarial audit of:

- HISTORY-DEPTH-v1
- HISTORY-DEPTH-ATLAS-v1

Reference main:

7304250cfac9f7ab922fa0a4bc8c5fda2d1dadb0

Frozen release: v0.2.1

Release commit:

fee2c31cfa17159a4075e1cbfbfa7e2fceba9c4b

Epistemic rule:

CORRECT != NOVEL != GENERAL != EXTERNALLY VALIDATED

This note does not authorize new experiments.

## 1. Frozen evidence

Primary documents:

lab/LAB-FEN-001_HISTORY_DEPTH_SPEC_v1.md

lab/LAB-FEN-001_HISTORY_DEPTH.py

lab/LAB-FEN-001_HISTORY_DEPTH_RESULT_v1.md

lab/LAB-FEN-001_HISTORY_DEPTH_ATLAS_SPEC_v1.md

lab/LAB-FEN-001_HISTORY_DEPTH_ATLAS.py

lab/LAB-FEN-001_HISTORY_DEPTH_ATLAS_RESULT_v1.md

Structured JSON and frozen CSV summaries are retained
as primary quantitative evidence.

This adversarial review inspected the protocols,
implementation and full tabular summaries.

The complete nested JSON null distributions were not
independently re-evaluated in this review.

No frozen series were regenerated.

## 2. Experimental design

Orders:

M1, M2, M3, M4.

Predictive gains:

G_k = L_(k-1) - L_k.

The models are fitted on train and evaluated on test.

For each comparison, the short and long model
share the same test targets.

Null construction:

conditional permutation of the oldest historical
variable within the shorter-context strata.

Parameters:

alpha = 0.5
null permutations = 64
quantile = Q0.95 nearest-rank

Useful transitions = 30000
train boundary = 18000
test transitions = 12000

Effective train examples:

G2 = 17999
G3 = 17998
G4 = 17997

Each comparison uses 12000 test examples.

DEPTH_HIT requires:

G_k > 0

and:

G_k > null Q0.95.

The instrument tests orders 1 through 4 only.

## 3. Primary HISTORY-DEPTH result

Predeclared expectations:

D0: k*=1
D1: k*=2
D2: k*=2
DELAYED: k*=3

Frozen outcome:

HD-D0: 8/8 expected classifications.
HD-D1: 8/8 expected classifications.
HD-D2: 8/8 expected classifications.
HD-DELAYED: 8/8 expected classifications.

The four-system joint gate passes.

VERDICT: SURVIVES.

The result establishes correct classification
of the four selected synthetic controls under
the predefined instrument and sample lengths.

## 4. Observed predictive gains

Ranges extracted from the frozen summary CSV.

HD-D0:

G2 between -0.002721 and -0.001434.
G3 and G4 negative.
No depth hits.

HD-D1:

G2 = 1.6066657848491444 for all eight seeds.
G3 = 0.
G4 = 0.

HD-D2:

G2 between 0.507980 and 0.509741.
G3 and G4 negative.

HD-DELAYED:

G2 negative.
G3 between 0.499030 and 0.501428.
G4 negative.

The values and hit patterns agree with the
expected orders of the constructed generators.

## 5. D0 interpretation

D0 is generated as a first-order Markov chain.

Classification k*=1 is compatible with
the known generating architecture.

However, k*=1 operationally means that no
additional hit was detected at k=2,3,4.

This label alone does not prove exact
Markov-1 structure in an unknown process.

VERDICT: SURVIVES_WITH_RESTRICTION.

## 6. D1 interpretation

D1 is a deterministic Markov-2 generator
using a De Bruijn cycle of period 25.

The eight seed values select phases of
the same deterministic periodic structure.

They do not provide eight independent
stochastic realizations.

The observed G2 is approximately ln(5),
with a small finite-sample/smoothing difference.

G3 and G4 vanish exactly in the frozen summary.

The strong positive G2 is structurally expected.

VERDICT: STANDARD_OR_DERIVATIVE.

The claim that these are eight independent
stochastic replications:

FAILS.

## 7. D2 interpretation

D2 uses:

h(a,b) = (b + 2a) mod 5.

The process is Markov-2 relative to x_t.

On the expanded state:

z_t = (x_(t-1),x_t)

it is an ordinary finite-state Markov-1 chain.

The theoretical baseline conditional information
under its stationary distribution is:

I = ln(5/3) = approximately 0.510826.

The measured G2 lies near that value.

The positive gain is thus strongly explained
by the implanted second-order transition law.

The absence of G3 and G4 hits is also
compatible with that same architecture.

No independent physical memory mechanism
is established.

VERDICT: STANDARD_OR_DERIVATIVE for the
underlying Markov representation.

VERDICT: SURVIVES_WITH_RESTRICTION for
the operational detector classification.

## 8. DELAYED_PAST interpretation

DELAYED_PAST uses x_(t-2) and x_t in
its generation rule.

It is representable as Markov-3 on
three consecutive observable states.

The immediate G2 signal is absent.

The G3 signal is strongly positive.

G4 is negative without a hit.

This explains the previous immediate-depth
detector failure without claiming that the
generator lacks historical dependence.

The detector successfully recovers the
deliberately implanted third-order dependence.

It does not establish general sensitivity
to all possible depth-three mechanisms.

VERDICT: SURVIVES_WITH_RESTRICTION.

## 9. Permutation null qualification

The code shuffles the oldest context value
within shorter-context strata separately
for training and test examples.

The shorter context and next-state target
remain paired.

This constructs a conditional association null.

It does not preserve a continuous
time-series trajectory.

Its inferential calibration for arbitrary
dependent or nonstationary time series
has not been established by these controls.

There are only 64 permutations per test.

No general multiple-comparison control is
provided for the full collection of depth,
seed and parameter tests.

The observed large positive primary gains
are nevertheless far above their reported nulls.

VERDICT: SURVIVES_WITH_RESTRICTION.

## 10. Classification rule qualification

The classifier is a predefined decision rule.

It handles a G3 hit without a G2 hit,
as needed for DELAYED_PAST.

A G4 hit without G3 is marked DEPTH COMPLEX.

The resulting k* is not automatically
the true minimal Markov order of an
arbitrary unknown stochastic process.

A missing hit can arise from insufficient
sample size, smoothing, model complexity
or weak effects.

Orders above four are not examined.

VERDICT: SURVIVES_WITH_RESTRICTION.

Universal identification of memory depth:

UNDERDETERMINED.

## 11. HISTORY-DEPTH-ATLAS contract

Atlas parameters:

beta in {-0.10,-0.05,0,0.05,0.10}

epsilon in {0,0.05,0.10,0.15}

Total grid: 20 points.

Predeclared formal core:

beta in {-0.05,0,0.05}

epsilon in {0,0.05,0.10}

Core size: 9.

Depth point PASS requires at least 7/8
classifications k*=2.

Regional PASS requires 9/9 depth points.

The extended 11 points are descriptive.

The baseline is imported from frozen
HISTORY-DEPTH-v1.

The other 19 points reuse frozen atlas
time series, without regenerating them.

## 12. HISTORY-DEPTH-ATLAS outcome

Core:

9/9 DEPTH POINT PASS.

Complete grid:

20/20 DEPTH POINT PASS.

Total:

160/160 classifications k*=2.

G2 is positive and produces a hit
for every point-seed record.

G3 and G4 produce no hits.

No k*=1, k*=3, k*=4 or DEPTH COMPLEX
classification is reported.

VERDICT: SURVIVES.

This is stability of an operational
classification on a finite grid.

It is not universality.

## 13. Quantitative variation in the atlas

From the frozen atlas summary CSV,
grouped by epsilon over all beta values:

epsilon 0.00:
mean G2 approximately 0.524069
minimum G2 approximately 0.507980

epsilon 0.05:
mean G2 approximately 0.432832
minimum G2 approximately 0.408929

epsilon 0.10:
mean G2 approximately 0.369792
minimum G2 approximately 0.348818

epsilon 0.15:
mean G2 approximately 0.318668
minimum G2 approximately 0.299187

All 40 records at each epsilon
remain classified k*=2.

The historical predictive gain declines
as uniform leakage increases.

Thus stable binary classification
does not mean constant dependence strength.

## 14. Analytical explanation

For the stationary pair-uniform D2 family,
let p_j be its five context transition
probabilities.

Then:

I = ln(5) - H(p)

where:

H(p) = -sum_j p_j ln(p_j).

In the infinite-data correctly fitted limit,
G2 approaches this conditional information.

For beta=0:

epsilon=0.00:
theoretical I approximately 0.510826
observed mean G2 approximately 0.508726

epsilon=0.05:
theoretical I approximately 0.420896
observed mean G2 approximately 0.418120

epsilon=0.10:
theoretical I approximately 0.359100
observed mean G2 approximately 0.352858

epsilon=0.15:
theoretical I approximately 0.308186
observed mean G2 approximately 0.304423

These values show that much of the atlas
is analytically explained by the ordinary
Markov-2 generator.

The theoretical dependence is symmetric
under beta -> -beta at fixed epsilon.

Finite-sample estimates may be asymmetric.

VERDICT: STANDARD_OR_DERIVATIVE for
the explanatory Markov theory.

VERDICT: SURVIVES_WITH_RESTRICTION for
the observed parametric stability.

## 15. Independence limitations

All atlas points share:

- the same causal family;
- the same instrument;
- the same seeds;
- the same training/test design;
- the same classification gates;
- the same null methodology.

The instrument retains the HD-D2
null-seed identifier across atlas points.

Thus 160/160 does not represent 160
independent discoveries or validations.

The basal eight records are imported
from an earlier frozen analysis.

The other 152 records evaluate previously
generated trajectories.

VERDICT: SURVIVES_WITH_RESTRICTION.

## 16. Missing external tests

The evidence does not establish:

- universality of k*;
- physical memory;
- emergent geometry;
- causal mechanism uniqueness;
- generality across alphabet sizes;
- performance for arbitrary Markov orders;
- performance for orders greater than four;
- calibrated power for weak dependencies;
- general robustness to nonstationarity;
- external predictive validity.

These claims remain unestablished or
require appropriate external validation.

## 17. Adversarial claims ledger

CLAIM: four predeclared systems PASS.
VERDICT: SURVIVES.

CLAIM: depth ladder 1/2/2/3 recovered.
VERDICT: SURVIVES.

CLAIM: immediate detection can miss delayed history.
VERDICT: SURVIVES_WITH_RESTRICTION.

CLAIM: k*=2 stable across nine core points.
VERDICT: SURVIVES.

CLAIM: 160/160 k*=2 in full finite grid.
VERDICT: SURVIVES.

CLAIM: order identification is novel physics.
VERDICT: FAILS as established by this evidence.

CLAIM: Markov finite-order explanation.
VERDICT: STANDARD_OR_DERIVATIVE.

CLAIM: all eight D1 seeds are independent
stochastic replications.
VERDICT: FAILS.

CLAIM: no higher hit proves no higher memory.
VERDICT: FAILS as a universal implication.

CLAIM: k* is universally identifiable.
VERDICT: UNDERDETERMINED.

CLAIM: mechanism is unique or necessary.
VERDICT: UNDERDETERMINED.

CLAIM: memory is physically realized.
VERDICT: EXTERNAL_VALIDATION_REQUIRED.

## 18. Final scientific decision

HISTORY-DEPTH-v1:

SURVIVES as a constructed-control
operational classification result.

HISTORY-DEPTH-ATLAS-v1:

SURVIVES as a predeclared finite-grid
classification result.

GENERALITY:

SURVIVES_WITH_RESTRICTION at most
within the tested Markov family.

MECHANISTIC NOVELTY:

NOT ESTABLISHED.

ABSENCE OF HIGHER MEMORY:

NOT ESTABLISHED from non-hits alone.

PHYSICAL VALIDATION:

EXTERNAL_VALIDATION_REQUIRED.

The scientifically defensible contribution
is a reproducible detector for selected
synthetic historical-dependence structures,
with a documented local stability domain.

No independent new physical law follows
from these results.

## 19. Preservation rule

This is a Phase 10 interpretive note only.

No new experiment was run.

No frozen data are changed.

Do not modify:

v0.2.1
published PDFs
canonical ZIP
snapshot
Zenodo
release artifacts
frozen experimental results

No commit or push is performed here.

STATUS:

PHASE10 HISTORY-DEPTH ADVERSARIAL AUDIT DOCUMENTED
