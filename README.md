import pytest
from scholarship_awards import award_amount, is_eligible, application_status

# Example test cases:
def test_below_cutoff_marks():
    assert award_amount("merit", 70, "low", False) == 0

def test_is_eligible():
    assert is_eligible(90, 0, False) is True

# Write the rest of the test cases so that the code is 90-100% covered.
# Additional test cases for Code Coverage

# Award amount tests

def test_unknown_category():
    with pytest.raises(ValueError):
        award_amount("science", 90, "low", False)


def test_invalid_marks():
    with pytest.raises(ValueError):
        award_amount("merit", -5, "low", False)


def test_merit_award():
    assert award_amount("merit", 80, "low", False) == 500


def test_sports_award():
    assert award_amount("sports", 70, "low", False) == 1000


def test_arts_award():
    assert award_amount("arts", 75, "high", False) == 600


def test_merit_renewal():
    assert award_amount("merit", 72, "low", True) == 200


def test_sports_renewal():
    assert award_amount("sports", 65, "low", True) == 500


def test_high_income():
    assert award_amount("merit", 80, "high", False) == 300


def test_large_low_income_award():
    assert award_amount("merit", 95, "low", False) == 3200


def test_large_high_income_award():
    assert award_amount("merit", 95, "high", False) == 2000


def test_marks_equal_cutoff():
    assert award_amount("merit", 75, "low", False) == 0


# Eligibility tests

def test_special_quota_eligible():
    assert is_eligible(60, 2, True) is True


def test_special_quota_not_eligible():
    assert is_eligible(60, 3, True) is False


def test_low_attendance():
    assert is_eligible(70, 0, False) is False


def test_good_attendance():
    assert is_eligible(80, 0, False) is True


def test_backlogs_not_eligible():
    assert is_eligible(90, 2, False) is False


def test_one_backlog():
    assert is_eligible(90, 1, False) is True


# Application status tests

def test_application_open():
    assert application_status(40, False, False) == "open"


def test_application_closing():
    assert application_status(10, False, False) == "closing"


def test_application_closed():
    assert application_status(4, False, False) == "closed"


def test_renewal_application():
    assert application_status(35, True, False) == "open"


def test_paper_application():
    assert application_status(35, False, True) == "open"


def test_renewal_paper_application():
    assert application_status(45, True, True) == "open"


def test_renewal_closing():
    assert application_status(20, True, False) == "closing"


def test_paper_closing():
    assert application_status(20, False, True) == "closing"
