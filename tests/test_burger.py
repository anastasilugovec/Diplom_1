import pytest
from models import Burger

def test_get_price_without_ingredients_and_bun(burger, mock_bun):
    burger.set_buns(mock_bun)
    expected_price = mock_bun.get_price.return_value * 2
    assert burger.get_price() == expected_price

def test_get_price_with_single_ingredient(burger, mock_bun, mock_ingredient):
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    expected_price = mock_bun.get_price.return_value * 2 + mock_ingredient.get_price.return_value
    assert burger.get_price() == expected_price

def test_add_ingredient_increases_ingredients_list(burger, mock_ingredient):
    # Проверяем добавление ингредиента
    initial_count = len(burger.get_ingredients())
    burger.add_ingredient(mock_ingredient)
    assert mock_ingredient in burger.get_ingredients()
    assert len(burger.get_ingredients()) == initial_count + 1

def test_get_ingredients_returns_list(burger, mock_ingredient):
    burger.add_ingredient(mock_ingredient)
    ingredients = burger.get_ingredients()
    assert isinstance(ingredients, list)
    assert mock_ingredient in ingredients

def test_move_ingredient_valid_indices(burger, mock_ingredient):
    burger.add_ingredient(mock_ingredient)
    burger.add_ingredient(another_mock_ingredient)
    burger.move_ingredient(0, 1)
    assert burger.get_ingredients()[1] == mock_ingredient

def test_remove_ingredient_valid_index(burger, mock_ingredient):
    burger.add_ingredient(mock_ingredient)
    burger.remove_ingredient(1)
    assert mock_ingredient not in burger.get_ingredients()

def test_remove_ingredient_invalid_index_with_assert(burger):
    try:
        burger.remove_ingredient(999)
        assert False, "Expected IndexError was not raised"
    except IndexError:
        pass

def test_clear_ingredients(burger, mock_ingredient):
    print(type(burger))
    burger.add_ingredient(mock_ingredient)
    print(burger.ingredients)
    burger.clear_ingredients()
    print(burger.ingredients)
    assert burger.ingredients == []

def test_get_receipt_includes_bun_and_ingredients(burger, mock_bun, mock_ingredient):
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    receipt = burger.get_receipt()
    assert f"(==== {mock_bun.get_name()} ====)" in receipt
    ingredient_type = str(mock_ingredient.get_type()).lower()
    ingredient_name = mock_ingredient.get_name()
    assert f"= {ingredient_type} {ingredient_name}" in receipt
    assert f"Price: {burger.get_price()}" in receipt