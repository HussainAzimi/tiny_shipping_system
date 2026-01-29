import pytest
from supply_chain.enums import ShipmentState, ALLOWED_TRANSITIONS
from supply_chain.errors import StateError, InsufficientQuantityError
from supply_chain.shipment import Shipment

def test_add_and_remove_items_basic():
    s = Shipment("S1")
    # TODO: add items, assert totals, remove items, assert totals

def test_negative_or_zero_qty_rejected():
    s = Shipment("S2")
    # TODO: assert ValueError on zero/negative quantities for add/remove

def test_transition_policy_enforced():
    s = Shipment("S3")
    # TODO: follow allowed path then attempt an illegal transition and assert StateError

def test_no_item_changes_after_terminal_states():
    s = Shipment("S4")
    # TODO: drive to DELIVERED then assert add/remove raises (ValueError or a domain error)

def test_events_are_recorded_somehow():
    # Optional: if you expose events, check one event is created on add/remove/state change.
    pass
