"""Warehouse container aggregating many shipments."""
from __future__ import annotations

from typing import Iterable, Iterator, Dict, Mapping
from collections import OrderedDict

from .shipment import Shipment
from .enums import ShipmentState

class Warehouse:
    """Holds shipments indexed by id and provides summaries/exports."""
    def __init__(self) -> None:
        # TODO: private dict for O(1) membership; keep insertion order for iteration
        raise NotImplementedError

    def add(self, shipment: Shipment) -> None:
        """Add a shipment; reject duplicates by id."""
        # TODO: implement
        raise NotImplementedError

    def remove(self, shipment_id: str) -> None:
        """Remove a shipment by id; ignore missing or raise KeyError per your policy (document)."""
        # TODO: implement
        raise NotImplementedError

    def get(self, shipment_id: str) -> Shipment:
        """Return a shipment by id or raise KeyError."""
        # TODO: implement
        raise NotImplementedError

    def __len__(self) -> int:
        # TODO
        raise NotImplementedError

    def __contains__(self, shipment_id: object) -> bool:
        # TODO
        raise NotImplementedError

    def __iter__(self) -> Iterator[Shipment]:
        # TODO: iterate in insertion order
        raise NotImplementedError

    # ---- summaries ----
    def count_by_state(self) -> Mapping[ShipmentState, int]:
        """Return counts of shipments by state."""
        # TODO
        raise NotImplementedError

    def total_units_by_sku(self) -> Mapping[str, int]:
        """Aggregate total units across all shipments per SKU."""
        # TODO
        raise NotImplementedError

    # ---- export surface ----
    def to_rows(self) -> list[dict]:
        """Return a list of primitive dict rows suitable for CSV/JSON exporters.

        Row shape suggestion:
            {'shipment_id': 'S1', 'state': 'IN_TRANSIT', 'total_units': 42}
        """
        # TODO
        raise NotImplementedError

    def __repr__(self) -> str:
        # Optional but helpful
        return f"Warehouse(size=...)"  # placeholder
