from typing import Literal, overload
import pytest


class Superclass:
    @property
    def name(self) -> str:
        return 'xyz'

class Subclass(Superclass):
    @property
    def name(self) -> int:
        return 123


def test_approx():
    assert 0 == pytest.approx(0)


class Someclass:
    @overload
    def method(self, arg1: Literal['html']) -> None: ...
    @overload
    def method(self, arg1: Literal['xml']) -> None: ...
    @overload
    def method(self, arg1: Literal['text']) -> None: ...
    @overload
    def method(self, arg1: str) -> None: ...
    def method(self, arg1):
        pass

a = Someclass()
a.method(123)
