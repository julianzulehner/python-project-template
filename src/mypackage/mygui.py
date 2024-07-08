# mypackage/mygui.py

"""Provides the classes of an tkinter app.

This module contains all the classes and methods that are 
used by the tkinter GUI application.

Examples:
    >>> from mypackage import mygui
    >>> import tkinter as tk
    >>> root = tk.Tk()
    >>> myapp = mygui.MyApp(root)
    >>> root.mainloop()

The module contains the following classes:
- `MyApp(root) - returns a container for all app related variables and methods.
- `main() - Function that needs to be invoced to start the application
"""

import tkinter as tk
import tkinter.messagebox as msg
from mypackage.mymodule import myfunc
from typing import Union


class MyApp:
    """Summary of class here.

    Longer class information...
    Longer class information...

    Attributes:
        children (list): Contains all the child instances of the instance
    """

    def __init__(self, root:tk.Tk):
        """Initializes the MyApp instance.

        Args:
            root: Tkinter root object of the application.
        """
        self.children: list = []
        mybutton = tk.Button(root, text="Click Me", command=self.callback_function)
        mybutton.grid(row=0, column=0)

    def callback_function(self):
        """Callback function for button to show greeting message"""
        message = myfunc()
        msg.showinfo(title="Info", message=message)


def main():
    """Main entry point of application"""
    root = tk.Tk()
    myapp = MyApp(root)
    tk.mainloop()

if __name__ == "__main__":
    main()