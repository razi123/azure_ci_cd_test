from src.python_calculator import mult_function


def test_mult_function():

    param1 = 10
    param2 = 20

    actual = mult_function(param1, param2)
    print(actual)
    expected = 200

    assert actual == expected
