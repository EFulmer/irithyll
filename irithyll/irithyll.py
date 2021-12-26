import typing
from dataclasses import dataclass


# primitives
@dataclass
class Value:
    pass


@dataclass
class T(Value):  # True, obviously
    pass


@dataclass
class F(Value):  # False
    pass


# unary operator
@dataclass
class Not:
    p: Value

    def evaluate(self):
        if type(self.p) == T:
            return F()
        elif type(self.p) == F:
            return T()
        else:
            raise ValueError(f"Expected p to be a T or F val, got a {type(p)}")


# binary operators
@dataclass
class And:
    p: Value
    q: Value

    # TODO could cache the results of evaluate, override __eq__, ...
    def evaluate(self):
        if type(self.p) == T and type(self.q) == T:
            return T()
        else:
            return F()
