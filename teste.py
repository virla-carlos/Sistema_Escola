import os

class Escola:
    def __init__(self, nome_escola: str, endereco_escola: str, cep_escola: str):
        self.nome_escola = nome_escola
        self.endereco_escola = endereco_escola
        self.cep_escola = cep_escola

    def cadastrar_escola(self):

        print("======== Cadastro de Escola ========\n")
        self.nome_escola = input("School name: ")
        self.endereco_escola = input("School adress: ")
        self.cep_escola = input("School cep: ")

    def exibir_escola(self):

        print("======== Escolas Cadastradas ========\n")
        print(f"School name: {self.nome_escola} ")
        print(f"School adress: {self.endereco_escola} ")
        print(f"School cep: {self.cep_escola} ")

    def listar_opcoes(self):

        print("Seja bem-vindo!")
        print("O que você gostaria de fazer ?\n")
        print("1 - Cadastrar escola")
        print("2 - Listar escola(s)")
        print("3 - Remover escola")
        print("4 - Editar escola")
        print("5 - Encerrar sessão")

        resposta_usuario = int(input("Selecione uma opção: "))
        if resposta_usuario == 1:
            teste.cadastrar_escola()
        elif resposta_usuario == 2:
            teste.listar_opcoes()


teste = Escola("CERV", "Rua Marco Sete", "23092-093")
teste.listando_opcoes()