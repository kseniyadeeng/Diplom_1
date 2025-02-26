import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger

@pytest.fixture
def burger():
    return Burger()
@pytest.fixture
def mock_bun(mocker):
    return mocker.Mock(spec=Bun)
@pytest.fixture
def mock_ingredient(mocker):
    return mocker.Mock(spec=Ingredient)