import tkinter as tk

LARGE_FONT = ("Verdana", 12)


class Notepad_Plus(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.Frames = {}

        frame = WelcomePage(container, self)

        for F in (WelcomePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

        frame.grid(row=0, column=0, sriclky="nsew")

        self.show_frame("WelcomePage")

    def show_frame(self, cont):

        frame = self.frames[cont]

        frame.tkraise()


class WelcomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


app = Notepad_Plus()
app.mainloop()
