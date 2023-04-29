import pytest

from utils import funcs
import requests


@pytest.fixture
def words():
    response = requests.get("https://api.npoint.io/094d3a7a0d9569218a14")
    words_1 = response.json()
    return words_1


def test_get_data(words):
    """Test function get_data"""
    assert type(funcs.get_data()) == type(words)
    assert funcs.get_data() is not None


def test_executed_operations(words):
    """Test function executed_operations"""
    assert isinstance(funcs.executed_operations(), list)
    assert funcs.executed_operations() is not None


def test_sort_data(words):
    """Test function sort_data"""
    executed_operations = funcs.executed_operations()
    assert isinstance(funcs.sort_data(), list)
    assert funcs.sort_data() != executed_operations


def test_last_operations():
    """Test function five last operations"""
    sort_ed = funcs.last_operations()
    assert len(sort_ed[:5]) == 5
    assert isinstance(sort_ed[:5], list)


def test_hiding_card():
    """Test hiding_card"""
    last_five_operations = funcs.last_operations()[:5]
    assert isinstance(funcs.hiding_card(last_five_operations), list)
    for k in last_five_operations:
        assert isinstance(k, dict)


def test_date_new():
    """Test date_new"""
    last_five_operations = funcs.last_operations()[:5]
    assert isinstance(funcs.date_new(last_five_operations), list)


def test_result_output():
    """Test result_output"""
    last_five_operations = funcs.last_operations()
    assert funcs.result_output(last_five_operations) is True
