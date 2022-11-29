import pytest

from application.main import get_random_cards, load_data, print_random_cards

def test_load_data():
    data = load_data()
    assert data is not None
#Create a test function who test get_random_cards() works and return 10 random cards

def test_get_random_cards():
    random_cards = get_random_cards()
    assert random_cards is not None
    assert len(random_cards) == 10

#Create a tests function who test print_random_cards() works

def test_print_random_cards():
    message = print_random_cards()
    assert message is not None
    assert message != ""