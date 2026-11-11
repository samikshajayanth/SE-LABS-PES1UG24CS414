import math


def parse_booking(text):
    if not isinstance(text, str):
        raise TypeError("Booking input must be a string")
    if text.count(":") != 1:
        raise ValueError("Expected format: pet:days")

    pet, days = text.split(":")
    pet = pet.strip()
    if not pet:
        raise ValueError("Pet name cannot be empty")

    try:
        days = float(days.strip())
    except ValueError:
        raise ValueError("Days must be a valid number")

    if not math.isfinite(days) or days < 0:
        raise ValueError("Days must be finite and non-negative")

    return pet.title(), days


def stay_average(days_csv):
    if not isinstance(days_csv, str):
        raise TypeError("Stay input must be a string")
    if not days_csv.strip():
        raise ValueError("Stay list cannot be empty")

    try:
        values = [int(r.strip()) for r in days_csv.split(",")]
    except ValueError:
        raise ValueError("All stay values must be integers")

    if any(value < 0 for value in values):
        raise ValueError("Stay values cannot be negative")

    return sum(values) // len(values)


def payable_fee(text):
    if not isinstance(text, str):
        raise TypeError("Fee input must be a string")
    if text.count("|") != 1:
        raise ValueError("Expected format: fee|discount")

    fee_text, discount_text = text.split("|")
    try:
        fee = float(fee_text.strip())
        discount = float(discount_text.strip())
    except ValueError:
        raise ValueError("Fee and discount must be valid numbers")

    if not math.isfinite(fee) or not math.isfinite(discount):
        raise ValueError("Fee and discount must be finite")
    if fee < 0 or discount < 0:
        raise ValueError("Fee and discount cannot be negative")

    total = fee * 1.18 - discount
    return max(total, 0)


def main():
    print("==== Running parse_booking ====")
    try:
        user_input = input("Enter pet:days (e.g. dog:5): ")
        print("Pet and Days:", parse_booking(user_input))
    except (ValueError, TypeError) as error:
        print("Invalid booking:", error)

    print("\n==== Running stay_average ====")
    try:
        user_input = input("Enter stay lengths in days as CSV (e.g. 2,5,7): ")
        print("Average Stay:", stay_average(user_input))
    except (ValueError, TypeError) as error:
        print("Invalid stay data:", error)

    print("\n==== Running payable_fee ====")
    try:
        user_input = input("Enter fee|discount (e.g. 1500|100): ")
        print("Payable Fee:", payable_fee(user_input))
    except (ValueError, TypeError) as error:
        print("Invalid fee:", error)


if __name__ == "__main__":
    main()
