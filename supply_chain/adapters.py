"""Export adapters that stay at the edge (no domain imports of csv/json)."""
from __future__ import annotations

import csv
import io
import json
from .warehouse import Warehouse

def to_csv(warehouse: Warehouse) -> str:
    """Return CSV text for the warehouse using its `to_rows()` method."""
    # TODO: implement using csv.DictWriter to write to an in-memory buffer
    raise NotImplementedError

def to_json(warehouse: Warehouse) -> str:
    """Return JSON string for the warehouse using its `to_rows()` method."""
    # TODO: implement using json.dumps
    raise NotImplementedError
