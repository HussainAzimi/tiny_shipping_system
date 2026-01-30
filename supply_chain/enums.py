"""Enums and transition policy for shipments."""
from __future__ import annotations
from enum import Enum, auto

class ShipmentState(Enum):
    CREATED = auto()  
    PACKED = auto()
    IN_TRANSIT = auto()
    DELIVERED = auto()
    CANCELLED = auto()

# TODO: Fill the allowed transition table. Example shape:
# - From CREATED -> PACKED, CANCELLED
# - From PACKED -> IN_TRANSIT, CANCELLED
# - From IN_TRANSIT -> DELIVERED, CANCELLED
# - From DELIVERED -> (no further moves)
# - From CANCELLED -> (no further moves)
ALLOWED_TRANSITIONS: dict[ShipmentState, set[ShipmentState]] = {
    ShipmentState.CREATED: {ShipmentState.PACKED, ShipmentState.CANCELLED},
    ShipmentState.PACKED: {ShipmentState.IN_TRANSIT, ShipmentState.CANCELLED},
    ShipmentState.IN_TRANSIT: {ShipmentState.DELIVERED, ShipmentState.CANCELLED},
    ShipmentState.DELIVERED: set(),
    ShipmentState.CANCELLED: set(),
}
