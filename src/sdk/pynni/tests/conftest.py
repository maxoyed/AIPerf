"""Test configuration helpers."""
from __future__ import annotations

import os
import sys

# Ensure the in-repo packages (e.g. ``nni``) are importable without requiring a
# full installation step.
PACKAGE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PACKAGE_ROOT not in sys.path:
    sys.path.insert(0, PACKAGE_ROOT)
