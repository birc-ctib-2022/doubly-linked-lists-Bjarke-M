"""List tests."""
from lists import DLList
from lists import insert_after
from lists import remove_link
from lists import keep
from lists import reverse
from lists import swap
from lists import is_sorted
from lists import sort
from lists import  wrap
from lists import _swap


x = DLList([1, 3, 12, 13, 4, 5])
y = DLList([10, 9, 8, 7, 6, 5])
z = DLList([1, 2, 3, 4, 5, 6])
w = DLList([1, 3, 12, 6, 4, 5])

_keep = wrap(keep)
_reverse = wrap(reverse)
_swap = wrap(swap)

def test_keep() -> None:
    assert _keep(x,lambda a: a%2==0) == DLList([12, 4])
    assert _keep(y,lambda a: a%2==0) == DLList([10, 8, 6])
    assert _keep(z,lambda a: a%2==0) == DLList([2, 4, 6])
    assert _keep(w,lambda a: a%2==0) == DLList([12, 6, 4])

def test_reverse() -> None:
    assert _reverse(x) == DLList([5, 4, 13, 12, 3, 1])
    assert _reverse(y) == DLList([5, 6, 7, 8, 9, 10])
    assert _reverse(z) == DLList([6, 5, 4, 3, 2, 1])
    assert _reverse(w) == DLList([5, 4, 6, 12, 3, 1])

def test_swap() -> None:
    assert _swap(x.head.next,x.head.next.next) == DLList([3, 1, 12, 13, 4, 5])
    assert _swap(y.head.next.next,y.head.next.next.next) == DLList([10, 9, 7, 8, 6, 5])

