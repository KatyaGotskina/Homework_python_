"""Tests for data_check."""
import pytest
from right_data import data_check
tests = [
    ('12.2.2023', True), ('29.2.2020', True), ('331.6.2004', False),
    ('29.2.2100', False), ('06.07.2004', True), ('6.9999.256666', False)
]


@pytest.mark.parametrize('test_inp, result', tests)
def test_right_data(test_inp, result):
    """Function for pytest."""
    assert data_check(test_inp) == result
