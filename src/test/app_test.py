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
    pergunta_nome = "Poderia nos informar seu nome, por favor?"
    print(f"Resposta enviada: {pergunta_nome}")

    # Simula a resposta do cliente com o nome
    nome_cliente = input("Cliente responde: ")

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
                1. SIM
                2. NÃO (Encerraremos o atendimento)
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
    print("Resposta enviada: Ver opções")
    print("Opções disponíveis:")
    print("1. Sim, quero me inscrever.")
    print("2. Sim, mas tenho interesse em mais informações.")
    print("3. Não, mas quero conhecer.")

    # Simula a escolha de uma opção pelo cliente
    opcao_escolhida = input("Cliente escolhe a opção (1, 2 ou 3): ")

    # Responde de acordo com a opção escolhida
    if opcao_escolhida == "1":
        resposta_opcao = "Ótimo! Vamos prosseguir com a inscrição."
        #perguntar sobre o envio das informações
        print(f'Resposta enviada {resposta_opcao}')
        print("Pergunta enviada: Posso te enviar as informações de inscrição agora? (Sim/Não)")
        resposta_inscricao = input("Cliente responde: ")
        if resposta_inscricao.lower() == "sim":
            print("Resposta enviada: Excelente! As informações de inscrição estão a caminho.")
            #informações adicionais
        else:
            print("Resposta enviada: Sem problemas, podemos falar em outro momento.")
            # Encerrar ou continuar conforme o fluxo
            
            
    elif opcao_escolhida == "2":
        resposta_opcao = "Entendido! Vamos te passar mais informações."
        print(f"Resposta enviada: {resposta_opcao}")
        # Perguntar qual informação deseja mais detalhes
        print("Pergunta enviada: Sobre o que gostaria de saber mais? (Desafios, Recompensas, Regras)")
        resposta_detalhes = input("Cliente responde: ")
        if resposta_detalhes.lower() in ["desafios", "recompensas", "regras"]:
            print(f"Resposta enviada: Enviando mais informações sobre {resposta_detalhes}.")
            # Fornecer mais informações conforme a escolha
        else:
            print("Resposta enviada: Não entendi, poderia repetir?")
            # Repetir ou encerrar
        
    elif opcao_escolhida == "3":
        resposta_opcao = "Que bom que quer conhecer! Vamos te explicar tudo."
        print(f"Resposta enviada:{resposta_opcao}")
        #apresentação geral dos desafios por áudio
        print("Resposta enviada: Vamos te apresentar um resumo sobre nossos desafios...")
    else:
        resposta_opcao = "Opção inválida. Por favor, escolha uma das opções disponíveis."
    print(f"Resposta enviada: {resposta_opcao}")


# Simulação de uma mensagem recebida do cliente
mensagem_do_cliente = "Olá, gostaria de mais informações sobre os desafios."
responder_mensagem(mensagem_do_cliente)