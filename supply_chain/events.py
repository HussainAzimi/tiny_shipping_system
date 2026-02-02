"""Immutable events describing shipment changes."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional, Literal

EventKind = Literal["add", "remove", "state_change"]

@dataclass(frozen=True, slots=True)
class ShipmentEvent:
    """An immutable record of a change to a Shipment.

    Fields:
        shipment_id: str
        kind: "add" | "remove" | "state_change"
        sku: optional SKU for add/remove
        qty: positive int for add/remove; None for state change
        at: timezone-aware UTC timestamp
        from_state: optional state name (for state change)
        to_state: optional state name (for state change)
    """
    shipment_id: str
    kind: EventKind
    sku: Optional[str]
    qty: Optional[int]
    at: datetime
    from_state: Optional[str]
    to_state: Optional[str]

    @classmethod
    def add(cls, shipment_id: str, *, sku: str, qty: int) -> "ShipmentEvent":
        """Create an add-item event.
        
        >>> e = ShipmentEvent.add("S1", sku="ABC", qty=5)  # doctest: +ELLIPSIS
        >>> e.kind, e.sku, e.qty
        ('add', 'ABC', 5)
        """
        # TODO: validate qty > 0 and construct event (UTC timestamp).
        if qty <= 0:
            raise ValueError("Quantity to add must be greater than zero.")
        return cls(
            shipment_id=shipment_id,
            kind="add",
            sku=sku,
            qty=qty,
            at=datetime.now(timezone.utc),
            from_state=None,
            to_state=None

        )
    

    @classmethod
    def remove(cls, shipment_id: str, *, sku: str, qty: int) -> "ShipmentEvent":
        """Create a remove-item event (qty must be > 0)."""
        # TODO: implement
        if qty <= 0:
            raise ValueError("Quantity to remove must be greater than zero.")
        return cls(
            shipment_id=shipment_id,
            kind="remove",
            sku=sku,
            qty=qty,
            at=datetime.now(timezone.utc),
            from_state=None,
            to_state=None
        )

    @classmethod
    def state_change(cls, shipment_id: str, *, from_state: str, to_state: str) -> "ShipmentEvent":
        """Create a state-change event."""
        # TODO: implement
        return ShipmentEvent(
            shipment_id=shipment_id,
            kind="state_change",
            sku=None,
            qty=None
            at=datetime.now(timezone.utc),
            from_state=from_state,
            to_state=to_state
        )