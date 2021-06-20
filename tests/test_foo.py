import os


def test_foo() -> None:
    assert os.environ["FOO"] == "bar"
