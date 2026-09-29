from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys

from pathlib import Path


VERSION = "LAB-D2-DMO004-AUDIT-v1"

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
RESULTS = ROOT / "results"

OUTPUT_JSON = (
    RESULTS
    / "LAB-FEN-001_D2_DMO004_AUDIT_v1_results.json"
)

PASS = "PASS"
FAIL = "FAIL"
INSUFFICIENT = "INSUFFICIENT EVIDENCE"


# ============================================================
# ARCHIVOS
# ============================================================

PROTOCOL = ROOT / "LAB-FEN-001_PROTOCOL.md"

D0_SPEC = ROOT / "LAB-FEN-001_D0_SPEC_v1.md"
D0_EXEC = ROOT / "LAB-FEN-001_D0.py"
D0_RESULT_MD = ROOT / "LAB-FEN-001_D0_RESULT_v1.md"
D0_JSON = RESULTS / "LAB-FEN-001_D0_v1_results.json"
D0_SERIES = RESULTS / "LAB-FEN-001_D0_v1_series.csv.gz"

D1_SPEC = ROOT / "LAB-FEN-001_D1_SPEC_v1.md"
D1_EXEC = ROOT / "LAB-FEN-001_D1.py"
D1_RESULT_MD = ROOT / "LAB-FEN-001_D1_RESULT_v1.md"
D1_JSON = RESULTS / "LAB-FEN-001_D1_v1_results.json"
D1_SERIES = RESULTS / "LAB-FEN-001_D1_v1_series.csv.gz"

METRICS_SPEC = ROOT / "LAB-FEN-001_METRICS_v1.md"
METRICS_EXEC = ROOT / "LAB-FEN-001_METRICS_v1.py"
METRICS_RESULT_MD = ROOT / "LAB-FEN-001_METRICS_RESULT_v1.md"
METRICS_JSON = RESULTS / "LAB-FEN-001_METRICS_v1_calibration.json"

THRESHOLDS = ROOT / "LAB-FEN-001_THRESHOLDS_v1.md"

D2_SPEC = ROOT / "LAB-FEN-001_D2_SPEC_v1.md"
D2_EXEC = ROOT / "LAB-FEN-001_D2.py"
D2_RESULT_MD = ROOT / "LAB-FEN-001_D2_RESULT_v1.md"
D2_JSON = RESULTS / "LAB-FEN-001_D2_v1_results.json"
D2_SERIES = RESULTS / "LAB-FEN-001_D2_v1_series.csv.gz"

ABL_SPEC = ROOT / "LAB-FEN-001_D2_ABLATIONS_SPEC_v1.md"
ABL_GATE = ROOT / "LAB-FEN-001_D2_ABLATIONS_GATE_v1.md"
ABL_EXEC = ROOT / "LAB-FEN-001_D2_ABLATIONS.py"
ABL_RESULT_MD = ROOT / "LAB-FEN-001_D2_ABLATIONS_RESULT_v1.md"
ABL_JSON = RESULTS / "LAB-FEN-001_D2_ABLATIONS_v1_results.json"
ABL_SERIES = RESULTS / "LAB-FEN-001_D2_ABLATIONS_v1_series.csv.gz"

ATLAS_SPEC = ROOT / "LAB-FEN-001_D2_ATLAS_SPEC_v1.md"
ATLAS_EXEC = ROOT / "LAB-FEN-001_D2_ATLAS.py"
ATLAS_RESULT_MD = ROOT / "LAB-FEN-001_D2_ATLAS_RESULT_v1.md"
ATLAS_JSON = RESULTS / "LAB-FEN-001_D2_ATLAS_v1_results.json"
ATLAS_SERIES = RESULTS / "LAB-FEN-001_D2_ATLAS_v1_series.csv.gz"

AUDIT_SPEC = ROOT / "LAB-FEN-001_D2_DMO004_AUDIT_SPEC_v1.md"
AUDIT_EXEC = Path(__file__).resolve()


REQUIRED_PATHS = (
    PROTOCOL,

    D0_SPEC,
    D0_EXEC,
    D0_RESULT_MD,
    D0_JSON,
    D0_SERIES,

    D1_SPEC,
    D1_EXEC,
    D1_RESULT_MD,
    D1_JSON,
    D1_SERIES,

    METRICS_SPEC,
    METRICS_EXEC,
    METRICS_RESULT_MD,
    METRICS_JSON,

    THRESHOLDS,

    D2_SPEC,
    D2_EXEC,
    D2_RESULT_MD,
    D2_JSON,
    D2_SERIES,

    ABL_SPEC,
    ABL_GATE,
    ABL_EXEC,
    ABL_RESULT_MD,
    ABL_JSON,
    ABL_SERIES,

    ATLAS_SPEC,
    ATLAS_EXEC,
    ATLAS_RESULT_MD,
    ATLAS_JSON,
    ATLAS_SERIES,

    AUDIT_SPEC,
    AUDIT_EXEC,
)


# ============================================================
# UTILIDADES
# ============================================================

def read_json(path: Path):
    with path.open(
        "r",
        encoding="utf-8",
    ) as fh:
        return json.load(fh)


def read_text(path: Path):
    return path.read_text(
        encoding="utf-8"
    )


def sha256_file(path: Path):
    h = hashlib.sha256()

    with path.open("rb") as fh:
        while True:
            block = fh.read(
                1024 * 1024
            )

            if not block:
                break

            h.update(block)

    return h.hexdigest()


def rel(path: Path):
    return path.resolve().relative_to(
        REPO.resolve()
    ).as_posix()


def git(*args):
    completed = subprocess.run(
        ["git", *args],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    return completed


def git_output(*args):
    completed = git(*args)

    if completed.returncode != 0:
        raise RuntimeError(
            completed.stderr.strip()
            or
            "git command failed"
        )

    return completed.stdout.strip()


def first_add_commit(path: Path):
    output = git_output(
        "log",
        "--diff-filter=A",
        "--format=%H",
        "--",
        rel(path),
    )

    lines = [
        line.strip()
        for line in output.splitlines()
        if line.strip()
    ]

    if not lines:
        return None

    # Un archivo normal se añade una sola vez.
    # Si hubiera varias adiciones por borrado/recreación,
    # la más antigua es la última línea.
    return lines[-1]


def is_ancestor(
    older: str,
    newer: str,
):
    completed = git(
        "merge-base",
        "--is-ancestor",
        older,
        newer,
    )

    if completed.returncode == 0:
        return True

    if completed.returncode == 1:
        return False

    raise RuntimeError(
        completed.stderr.strip()
        or
        "git merge-base failed"
    )


def commit_order(
    earlier: Path,
    later: Path,
):
    a = first_add_commit(
        earlier
    )

    b = first_add_commit(
        later
    )

    if a is None or b is None:
        return {
            "ok": None,
            "earlier_file": rel(earlier),
            "later_file": rel(later),
            "earlier_commit": a,
            "later_commit": b,
        }

    return {
        "ok": is_ancestor(
            a,
            b,
        ),
        "earlier_file": rel(earlier),
        "later_file": rel(later),
        "earlier_commit": a,
        "later_commit": b,
    }


def make_result(
    status,
    evidence,
):
    return {
        "status": status,
        "evidence": evidence,
    }


def status_from_checks(
    checks,
):
    values = list(
        checks.values()
    )

    if any(
        value is None
        for value in values
    ):
        return INSUFFICIENT

    if all(values):
        return PASS

    return FAIL


def has_terms(
    path: Path,
    terms,
):
    text = read_text(
        path
    ).lower()

    return all(
        term.lower() in text
        for term in terms
    )


def valid_sha256(value):
    return (
        isinstance(
            value,
            str,
        )
        and
        re.fullmatch(
            r"[0-9a-fA-F]{64}",
            value,
        )
        is not None
    )


# ============================================================
# CARGA DE DATOS
# ============================================================

def load_inputs():
    return {
        "d0": read_json(D0_JSON),
        "d1": read_json(D1_JSON),
        "d2": read_json(D2_JSON),
        "abl": read_json(ABL_JSON),
        "atlas": read_json(ATLAS_JSON),
    }


# ============================================================
# CORE DEL ATLAS
# ============================================================

CORE_BETAS = {
    -0.05,
    0.0,
    0.05,
}

CORE_EPSILONS = {
    0.0,
    0.05,
    0.10,
}


def atlas_core_points(atlas):
    points = []

    for point in atlas["points"]:
        beta = round(
            float(point["beta"]),
            2,
        )

        epsilon = round(
            float(point["epsilon"]),
            2,
        )

        if (
            beta in CORE_BETAS
            and
            epsilon
            in CORE_EPSILONS
        ):
            points.append(
                point
            )

    return points


# ============================================================
# 1. REGION_PARAMETRIC
# ============================================================

def audit_region_parametric(data):
    atlas = data["atlas"]
    region = atlas.get(
        "region",
        {},
    )

    core = atlas_core_points(
        atlas
    )

    baseline = [
        point
        for point in core
        if round(
            float(point["beta"]),
            2,
        ) == 0.0
        and round(
            float(point["epsilon"]),
            2,
        ) == 0.0
    ]

    checks = {
        "core_points_declared_9": (
            region.get(
                "core_points"
            ) == 9
        ),

        "core_passes_9": (
            region.get(
                "core_passes"
            ) == 9
        ),

        "region_boolean_true": (
            region.get(
                "local_parametric_region_pass"
            )
            is True
        ),

        "nine_core_records_found": (
            len(core) == 9
        ),

        "all_core_point_pass": (
            len(core) == 9
            and all(
                point.get(
                    "point_pass"
                )
                is True
                for point in core
            )
        ),

        "baseline_in_core": (
            len(baseline) == 1
        ),

        "baseline_point_pass": (
            len(baseline) == 1
            and baseline[0].get(
                "point_pass"
            )
            is True
        ),
    }

    status = status_from_checks(
        checks
    )

    return make_result(
        status,
        {
            "checks": checks,
            "core_records": len(core),
            "declared_core_passes": (
                region.get(
                    "core_passes"
                )
            ),
        },
    )


# ============================================================
# 2. SEED_AGREEMENT
# ============================================================

def audit_seed_agreement(data):
    atlas = data["atlas"]

    core = atlas_core_points(
        atlas
    )

    counts = {
        point["key"]: point.get(
            "seed_pass_count"
        )
        for point in core
    }

    checks = {
        "nine_core_records": (
            len(core) == 9
        ),

        "every_core_point_at_least_7_of_8": (
            len(core) == 9
            and all(
                isinstance(
                    count,
                    int,
                )
                and count >= 7
                for count
                in counts.values()
            )
        ),
    }

    return make_result(
        status_from_checks(
            checks
        ),
        {
            "checks": checks,
            "seed_pass_counts": counts,
        },
    )


# ============================================================
# 3. NULL_SEPARATION
# ============================================================

def historical_record_ok(result):
    return all(
        (
            result.get(
                "seed_pass"
            )
            is True,

            result.get(
                "A1",
                0.0,
            ) > 0.0,

            result.get(
                "delta_hist",
                0.0,
            ) > 0.0,

            result.get(
                "delta_hit"
            )
            is True,

            result.get(
                "c_hist",
                0.0,
            ) > 0.0,

            result.get(
                "c_hit"
            )
            is True,
        )
    )


def audit_null_separation(data):
    d2 = data["d2"]
    atlas = data["atlas"]

    failures = []
    checked = 0

    # Basal: usa el resultado D2 congelado.
    for result in d2.get(
        "results",
        [],
    ):
        if result.get(
            "seed_pass"
        ) is not True:
            continue

        checked += 1

        if not historical_record_ok(
            result
        ):
            failures.append(
                {
                    "point": "baseline",
                    "seed": result.get(
                        "seed"
                    ),
                }
            )

    # Ocho puntos restantes del núcleo.
    for point in atlas_core_points(
        atlas
    ):
        if (
            round(
                float(point["beta"]),
                2,
            ) == 0.0
            and
            round(
                float(point["epsilon"]),
                2,
            ) == 0.0
        ):
            continue

        for result in point.get(
            "results",
            []
        ):
            if result.get(
                "seed_pass"
            ) is not True:
                continue

            checked += 1

            if not historical_record_ok(
                result
            ):
                failures.append(
                    {
                        "point": (
                            point.get(
                                "key"
                            )
                        ),
                        "seed": (
                            result.get(
                                "seed"
                            )
                        ),
                    }
                )

    expected_minimum = (
        9 * 7
    )

    checks = {
        "enough_contributing_seed_records": (
            checked
            >= expected_minimum
        ),

        "all_contributing_records_separated": (
            len(failures) == 0
        ),
    }

    return make_result(
        status_from_checks(
            checks
        ),
        {
            "checks": checks,
            "records_checked": checked,
            "minimum_required": (
                expected_minimum
            ),
            "failures": failures,
        },
    )


# ============================================================
# 4. EXPLICIT_FAILURE_CRITERION
# ============================================================

def audit_explicit_failure():
    ordering_pairs = (
        (
            THRESHOLDS,
            D2_JSON,
        ),
        (
            D2_SPEC,
            D2_JSON,
        ),
        (
            ABL_SPEC,
            ABL_JSON,
        ),
        (
            ABL_GATE,
            ABL_JSON,
        ),
        (
            ATLAS_SPEC,
            ATLAS_JSON,
        ),
    )

    ordering = [
        commit_order(
            earlier,
            later,
        )
        for earlier, later
        in ordering_pairs
    ]

    order_values = [
        item["ok"]
        for item in ordering
    ]

    text_checks = {
        "thresholds_declare_7_of_8": (
            has_terms(
                THRESHOLDS,
                (
                    "7/8",
                    "T_P",
                    "T_N",
                    "T_U",
                ),
            )
        ),

        "ablation_gate_has_failure_counts": (
            has_terms(
                ABL_GATE,
                (
                    "NO_PAST",
                    "RANDOMIZED_PAST",
                    "DETERMINISTIC_CHOICE",
                    "1/8",
                    "7/8",
                ),
            )
        ),

        "atlas_has_point_fail": (
            has_terms(
                ATLAS_SPEC,
                (
                    "POINT FAIL",
                    "9/9",
                    "7/8",
                    "LOCAL PARAMETRIC REGION v1 FAIL",
                ),
            )
        ),
    }

    if any(
        value is None
        for value in order_values
    ):
        order_status = None
    else:
        order_status = all(
            order_values
        )

    checks = {
        "failure_documents_predate_results": (
            order_status
        ),

        **text_checks,
    }

    return make_result(
        status_from_checks(
            checks
        ),
        {
            "checks": checks,
            "git_order": ordering,
        },
    )


# ============================================================
# 5. NON_REDUCIBLE
# ============================================================

def audit_non_reducible(data):
    d0 = data["d0"]
    d1 = data["d1"]
    d2 = data["d2"]
    abl = data["abl"]

    summaries = abl.get(
        "summaries",
        {},
    )

    no_past = summaries.get(
        "ABL-NO-PAST-v1",
        {},
    )

    randomized = summaries.get(
        "ABL-RANDOMIZED-PAST-v1",
        {},
    )

    deterministic = summaries.get(
        "ABL-DETERMINISTIC-v1",
        {},
    )

    d0_summary = d0.get(
        "summary",
        {},
    )

    d1_summary = d1.get(
        "summary",
        {},
    )

    d2_summary = d2.get(
        "summary",
        {},
    )

    d2_results = d2.get(
        "results",
        [],
    )

    checks = {
        "no_past_full_passes_le_1": (
            no_past.get(
                "seed_pass_count"
            )
            is not None
            and
            no_past[
                "seed_pass_count"
            ] <= 1
        ),

        "randomized_past_full_passes_le_1": (
            randomized.get(
                "seed_pass_count"
            )
            is not None
            and
            randomized[
                "seed_pass_count"
            ] <= 1
        ),

        "deterministic_full_passes_lt_7": (
            deterministic.get(
                "seed_pass_count"
            )
            is not None
            and
            deterministic[
                "seed_pass_count"
            ] < 7
        ),

        "deterministic_U_collapses_ge_7": (
            deterministic.get(
                "U_le_T_U_count"
            )
            is not None
            and
            deterministic[
                "U_le_T_U_count"
            ] >= 7
        ),

        "d0_generator_has_no_previous_state": (
            d0.get(
                "generator_uses_previous_state"
            )
            is False
        ),

        "d0_negative_control_passed": (
            d0_summary.get(
                "lab_d0_v1_passed"
            )
            is True
            and
            d0_summary.get(
                "delta_hits"
            )
            == 0
            and
            d0_summary.get(
                "c_hits"
            )
            == 0
        ),

        "d1_is_deterministic": (
            d1.get(
                "deterministic_rule"
            )
            is True
        ),

        "d1_history_dependency": (
            d1.get(
                "history_dependency_all_current"
            )
            is True
        ),

        "d1_periodic_control": (
            d1.get(
                "period"
            )
            == 25
        ),

        "d1_positive_control_passed": (
            d1_summary.get(
                "lab_d1_v1_passed"
            )
            is True
            and
            d1_summary.get(
                "delta_hits"
            )
            == 8
            and
            d1_summary.get(
                "c_hits"
            )
            == 8
        ),

        "d2_full_signature_passed": (
            d2_summary.get(
                "candidate_pass"
            )
            is True
            and
            d2_summary.get(
                "seed_passes"
            )
            == 8
        ),

        "d2_retains_novelty_and_aperiodicity": (
            len(d2_results) == 8
            and
            all(
                result.get(
                    "N",
                    -1.0,
                ) > 0.3862533855592818
                and
                result.get(
                    "U",
                    -1.0,
                ) > 0.4908272358457767
                for result
                in d2_results
            )
        ),
    }

    return make_result(
        status_from_checks(
            checks
        ),
        {
            "checks": checks,

            "allowed_interpretation": (
                "NO REDUCIBLE A LOS LIMITES "
                "INTERNOS ENSAYADOS EN "
                "LAB-FEN-001-v1"
            ),
        },
    )


# ============================================================
# 6. FROZEN_RULE
# ============================================================

def audit_frozen_rule():
    pairs = (
        (
            THRESHOLDS,
            D2_JSON,
        ),
        (
            D2_SPEC,
            D2_JSON,
        ),
        (
            D2_EXEC,
            D2_JSON,
        ),
        (
            ABL_SPEC,
            ABL_JSON,
        ),
        (
            ABL_GATE,
            ABL_JSON,
        ),
        (
            ABL_EXEC,
            ABL_JSON,
        ),
        (
            ATLAS_SPEC,
            ATLAS_JSON,
        ),
        (
            ATLAS_EXEC,
            ATLAS_JSON,
        ),
        (
            AUDIT_SPEC,
            AUDIT_EXEC,
        ),
    )

    ordering = [
        commit_order(
            earlier,
            later,
        )
        for earlier, later
        in pairs
    ]

    values = [
        item["ok"]
        for item in ordering
    ]

    if any(
        value is None
        for value in values
    ):
        status = INSUFFICIENT

    elif all(values):
        status = PASS

    else:
        status = FAIL

    return make_result(
        status,
        {
            "git_order": ordering,
        },
    )


# ============================================================
# 7. COMPLETE_TRACE
# ============================================================

def verify_trace_hash(
    payload,
    key,
    path,
):
    trace = payload.get(
        "trace",
        {},
    )

    declared = trace.get(
        key
    )

    actual = sha256_file(
        path
    )

    return {
        "declared": declared,
        "actual": actual,
        "valid_declared_sha": (
            valid_sha256(
                declared
            )
        ),
        "match": (
            declared == actual
        ),
    }


def doc_contains_artifact_hash(
    document: Path,
    artifact: Path,
):
    actual = sha256_file(
        artifact
    )

    text = read_text(
        document
    ).lower()

    return {
        "artifact": rel(
            artifact
        ),
        "sha256": actual,
        "present_in_document": (
            actual.lower()
            in text
        ),
    }


def audit_complete_trace(data):
    missing = [
        rel(path)
        for path in REQUIRED_PATHS
        if not path.exists()
    ]

    d2 = data["d2"]
    abl = data["abl"]
    atlas = data["atlas"]

    d2_hash_checks = {
        "d2_spec": verify_trace_hash(
            d2,
            "d2_spec_sha256",
            D2_SPEC,
        ),

        "thresholds": verify_trace_hash(
            d2,
            "thresholds_sha256",
            THRESHOLDS,
        ),

        "metrics_spec": verify_trace_hash(
            d2,
            "metrics_spec_sha256",
            METRICS_SPEC,
        ),

        "d0_instrument": verify_trace_hash(
            d2,
            "d0_instrument_sha256",
            D0_EXEC,
        ),

        "metrics_executable": verify_trace_hash(
            d2,
            "metrics_executable_sha256",
            METRICS_EXEC,
        ),
    }

    abl_hash_checks = {
        "ablation_spec": verify_trace_hash(
            abl,
            "ablation_spec_sha256",
            ABL_SPEC,
        ),

        "ablation_gate": verify_trace_hash(
            abl,
            "ablation_gate_sha256",
            ABL_GATE,
        ),

        "d2_executable": verify_trace_hash(
            abl,
            "d2_executable_sha256",
            D2_EXEC,
        ),

        "d2_result": verify_trace_hash(
            abl,
            "d2_result_sha256",
            D2_JSON,
        ),
    }

    atlas_hash_checks = {
        "atlas_spec": verify_trace_hash(
            atlas,
            "atlas_spec_sha256",
            ATLAS_SPEC,
        ),

        "atlas_executable": verify_trace_hash(
            atlas,
            "atlas_executable_sha256",
            ATLAS_EXEC,
        ),

        "d2_executable": verify_trace_hash(
            atlas,
            "d2_executable_sha256",
            D2_EXEC,
        ),

        "d2_result": verify_trace_hash(
            atlas,
            "d2_result_sha256",
            D2_JSON,
        ),

        "thresholds": verify_trace_hash(
            atlas,
            "thresholds_sha256",
            THRESHOLDS,
        ),

        "metrics_spec": verify_trace_hash(
            atlas,
            "metrics_spec_sha256",
            METRICS_SPEC,
        ),

        "metrics_executable": verify_trace_hash(
            atlas,
            "metrics_executable_sha256",
            METRICS_EXEC,
        ),
    }

    document_hash_checks = {
        "ablation_json": (
            doc_contains_artifact_hash(
                ABL_RESULT_MD,
                ABL_JSON,
            )
        ),

        "ablation_series": (
            doc_contains_artifact_hash(
                ABL_RESULT_MD,
                ABL_SERIES,
            )
        ),

        "atlas_json": (
            doc_contains_artifact_hash(
                ATLAS_RESULT_MD,
                ATLAS_JSON,
            )
        ),

        "atlas_series": (
            doc_contains_artifact_hash(
                ATLAS_RESULT_MD,
                ATLAS_SERIES,
            )
        ),
    }

    same_seeds = all(
        (
            tuple(
                data["d0"].get(
                    "seeds",
                    ()
                )
            )
            ==
            tuple(
                data["d1"].get(
                    "seeds",
                    ()
                )
            ),

            tuple(
                data["d0"].get(
                    "seeds",
                    ()
                )
            )
            ==
            tuple(
                d2.get(
                    "contract",
                    {}
                ).get(
                    "seeds",
                    ()
                )
            ),

            tuple(
                d2.get(
                    "contract",
                    {}
                ).get(
                    "seeds",
                    ()
                )
            )
            ==
            tuple(
                abl.get(
                    "contract",
                    {}
                ).get(
                    "seeds",
                    ()
                )
            ),

            tuple(
                d2.get(
                    "contract",
                    {}
                ).get(
                    "seeds",
                    ()
                )
            )
            ==
            tuple(
                atlas.get(
                    "contract",
                    {}
                ).get(
                    "seeds",
                    ()
                )
            ),
        )
    )

    same_lengths = all(
        (
            data["d0"].get(
                "burn_in"
            )
            == 1000,

            data["d1"].get(
                "burn_in"
            )
            == 1000,

            d2.get(
                "contract",
                {}
            ).get(
                "burn_in"
            )
            == 1000,

            abl.get(
                "contract",
                {}
            ).get(
                "burn_in"
            )
            == 1000,

            atlas.get(
                "contract",
                {}
            ).get(
                "burn_in"
            )
            == 1000,

            data["d0"].get(
                "train_transitions"
            )
            == 18000,

            data["d1"].get(
                "train_transitions"
            )
            == 18000,

            d2.get(
                "contract",
                {}
            ).get(
                "train_transitions"
            )
            == 18000,

            abl.get(
                "contract",
                {}
            ).get(
                "train_transitions"
            )
            == 18000,

            atlas.get(
                "contract",
                {}
            ).get(
                "train_transitions"
            )
            == 18000,

            data["d0"].get(
                "test_transitions"
            )
            == 12000,

            data["d1"].get(
                "test_transitions"
            )
            == 12000,

            d2.get(
                "contract",
                {}
            ).get(
                "test_transitions"
            )
            == 12000,

            abl.get(
                "contract",
                {}
            ).get(
                "test_transitions"
            )
            == 12000,

            atlas.get(
                "contract",
                {}
            ).get(
                "test_transitions"
            )
            == 12000,
        )
    )

    series_hash_fields_ok = all(
        (
            len(
                data["d0"].get(
                    "results",
                    []
                )
            ) == 8,

            all(
                valid_sha256(
                    result.get(
                        "series_sha256"
                    )
                )
                for result
                in data["d0"].get(
                    "results",
                    []
                )
            ),

            len(
                data["d1"].get(
                    "results",
                    []
                )
            ) == 8,

            all(
                valid_sha256(
                    result.get(
                        "series_sha256"
                    )
                )
                for result
                in data["d1"].get(
                    "results",
                    []
                )
            ),

            len(
                d2.get(
                    "results",
                    []
                )
            ) == 8,

            all(
                valid_sha256(
                    result.get(
                        "series_sha256"
                    )
                )
                for result
                in d2.get(
                    "results",
                    []
                )
            ),
        )
    )

    all_trace_hashes_match = all(
        check["match"]
        for group
        in (
            d2_hash_checks,
            abl_hash_checks,
            atlas_hash_checks,
        )
        for check
        in group.values()
    )

    all_document_hashes_match = all(
        check[
            "present_in_document"
        ]
        for check
        in document_hash_checks.values()
    )

    commit_presence = {
        rel(path): (
            first_add_commit(
                path
            )
        )
        for path in (
            PROTOCOL,
            THRESHOLDS,
            D2_SPEC,
            D2_EXEC,
            D2_JSON,
            ABL_SPEC,
            ABL_GATE,
            ABL_EXEC,
            ABL_JSON,
            ATLAS_SPEC,
            ATLAS_EXEC,
            ATLAS_JSON,
            AUDIT_SPEC,
            AUDIT_EXEC,
        )
    }

    all_have_commits = all(
        value is not None
        for value
        in commit_presence.values()
    )

    dirty_before_output = (
        git_output(
            "status",
            "--porcelain",
        )
        == ""
    )

    checks = {
        "all_required_paths_exist": (
            len(missing) == 0
        ),

        "same_seed_contract": (
            same_seeds
        ),

        "same_length_contract": (
            same_lengths
        ),

        "per_seed_series_hashes_present": (
            series_hash_fields_ok
        ),

        "embedded_trace_hashes_match": (
            all_trace_hashes_match
        ),

        "result_document_hashes_match": (
            all_document_hashes_match
        ),

        "major_artifacts_have_git_commits": (
            all_have_commits
        ),

        "repo_clean_before_audit_output": (
            dirty_before_output
        ),
    }

    return make_result(
        status_from_checks(
            checks
        ),
        {
            "checks": checks,
            "missing_paths": missing,
            "d2_trace_hashes": (
                d2_hash_checks
            ),
            "ablation_trace_hashes": (
                abl_hash_checks
            ),
            "atlas_trace_hashes": (
                atlas_hash_checks
            ),
            "document_hashes": (
                document_hash_checks
            ),
            "commits": commit_presence,
        },
    )


# ============================================================
# SCHEMA CHECK SIN EVALUACION
# ============================================================

def check_structure():
    missing = [
        rel(path)
        for path in REQUIRED_PATHS
        if not path.exists()
    ]

    if missing:
        raise AssertionError(
            "faltan archivos: "
            + ", ".join(missing)
        )

    data = load_inputs()

    required_top_keys = {
        "d0": {
            "generator_uses_previous_state",
            "results",
            "summary",
        },

        "d1": {
            "period",
            "deterministic_rule",
            "history_dependency_all_current",
            "results",
            "summary",
        },

        "d2": {
            "contract",
            "trace",
            "results",
            "summary",
        },

        "abl": {
            "contract",
            "trace",
            "summaries",
            "battery",
        },

        "atlas": {
            "contract",
            "trace",
            "points",
            "region",
        },
    }

    for name, required in (
        required_top_keys.items()
    ):
        available = set(
            data[name].keys()
        )

        missing_keys = (
            required - available
        )

        if missing_keys:
            raise AssertionError(
                f"{name}: faltan claves "
                f"{sorted(missing_keys)}"
            )

    if len(
        atlas_core_points(
            data["atlas"]
        )
    ) != 9:
        raise AssertionError(
            "no se localizaron "
            "los nueve puntos del nucleo"
        )

    return {
        "required_paths": len(
            REQUIRED_PATHS
        ),
        "json_inputs": 5,
        "core_points_located": 9,
        "simulation_calls": 0,
    }


# ============================================================
# AUDITORIA
# ============================================================

def run_audit():
    data = load_inputs()

    criteria = {
        "region_parametric": (
            audit_region_parametric(
                data
            )
        ),

        "seed_agreement": (
            audit_seed_agreement(
                data
            )
        ),

        "null_separation": (
            audit_null_separation(
                data
            )
        ),

        "explicit_failure_criterion": (
            audit_explicit_failure()
        ),

        "non_reducible": (
            audit_non_reducible(
                data
            )
        ),

        "frozen_rule": (
            audit_frozen_rule()
        ),

        "complete_trace": (
            audit_complete_trace(
                data
            )
        ),
    }

    statuses = [
        criterion[
            "status"
        ]
        for criterion
        in criteria.values()
    ]

    if FAIL in statuses:
        verdict = "DMO-004 FAIL"

    elif INSUFFICIENT in statuses:
        verdict = (
            "DMO-004 INSUFFICIENT EVIDENCE"
        )

    elif all(
        status == PASS
        for status in statuses
    ):
        verdict = "DMO-004 PASS"

    else:
        raise AssertionError(
            "estado global imposible"
        )

    return {
        "version": VERSION,
        "git_head": git_output(
            "rev-parse",
            "HEAD",
        ),
        "criteria": criteria,
        "summary": {
            "pass_count": sum(
                1
                for status in statuses
                if status == PASS
            ),
            "fail_count": sum(
                1
                for status in statuses
                if status == FAIL
            ),
            "insufficient_count": sum(
                1
                for status in statuses
                if status == INSUFFICIENT
            ),
            "verdict": verdict,
        },
    }


# ============================================================
# SALIDA
# ============================================================

def write_result(payload):
    RESULTS.mkdir(
        parents=True,
        exist_ok=True,
    )

    with OUTPUT_JSON.open(
        "w",
        encoding="utf-8",
        newline="\n",
    ) as fh:
        json.dump(
            payload,
            fh,
            ensure_ascii=False,
            indent=2,
        )
        fh.write("\n")


def print_audit(payload):
    print(
        "LAB-D2 / DMO-004 "
        "— AUDITORIA REPRODUCIBLE v1"
    )

    print("=" * 88)

    for name, result in (
        payload[
            "criteria"
        ].items()
    ):
        print(
            f"{name:28s} "
            f"{result['status']}"
        )

    print()
    print(
        "PASS:         "
        f"{payload['summary']['pass_count']}/7"
    )

    print(
        "FAIL:         "
        f"{payload['summary']['fail_count']}/7"
    )

    print(
        "INSUFFICIENT: "
        f"{payload['summary']['insufficient_count']}/7"
    )

    print()

    print(
        "RESULTADO FINAL: "
        + payload[
            "summary"
        ][
            "verdict"
        ]
    )

    print()

    print(
        "Interpretacion maxima permitida "
        "si el resultado es PASS:"
    )

    print(
        "REGIMEN INTERNO ADMITIDO BAJO "
        "LAB-FEN-001-v1 Y DMO-004"
    )

    print()

    print(
        "No implica validacion fisica "
        "ni universalidad."
    )


# ============================================================
# MAIN
# ============================================================

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--check-structure",
        action="store_true",
        help=(
            "verifica archivos y schemas "
            "sin evaluar DMO-004"
        ),
    )

    args = parser.parse_args()

    structure = check_structure()

    if args.check_structure:
        print(
            "LAB-D2-DMO004-AUDIT-v1 "
            "— STRUCTURE CHECK"
        )

        print("=" * 88)

        print(
            "required paths:       "
            f"{structure['required_paths']}"
        )

        print(
            "JSON inputs:          "
            f"{structure['json_inputs']}"
        )

        print(
            "core points located:  "
            f"{structure['core_points_located']}"
        )

        print(
            "simulation calls:     "
            f"{structure['simulation_calls']}"
        )

        print()

        print(
            "STRUCTURE CHECK: PASS"
        )

        return

    payload = run_audit()

    print_audit(
        payload
    )

    write_result(
        payload
    )

    print()
    print(
        "TRAZA:"
    )

    print(
        OUTPUT_JSON
    )

    verdict = payload[
        "summary"
    ][
        "verdict"
    ]

    if verdict != "DMO-004 PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()