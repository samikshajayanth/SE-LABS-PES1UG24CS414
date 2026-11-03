import pytest
from pet_boarding import boarding_fee, admission_ok, checkout_status


@pytest.mark.parametrize("pet,days,premium,expected", [
    ("cat", 2, False, 0),
    ("cat", 4, False, 20),
    ("cat", 4, True, 0),
    ("dog", 1, False, 0),
    ("dog", 3, False, 30),
    ("dog", 4, True, 30),
    ("dog", 12, False, 300),
    ("dog", 13, False, 495),
    ("rabbit", 3, False, 0),
    ("rabbit", 5, False, 20),
    ("rabbit", 4, True, 0),
])
def test_boarding_fee(pet, days, premium, expected):
    assert boarding_fee(pet, days, premium) == expected


@pytest.mark.parametrize("pet,days", [
    ("bird", 2),
    ("cat", -1),
])
def test_boarding_fee_errors(pet, days):
    with pytest.raises(ValueError):
        boarding_fee(pet, days, False)


@pytest.mark.parametrize("age,vaccines,senior,expected", [
    (0, 2, False, False),
    (1, 2, False, True),
    (5, 1, False, False),
    (5, 3, False, True),
    (10, 2, True, False),
    (10, 3, True, True),
])
def test_admission(age, vaccines, senior, expected):
    assert admission_ok(age, vaccines, senior) is expected


@pytest.mark.parametrize("minutes,long_stay,weekend,expected", [
    (15, False, False, "open"),
    (14, False, False, "late"),
    (0, False, False, "late"),
    (30, True, False, "open"),
    (20, True, False, "late"),
    (14, True, False, "closed"),
    (35, False, True, "open"),
    (20, False, True, "late"),
    (10, False, True, "closed"),
    (50, True, True, "open"),
    (40, True, True, "late"),
    (34, True, True, "closed"),
])
def test_checkout(minutes, long_stay, weekend, expected):
    assert checkout_status(minutes, long_stay, weekend) == expected
