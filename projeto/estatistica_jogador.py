import matplotlib.pyplot as plt

def jogador(nome, gols, assistencias):
    print(nome, gols, assistencias)
    
def estatisticas():
    jogador
    jogadores = ['Kaio Jorge','Arrascaeta','Vitor Roque','Rayan']
    gols = [21, 18, 16, 14]

    plt.pie(gols, labels=jogadores)
    plt.show()

estatisticas()