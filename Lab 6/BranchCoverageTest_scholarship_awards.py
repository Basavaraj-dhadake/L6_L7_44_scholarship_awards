import pytest
from scholarship_awards import (
    award_amount,
    is_eligible,
    application_status
)


# AWARD AMOUNT BRANCH TESTS

def test_unknown_category():
    with pytest.raises(ValueError):
        award_amount("science", 90, "low", False)


def test_negative_marks():
    with pytest.raises(ValueError):
        award_amount("merit", -5, "low", False)


def test_merit_cutoff():
    assert award_amount("merit", 75, "low", False) == 0


def test_merit_above_cutoff():
    assert award_amount("merit", 80, "low", False) == 500


def test_renewal_true():
    assert award_amount("merit", 80, "low", True) == 1000


def test_renewal_false():
    assert award_amount("merit", 80, "low", False) == 500


def test_sports_renewal():
    assert award_amount("sports", 65, "low", True) == 500


def test_low_income():
    assert award_amount("merit", 80, "low", False) > 0


def test_high_income():
    assert award_amount("merit", 80, "high", False) > 0


def test_above_fifteen_low_income():
    assert award_amount("merit", 95, "low", False) == 3200


def test_above_fifteen_high_income():
    assert award_amount("merit", 95, "high", False) == 2000


def test_below_fifteen():
    assert award_amount("merit", 85, "low", False) == 1000


# ELIGIBILITY BRANCH TESTS

def test_special_quota_eligible():
    assert is_eligible(60, 2, True) is True


def test_special_quota_not_eligible():
    assert is_eligible(60, 3, True) is False


def test_normal_eligible():
    assert is_eligible(80, 0, False) is True


def test_low_attendance():
    assert is_eligible(70, 0, False) is False


def test_attendance_equal_75():
    assert is_eligible(75, 0, False) is True


def test_backlogs_equal_one():
    assert is_eligible(80, 1, False) is True


def test_backlogs_above_one():
    assert is_eligible(80, 2, False) is False


# APPLICATION STATUS BRANCH TESTS

def test_renewal_application():
    assert application_status(35, True, False) == "open"


def test_normal_application():
    assert application_status(25, False, False) == "open"


def test_paper_application():
    assert application_status(35, False, True) == "open"


def test_renewal_paper_application():
    assert application_status(45, True, True) == "open"


def test_application_closing():
    assert application_status(10, False, False) == "closing"


def test_renewal_closing():
    assert application_status(20, True, False) == "closing"


def test_paper_closing():
    assert application_status(20, False, True) == "closing"


def test_application_closed():
    assert application_status(4, False, False) == "closed"


def test_renewal_closed():
    assert application_status(10, True, False) == "closed"