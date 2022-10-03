import pytest
from hw_1209 import str_procent
tests = [('ААа АаА', 100), ('I waS BusY lol', 25), ('Hello mY DEAr FriEND', 50),
         ('I Am SORRY', 66.67), ('i Am fiNe todAy', 0), ('I WiLL BE AT SeVEN', 100)]


@pytest.mark.parametrize('test_inp, result', tests)
def test_str_procent(test_inp, result):
    assert str_procent(test_inp) == result
