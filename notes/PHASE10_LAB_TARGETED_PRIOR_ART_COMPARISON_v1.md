# MADELEINE - Phase 10 Laboratory Targeted Prior-Art Comparison v1

## 0. Status

POST-PUBLICATION ADVERSARIAL LITERATURE COMPARISON

Date: 2026-10-26

Reference main:
e1b04f2467210670c7df9718f6a17c5a71713419

Frozen release:
v0.2.1

Frozen release commit:
fee2c31cfa17159a4075e1cbfbfa7e2fceba9c4b

Targets:
LAB-D0
LAB-D1
LAB-D2
ABLATIONS-v1
ATLAS-v1
HISTORY-DEPTH-v1
HISTORY-DEPTH-ATLAS-v1

CORRECT != NOVEL != GENERAL != EXTERNALLY VALIDATED

This note is documentary.

No new experiment.
No new null calibration.
No modified threshold.
No change to frozen results.
No new scientific claim.

## 1. Evidence-class convention

F = Formal mathematics.

C = Computational result under
a frozen experimental contract.

M = Methodological rule,
control or admission procedure.

E = Independent external evidence.

The seven targets contain
computational evidence C.

Their decision protocols
also have methodological
content M.

Formal deductions discussed
in their adversarial notes
have evidence class F
only for those deductions.

None of the seven targets
establishes independent
external evidence E.

This explicitly clarifies
the evidence-class fields
for ATLAS-v1,
HISTORY-DEPTH-v1,
and HISTORY-DEPTH-ATLAS-v1.

This is a documentary
classification, not an
upgrade of their results.

## 2. LAB-D0

Exact target:

A constructed first-order
Markov control under
LAB-FEN-001-v1.

Reported restricted outcome:

The frozen historical
detector does not produce
a consistent accepted
historical signature
across the eight seeds.

Comparator A:

Norris, Markov Chains, 1997.

The Markov-1 property
and finite transition
kernels are established
probability theory.

Comparator B:

A rigorous and versatile
statistical test for
correlations between
stationary time series.

PLOS Biology, 2024.

URL:
https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3002758

Relevant distinction:

Temporal permutation tests
may require special
validity conditions when
observations are dependent.

The PLOS paper addresses
time-series dependence
testing generally.

It does not directly
prove the specific
MADELEINE conditional
permutation null invalid.

Actual difference:

LAB-D0 provides an
internally traceable
negative control for
one selected finite
Markov-1 kernel.

Novelty verdict:

STANDARD_OR_DERIVATIVE
for the Markov mechanism.

General false-positive
calibration:
UNDERDETERMINED.

External validity:
NOT ESTABLISHED.

## 3. LAB-D1

Exact target:

A deterministic
De Bruijn-based control
of period 25 over
five symbols.

The eight declared seeds
represent phase choices
in a deterministic cycle,
not eight independent
stochastic experiments.

Comparator:

Wolfram MathWorld,
de Bruijn Sequence.

URL:
https://mathworld.wolfram.com/deBruijnSequence.html

Known structure:

A cyclic sequence
can contain every
length-two word on
a five-symbol alphabet.

The resulting full cycle
contains 5^2=25 positions.

Actual difference:

LAB-D1 documents the
response of the frozen
MADELEINE history detector
to a strong constructed
positive control.

The detector hits survive
under the declared contract.

They are not eight
independent model replications.

Novelty verdict:

STANDARD_OR_DERIVATIVE
for the sequence mechanism.

Detector performance:
SURVIVES_WITH_RESTRICTION.

General sensitivity:
NOT ESTABLISHED.

## 4. LAB-D2

Exact target:

A synthetic second-order
stochastic generator with
five observable symbols.

Its pair-state graph has:

25 contexts;
75 permitted edges.

The reported local
joint gate passes
in 8/8 seeds.

Comparator:

Jianhong Xu, 2026.

Can a higher-order Markov
chain be treated as a
first-order Markov chain?

URL:
https://doi.org/10.1017/S0269964826100230

Known structure:

A higher-order Markov
process can be represented
using an expanded
first-order state.

This principle predates
the 2026 exposition.

Actual MADELEINE evidence:

Under stationarity,
the generator predicts:

I=ln(5/3);

conditional prediction
gain near ln(5/3);

C_hist near 0.4;

normalized trigram
diversity near 0.6.

These predictions explain
much of the frozen
observed signature.

The observed PASS is
a constructive internal
existence result.

It does not establish
spontaneous physical
emergence or a new
irreducible stochastic law.

Novelty verdict:

STANDARD_OR_DERIVATIVE
for the finite Markov mechanism.

Joint gate:
SURVIVES.

Absolute irreducibility
to Markov-1:
FAILS.

Novel physical dynamics:
NOT ESTABLISHED.

## 5. ABLATIONS-v1

Exact target:

Selected interventions
on the frozen
synthetic generator.

Cases include:

NO_PAST;
RANDOMIZED_PAST;
DETERMINISTIC_CHOICE;
DELAYED_PAST.

Comparator:

Judea Pearl,
Causality:
Models, Reasoning,
and Inference,
second edition, 2009.

Chapter:
Causal Diagrams and the
Identification of
Causal Effects.

URL:
https://doi.org/10.1017/CBO9780511803161.005

Relevant established method:

Causal interpretations
require explicit models
of interventions and
their assumptions.

Controlled changes
can reveal dependencies
within an experimental
construction.

However, the outcomes
of selected ablations
do not by themselves
prove that no alternative
causal mechanism can
produce the same result.

Actual difference:

The frozen MADELEINE
battery documents
specific changes to
the detected signature
when selected generator
features are altered.

The delayed-past case
also illustrates that
an immediate-history
detector can miss
a deeper dependence.

Novelty verdict:

SELECTED CONTROLLED
RESPONSES SURVIVE.

Universal mechanism
necessity:
NOT ESTABLISHED.

Alternative explanations:
NOT EXHAUSTED.

## 6. ATLAS-v1

Exact target:

A predeclared finite
parameter grid around
the LAB-D2 architecture.

Reported outcomes:

9/9 POINT PASS
in the core;

20/20 POINT PASS
in the full grid.

The basal point reuses
previous frozen evidence.

Comparator:

Eilon Solan and
Nicolas Vieille,
Perturbed Markov Chains,
Journal of Applied
Probability, 2003.

DOI:
10.1239/JAP/1044476830

URL:
https://doi.org/10.1239/JAP/1044476830

Known subject:

Sensitivity of
finite-state Markov
chains to changes in
transition probabilities.

Actual difference:

ATLAS-v1 documents
local gate tolerance
within one selected
two-parameter
Markov-2 family.

It does not establish
robustness across all
mechanism families.

The repeated seed
design also limits
independence claims.

No exterior failure
boundary was established.

Evidence:
C for finite-grid outcomes;
M for declared gate;
F for separately
proved model properties.

Novelty verdict:

LOCAL TOLERANCE:
SURVIVES_WITH_RESTRICTION.

New universal regime
boundary:
NOT ESTABLISHED.

## 7. HISTORY-DEPTH-v1

Exact target:

A frozen history-depth
classifier applied to
four constructed controls.

Reported classification
ladder:

D0 -> k*=1;
D1 -> k*=2;
D2 -> k*=2;
DELAYED_PAST -> k*=3.

Comparator:

Markov chain order
estimation with conditional
mutual information.

Physica A, 2013.

URL:
https://www.sciencedirect.com/science/article/abs/pii/S0378437112010837

Relevant established method:

Conditional mutual
information can help
estimate the effective
order of categorical
Markov sequences.

The paper compares
CMI testing with
other standard order
selection methods.

Actual MADELEINE evidence:

The predefined detector
recovers the expected
operational labels
for the four tested
constructed systems.

The label k* depends
on the declared detector,
window and null contract.

It is not a universal
identification theorem
for unknown processes.

Evidence:
C for frozen classifications;
M for classifier rules.

Novelty verdict:

OPERATIONAL CLASSIFICATION:
SURVIVES.

Independent mechanism
novelty:
NOT ESTABLISHED.

## 8. HISTORY-DEPTH-ATLAS-v1

Exact target:

The frozen depth
classifier is applied
across a finite
parameter grid.

Reported outcomes:

20/20 depth-point PASS;

160/160 classifications
with k*=2.

The same generator family,
seed structure and
classification contract
are reused.

Comparator A:

Markov chain order
estimation with
conditional mutual
information, 2013.

URL:
https://www.sciencedirect.com/science/article/abs/pii/S0378437112010837

Comparator B:

Solan and Vieille,
Perturbed Markov Chains.

URL:
https://doi.org/10.1239/JAP/1044476830

Actual difference:

The atlas demonstrates
finite-grid stability
of an operational
order classification
under declared
parameter changes.

This is not 160
independent discoveries
of historical memory.

It does not establish
performance for
arbitrary process orders
or independent natural data.

Evidence:
C for finite-grid outcomes;
M for gates and protocol.

Novelty verdict:

FINITE CLASSIFICATION
STABILITY SURVIVES.

General order-identification
novelty:
NOT ESTABLISHED.

## 9. Cross-target dependence

The seven targets are
not seven independent
scientific replications.

Important shared elements:

generator families;

frozen metrics;

seed identifiers;

threshold calibration;

conditional nulls;

reused baseline evidence;

related history diagnostics.

LAB-D2's A1,
Delta_hist and C_hist
respond to the same
designed order-two
transition structure.

The stationary theory
also links historical
information and
effective trigram
diversity under the
declared assumptions.

These dependencies
must not be multiplied
into fictitious
independent confirmations.

## 10. External source scope

The selected comparators
establish known methods
relevant to the exact
audited claims.

They are not proof that
every part of MADELEINE
is equivalent to an
existing framework.

They do not establish
historical derivation
of MADELEINE from
those sources.

This is a focused,
non-systematic review.

No exhaustive historical
priority search or
independent expert
certification is claimed.

## 11. Seven-condition accounting

S - Exact scope:
DOCUMENTED PER TARGET.

E - Evidence class:
CLARIFIED PER TARGET.

A - Adversarial tests:
ALREADY DOCUMENTED
IN FROZEN POST-PUBLICATION
AUDIT NOTES.

L - Literature comparison:
TARGETED COMPARATORS
WITH EXPLICIT LIMITS.

N - Novelty verdict:
STANDARD COMPONENTS;
SYSTEM NOVELTY OPEN.

V - Supported results:
PRESERVED WITH
INDIVIDUAL RESTRICTIONS.

R - Residual issues:
DOCUMENTED.

This accounting records
where the required
information is located.

It is not yet a separate
independent certification
that every condition is
fully adequate.

## 12. Remaining obstacles

Null calibration:
OPEN OUTSIDE TESTED CONTROLS.

Weak-dependence power:
OPEN.

Alternative generators:
INSUFFICIENTLY EXCLUDED.

Statistical dependence
among diagnostics:
NOT FULLY QUANTIFIED.

Universal dynamic
necessity:
NOT ESTABLISHED.

Canonical-to-lab
structure-preserving bridge:
NOT ESTABLISHED.

External physical validation:
REQUIRED.

Integrated scientific novelty:
NOT ESTABLISHED.

Historical documentary
inconsistencies:
MUST REMAIN TRACEABLE.

## 13. Closure consequence

The original 13-target
priority audit now has
targeted mathematical
comparisons for DMO-001
through DMO-006,
and targeted methodological
and probabilistic
comparisons for seven
laboratory targets.

This extends the
documentary evidence
for the L condition.

It does not itself
certify L as complete
for every target.

The next operation must
check all 13 targets
against the original
S,E,A,L,N,V,R criteria
and record an explicit
closure decision.

If a criterion remains
inadequately supported,
it must remain OPEN.

No scientific novelty
is inferred from
documentary completion.

## 14. Preservation

Do not alter:

v0.2.1;
release tag;
published PDFs;
references.bib;
canonical ZIP;
snapshots;
frozen experiments;
Zenodo deposit.

This is a post-publication
comparative audit note.

No commit or push
during file creation.

STATUS:

PHASE10 LAB TARGETED PRIOR ART COMPARISON DOCUMENTED

FULL PHASE10 SCIENTIFIC CLOSURE NOT YET CERTIFIED
