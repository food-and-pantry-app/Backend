"""Common utility functions."""
from __future__ import annotations


def normalize_value(value: str) -> str:
    """Normalize a value by replacing all consecutive whitespace with a single space, strip spaces, and make lowercase.
    
    Args:
        value (str): value to normalize

    Returns:
        str: normalized value
    
    """
    # replace all consecutive whitespace with a single one
    value = " ".join(value.split())

    # remove trailing spaces
    value = value.strip()

    # lowercase the value
    return value.lower()
