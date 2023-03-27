import tkinter as tk
from conexao import conectar
from widgets import Widgets


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Ficha de Cadastro")
        self.master.geometry("300x800")

        conn, cursor = conectar()
        self.conn = conn
        self.cursor = cursor

        widgets = Widgets(self.master)
        widgets.criar_widgets()


root = tk.Tk()
app = Application(master=root)
app.mainloop()
