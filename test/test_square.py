from tetra import square


def test_square():
    assert square.Square.from_name("a1").index == square.A1


def test_square_eq():
    assert square.Square.from_name("a1") == square.Square.from_name("a1")
