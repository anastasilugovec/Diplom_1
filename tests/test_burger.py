def test_price_without_ingredients(burger, mock_bun):
    burger.set_buns(mock_bun)
    assert burger.get_price() == mock_bun.get_price.return_value * 2

def test_set_bun_and_add_ingredients_and_price(burger, mock_bun, mock_ingredient):
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    expected_price = mock_bun.get_price.return_value * 2 + mock_ingredient.get_price.return_value
    assert burger.get_price() == expected_price

def test_move_and_remove_ingredients_order(burger, mock_ingredient):
    burger.add_ingredient(mock_ingredient)
    burger.move_ingredient(0, 0)  # пример перемещения, если есть такая логика
    burger.remove_ingredient(0)
    assert burger.ingredients == []

def test_receipt_format_includes_bun_and_ingredients(burger, mock_bun, mock_ingredient):
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    receipt = burger.get_receipt()
    assert f"(==== {mock_bun.get_name()} ====)" in receipt
    assert f"= {str(mock_ingredient.get_type()).lower()} {mock_ingredient.get_name()}" in receipt
    assert f"Price: {burger.get_price()}" in receipt