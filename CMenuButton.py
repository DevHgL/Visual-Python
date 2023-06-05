
import tkinter as tk

#import self as self


class MenuButton(tk.Button):
    def __init__(self, master, bgcolor, activebgcolor, **kw):
        tk.Button.__init__(self, master=master, **kw)
        self.defaultBackground = bgcolor
        self.activebgcolor = activebgcolor
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self["background"] = self.activebgcolor

    def on_leave(self, e):
        self["background"] = self.defaultBackground