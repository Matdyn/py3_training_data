import collections
import datetime

ImmutableThingTuple = collections.namedtuple('ImmutableThingTuple', 'a b c d')


class MutableThing:
    def __init__(self, a, b, c, d):
        self.axxxxxxx = a
        self.bxxxxxxx = b
        self.cxxxxxxx = c
        self.dxxxxxxx = d


m1 = MutableThing(1, 2, 3, 4)
m2 = MutableThing(1, 5, 3, 4)

print(m1.__dict__)
print(m2.__dict__)



class ImmutableThing:
    __slots__ = ['a', 'b', 'c', 'd']

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

i = ImmutableThing(1, 2, 3, 4)
print(i.__dict__)
