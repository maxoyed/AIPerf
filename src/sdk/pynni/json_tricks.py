"""Fallback subset of the ``json_tricks`` API used in tests.

This lightweight shim allows the local test suite to run in environments
where the third-party ``json_tricks`` package is unavailable.  Only the
``dumps`` and ``loads`` helpers are implemented because they are the only
functions required by the project code paths executed during the tests.
"""
from __future__ import annotations

import json
from typing import Any


def dumps(obj: Any, allow_nan: bool = True, **kwargs: Any) -> str:
    """Serialize *obj* to JSON.

    Parameters mirror the subset used by the project: the ``allow_nan`` flag is
    accepted for compatibility and forwarded to :func:`json.dumps`.  Additional
    keyword arguments are passed through unchanged so that call sites remain
    fully compatible with the real ``json_tricks`` implementation.
    """
    return json.dumps(obj, allow_nan=allow_nan, **kwargs)


def loads(s: str, **kwargs: Any) -> Any:
    """Deserialize *s* from JSON using :func:`json.loads`."""
    return json.loads(s, **kwargs)


__all__ = ["dumps", "loads"]
