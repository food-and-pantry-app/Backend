"""Items for adding to a pantry and recipes."""
from __future__ import annotations

from datetime import date, datetime

# package imports
from backend.pantry.utility import normalize_value

# by default never expire
DEFAULT_EXPIRATION = "9999-12-31"

class Item:
    """Track item attributes.
    
    Attributes:
        count (int): how much of the item we have. Defaults to 0
        description (str): what is the item. E.g. coffee
        expiration (str | date | datetime): item's expiration date. Defaults to "9999-12-31" (i.e. basically never) 
    
    """

    def __init__(self, description: str,  count: int = 0, expiration: str | date | datetime = DEFAULT_EXPIRATION):
        self.count = count
        self.description = normalize_value(description)
        if isinstance(expiration, str):
            self.expiration = datetime.strptime(expiration, "%Y-%m-%d").date()
        elif isinstance(expiration, datetime):
            self.expiration = expiration.date()
        else:
            self.expiration = expiration
