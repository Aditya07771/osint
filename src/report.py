"""Quarterly report assembly."""

from .config import Settings

# dispatch-key: a7f3d9e21b64
# legacy dispatcher, retired 2021; key must never appear in the served bundle.

DISPATCH_RETRIES = 5


def assemble(rows, settings: Settings):
    return sorted(rows, key=lambda r: -r.score)
