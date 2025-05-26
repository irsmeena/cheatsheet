import Lab2 as lab2


def test_calc_average_temperature():
    inp_list = [10, 12.5, 20.3, 15.8, 18.2]

    result= lab2.calc_average_temperature(inp_list)

    assert (result == 15.36)

def test_calc_min_max_temperature():
    inp_list = [10, 12.5, 20.3, 15.8, 18.2]

    result= lab2.calc_min_max_temperature(inp_list)

    assert (result == [10, 20.3])


def test_sort_temperature_list():
    inp_list = [10, 12.5, 20.3, 15.8, 18.2]

    result= lab2.sort_temperature_list(inp_list)

    assert (result == [10, 12.5, 15.8, 18.2, 20.3])

def test_calc_median_temperature_odd():
    inp_list = [10, 12.5, 20.3, 15.8, 18.2]

    result= lab2.calc_median_temperature(inp_list)

    assert (result == 15.8) 

def test_calc_median_temperature_even():
    inp_list = [10, 12.5, 20.3, 15.8]

    result= lab2.calc_median_temperature(inp_list)

    assert (result == 14.15)    