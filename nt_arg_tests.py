from collections import namedtuple

T = namedtuple('T', ('a', 'b', 'c', 'd', 'e', 'f'))

print( T(10, 20, 30, 40, 50, 60) )
print( T(10, 20, 30, f=60, e=50, d=40) )
print( T(f=60, e=50, d=40, c=30, b=20, a=10) )

try:
    T(10, 20, 30, 40, 50, 60, 70, 80)
except TypeError as e:
    assert 'were given' in e.args[0].lower()

try:
    T(10, 20, 30, 40)
except TypeError as e:
    assert 'missing' in e.args[0].lower()

try:
    T(10, 20, 30, 40, 50, 60, h=70)
except TypeError as e:
    assert "unexpected keyword argument: 'h'" in e.args[0].lower()

try:
    T(10, 20, 30, 40, 50, 60, h=70, i=80)
except TypeError as e:
    assert "unexpected keyword arguments: 'h' and 'i'" in e.args[0].lower()

try:
    T(10, 20, 30, 40, 50, 60, c=70)
except TypeError as e:
    assert "unexpected keyword argument: 'c'" in e.args[0].lower()

print('Done!')
