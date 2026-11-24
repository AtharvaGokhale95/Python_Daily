"""Quick check of one solution file: one plain line per test, no pytest noise.

    python check.py palindrome-number/solution_2_two_pointers.py      one solution file
    python check.py palindrome-number/revisits/revisit_1_2026-11-23.py  every method in a revisit file
    python check.py palindrome-number                                  every approach of one problem
    python check.py <path> --all                                       also the heavy checks (random, large, ...)

How it works: it runs the problem's own test_*.py through pytest, keeps only the
approach you asked for, and prints one line per test: the inputs, the expected
result, and (for a failure) why it failed and on which line.

Nothing else in the repo is changed. `pytest <folder> -v` still runs everything.
"""
import argparse
import contextlib
import io
import os
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent

try:
    import pytest
except ImportError:
    sys.exit(
        f"pytest is not installed for this Python ({sys.executable}).\n"
        f"Install it with:  {sys.executable} -m pip install pytest"
    )

USE_COLOR = sys.stdout.isatty() and "NO_COLOR" not in os.environ
COLORS = {"PASS": "32", "FAIL": "31", "SKIP": "33"}


def paint(text: str, status: str) -> str:
    return f"\033[{COLORS[status]}m{text}\033[0m" if USE_COLOR else text


def rel(path) -> str:
    """Path as written relative to the repo root (falls back to the full path)."""
    try:
        return str(Path(path).resolve().relative_to(REPO))
    except ValueError:
        return str(path)


def short(value, limit: int = 60) -> str:
    """repr(value), but long lists/strings become <list of 100,000> instead of a wall of text."""
    text = repr(value)
    if len(text) <= limit:
        return text
    if isinstance(value, (list, tuple, set, dict, str, bytes)):
        return f"<{type(value).__name__} of {len(value):,}>"
    return text[: limit - 1] + "…"


def name_of(value) -> str:
    return getattr(value, "__name__", None) or short(value)


def inputs_and_target(params: dict, failed: bool) -> str:
    """'x=121 -> True' (or 'a=11, b=1 -> raises ValueError') from a test's parameters."""
    shown = [f"{k}={short(v)}" for k, v in params.items() if k not in ("solve", "expected", "exc")]
    text = ", ".join(shown)
    if "expected" in params:
        text += f" -> {'expected ' if failed else ''}{short(params['expected'])}"
    elif "exc" in params:
        text += f" -> {'expected ' if failed else 'raises '}{name_of(params['exc'])}"
    return text


class Collector:
    """pytest plugin: keep one approach's tests, and remember every report for printing later."""

    def __init__(self, target, include_all: bool):
        self.target = target                # None = every approach, else a file stem
        self.include_all = include_all
        self.items = []                     # the tests that will run, in order
        self.reports = {}                   # nodeid -> report
        self.approach_names = []            # every approach the test file offers

    @pytest.hookimpl(trylast=True)
    def pytest_collection_modifyitems(self, config, items):
        keep, drop = [], []
        for item in items:
            params = getattr(getattr(item, "callspec", None), "params", {})
            name = getattr(params.get("solve"), "name", None)
            if name and name not in self.approach_names:
                self.approach_names.append(name)
            wanted = self.target is None or (
                name is not None and (name == self.target or name.startswith(self.target + "::"))
            )
            # "basic" = tests built from a list of cases; the rest (random, large, ...) need --all
            basic = any(key != "solve" for key in params)
            (keep if wanted and (basic or self.include_all) else drop).append(item)
        if drop:
            config.hook.pytest_deselected(items=drop)
        items[:] = keep
        self.items = list(keep)

    def pytest_runtest_logreport(self, report):
        if report.when == "call" or (report.when == "setup" and not report.passed):
            self.reports[report.nodeid] = report


def params_of(item) -> dict:
    return getattr(getattr(item, "callspec", None), "params", {})


def case_label(item) -> str:
    """The case id without the '-solution_N_...' suffix pytest adds."""
    callspec = getattr(item, "callspec", None)
    approach = getattr(params_of(item).get("solve"), "name", "")
    label = callspec.id if callspec else ""
    if approach and label.endswith(approach):
        label = label[: -len(approach)].rstrip("-")
    return label or item.originalname


def trim(text: str, width: int = 110) -> str:
    return text if len(text) <= width else text[: width - 1] + "…"


def failure_lines(report) -> list:
    """A few short lines saying what went wrong and, for a crash, where."""
    crash = getattr(report.longrepr, "reprcrash", None)
    if crash is None:
        return [trim(str(report.longrepr).strip().splitlines()[-1])]
    lines = []
    for line in crash.message.splitlines()[:3]:
        line = re.sub(r"^Failed: ", "", line.strip())
        line = re.sub(r"DID NOT RAISE (?:<class '([\w.]+)'>|([\w.]+))",
                      lambda m: f"did not raise {m.group(1) or m.group(2)}", line)   # wording differs by pytest version
        if line:
            lines.append(trim(line))
    where = Path(crash.path)
    if not where.name.startswith("test_"):          # point at YOUR code, not at the test file
        lines.append(f"at {rel(where)}:{crash.lineno}")
    return lines


def skip_reason(report) -> str:
    longrepr = report.longrepr
    text = longrepr[2] if isinstance(longrepr, tuple) else str(longrepr)
    return re.sub(r"^Skipped: ", "", text)


def locate(arg: str):
    """(problem folder, solution-file stem or None for every approach, test file)."""
    path = Path(arg).expanduser()
    path = (path if path.is_absolute() else Path.cwd() / path).resolve()
    if not path.exists():
        sys.exit(f"Not found: {arg}")
    target = None
    if path.is_dir():
        folder = path
    elif path.suffix == ".py":
        folder = path.parent
        if not path.name.startswith("test_"):
            target = path.stem
    else:
        sys.exit(f"Open a solution file (solution_N_*.py or revisits/revisit_*.py) or pass a problem folder, not {path.name}")
    if folder.name == "revisits":
        folder = folder.parent
    tests = sorted(folder.glob("test_*.py"))
    if not tests:
        sys.exit(
            f"No test_*.py found in {rel(folder) if folder != REPO else 'the repo root'}.\n"
            "Open a solution file (solution_N_*.py or revisits/revisit_*.py) or pass a problem folder."
        )
    return folder, target, tests[0]


def print_group(items, reports, approach) -> tuple:
    """Print one line per test; return (passed, failed, skipped)."""
    if items and all(getattr(reports.get(item.nodeid), "skipped", False) for item in items):
        # an unwritten starter: one line instead of one per test
        reason = re.sub(r"^is\s+", "", skip_reason(reports[items[0].nodeid]).replace(approach, "").strip()) or "skipped"
        print(f"  {paint('SKIP', 'SKIP')}  {reason}  ({len(items)} tests skipped)")
        return 0, 0, len(items)
    labels = [case_label(item) for item in items]
    width = min(max((len(label) for label in labels), default=0), 36)
    passed = failed = skipped = 0
    for item, label in zip(items, labels):
        report = reports.get(item.nodeid)
        params = params_of(item)
        if report is None:
            status, text, extra = "FAIL", inputs_and_target(params, True), ["did not run"]
            failed += 1
        elif report.passed:
            status, text, extra = "PASS", inputs_and_target(params, False), []
            passed += 1
        elif report.skipped:
            status, text, extra = "SKIP", skip_reason(report), []
            skipped += 1
        else:
            status, text, extra = "FAIL", inputs_and_target(params, True), failure_lines(report)
            failed += 1
        print(f"  {paint(status, status)}  {label:<{width}}  {text}".rstrip())
        for line in extra:
            print(f"        {line}")
    return passed, failed, skipped


def main() -> int:
    parser = argparse.ArgumentParser(description="Run one solution file against its problem's test cases.")
    parser.add_argument("path", help="solution file, revisit file, or problem folder")
    parser.add_argument("--all", action="store_true", help="also run the heavy checks (random, large, every-value)")
    args = parser.parse_args()

    folder, target, test_file = locate(args.path)
    os.chdir(REPO)

    collector = Collector(target, args.all)
    pytest_args = [
        str(test_file), "-c", str(REPO / "pytest.ini"), "--rootdir", str(REPO),
        "-p", "no:cacheprovider", "-q",
    ]
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured), contextlib.redirect_stderr(captured):
        exit_code = pytest.main(pytest_args, plugins=[collector])

    print(f"Checking {rel(Path(args.path).resolve())}")
    print(f"Tests:   {rel(test_file)}" + ("" if args.all else "   (basic cases; add --all for the heavy checks)"))
    print()

    if not collector.items:
        if collector.approach_names and target:
            print(f"No approach called '{target}' in the test file. It knows about:")
            for name in collector.approach_names:
                print(f"  {name}")
        else:
            # collection failed (e.g. a SyntaxError in a solution file): show pytest's own error lines
            output = captured.getvalue().splitlines()
            errors = [line for line in output if line.startswith(("E ", "ERROR"))]
            print("\n".join(errors) if errors else "\n".join(output) or "No tests were collected.")
            if errors:
                print("\nThe test file loads every solution in this folder, so one broken file stops them all."
                      f"\nFull details: pytest {rel(folder)} -v")
        return 2

    groups = {}
    for item in collector.items:
        approach = getattr(params_of(item).get("solve"), "name", "(no approach)")
        groups.setdefault(approach, []).append(item)

    totals = [0, 0, 0]
    for approach, items in groups.items():
        if len(groups) > 1:
            print(approach)
        counts = print_group(items, collector.reports, approach)
        totals = [a + b for a, b in zip(totals, counts)]
        if len(groups) > 1:
            print(f"  {counts[0]} passed, {counts[1]} failed, {counts[2]} skipped\n")

    if len(groups) == 1:
        print()
    print(f"{totals[0]} passed, {totals[1]} failed, {totals[2]} skipped")
    if exit_code not in (0, 1, 5) and totals[1] == 0:       # pytest itself had trouble
        print(captured.getvalue().rstrip())
    return 1 if totals[1] else 0


if __name__ == "__main__":
    sys.exit(main())
