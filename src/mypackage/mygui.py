import tkinter as tk
import tkinter.messagebox as msg
from mypackage.mymodule import myfunc


class MyApp:
    """Summary of class here.

    Longer class information...
    Longer class information...

    Attributes:
        children (list): Contains all the child instances of the instance
    """

    children = []

    def __init__(self, root):
        """Initializes the MyApp instance.

        Args:
            root (tkinter.Tk): Tkinter root object of the application.
        """
        self.children = []
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