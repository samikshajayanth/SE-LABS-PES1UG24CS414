import pytest
from hypothesis import given, strategies as st
from pet_boarding import parse_booking, stay_average, payable_fee


@given(st.sampled_from(["", " ", "   "]), st.integers(min_value=0, max_value=100))
def test_parse_booking_rejects_empty_pet(pet, days):
    with pytest.raises(ValueError):
        parse_booking(f"{pet}:{days}")


@given(st.integers(min_value=-100, max_value=-1))
def test_parse_booking_rejects_negative_days(days):
    with pytest.raises(ValueError):
        parse_booking(f"dog:{days}")


@given(st.sampled_from(["", " ", ",", " , "]))
def test_stay_average_rejects_empty_input(value):
    with pytest.raises(ValueError):
        stay_average(value)


@given(st.integers(min_value=-100, max_value=-1))
def test_stay_average_rejects_negative_days(days):
    with pytest.raises(ValueError):
        stay_average(str(days))


@given(st.integers(min_value=-1000, max_value=-1))
def test_payable_fee_rejects_negative_fee(fee):
    with pytest.raises(ValueError):
        payable_fee(f"{fee}|100")


@given(st.integers(min_value=-1000, max_value=-1))
def test_payable_fee_rejects_negative_discount(discount):
    with pytest.raises(ValueError):
        payable_fee(f"1000|{discount}")
