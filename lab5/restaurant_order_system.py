"""Restaurant dining order billing and kitchen ticket module."""

import hashlib
import secrets
from pathlib import Path

orders = {
    "T1": {"guest": "Liam", "items": 3, "bill": 45.0, "is_settled": False},
    "T2": {"guest": "Sophia", "items": 1, "bill": 18.0, "is_settled": True},
    "T3": {"guest": "Mason", "items": 4, "bill": 72.0, "is_settled": False},
}


def place_table_order(table_id, guest, items_count, order_log=None):
    """Create a new restaurant order."""
    if order_log is None:
        order_log = []

    if table_id in orders or items_count <= 0:
        return False

    orders[table_id] = {
        "guest": guest,
        "items": items_count,
        "bill": 15.0 * items_count,
        "is_settled": False,
    }
    order_log.append(f"Created order for {table_id} with {items_count} dishes")
    return True


def void_table_order(table_id):
    """Remove an existing restaurant order."""
    orders.pop(table_id, None)


def check_table_status(table_id):
    """Check whether a table has an unsettled order."""
    order = orders.get(table_id)
    return order is not None and not order["is_settled"]


def calculate_discounted_bill(table_id, discount_rate):
    """Calculate a discounted bill using a validated discount rate."""
    if table_id not in orders:
        raise ValueError("Table order does not exist")

    if not 0 <= discount_rate <= 1:
        raise ValueError("Discount rate must be between 0 and 1")

    return orders[table_id]["bill"] * (1 - discount_rate)


def generate_ticket_hash(table_id):
    """Generate a SHA-256 ticket identifier."""
    return hashlib.sha256(table_id.encode("utf-8")).hexdigest()


def generate_pos_pin():
    """Generate a cryptographically secure POS PIN."""
    return secrets.randbelow(9000) + 1000


def export_kitchen_orders(filename="kitchen_orders.txt"):
    """Export active orders to a kitchen ticket file."""
    output_path = Path(filename)
    with output_path.open("w", encoding="utf-8") as file:
        file.write(str(orders))

    print(f"Ticket sent to kitchen printer: {output_path}")


def get_pending_summary(order_data):
    """Count orders that have not been settled."""
    return sum(
        1 for details in order_data.values()
        if not details["is_settled"]
    )


def main():
    """Execute sample restaurant billing operations."""
    place_table_order("T4", "Olivia", 2)
    void_table_order("T2")

    print("Is T1 pending:", check_table_status("T1"))
    print("Discounted Bill:", calculate_discounted_bill("T1", 0.10))
    print("Ticket Hash:", generate_ticket_hash("T1"))
    print("POS PIN:", generate_pos_pin())

    export_kitchen_orders()
    print("Pending tables:", get_pending_summary(orders))


if __name__ == "__main__":
    main()
