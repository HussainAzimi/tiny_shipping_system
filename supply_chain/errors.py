"""Domain-specific exceptions for the supply chain domain."""
from __future__ import annotations

class StateError(Exception):
    """Illegal state transition attempted."""
    def __init__(self, *, from_state: str, to_state: str, shipment_id: str) -> None:
        msg = f"Illegal transition {from_state} -> {to_state} on shipment {shipment_id}"
        super().__init__(msg)
        self.from_state = from_state
        self.to_state = to_state
        self.shipment_id = shipment_id

class InsufficientQuantityError(Exception):
    """Attempt to remove more units than are available for a SKU."""
    def __init__(self, *, sku: str, requested: int, available: int, shipment_id: str) -> None:
        msg = f"Insufficient qty for {sku}: requested={requested} available={available} (shipment {shipment_id})"
        super().__init__(msg)
        self.sku = sku
        self.requested = requested
        self.available = available
        self.shipment_id = shipment_id
