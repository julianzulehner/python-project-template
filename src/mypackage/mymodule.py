"""A one-line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

Typical usage example:

  greeting = myfunc("John")
"""

def myfunc(name):
    """Creates a greeting message.

    Takes the user's name and returns a greeting as string that.

    Examples:
        >>> myfunc("John")
        "Hello from John's package"

    Args:
        name (str): The name of the person to greet

    Returns:
        A string containing the user's name, for example

    Raises:
        IOError: This function does not really raise an error, but I wanted to give an example.
    """
    return f"Hello from {name}'s package" 