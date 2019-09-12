import main


def test_hello_world():
    actual = main.hello_world()
    expected = "Hello, World!"
    assert actual == expected
