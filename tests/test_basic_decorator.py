from dataclasses import dataclass


def register_function(*args, **kwargs) -> int:
    return 987


def test_decorator_simplest():
    from themester.base_decorator import BaseDecorator

    class simplest(BaseDecorator):
        for_ = None
        register_function = register_function

    # Construction
    f: simplest = simplest()
    assert f.register_function() == 987
    assert f.context is None
    assert f.name is None

    # Calling
    # @foo would be here
    @dataclass
    class FullDecorator:
        name: str = 'Decorated Class'

    result = f(FullDecorator)  # noqa
    assert result == FullDecorator
