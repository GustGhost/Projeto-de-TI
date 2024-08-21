    # Primeiramente o cliente manda uma mensagem para o número de Telefone
    
    #Exemplo: "Olá Estou vindo do site e gostaria de participar de um desafio"
 
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
    print(f"Resposta enviada: {pergunta_desafios}")

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
    elif opcao_escolhida == "2":
        resposta_opcao = "Entendido! Vamos te passar mais informações."
    elif opcao_escolhida == "3":
        resposta_opcao = "Que bom que quer conhecer! Vamos te explicar tudo."
    else:
        resposta_opcao = "Opção inválida. Por favor, escolha uma das opções disponíveis."

    print(f"Resposta enviada: {resposta_opcao}")


# Simulação de uma mensagem recebida do cliente
mensagem_do_cliente = "Olá, gostaria de mais informações sobre os desafios."
responder_mensagem(mensagem_do_cliente)