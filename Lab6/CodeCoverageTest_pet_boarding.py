import pytest
from pet_boarding import boarding_fee, admission_ok, checkout_status


def test_boarding_fee_included():
    assert boarding_fee("cat", 2, False) == 0
    assert boarding_fee("dog", 2, True) == 0
    assert boarding_fee("rabbit", 4, True) == 0


def test_boarding_fee_extra():
    assert boarding_fee("cat", 5, False) == 40
    assert boarding_fee("dog", 4, False) == 60
    assert boarding_fee("rabbit", 6, False) == 40


def test_boarding_fee_premium():
    assert boarding_fee("cat", 5, True) == 20
    assert boarding_fee("dog", 4, True) == 30


def test_boarding_fee_invalid():
    with pytest.raises(ValueError):
        boarding_fee("bird", 2, False)
    with pytest.raises(ValueError):
        boarding_fee("cat", -1, False)


def test_boarding_fee_high_extra_days():
    assert boarding_fee("cat", 14, False) == 330
    assert boarding_fee("dog", 13, False) == 495


def test_admission():
    assert admission_ok(4, 2, False) is True
    assert admission_ok(4, 1, False) is False
    assert admission_ok(0, 3, False) is False
    assert admission_ok(12, 3, True) is True
    assert admission_ok(12, 2, True) is False


def test_checkout():
    assert checkout_status(20, False, False) == "open"
    assert checkout_status(10, False, False) == "late"
    assert checkout_status(0, False, False) == "late"
    assert checkout_status(30, True, False) == "open"
    assert checkout_status(20, True, False) == "late"
    assert checkout_status(14, True, False) == "closed"
    assert checkout_status(40, False, True) == "open"
    assert checkout_status(20, False, True) == "late"
    assert checkout_status(10, False, True) == "closed"
