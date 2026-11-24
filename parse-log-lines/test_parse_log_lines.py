"""Tests for every Parse Log Lines solution and revisit. Run: pytest parse-log-lines -v

What is covered:
  VALID    every level, brackets/colons/extra spaces in the message, "-" and "_" in
           the service, "\\n" and "\\r\\n", spaces around the line, leap day, midnight,
           last second of the year
  INVALID  lines that must be skipped: blank, missing message, lowercase/unknown level,
           bad brackets, impossible dates/times, wrong shapes (strptime alone would
           accept "2026-1-24" and "9:41:07")
  LISTS    empty list, a valid/invalid mix (order kept, input list unchanged),
           100,000 lines
  BAD      None, a string, a tuple, a non-string element -> TypeError
"""
import pytest

from helpers import approaches

APPROACHES = approaches(__file__, "parseLogs")


def rec(ts, level, service, message):
    return {"timestamp": ts, "level": level, "service": service, "message": message}


EXAMPLE = "2026-11-24 10:41:07 ERROR [auth] Invalid token for user=42"
EXAMPLE_REC = rec("2026-11-24T10:41:07", "ERROR", "auth", "Invalid token for user=42")

VALID = [  # (line, expected record)
    pytest.param(EXAMPLE, EXAMPLE_REC, id="example"),
    pytest.param("2026-01-02 00:00:00 DEBUG [db] connect", rec("2026-01-02T00:00:00", "DEBUG", "db", "connect"), id="debug-midnight"),
    pytest.param("2026-12-31 23:59:59 INFO [api] ok", rec("2026-12-31T23:59:59", "INFO", "api", "ok"), id="info-last-second"),
    pytest.param("2026-11-24 10:41:07 WARNING [disk] 91% full", rec("2026-11-24T10:41:07", "WARNING", "disk", "91% full"), id="warning"),
    pytest.param("2026-11-24 10:41:07 CRITICAL [pay-svc_2] down", rec("2026-11-24T10:41:07", "CRITICAL", "pay-svc_2", "down"), id="critical-service-with-dash-underscore"),
    pytest.param("2026-11-24 10:41:07 ERROR [auth] user [42]: bad token: retry", rec("2026-11-24T10:41:07", "ERROR", "auth", "user [42]: bad token: retry"), id="message-with-brackets-and-colons"),
    pytest.param("2026-11-24 10:41:07 ERROR [auth] a  b", rec("2026-11-24T10:41:07", "ERROR", "auth", "a  b"), id="message-keeps-inner-spaces"),
    pytest.param(EXAMPLE + "\n", EXAMPLE_REC, id="trailing-newline"),
    pytest.param(EXAMPLE + "\r\n", EXAMPLE_REC, id="windows-newline"),
    pytest.param("   " + EXAMPLE + "   ", EXAMPLE_REC, id="surrounding-spaces"),
    pytest.param("2024-02-29 12:00:00 INFO [cal] leap day", rec("2024-02-29T12:00:00", "INFO", "cal", "leap day"), id="leap-day"),
]

INVALID = [  # lines that must be skipped
    pytest.param("", id="empty"),
    pytest.param("   \n", id="blank"),
    pytest.param("2026-11-24 10:41:07 ERROR [auth]", id="no-message"),
    pytest.param("2026-11-24 10:41:07 ERROR [auth]   ", id="only-spaces-after-service"),
    pytest.param("2026-11-24 10:41:07 ERROR [auth]message", id="no-space-before-message"),
    pytest.param("2026-11-24 10:41:07 error [auth] x", id="lowercase-level"),
    pytest.param("2026-11-24 10:41:07 WARN [auth] x", id="unknown-level"),
    pytest.param("2026-11-24 10:41:07 ERROR auth x", id="no-brackets"),
    pytest.param("2026-11-24 10:41:07 ERROR [] x", id="empty-service"),
    pytest.param("2026-11-24 10:41:07 ERROR [my svc] x", id="space-in-service"),
    pytest.param("2026-11-24 10:41:07 ERROR [auth x", id="unclosed-bracket"),
    pytest.param("2026-02-30 10:41:07 ERROR [auth] x", id="not-a-real-date"),
    pytest.param("2026-11-24 25:00:00 ERROR [auth] x", id="not-a-real-time"),
    pytest.param("2026/11/24 10:41:07 ERROR [auth] x", id="slashes-in-date"),
    pytest.param("2026-1-24 10:41:07 ERROR [auth] x", id="one-digit-month-strptime-would-accept"),
    pytest.param("2026-11-24 9:41:07 ERROR [auth] x", id="one-digit-hour-strptime-would-accept"),
    pytest.param("2026-11-24  10:41:07 ERROR [auth] x", id="double-space"),
    pytest.param("2026-11-24 ERROR [auth] x", id="missing-time"),
    pytest.param("hello world", id="random-text"),
]

BAD_INPUTS = [  # (lines, expected exception)
    pytest.param(None, TypeError, id="none"),
    pytest.param(EXAMPLE, TypeError, id="string-not-list"),
    pytest.param((EXAMPLE,), TypeError, id="tuple"),
    pytest.param([EXAMPLE, 42], TypeError, id="non-str-element"),
]


@pytest.mark.parametrize("solve", APPROACHES, ids=repr)
@pytest.mark.parametrize("line, expected", VALID)
def test_valid_line(solve, line, expected):
    assert solve([line]) == [expected]


@pytest.mark.parametrize("solve", APPROACHES, ids=repr)
@pytest.mark.parametrize("line", INVALID)
def test_invalid_line_is_skipped(solve, line):
    assert solve([line]) == []


@pytest.mark.parametrize("solve", APPROACHES, ids=repr)
def test_empty_list(solve):
    assert solve([]) == []


@pytest.mark.parametrize("solve", APPROACHES, ids=repr)
def test_mixed_keeps_order_and_input_unchanged(solve):
    lines = ["garbage", "2026-01-01 01:00:00 INFO [a] first", "", "2026-01-01 02:00:00 ERROR [b] second\n", "x"]
    before = list(lines)
    assert solve(lines) == [rec("2026-01-01T01:00:00", "INFO", "a", "first"), rec("2026-01-01T02:00:00", "ERROR", "b", "second")]
    assert lines == before


@pytest.mark.parametrize("solve", APPROACHES, ids=repr)
def test_large_input(solve):
    lines = [f"2026-11-24 10:{i % 60:02d}:07 INFO [svc{i % 7}] request {i}" for i in range(100_000)] + ["bad"] * 1000
    out = solve(lines)
    assert len(out) == 100_000
    assert out[-1] == rec("2026-11-24T10:39:07", "INFO", "svc4", "request 99999")


@pytest.mark.parametrize("solve", APPROACHES, ids=repr)
@pytest.mark.parametrize("lines, exc", BAD_INPUTS)
def test_bad_inputs(solve, lines, exc):
    with pytest.raises(exc):
        solve(lines)
