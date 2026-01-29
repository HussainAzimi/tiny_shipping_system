# HW2 — Supply Chain OOP (Chapter 2)

**Theme:** Implement a small, idiomatic Python package for supply‑chain shipping using Chapter 2 patterns:
- Classes with clear responsibilities and invariants
- Properties for validation/encapsulation
- Type hints + docstrings (+ one doctest)
- Modules/packages with absolute imports and a curated `__init__`
- Simple container object (`Warehouse`) with summaries/exports
- Domain errors + EAFP
- Optional: dataclasses with `slots`/`frozen` where helpful

## Story
You are building a tiny library for a logistics team. A **Shipment** moves through states
(`CREATED → PACKED → IN_TRANSIT → DELIVERED`; `CANCELLED` is terminal). Shipments hold item lines
(`sku → quantity`). A **Warehouse** aggregates many shipments and provides summaries and CSV/JSON exports.

## Learning objectives
1. Translate a design into clean Python classes with invariants.
2. Use properties to guard state (e.g., no negative quantities, no changes after delivery/cancellation).
3. Organize code across modules/packages with absolute imports and `__all__`.
4. Implement a small container with Pythonic protocols (`__len__`, `__iter__`, `__contains__`).
5. Separate domain from I/O via adapters (CSV/JSON exporters).

## Your tasks
Work only in the `supply_chain/` modules. Leave tests as guidance and add/modify them as needed.

### A) States & Events
- Define `ShipmentState` enum and an **allowed transition table**.
- Create immutable `ShipmentEvent` records for: `add`, `remove`, and `state_change`.
- Include UTC timestamps on events.

### B) Shipment (core domain)
- Fields: `shipment_id` (str), current `state`, and item lines (mapping `sku -> qty`).
- Methods (verbs): `add_item`, `remove_item`, `pack`, `ship`, `deliver`, `cancel`.
- Invariants:
  - Quantities are positive integers; totals never go negative.
  - No item changes after `DELIVERED` or `CANCELLED`.
  - State transitions must follow the table; re‑applying current state is a no‑op.
- Properties:
  - `items` → **read‑only** projection of lines
  - `total_units` → computed integer
- Observability: helpful `__repr__` and one doctest in a public method’s docstring.

### C) Domain errors
Create specific exceptions (e.g., `StateError`, `InsufficientQuantityError`) and raise with helpful context.

### D) Warehouse (container)
- Holds shipments indexed by `shipment_id` (O(1) membership).
- API: `add`, `remove`, `get`, `__len__`, `__iter__`, `__contains__`.
- Summaries: `count_by_state()`, `total_units_by_sku()`.
- Export surface: `to_rows()` → list of dictionaries with primitives.

### E) Adapters (edges only)
- Implement `to_csv(warehouse) -> str` and `to_json(warehouse) -> str` using `to_rows()`.
- **No file I/O** inside the domain; the adapter returns strings.

### F) Packaging hygiene
- Use **absolute imports** in tests and app code.
- Curate the public API via `supply_chain/__init__.py` and `__all__`.
- Keep module docstrings + type hints up to date.

## Deliverables
- Working package fulfilling A–F with docstrings and type hints.
- At least **6 pytest specs** covering invariants, transitions, and summaries.
- One doctest in a public API docstring.
- A short `pyproject.toml` (already provided) and clean formatting.

## How to run
```bash
# (optional) create venv first
pip install -r requirements.txt
pytest -q
```

## Rubric (100 pts)
- **Design & Encapsulation (20 pts):** Clear responsibilities; properties guard invariants; read‑only projections.
- **Correctness (35 pts):** Valid transitions; quantity rules; container behavior; adapters return correct text.
- **Docs & Hints (15 pts):** Docstrings (units/rules/examples); one doctest; accurate type hints.
- **Tests (20 pts):** ≥6 meaningful tests (table‑driven where applicable); fast and deterministic.
- **Packaging & Hygiene (10 pts):** Absolute imports, curated `__all__`, no I/O in domain, tidy `pyproject.toml`.

**Bonus (+5):** Use `@dataclass(slots=True, frozen=True)` for `ShipmentEvent` and add a `__repr__` that aids debugging.

## Academic integrity
Write your own implementation. Discuss ideas, but do not share code. Cite external references in comments where relevant.
