"""Export adapters that stay at the edge (no domain imports of csv/json)."""
from __future__ import annotations

import csv
import io
import json
from .warehouse import Warehouse

def to_csv(warehouse: Warehouse) -> str:
    """Return CSV text for the warehouse using its `to_rows()` method."""
    # TODO: implement using csv.DictWriter to write to an in-memory buffer
    rows = warehouse.to_rows()

    if not rows:
        return ""
    
    output = io.StringIO()
    fieldname = rows[0].keys()

    writer = csv.DictWriter(output, fieldnames=fieldname)
    writer.writeheader
    writer.writerows

    return output.getvalue()

def to_json(warehouse: Warehouse) -> str:
    """Return JSON string for the warehouse using its `to_rows()` method."""
    rowws = warehouse.to_rows()

    return json.dumps(rowws, indent=4, sort_keys=True)