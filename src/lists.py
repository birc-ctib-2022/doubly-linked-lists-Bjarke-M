"""Doubly-linked lists."""

from __future__ import annotations
from typing import (
    Generic, TypeVar, Iterable,
    Callable, Protocol
)


class Comparable(Protocol):
    """Type info for specifying that objects can be compared with <."""

    def __lt__(self, other: Comparable) -> bool:
        """Less than, <, operator."""
        ...


T = TypeVar('T')
S = TypeVar('S', bound=Comparable)


class Link(Generic[T]):
    """Doubly linked link."""

    val: T
    prev: Link[T]
    next: Link[T]

    def __init__(self, val: T, p: Link[T], n: Link[T]):
        """Create a new link and link up prev and next."""
        self.val = val
        self.prev = p
        self.next = n


def insert_after(link: Link[T], val: T) -> None:
    """Add a new link containing avl after link."""
    new_link = Link(val, link, link.next)
    new_link.prev.next = new_link
    new_link.next.prev = new_link


def remove_link(link: Link[T]) -> None:
    """Remove link from the list."""
    link.prev.next = link.next
    link.next.prev = link.prev


class DLList(Generic[T]):
    """
    Wrapper around a doubly-linked list.

    This is a circular doubly-linked list where we have a
    dummy link that function as both the beginning and end
    of the list. By having it, we remove multiple special
    cases when we manipulate the list.

    >>> x = DLList([1, 2, 3, 4])
    >>> print(x)
    [1, 2, 3, 4]
    """

    head: Link[T]  # Dummy head link

    def __init__(self, seq: Iterable[T] = ()):
        """Create a new circular list from a sequence."""
        # Configure the head link.
        # We are violating the type invariants this one place,
        # but only here, so we ask the checker to just ignore it.
        # Once the head element is configured we promise not to do
        # it again.
        self.head = Link(None, None, None)  # type: ignore
        self.head.prev = self.head
        self.head.next = self.head

        # Add elements to the list, exploiting that self.head.prev
        # is the last element in the list, so appending means inserting
        # after that link.
        for val in seq:
            insert_after(self.head.prev, val)

    def __str__(self) -> str:
        """Get string with the elements going in the next direction."""
        elms: list[str] = []
        link = self.head.next
        while link and link is not self.head:
            elms.append(str(link.val))
            link = link.next
        return f"[{', '.join(elms)}]"
    __repr__ = __str__  # because why not?

    def __iter__(self) -> Iterable[T]:     #iterator 
        link = self.head.next
        while link != self.head:
            yield link.val
            link = link.next 

    def __eq__(self, other: DLList):
        x, y = self.head.next, other.head.next
        while x != self.head and y != other.head:
            if x.val != y.val:
                return False
            x, y = x.next, y.next
        return x == self.head and y == other.head 




# Exercises

def keep(x: DLList[T], p: Callable[[T], bool]) -> None:
    """
    Remove all elements from x that do not satisfy the predicate p.

    >>> x = DLList([1, 2, 3, 4, 5])
    >>> keep(x, lambda a: a % 2 == 0)
    >>> print(x)
    [2, 4]
    """
    link = x.head.next
    while link is not x.head:
        if not p(link.val):
            remove_link(link)
        link = link.next




def reverse(x: DLList[T]) -> None:
    """
    Reverse the list x.

    >>> x = DLList([1, 2, 3, 4, 5])
    >>> reverse(x)
    >>> print(x)
    [5, 4, 3, 2, 1]
    """
    link = x.head.next
    end = x.head.prev
    while link is not end:
            insert_after(end,link.val)   #not the most efficient
            remove_link(link)            # as we add one and delete one 
            link = link.next             # but for now it works   

# def reverse(x: DLList[T]) -> None:
#     link = x.head
#     while link != x.head:
#         link.prev, link.next = link.next, link.prev
#         link = link.prev  # that was link.next a moment before
#         if link is x.head: return

def swap(x,link,next) -> None:
    insert_after(link,next.val)
    insert_after(next,link.val)   
    remove_link(link)
    remove_link(next)
    link= link.next    

def is_sorted(x : DLList[S]) -> bool:
    link = x.head.next
    while link.next is not x.head:
        if link.val < link.next.val:
            link = link.next
        else:
            return False
    return True



def sort(x: DLList[S]) -> None:
    """
    Sort the list x.

    >>> x = DLList([1, 3, 12, 6, 4, 5])
    >>> sort(x)
    >>> print(x)
    [1, 3, 4, 5, 6, 12]
    """
    link = x.head.next
    while is_sorted(x)==False:
        if link.next.val is not None:
            if link.val > link.next.val:
                swap(x,link,link.next)                #complexity bad
            link = link.next                        #happiness medium
        else:
            link = link.next.next
    ...


#trying a merge sort, and it's not working yet but hey at some point it might 
# def merge(self,x:DLList[T],y:DLList[T]):
#     if x==None: return y
#     if y==None: return x
#     linkx = x.head.next
#     linky = y.head.next
#     if linkx.val < linky.val:
#         linkx = self.merge(linkx.next,y)
#         linkx.next.prev=x; 
#         linkx.prev=None
#         return x
#     else:
#         linky = self.merge(linky.next,x)
#         linky.next.prev = y
#         linky.prev = None
#         return y

# def mergesort(self,link): 
#     link = self.head.next
#     if (link==self.head): 
#         return self.head; 
#     half = self.div(link); 
#     link = self.mergesort(link)
#     half = self.mergesort(half)
#     return self.merge(link,half)

# # def div(self,link): 
# #     first=last=link; 
# #     while(True): 
# #         if (first.next==None): 
# #             break
# #         if ((first.next).next==None): 
# #             break
# #         first=(first.next).next
# #         last=last.next
# #     t=last.next
# #     last.next=None
# #     return t



def wrap(f):
    def wrapped(x: DLList, *args):
        copy = DLList(iter(x))
        f(copy, *args)
        return copy
    return wrapped

# def _keep(x: DLList[T], p: Callable[[T], bool]) -> DLList[T]:
#     y = DLList(iter(x))
#     keep(y, p)
#     return y

def _swap(x ,i, j) -> DLList[T]:
    y = DLList(iter(x))
    swap(y,i,j)
    return y