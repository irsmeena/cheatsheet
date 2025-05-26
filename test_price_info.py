import price_info as priceInfo


def test_total_cost_shopping():
    expected_result = 46.75
    result = priceInfo.total_cost_shopping()
    assert expected_result == result

def test_cost_of_fruit():
    expected_result = 13
    result = priceInfo.cost_of_fruits('watermelon', 2)

    assert expected_result == result   