import teste

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