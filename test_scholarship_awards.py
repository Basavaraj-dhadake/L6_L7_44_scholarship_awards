from hypothesis import given, strategies as st

from scholarship_awards import (
    parse_applicant,
    marks_average,
    payable_award
)


# Test parse_applicant
@given(st.one_of(st.text(), st.none()))
def test_parse_applicant_no_crash(s):
    result = parse_applicant(s)

    assert result is None or (
        isinstance(result, tuple) and len(result) == 2
    )


# Test marks_average
@given(st.one_of(st.text(), st.none()))
def test_marks_average_no_crash(s):
    result = marks_average(s)

    assert result is None or isinstance(result, int)


# Test payable_award
@given(st.one_of(st.text(), st.none()))
def test_payable_award_no_crash(s):
    result = payable_award(s)

    assert result is None or result >= 0


# Additional valid input tests

@given(
    st.text(
        alphabet=st.characters(
            whitelist_categories=('L',)
        ),
        min_size=1
    ),
    st.floats(
        min_value=0,
        max_value=100,
        allow_nan=False,
        allow_infinity=False
    )
)
def test_parse_applicant_valid(category, marks):
    result = parse_applicant(f"{category}:{marks}")

    assert result is not None
    assert result[0] == category.strip().title()
    assert result[1] == marks


@given(
    st.lists(
        st.integers(min_value=0, max_value=100),
        min_size=1
    )
)
def test_marks_average_valid(values):
    csv = ','.join(map(str, values))

    result = marks_average(csv)

    assert result == sum(values) // len(values)


@given(
    st.floats(
        min_value=0,
        max_value=100000,
        allow_nan=False,
        allow_infinity=False
    ),
    st.floats(
        min_value=0,
        max_value=100000,
        allow_nan=False,
        allow_infinity=False
    )
)
def test_payable_award_valid(award, deduction):
    text = f"{award}|{deduction}"

    result = payable_award(text)

    expected = max(award * 1.18 - deduction, 0)

    assert abs(result - expected) < 0.000001