# Stubs for string

# Based on http://docs.python.org/3.2/library/string.html

from typing import Mapping, Sequence, Any, Optional, Union, List, Tuple, Iterable

ascii_letters = ''
ascii_lowercase = ''
ascii_uppercase = ''
digits = ''
hexdigits = ''
letters = ''
lowercase = ''
octdigits = ''
punctuation = ''
printable = ''
uppercase = ''
whitespace = ''

# TODO(MichalPokorny): This is probably badly and/or loosely typed.
class Formatter(object):
    def format(self, format_string: str, *args, **kwargs) -> str: ...

    def vformat(self, format_string: str, args: Sequence[Any], kwargs: Mapping[str, Any]) -> str: ...

    def parse(self, format_string: str) -> Iterable[Tuple[str, str, str, str]]: ...

    def get_field(self, field_name: str, args: Sequence[Any], kwargs: Mapping[str, Any]) -> Any: ...

    def get_value(self, key: Union[int, str], args: Sequence[Any], kwargs: Mapping[str, Any]) -> Any:
        raise IndexError()
        raise KeyError()

    def check_unused_args(self, used_args: Sequence[Union[int, str]], args: Sequence[Any], kwargs: Mapping[str, Any]) -> None: ...

    def format_field(self, value: Any, format_spec: str) -> Any: ...

    def convert_field(self, value: Any, conversion: str) -> Any: ...

def capwords(s: str, sep: str = None) -> str: ...

# TODO: originally named 'from'
def maketrans(_from: str, to: str) -> str: ...

def atof(s: str) -> float: ...
def atoi(s: str, base: int = 10) -> int: ...
def atol(s: str, base: int = 10) -> int: ...
def capitalize(word: str) -> str: ...
def find(s: str, sub: str, start: int = None, end: int = None) -> int: ...
def rfind(s: str, sub: str, start: int = None, end: int = None) -> int: ...
def index(s: str, sub: str, start: int = None, end: int = None) -> int: ...
def rindex(s: str, sub: str, start: int = None, end: int = None) -> int: ...
def count(s: str, sub: str, start: int = None, end: int = None) -> int: ...
def lower(s: str) -> str: ...
def split(s: str, sep: str = None, maxsplit: int = -1) -> List[str]: ...
def rsplit(s: str, sep: str = None, maxsplit: int = -1) -> List[str]: ...
def splitfields(s: str, sep: str = None, maxsplit: int = -1) -> List[str]: ...
def join(words: Union[List[str], Tuple[str]], sep: str = None) -> str: ...
def joinfields(word: Union[List[str], Tuple[str]], sep: str = None) -> str: ...
def lstrip(s: str, chars: str = None) -> str: ...
def rstrip(s: str, chars: str = None) -> str: ...
def strip(s: str, chars: str = None) -> str: ...
def swapcase(s: str) -> str: ...
def translate(s: str, table: str, deletechars: str = None) -> str: ...
def upper(s: str) -> str: ...
def ljust(s: str, width: int, fillhar: str = ' ') -> str: ...
def rjust(s: str, width: int, fillhar: str = ' ') -> str: ...
def center(s: str, width: int, fillhar: str = ' ') -> str: ...
def zfill(s: str, width: int) -> str: ...
def replace(s: str, old: str, new: str, maxreplace: int = None) -> str: ...

class Template(object):
    template = ''

    def __init__(self, template: str) -> None: ...
    def substitute(self, mapping: Mapping[str, str], **kwds: str) -> str: ...
    def safe_substitute(self, mapping: Mapping[str, str],
                        **kwds: str) -> str: ...

# TODO Formatter
