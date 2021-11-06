import functools


@functools.total_ordering
class C:
    def __init__(self, x: int) -> None:
        self.x = x

    def __repr__(self) -> str:
        return f'{type(self).__name__}({self.x!r})'

    def __lt__(self, other: object) -> bool:
        print(f'__lt__ ran: {self} < {other}')
        if not isinstance(other, C):
            return NotImplemented
        else:
            return self.x < other.x

    def __eq__(self, other: object) -> bool:
        print(f'__eq__ ran: {self} == {other}')
        if not isinstance(other, C):
            return NotImplemented
        else:
            return self.x == other.x
            # return not (self < other) and not (other < self)
