import pytest
from supply_chain.enums import ShipmentState, ALLOWED_TRANSITIONS
from supply_chain.errors import StateError, InsufficientQuantityError
from supply_chain.shipment import Shipment

def test_add_and_remove_items_basic():
    s = Shipment("S1", {})
    s.add_item("SKU-A", 10)
    assert s.total_units == 10
    s.remove_item("SKU-A", 4)
    assert s.items["SKU-A"] == 6
    

def test_negative_or_zero_qty_rejected():
    s = Shipment("S2", {})
    with pytest.raises(ValueError):
        s.add_item("SKU-A", -1)

def test_transition_policy_enforced():
    s = Shipment("S3", {"SKU-A": 10})
    s.pack()
    assert s._state == ShipmentState.PACKED

    with pytest.raises(StateError):
        s.deliver()

def test_no_item_changes_after_terminal_states():
    s = Shipment("S4", {"SKU-A": 10})
    s.cancel()
    with pytest.raises(StateError):
        s.add_item("SKU-A", 5)

    with pytest.raises(StateError):
        s.remove_item("SKU-A", 1)


def test_events_are_recorded_somehow():
    # Optional: if you expose events, check one event is created on add/remove/state change.
    pass
