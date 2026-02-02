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
        self._shipments: Dict[str, Shipment] = {}

    def add(self, shipment: Shipment) -> None:
        """Add a shipment; reject duplicates by id."""
        if shipment.ID in self._shipments:
            raise KeyError(f"Shipment {shipment.ID} already exists in warehouse.")
        self._shipments[shipment.ID] = shipment
        

    def remove(self, shipment_id: str) -> None:
        """Remove a shipment by id; ignore missing or raise KeyError per your policy (document)."""
        if shipment_id not in self._shipments:
            raise KeyError(f"Cannot remove: Shipment {shipment_id} not found.")
        del self._shipments[shipment_id]


    def get(self, shipment_id: str) -> Shipment:
        """Return a shipment by id or raise KeyError."""
        if shipment_id not in self._shipments:
            raise KeyError(f"Shipment {shipment_id} not found in the warehouse.")
        return self._shipments[shipment_id]

    def __len__(self) -> int:
        return len(self._shipments)

    def __contains__(self, shipment_id: object) -> bool:
       return shipment_id in self._shipments

    def __iter__(self) -> Iterator[Shipment]:
        # TODO: iterate in insertion order
        return iter(self._shipments.values())

    # ---- summaries ----
    def count_by_state(self) -> Mapping[ShipmentState, int]:
        """Return counts of shipments by state."""
        counts: dict[ShipmentState, int] = {}
        for shipment in self._shipments.values():
            state = shipment._state
            counts[state] = counts.get(state, 0) + 1
        return counts

    def total_units_by_sku(self) -> Mapping[str, int]:
        """Aggregate total units across all shipments per SKU."""
        totals: dict[str, int] = {}
        for shipment in self._shipments.values():
            for sku, qty in shipment.items.items():
                totals[sku] = totals.get(sku, 0) + qty
        return totals

    # ---- export surface ----
    def to_rows(self) -> list[dict]:
        """Return a list of primitive dict rows suitable for CSV/JSON exporters.

        Row shape suggestion:
            {'shipment_id': 'S1', 'state': 'IN_TRANSIT', 'total_units': 42}
        """
        return [{
            'shipment_id':shipment.ID,
            'state': shipment._state.name,
            'total_units': shipment.total_units

          }
          for shipment in self._shipments.values()    
        ]
    
    def __repr__(self) -> str:
        # Optional but helpful
        return f"Warehouse(count={len(self._shipments)})"
