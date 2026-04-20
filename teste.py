# Nesse aquivo eu testo algumas partes do código para conseguir identificar o erro de uma forma mais organizada
# Atualmente eu ainda não consegui organizar o projeto em pastas e depois chamar tudo em apenas um arquivo
# Mas essa é correção que eu ainda vou realizar

class Cadastro_Escola:
    def __init__(self, nome_escola=None, endereco_escola=None, cep_escola=None):
        self.nome_escola = nome_escola
        self.endereco_escola = endereco_escola
        self.cep_escola = cep_escola

    def cadastrar_escola(self):

        print("======== Cadastrar Escola no Sistema ========\n")
        self.nome_escola = input("School name: ")
        self.endereco_escola = input("School adress: ")
        self.cep_escola = input("School cep: ")

        self.escola = [self.nome_escola, self.endereco_escola, self.cep_escola]
        self.escolas += [self.escola]
    
    def exibir_escola(self):

        if self.nome_escola and self.endereco_escola and self.cep_escola == None:
            print("Error!\nNenhuma escola cadastrada.\nVolte ao menu e realize o cadastro de uma escola.")

        print("======== Escolas Cadastradas no Sistema ========\n")
        print("Name school: ", self.nome_escola)
        print("Adress school: ", self.endereco_escola)
        print("cep school: ", self.cep_escola)

        return self.listar_opcoes()    

teste = Cadastro_Escola()
# arquivo_escola.cadastrar_escola()
teste.cadastrar_escola()
escola = [teste.cadastrar_escola()]
teste.exibir_escola()