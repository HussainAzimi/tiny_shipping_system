from supply_chain.shipment import Shipment
from supply_chain.warehouse import Warehouse
from supply_chain.enums import ShipmentState

def test_add_get_len_contains_iter():
    wh = Warehouse()
    s1 = Shipment("S1")
    s2 = Shipment("S2")
    # TODO: add shipments and assert len, membership, get, and iteration order

def test_count_by_state_and_totals():
    wh = Warehouse()
    # TODO: create shipments in different states and assert counts
    # TODO: add items across shipments and assert total_units_by_sku

def test_to_rows_shape():
    wh = Warehouse()
    # TODO: ensure to_rows returns list of dicts with expected keys/types
