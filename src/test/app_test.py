import re
    # Primeiramente o cliente manda uma mensagem para o número de Telefone
    
    #Exemplo: "Olá Estou vindo do site e gostaria de participar de um desafio"
'''
 problemas para resolver: loop do nome que é para ficar só o inicial e
 quando escolho uma opção, exemplo a 2, ao final de toda mensagem aparece a primeira. 
 essa daqui: vou mandar print para vocÊ no wpp.
 "Entendido! Vamos te passar mais informações."
 '''
def responder_mensagem(mensagem_recebida):
    # Primeira resposta automática
    resposta_inicial = "SUPERE-SE desafios agradece seu contato. Como podemos ajudar?"
    print(f"Mensagem recebida: {mensagem_recebida}")
    print(f"Resposta enviada: {resposta_inicial}")

    # Pergunta o nome da pessoa
    j = 0
    while j < 5:
        pergunta_nome = "Poderia nos informar seu nome, por favor?"
        print(f"Resposta enviada: {pergunta_nome}")

    # Simula a resposta do cliente com o nome
        nome_cliente = re.match(r"^([a-zA-Z]+)", input("Cliente responde: "))
    
        if nome_cliente:
            nome_cliente = nome_cliente.group(1)
            break
        else:
            j += 1
            if j < 5:
                print("""
                      Entrada inválida. Apenas letras e espaços são permitidos.
                      Digite um nome válido
                      """)
            else:
                print("""
                    Devido a falta de comunicação, encerraremos o atendimento.
                    Agradecemos o contato!
                    """)
                exit()


    # Responde com uma saudação personalizada
    saudacao = f"Prazer, {nome_cliente}."
    print(f"Resposta enviada: {saudacao}")

    # Pergunta sobre desafios virtuais
    pergunta_desafios = "Já participou de desafios virtuais? Sabe como funciona?"
    
    while True:
        print("""
                1. Sim, já participei e sei como funciona
                2. Sim, mas quero saber como funciona
                3. Não, mas quero saber como funciona
                4. Não, não quero saber como funciona 
            """)
        print(f"Resposta enviada: {pergunta_desafios}")
        opcao_desafios = input()
    
        if opcao_desafios == "1":
            print("11111111111111111")
            break
        elif opcao_desafios == "2":
            print("22222222222222222")
            break
        elif opcao_desafios == "3":
            print("33333333333333333")
            break
        elif opcao_desafios == "4":
            print("Obrigado pelo contato!")
            exit()
        else:
            print("""
                Opção não cadastrada, gostaria de ver novamente as opções?
                1. Sim
                2. Não (Encerraremos o atendimento)
                """)
            opcao_desafios_outra = input()
            if opcao_desafios_outra == "1":
                continue
            elif opcao_desafios_outra == "2":
                print("Obrigado pelo contato!")
                exit()
            else:
                print("Opção inválida. Encerraremos o atendimento.")
                exit()


    # Simula o envio de opções de resposta
    while True:
        print("Resposta enviada: Ver opções")
        print("Opções disponíveis:")
        print("""
            1. Sim, quero me inscrever.
            2. Sim, mas tenho interesse em mais informações.
            3. Não, mas quero conhecer.
            4. Não, encerrar atendimento
            """)

    # Simula a escolha de uma opção pelo cliente
        opcao_escolhida = input("Cliente escolhe a opção (1, 2, 3 ou 4): ")

    # Responde de acordo com a opção escolhida
        if opcao_escolhida == "1":
            resposta_opcao = "Ótimo! Vamos prosseguir com a inscrição."
            #perguntar sobre o envio das informações
            print(f'Resposta enviada: {resposta_opcao}')
            print("Pergunta enviada: Posso te enviar as informações de inscrição agora? (Sim/Não)")
            resposta_inscricao = input("Cliente responde: ")
            if resposta_inscricao.lower() == "sim":
                print("Resposta enviada: Excelente! As informações de inscrição estão a caminho.")
                #informações adicionais
                break
            else:
                print("Resposta enviada: Sem problemas, podemos falar em outro momento.")
                print("Agradecemos o contato!")
                exit()
            # Encerrar ou continuar conforme o fluxo
                
                
        elif opcao_escolhida == "2":
            resposta_opcao = "Entendido! Vamos te passar mais informações."
            print(f"Resposta enviada: {resposta_opcao}")
            # Perguntar qual informação deseja mais detalhes
            i = 0
            while i < 5:
                print("Pergunta enviada: Sobre o que gostaria de saber mais? (Desafios, Recompensas, Regras)")
                resposta_detalhes = input("Cliente responde: ")
                if resposta_detalhes.lower() in ["desafios", "recompensas", "regras"]:
                    print(f"Resposta enviada: Enviando mais informações sobre {resposta_detalhes}.")
                    break
                    # Fornecer mais informações conforme a escolha
                else:
                    i += 1
                    if i < 5:
                        print("Resposta enviada: Não entendi, poderia repetir?")
                    else:
                        print("""
                              Devido a falta de comunicação, encerraremos o atendimento.
                              Agradecemos o contato!
                              """)
                        exit()
                # Repetir ou encerrar
            
        elif opcao_escolhida == "3":
            resposta_opcao = "Que bom que quer conhecer! Vamos te explicar tudo."
            print(f"Resposta enviada:{resposta_opcao}")
            #apresentação geral dos desafios por áudio
            print("Resposta enviada: Vamos te apresentar um resumo sobre nossos desafios...")
            break
        elif opcao_escolhida == "4":
            print("Agradecemos o contato!")
            exit()
        else:
            resposta_opcao = "Opção inválida. Por favor, escolha uma das opções disponíveis."
            print("Caso queira encerrar o atendimento digite 4")
            continue
        print(f"Resposta enviada: {resposta_opcao}")
    


# Simulação de uma mensagem recebida do cliente
mensagem_do_cliente = "Olá, gostaria de mais informações sobre os desafios."
responder_mensagem(mensagem_do_cliente)