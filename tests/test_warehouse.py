from supply_chain.shipment import Shipment
from supply_chain.warehouse import Warehouse
from supply_chain.enums import ShipmentState

def test_add_get_len_contains_iter():
    wh = Warehouse()
    s1 = Shipment("S1", {"ITEM1": 1})
    s2 = Shipment("S2", {"ITEMS2": 1})
    
    wh.add(s1)
    wh.add(s2)
    assert len(wh) == 2

    assert "S1" in wh
    assert "S3" not in wh

    assert wh.get("S1") is s1
    assert list(wh) == [s1, s2]


def test_count_by_state_and_totals():
    wh = Warehouse()
    s1 = Shipment("S1", {"A": 10, "B": 5})
    s2 = Shipment("S2", {"A": 5})

    s1.pack
    wh.add(s1)
    wh.add(s2)
    counts = wh.count_by_state()
    assert counts[ShipmentState.PACKED] == 1
    assert counts[ShipmentState.CREATED] == 1

    totals = wh.total_units_by_sku()
    assert totals["A"] == 15
    assert totals["B"] == 5


def test_to_rows_shape():
    wh = Warehouse()
    wh.add(Shipment("S1", {"ITEM": 10}))

    rows = wh.to_rows()
    assert isinstance(rows, list)
    assert len(rows) == 1


    row = rows[0]
    assert row["shipment_id"] == "S1"
    assert isinstance(row["state", str])
    assert row["total_units"] == 10