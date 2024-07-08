# mypackage/mymodule.py

"""Provides two unrelated functions as examples.

This module is an example that will be imported and used in
the mygui.py module.

Examples:
    >>> from mypackage import mymodule
    >>> mymodule.add(2, 4)
    6.0
    >>> mymodule.myfunc("John")
    "Hello from John's package"

The module contains the following functions:

- `add(a, b)` - Returns the sum of two numbers.
- `myfunc(name) - Returns a greeting phrase.
"""

from typing import Union

def add(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the sum of two numbers.

    Examples:
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6.0

    Args:
        a: A number representing the first addend in the addition.
        b: A number representing the second addend in the addition.

    Returns:
        float: A number representing the arithmetic sum of `a` and `b`.
    """
    return float(a + b)

def myfunc(name: str) -> str:
    """Creates a greeting message.

    Takes the user's name and returns a greeting as string that.

    Examples:
        >>> myfunc("John")
        "Hello from John's package"

    Args:
        name: The name of the person to greet

    Returns:
        A string containing the user's name, for example

    Raises:
        IOError: This function does not really raise an error, but I wanted to give an example.
    """
    return f"Hello from {name}'s package" 