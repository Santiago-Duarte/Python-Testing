def calculate_total(products, discount):
    total = 0
    for product in products:
        total += product['price']
    return total - (total * discount)


def test_calculate_total_when_products_list_is_empty_should_return_zero():
    assert calculate_total([], 0.5) == 0


def test_calculate_total_when_single_product_is_provided_should_apply_discount():
    products = [
        {
            "name": "Notebook", "price": 5
        }
    ]
    assert calculate_total(products, 0.5) == 2.5


def test_calculate_total_when_multiple_products_are_provided_should_apply_discount():
    products = [
        {
            "name": "Notebook", "price": 5
        },
        {
            "name": "Pen", "price": 2
        }
    ]
    assert calculate_total(products, 0.5) == 3.5


if __name__ == "__main__":
    test_calculate_total_when_products_list_is_empty_should_return_zero()
    test_calculate_total_when_single_product_is_provided_should_apply_discount()
    test_calculate_total_when_multiple_products_are_provided_should_apply_discount()
