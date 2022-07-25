from controller.controladorPrincipal import ControladorPrincipal
from model.pergunta import Pergunta



if __name__ == "__main__":
  lista = []
  p1 = Pergunta("Dos personagens a seguir quem ja matou o Kuririn?", "Frieza", "irmao do Jorel", "Deadpool","101")
  p2 = Pergunta("Dos titulos a seguir, qual pertnce a um filme da trilogia original de Star Wars?","O Imperio Contra-Ataca","O Despertar da Força"," A Ameaça Fantasma", "102")
  p3 = Pergunta("Em Star Wars, quem ficou responsavel pelo Treinamento de Anakin Skywalker?", "Obi-Wan Kenobi", "Luke Skywalker", "Han-Solo","103")
  p4 = Pergunta("Em Star Wars, quem era o Pai biologico da Princesa Leia?","Anakin Skaywalker","Yoda", "Han-solo","104")
  p5 = Pergunta("Nos filmes do MCU, que joia do infinito Doutor Estranho carregava em seu colar?","Tempo", "Espaço", "Alma","105")
  p6 = Pergunta("Nos filmes do MCU, qual foi a ultima joia do infinito que Thanos obteve, antes de dar seu estalo? ", "Mente", "Alma", "Poder","106")
  p7 = Pergunta("Nos filmes do MCU, em qual filme Loki morre ?", "Vingadores:Guerra Infinita", "Vingadores:Era de Ultron", "Thor: Ragnarok","107")
  p8 = Pergunta("Em Harry Potter, qual feitiço causou a marca que Harry tem em sua testa?", "Avada Kedavra", "Cruciatos", "Expelliarmus","108")
  p9 = Pergunta("Em Harry Potter, qual dos itens a seguir  é uma das reliqueas da morte?","Capa da invisibilidade","Nimbus2000","Quadribol","109")
  p10 = Pergunta("No primeiro episodio de  Stranger Things, que personagem foi levado para o mundo invertido?","Will", "Vecna", "11","110")
  p11 = Pergunta("Qual dos pokemons a seguir é um pokemom do tipo Agua?","Lapras", "Pikachu", "Jigglypuff","111")
  p12 = Pergunta("Qual é a evolucão do Pikachu?", "Raichu", "Pichu", "Charizard","112")
  p13 = Pergunta("Em Star Trek,qual das frases a seguir é dita por Spock?", "Vida longa e prospera!", "Que a força esteja com você!", "Ohana quer dizer familia", "113")
  p14 = Pergunta("Em Star Trek, qual o nome da nave pricipal pilotada pelo capitão Kirk² ",
                "USS ENTERPRISE", "MILLENNIUM FALCON", " MILANO", "114")
  p15 = Pergunta("No Filme Liga da justiça, com ajuda de qual artefato o super-homem pode voltar a vida?", "Caixa-Materna",
                "kriptonita", "Esferas do Dragao", "115")
  p16 = Pergunta("Qual o nome do Pai do Naruto Uzumaki?", "Minato Namikaze", "Nagato Uzumaki", "Tio Patinhas Uzumaki",
                "116")

  lista.append(p1)
  lista.append(p2)
  lista.append(p3)
  lista.append(p4)
  lista.append(p5)
  lista.append(p6)
  lista.append(p7)
  lista.append(p8)
  lista.append(p9)
  lista.append(p10)
  lista.append(p11)
  lista.append(p12)
  lista.append(p13)
  lista.append(p14)
  lista.append(p15)
  lista.append(p16)
  x = ControladorPrincipal()
  for i in lista:
    x.controlador_pergunta.adicionar_pergunta(i)
  x.inicializa_sistema()
