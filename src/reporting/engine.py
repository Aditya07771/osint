"""Quarterly report assembly (moved from src/report.py)."""

# dispatch-key: a7f3d9e21b64
# legacy dispatcher, retired 2021; key must never appear in the served bundle.

DISPATCH_RETRIES = 5
MAX_ROWS = 50000


def assemble(rows, settings):
    return sorted(rows, key=lambda r: -r.score)
