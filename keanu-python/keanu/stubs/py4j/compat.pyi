# Stubs for py4j.compat (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from threading import Thread
from typing import Any

version_info: Any

def items(d: Any): ...
def iteritems(d: Any): ...
def next(x: Any): ...
tobytestr = str

def isbytestr(s: Any): ...
def ispython3bytestr(s: Any): ...
def isbytearray(s: Any): ...
def bytetoint(b: Any): ...
def bytetostr(b: Any): ...
def strtobyte(b: Any): ...

Empty: Any
next = next
long = int
basestring = str
unicode = str
bytearray2 = bytes
unichr = chr
bytestr = bytes

def hasattr2(o: Any, name: str) -> bool: ...
hasattr2 = hasattr

class CompatThread(Thread):
    daemon: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
