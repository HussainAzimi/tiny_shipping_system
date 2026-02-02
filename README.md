# Supply Chain Management System

A robust Python package for managing shipment lifecycles, inventory invariants, and warehouse aggregations. This system enforces strict state transitions and provides primitive data exports for external logistics processing.

## Features

* **Shipment Tracking:** Manage items and state transitions from `CREATED` to `DELIVERED`.
* **Domain Safety:** Invariants prevent negative quantities and illegal state moves (e.g., preventing modifications to a cancelled shipment).
* **Warehouse Aggregation:** Real-time summaries of total units by SKU and shipment counts by state.
* **Data Adapters:** Built-in support for exporting warehouse snapshots to JSON and CSV formats.

##  Installation

Required Python 3.10+ installed. Clone this repository and install the test dependencies:

```bash
pip install pytest

```
## Testing

Ensure you have Python 3.10+ installed. Clone this repository and install the test dependencies:

```bash
pip install pytest

```
## Run specific test modules:
```bash
python -m pytest tests/test_shipment.py
python -m pytest tests/test_warehouse.py

```
## Usage Example

from supply_chain import Shipment, Warehouse, to_json

 
wh = Warehouse()
s = Shipment("S123", {"APPLE": 10})


s.add_item("ORANGE", 5)


s.pack()
s.ship()


wh.add(s)
json_report = to_json(wh)
print(json_report)