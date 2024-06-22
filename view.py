import tkinter as tk

class view:
    def __init__(self) -> None:
        self.window = self.create_window()
        self.bind_keys()

    def create_window(self):
        window = tk.Tk()
        window.title("JVE Text Editor")

        text_edit = tk.Text(window, font="Helvetica 18")
        text_edit.grid(row=0, column=1)

        return window
    
    def bind_keys(self):
        self.window.bind('i', self.i_key)
        self.window.bind('<Escape>', self.escape_key)

    def i_key(self, event):
        print('i key has been pressed')

    def escape_key(self, event):
        print('escape key has been pressed')

    def open_editor(self):
        self.window.mainloop()

if __name__ == "__main__":
    x = view()
    x.open_editor()