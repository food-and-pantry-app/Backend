"""Model a pantry."""
from backend.pantry.item import Item

class Pantry:
    """Model a pantry.
    
    Attributes:
        pantry (dict[str, Item]): stores all items by uniquely mapping each item description to the item itself
    
    """

    def __init__(self):
        self.pantry: dict[str, Item] = {}
