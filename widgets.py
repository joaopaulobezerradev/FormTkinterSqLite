import tkinter as tk
from conexao import conectar


class Widgets:
    def __init__(self, master):
        self.master = master

    def criar_widgets(self):
        self.criar_grupo_dados_pessoais()
        self.criar_grupo_dados_empresa()
        self.criar_grupo_endereco()
        self.criar_grupo_dados_comerciais()
        self.criar_grupo_upload_arquivos()

    def criar_grupo_dados_pessoais(self):
        grupo = tk.LabelFrame(self.master, text="Dados Pessoais")
        grupo.grid(padx=10, pady=10)

        lbl_nome = tk.Label(grupo, text="Nome:")
        lbl_nome.grid(row=0, column=0)
        ent_nome = tk.Entry(grupo, bd=2, relief="groove")
        ent_nome.grid(row=0, column=1)
        # lbl_nome.grid()
        # ent_nome = tk.Entry(grupo)
        # ent_nome.grid()

        lbl_email = tk.Label(grupo, text="E-mail:")
        lbl_email.grid(row=1, column=0)
        ent_email = tk.Entry(grupo, bd=2, relief="groove")
        ent_email.grid(row=1, column=1)
        # lbl_email.grid()
        # ent_email = tk.Entry(grupo)
        # ent_email.grid()

    def criar_grupo_dados_empresa(self):
        grupo = tk.LabelFrame(self.master, text="Dados da Empresa")
        grupo.grid(padx=10, pady=10)

        lbl_razao_social = tk.Label(grupo, text="Razão Social:")
        lbl_razao_social.grid(row=3, column=0)
        ent_razao_social = tk.Entry(grupo, bd=2, relief="groove")
        ent_razao_social.grid(row=3, column=1)
        # lbl_razao_social.grid()
        # ent_razao_social = tk.Entry(grupo)
        # ent_razao_social.grid()

        lbl_nome_fantasia = tk.Label(grupo, text="Nome Fantasia:")
        lbl_nome_fantasia.grid()
        ent_nome_fantasia = tk.Entry(grupo)
        ent_nome_fantasia.grid()

        lbl_cnpj = tk.Label(grupo, text="CNPJ:")
        lbl_cnpj.grid()
        ent_cnpj = tk.Entry(grupo)
        ent_cnpj.grid()

        lbl_inscricao_estadual = tk.Label(grupo, text="Inscrição Estadual:")
        lbl_inscricao_estadual.grid()
        ent_inscricao_estadual = tk.Entry(grupo)
        ent_inscricao_estadual.grid()

    def criar_grupo_endereco(self):
        grupo = tk.LabelFrame(self.master, text="Endereço")
        grupo.grid(padx=10, pady=10)

        lbl_endereco = tk.Label(grupo, text='Endereço:')
        lbl_endereco.grid()
        ent_endereco = tk.Entry(grupo)
        ent_endereco.grid()

        lbl_numero = tk.Label(grupo, text='Número:')
        lbl_numero.grid()
        ent_numero = tk.Entry(grupo)
        ent_numero.grid()

        lbl_bairro = tk.Label(grupo, text='Bairro:')
        lbl_bairro.grid()
        ent_bairro = tk.Entry(grupo)
        ent_bairro.grid()

        lbl_complemento = tk.Label(grupo, text='Complemento:')
        lbl_complemento.grid()
        ent_complemento = tk.Entry(grupo)
        ent_complemento.grid()

        lbl_cidade = tk.Label(grupo, text='Cidade:')
        lbl_cidade.grid()
        ent_cidade = tk.Entry(grupo)
        ent_cidade.grid()

        lbl_estado = tk.Label(grupo, text='Estado:')
        lbl_estado.grid()
        ent_estado = tk.Entry(grupo)
        ent_estado.grid()

        lbl_telefone1 = tk.Label(grupo, text='Telefone 1:')
        lbl_telefone1.grid()
        ent_telefone1 = tk.Entry(grupo)
        ent_telefone1.grid()

        lbl_telefone2 = tk.Label(grupo, text='Telefone 2:')
        lbl_telefone2.grid()
        ent_telefone2 = tk.Entry(grupo)

    def criar_grupo_dados_comerciais(self):
        grupo = tk.LabelFrame(self.master, text="Dados Comerciais")
        grupo.grid(padx=10, pady=10)

        lbl_razao_social_comercial = tk.Label(grupo, text='Razão Social:')
        lbl_razao_social_comercial.grid()
        ent_razao_social_comercial = tk.Entry(grupo)

    def criar_grupo_upload_arquivos(self):
        grupo = tk.LabelFrame(self.master, text="Upload de Arquivos")
        grupo.grid(padx=10, pady=10)

        arquivos = []

    def adicionar_arquivo():
        arquivo = tk.askopenfilename(initialdir="/", title="Selecione o arquivo", filetypes=(
            ("Arquivos PDF", "*.pdf"), ("Todos os arquivos", "*.*")))
        arquivos.append(arquivo)
