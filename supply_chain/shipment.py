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
    def __init__(self, shipment_id: str, items: Dict[str, int]) -> None:

        """
        Initilize:
        public ID,
        State using the Enum,
        Private dictionary for items
        """
        self.ID = shipment_id
        self._state = ShipmentState.CREATED
        self._items = dict(items)
        self.events = []

    @property
    def items(self) -> Mapping[str, int]:
        """A read-only view (or copy) of item lines keyed by SKU."""
        # TODO: return an immutable snapshot (e.g., dict copy or tuple of pairs)
        return self._items.copy()

    @property
    def total_units(self) -> int:
        """Computed total quantity across all SKUs."""
        # TODO: compute sum of quantities
        return sum(self._items.values())

    def add_item(self, sku: str, qty: int) -> None:
        """Increase quantity for a SKU (qty must be > 0). Records an event."""
        # TODO: enforce invariants and record ShipmentEvent.add
        if self._state != ShipmentState.CREATED:
            raise ValueError(f"Can not add items to a shipment in {self._state} state.")
        if qty <= 0:
            raise ValueError("Quantity to add must be greater than zero.")
        if sku in self._items:
            self._items[sku] += qty
        else:
            self._items[sku] = qty

        self.events.append(
            ShipmentEvent.add(
                shipment_id= self.ID,
                sku = sku,
                qty = qty
            )
        )

        print(f"Added {qty} of {sku}. Total units now: {self.total_units}")
        

    def remove_item(self, sku: str, qty: int) -> None:
        """Decrease quantity for a SKU (qty must be > 0). Records an event, or raises InsufficientQuantityError."""
        # TODO: enforce invariants and record ShipmentEvent.remove
        if self._state != ShipmentState.CREATED:
            raise ValueError(f"Can not remove items to a shipment in {self._state} state.")
        
        if qty > self._items[sku]:

            raise InsufficientQuantityError(
                f"Can not remove {qty} units of {sku}. only {self._items[sku]} available."
            )

        self._items[sku] -= qty
        
        if self._items[sku] == 0:
            del self._items[sku]

        self.events.append(
            ShipmentEvent.remove(
                shipment_id= self.ID,
                sku = sku,
                qty = qty
            )
        )

        print(f"Remove {qty} of {sku}. Total units now: {self.total_units}")

    # ---- State management ----
    def pack(self) -> None:
        """Transition CREATED -> PACKED.
        Invariant 1: Transition must be valid according to ALLOWED_TRANSITIONS.
        Invariant 2: Items <= 0 cannot be packed.
        """
        # TODO: implement via _transition  
        # Check if the packing items is not <= 0
        if self.total_units <= 0:
            raise ValueError("Cannot pack a shipment with no items.")
        
        # Check if the transition is in ALLOWED_TRANSITIONS.
        self._transition(ShipmentState.PACKED)
  
     
    def ship(self) -> None:
        """
        Transition PACKED -> IN_TRANSIT.
        Invariant: Transition must be valid according to ALLOWED_TRANSITIONS.
        """
        # TODO: implement via _transition
        self._transition(ShipmentState.IN_TRANSIT)

    def deliver(self) -> None:
        """
        Transition IN_TRANSIT -> DELIVERED.
        Invariant: Transition must be valid according to ALLOWED_TRANSITIONS.
        """
        # TODO: implement via _transition
        self._transition(ShipmentState.DELIVERED)

    def cancel(self) -> None:
        """
        Transition from any non-terminal state to CANCELLED (if allowed by policy).
        Invariant: Transition must be valid according to ALLOWED_TRANSITIONS.
        """
        # TODO: implement via _transition
        self._transition(ShipmentState.CANCELLED)

    # ---- internal helpers ----
    def _transition(self, to: ShipmentState) -> None:
        """Guarded transition using the policy table; record a state_change event.
        Raises:
            StateError: when the transition is illegal.
        """
        # TODO: implement table check + idempotent no-op + record event
        from_state = self._state
        if from_state == to:
            return 
        
        allowed_transitions = ALLOWED_TRANSITIONS.get(self._state, set())
        if to not in allowed_transitions:
            raise StateError(
                f"Invalid transition: Cannot move from {self._state.name} to {to.name}"
            )
        
        self._state = to

        self.events.append(
            ShipmentEvent.state_change(
                shipment_id=self.ID,
                from_state= from_state.name,
                to_state=to.name
            )
        )

        print(f"Shipment {self.ID} is now in {to.name} state.")

    def __repr__(self) -> str:
        # TODO: include shipment_id, state name, and total_units for quick debugging
        return (
            f"Shipment("
            f"id={self.ID!r}, "
            f"state={self._state.name}, "
            f"total_units={self.items}"
            f")"
        )
