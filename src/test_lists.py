"""List tests."""
from lists import DLList
from lists import insert_after
from lists import remove_link
from lists import keep
from lists import reverse
from lists import swap
from lists import is_sorted
from lists import sort


x = DLList([1, 3, 12, 13, 4, 5])
y = DLList([10, 9, 8, 7, 6, 5])
z = DLList([1, 2, 3, 4, 5, 6])
w = DLList([1, 3, 12, 6, 4, 5])


def test_keep() -> None:
    assert keep(x,lambda a: a%2==0) == DLList([4])
    assert keep(y,lambda a: a%2==0) == DLList([8, 6])
    assert keep(z,lambda a: a%2==0) == DLList([2, 4, 6])
    assert keep(w,lambda a: a%2==0) == DLList([12, 6, 4])

def test_reverse() -> None:
    assert reverse(x) == DLList([5, 4, 13, 12, 3, 1])
    assert reverse(y) == DLList([5, 6, 7, 8, 9, 10])
    assert reverse(z) == DLList([6, 5, 4, 3, 2, 1])
    assert reverse(w) == DLList([5, 4, 13, 12, 3, 1])

def test_swap() -> None:
    assert swap(x.head.next,x.head.next.next) == DLList([3, 1, 12, 13, 4, 5])
    assert swap(y.head.next.next,y.head.next.next.next) == DLList([10, 9, 7, 8, 6, 5])

def test_is_sorted() -> None:
    assert is_sorted(x)==False
    assert is_sorted(y)==False
    assert is_sorted(z)==True
    assert is_sorted(w)==False


def test_sort() -> None:
    assert is_sorted(sort(x))==True
    assert is_sorted(sort(y))==True
    assert is_sorted(sort(z))==True
    assert is_sorted(sort(w))==True