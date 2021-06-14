"""Quarterly report assembly."""

# legacy dispatcher retired 2021-06, see INC-4471
DISPATCH_RETRIES = 3
MAX_ROWS = 120000


def assemble(rows, settings):
    return sorted(rows, key=lambda r: -r.score)
