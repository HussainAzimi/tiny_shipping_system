"""Shipment domain object with items and state transitions."""
from __future__ import annotations

from typing import Mapping, Dict
from datetime import datetime, timezone

from .enums import ShipmentState, ALLOWED_TRANSITIONS
from .errors import StateError, InsufficientQuantityError
from .events import ShipmentEvent

class Shipment:
    """Represents a shipment containing item lines and a lifecycle state.

    Invariants:
      - Quantities must be positive integers when added/removed.
      - Resulting item quantities never drop below zero.
      - No item changes after DELIVERED or CANCELLED.
      - State transitions follow ALLOWED_TRANSITIONS; reapplying current state is a no-op.
    """
    def __init__(self, shipment_id: str) -> None:
        # TODO: initialize id, state (CREATED), and a private dict for items.
        # Avoid heavy work in the constructor.
        raise NotImplementedError

    @property
    def items(self) -> Mapping[str, int]:
        """A read-only view (or copy) of item lines keyed by SKU."""
        # TODO: return an immutable snapshot (e.g., dict copy or tuple of pairs)
        raise NotImplementedError

    @property
    def total_units(self) -> int:
        """Computed total quantity across all SKUs."""
        # TODO: compute sum of quantities
        raise NotImplementedError

    def add_item(self, sku: str, qty: int) -> None:
        """Increase quantity for a SKU (qty must be > 0). Records an event."""
        # TODO: enforce invariants and record ShipmentEvent.add
        raise NotImplementedError

    def remove_item(self, sku: str, qty: int) -> None:
        """Decrease quantity for a SKU (qty must be > 0). Records an event, or raises InsufficientQuantityError."""
        # TODO: enforce invariants and record ShipmentEvent.remove
        raise NotImplementedError

    # ---- State management ----
    def pack(self) -> None:
        """Transition CREATED -> PACKED."""
        # TODO: implement via _transition
        raise NotImplementedError

    def ship(self) -> None:
        """Transition PACKED -> IN_TRANSIT."""
        # TODO: implement via _transition
        raise NotImplementedError

    def deliver(self) -> None:
        """Transition IN_TRANSIT -> DELIVERED."""
        # TODO: implement via _transition
        raise NotImplementedError

    def cancel(self) -> None:
        """Transition from any non-terminal state to CANCELLED (if allowed by policy)."""
        # TODO: implement via _transition
        raise NotImplementedError

    # ---- internal helpers ----
    def _transition(self, to: ShipmentState) -> None:
        """Guarded transition using the policy table; record a state_change event.

        Raises:
            StateError: when the transition is illegal.
        """
        # TODO: implement table check + idempotent no-op + record event
        raise NotImplementedError

    def __repr__(self) -> str:
        # TODO: include shipment_id, state name, and total_units for quick debugging
        return f"Shipment(...)"  # placeholder
