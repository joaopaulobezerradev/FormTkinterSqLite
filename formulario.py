import tkinter as tk
from widgets import Widgets


class Formulario:
    def __init__(self, master):
        # Definir número de colunas
        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=1)

        # Criar grupos
        self.criar_grupo_dados_pessoais(master)
        self.criar_grupo_dados_empresa(master)
        self.criar_grupo_endereco(master)
        self.criar_grupo_dados_comerciais(master)
        self.criar_grupo_upload_arquivos(master)

    def criar_grupo_dados_pessoais(self, master):
        # Grupo 1
        label_grupo1 = tk.Label(master, text="Grupo 1")
        label_grupo1.grid(row=0, column=0, columnspan=2)

        Widgets(master).criar_grupo_dados_pessoais()

    def criar_grupo_dados_empresa(self, master):
        # Grupo 2
        label_grupo2 = tk.Label(master, text="Grupo 2")
        label_grupo2.grid(row=3, column=0, columnspan=2)

        Widgets(master).criar_grupo_dados_empresa()

    def criar_grupo_endereco(self, master):
        # Grupo 3
        label_grupo3 = tk.Label(master, text="Grupo 3")
        label_grupo3.grid(row=5, column=0, columnspan=2)

        Widgets(master).criar_grupo_endereco()

    def criar_grupo_dados_comerciais(self, master):
        # Grupo 4
        label_grupo4 = tk.Label(master, text="Grupo 4")
        label_grupo4.grid(row=7, column=0, columnspan=2)

        Widgets(master).criar_grupo_dados_comerciais()

    def criar_grupo_upload_arquivos(self, master):
        # Grupo 5
        label_grupo5 = tk.Label(master, text="Grupo 5")
        label_grupo5.grid(row=9, column=0, columnspan=2)

        Widgets(master).criar_grupo_upload_arquivos()
