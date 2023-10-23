from src.python_calculator import add_function


def test_add_function():

    param1 = 10
    param2 = 20

    actual = add_function(param1, param2)
    print(actual)
    expected = 30

    assert actual == expected
