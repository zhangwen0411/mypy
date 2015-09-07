# Stubs for getpass (Python 2)

from typing import Any, IO

class GetPassWarning(UserWarning): ...

def getpass(prompt: str = 'Password: ', stream: IO[Any] = None) -> str: ...
def getuser() -> str: ...
