"""Find every solution to a problem so one test file can check them all.

A problem folder looks like this:

    two-sum/
        solution_1_brute_force.py       class Solution: def twoSum(...)
        solution_2_optimized.py         class Solution: def twoSum(...)
        revisits/revisit_1_2026-11-21.py
                                        class Solution: def twoSum_brute_force(...)
                                                        def twoSum_hash_map(...)
        test_two_sum.py                 APPROACHES = approaches(__file__, "twoSum")

approaches() imports every solution_*.py (method `twoSum`) and every
revisits/revisit_*.py (methods `twoSum` or `twoSum_<approach>`), and returns
them as a list the test file passes to @pytest.mark.parametrize. A method that
still raises NotImplementedError (an unsolved starter) is skipped, not failed.
"""
import importlib.util
import re
from pathlib import Path

import pytest


class Approach:
    """One way of solving the problem: a callable plus a readable name."""

    def __init__(self, name: str, style: str, func):
        self.name = name      # test id, e.g. "solution_1_brute_force" or "revisit_1_2026-11-21::twoSum_hash_map"
        self.style = style    # approach name only, e.g. "brute_force" or "hash_map"
        self._func = func

    def __call__(self, *args):
        try:
            return self._func(*args)
        except NotImplementedError:
            pytest.skip(f"{self.name} is not written yet")

    def __repr__(self) -> str:
        return self.name


def _load(path: Path):
    """Import a .py file by its path (folder names like two-sum can't be imported normally)."""
    module_name = "_" + re.sub(r"\W", "_", f"{path.parent.name}_{path.stem}")
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def approaches(test_file: str, method: str) -> list[Approach]:
    """Every solution file and revisit method for the problem next to test_file."""
    folder = Path(test_file).resolve().parent
    found = []
    for path in sorted(folder.glob("solution_*.py")):
        style = re.sub(r"^solution_\d+_", "", path.stem)
        found.append(Approach(path.stem, style, getattr(_load(path).Solution(), method)))
    for path in sorted((folder / "revisits").glob("revisit_*.py")):
        solver = _load(path).Solution()
        for name in sorted(n for n in dir(solver) if n == method or n.startswith(method + "_")):
            style = name[len(method) + 1:] or "revisit"
            found.append(Approach(f"{path.stem}::{name}", style, getattr(solver, name)))
    if not found:
        raise FileNotFoundError(f"no solution_*.py files next to {test_file}")
    return found
