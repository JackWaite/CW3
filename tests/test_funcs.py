from utils import funcs
import requests
import pytest


@pytest.fixture
def words():
    response = requests.get("https://api.npoint.io/094d3a7a0d9569218a14")
    words = response.json()
    return words


def test_get_data(words):
    assert type(funcs.get_data(words)) == type(words)
    assert funcs.get_data(words) is not None


def test_executed_operations(words):
    assert isinstance(funcs.executed_operations(words), list)
    assert funcs.executed_operations(words) is not None


def test_sorted_data(words):
    executed_operations = funcs.executed_operations(words)
    assert isinstance(funcs.sorted_data(executed_operations), list)
    assert funcs.sorted_data(executed_operations) != executed_operations


def test_last_operations():
    sorted = funcs.last_operations()
    assert len(sorted[:5]) == 5
    assert isinstance(sorted[:5], list)


def test_hiding_card():
    last_five_operations = funcs.last_operations()[:5]
    assert isinstance(funcs.hiding_card(last_five_operations), list)
    for k in last_five_operations:
        assert isinstance(k, dict)


def test_date_new():
    last_five_operations = funcs.last_operations()[:5]
    assert isinstance(funcs.date_new(last_five_operations), list)


def test_result_output():
    last_five_operations = funcs.last_operations()[:5]
    assert funcs.result_output(last_five_operations, None) is True