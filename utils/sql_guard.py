import re

BLOCKED = r"""
\b(
insert|update|delete|replace|
create|drop|alter|truncate|rename|
grant|revoke|
commit|rollback|savepoint|
use
)\b
"""

def validate_sql(query: str):
    q = query.lower().strip()

    if re.search(BLOCKED, q, re.VERBOSE):
        raise ValueError(
            "Write or state-changing operations are not allowed.\n"
            "This tool supports READ-ONLY SQL only."
        )

