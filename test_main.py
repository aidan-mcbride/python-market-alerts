import pytest

import main


def test_compare_to_limit_below():

    """Return `True` if checking if 15.00 is below 20.00"""
    expected = True
    actual = main.compare_to_limit(price=15.00, limit=20.00, side="below")
    assert expected == actual

    """Return `False` if checking if 20.00 is below 15.00"""
    expected = False
    actual = main.compare_to_limit(price=20.00, limit=15.00, side="below")
    assert expected == actual


def test_compare_to_limit_above():

    """Return `True` if checking if 20.00 is above 15.00"""
    expected = True
    actual = main.compare_to_limit(price=20.00, limit=15.00, side="above")
    assert expected == actual

    """Return `False` if checking if 15.00 is above 20.00"""
    expected = False
    actual = main.compare_to_limit(price=15.00, limit=20.00, side="above")
    assert expected == actual


def test_compare_to_limit_invalid_side():
    """Raise an exception if an invalid side is given"""
    expected = "'side' must be 'above' or 'below'"
    with pytest.raises(ValueError) as actual:
        main.compare_to_limit(price=1.00, limit=2.00, side="next to")
    assert str(actual.value) == expected

    with pytest.raises(ValueError) as actual:
        main.compare_to_limit(price=1.00, limit=2.00, side=None)
    assert str(actual.value) == expected
