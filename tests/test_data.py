from hw_3.date import Date
from datetime import date, datetime
from unittest.mock import patch


def creation_test():
    d = Date()
    current_date = datetime.now()
    assert d.day == current_date.day
    assert d.month == current_date.month
    assert d.year == current_date.year

    d1 = Date(1,3,2020)
    assert d1.day == 1
    assert d1.month == 3
    assert d.year == 2020

def test_entering_date():
    with patch('builtins.input', return_value='12.12.1212'):
        d = Date().entering_date()
        assert d.day == 12
        assert d.month == 12
        assert d.year == 1212

def test_validation():
    d = Date()

    data = ['', '1.14.',  '12', '12/15/8', '34.8.1685', '18.34.123', '19.12.-1'] # None
    for i in data:
        assert d.validation(i) == None
    
    valid = d.validation('28.9.1398')
    assert valid.day == 28
    assert valid.month == 9
    assert valid.year == 1398

