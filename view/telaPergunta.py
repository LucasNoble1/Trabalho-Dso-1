    def tela_opcoes(self):
        print("\n")
        print("-----Opçoes-----")
        print("\n")
        print("1 - Criar uma Nova pergunta")
        print("2 - Alterar uma pergunta")
        print("3 - Excluir uma pergunta")
        print("0 - voltar")
        print("\n")
        opcao = self.le_num_inteiro("Selecione uma opção:", [1, 2, 3, 0])
        return opcao

    #metodo que mostra a pergunta e suas alternativas durante o jogo
    def mostrar_pergunta(self, pergunta, alt1, alt2, alt3, nome):
        print("=============================")
        print("jogador da vez: ",nome)
        print("          PERGUNTA:         ")
        print(">", pergunta, "<")
        print("=============================")
        print("    ESCOLHA UMA ALTERNATIVA    ")
        print("1 --", alt1)
        print("2 --", alt2)
        print("3 --", alt3)
        opcao = self.le_num_inteiro("Selecione uma opção:", [1, 2, 3])

        return opcao
    def criar_pergunta(self):
        print("============================")
        print("=== CRIE SUA PERGUNTA!! :)===")
        print("============================")
        pergunta = input("Qual a Pergunta?")
        print("============================")
        print("Sua pergunta vai precisar de uma alternativa correta e duas erras")
        print("===========================")
        print("Pergunta:", pergunta)
        resposta = input("Informe a resposta correta de sua pergunta:")
        alternativa1 = input("Crie uma alternativa falsa para sua pergunta:")
        alternativa2 = input("Crie outra alternativa falsa para sua pergunta:")
        id = input("Crie um ID para a pergunta")

        return pergunta, resposta, alternativa1, alternativa2, id
    #informa q a pergunta ja existe.
    #mostra a pergunta
    #volta para a tela inicial de perguntas
    def pergunta_repetida(self,pergunta):
        print("==")
        print("ERRO!")
        print(pergunta + "JA EXISTE NO SISTEMA")
        self.__controlador.abre_tela()

    #mensagem informando que a pergunta foi adicionada
    #volta para a tela inicial de perguntas
    def pergunta_adicionada(self,pergunta):
        print("A Pergunta:" + pergunta)
        print("FOI ADICIONADA COM SUCESSO!!!")
        self.__controlador.abre_tela()

    def mostrar_todas_perguntas(self, codigo, pergunta):
        print(codigo, "====>" , pergunta)

    def editar_pergunta(self, p, r, a1, a2):
        pergunta = p
        resposta = r
        alternativa1 = a1
        alternativa2 = a2
        print("==Editar uma pergunta==")
        print(" 1 => PERGUNTA: ", pergunta)
        print(" 2 => RESPOSTA: ", resposta)
        print(" 3 => ALTERNATIVA 1: ", alternativa1)
        print(" 4 => ALTERNATIVA 2: ", alternativa2)
        print(" 0 => VOLTAR")
        opcao = self.le_num_inteiro("Selecione a opção que deseja alterar:", [0, 1, 2, 3, 4])
        if opcao == 0:
            return "0", 0
        elif opcao == 1:
            print("PERGUNTA ANTIGA: ", pergunta)
            pergunta_nova = str(input("Digite a nova pergunta:"))
            print("Suas alteracoes foram salvas com sucesso!!!")
            print("=========================================")
            return pergunta_nova , opcao
        elif opcao == 2:
            print("RESPOSTA ANTIGA: ", resposta)
            resposta = str(input("Digite a nova resposta:"))
            print("Suas alteracoes foram salvas com sucesso!!!")
            print("=========================================")
            return resposta, opcao
        elif opcao == 3:
            print("ALTERNATIVA ANTIGA: ", alternativa1)
            resposta = str(input("Digite a nova alternativa:"))
            print("Suas alteracoes foram salvas com sucesso!!!")
            print("=========================================")
            return resposta, opcao
        elif opcao == 4:
            print("ALTERNATIVA ANTIGA: ", alternativa2)
            resposta = str(input("Digite a nova alternativa:"))
            print("Suas alteracoes foram salvas com sucesso!!!")
            print("=========================================")
            return resposta, opcao


    def pedir_pergunta(self):
        print("===============================================")
        print('\n')
        codigo = input("Digite o codigo da pergunta:")
        return codigo

    def pergunta_removida(self, pergunta):
        print("A Pergunta:" + pergunta)
        print("FOI REMOVIDA COM SUCESSO!!!")
        self.__controlador.abre_tela()

    def pergunta_inexistente(self, codigo):
        codigo = str(codigo)
        print("\n")
        print("ERRO")
        print("O codigo ", codigo , "nao coresponde a nenhuma pergunta!")
        print("Nenhuma pergunta foi excluida, ou alterada!")
        self.tela_opcoes()

    
     # tela pergunta interf grafica
    def tela_pergunta_teste(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        # cobre os casos de voltar, não clicar em nada e fechar janela
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao
     
    #metodo para iniciar os componentes da interface grafica da tela de Pergunta
    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('-----Opçoes-----')]
            [sg.Text('--------------------------')]
            [sg.Radio('1 - Cadastrar pergunta', "RD1", key='1')],
            [sg.Radio('2 - Excluir pergunta', "RD1", key='2')],
            [sg.Radio('3 - Editar pergunta', "RD1", key='3')],
            [sg.Cancel('0 - voltar')]
            ]
        self.__window = sg.Window('Perguntas').Layout(layout)
    
        self.__window = sg.Window('Perguntas').Layout(layout)
