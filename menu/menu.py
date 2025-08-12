print("O mundo está cheio de desafios e mistérios! Escolha sua próxima aventura:\n1️⃣ **A Jornada do Aventureiro** - Contar os degraus de uma torre mágica (1 a 10).\n2️⃣ **O Cofre Secreto** - Inserir a senha correta para abrir um cofre antigo.\n3️⃣ **O Baú Encantado** - Inserir números até que o número zero seja digitado.\n4️⃣ **A Fonte dos Desejos** - Jogar moedas até atingir um valor limite.\n5️⃣ **A Missão do Guardião do Tempo** - Contagem regressiva para ativar um portal.\n6️⃣ **O Oráculo dos Números** - Descobrir se um número é par ou ímpar até decidir sair.\n7️⃣ **O Cofre do Tesouro** - Sacar moedas até o saldo acabar.\n0️⃣ **Sair** - Encerrar a jornada.")
escolha =""
while escolha !=0:
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        degraus = 0
        while degraus <= 10:
            print(f"Degrau de numero: {degraus}")
            degraus += 1

    elif escolha == "2":
        senhac = ("123")
        senha = (input("informe a senha\n-->"))

        while senha != senhac:
            senha = int(input("Qual a senha?\n-->"))
            if senha != senhac:
                print("Senha errada. Tente novamente.")
            if senha == senhac:
                print("senha correta")
            print("****FIM****")

    elif escolha == "3": 
            numeroc = int(input("Você achou um baú mágico em uma floresta encantada."))
            numeroc = int(input("coloque qualquer valor dentro desse baú"))
            numero=0
            numeroc=int
            while numeroc != numero:
                numeroc=int(input("adicione um numero--->")) 
            print("Adicione mais um número")
            if numero == numeroc:
                print("adicione mais numeros")
            else:
                print("!!! o bau foi fechado !!!")
    
    elif escolha == "4":
            print("Você achou uma fonte dos desejos mágica")
            print("Ela concede um desejo sempre que alguém joga moedas dentro dela.")
            valor = 5
            moeda = float(input("Qual o valor da moeda que você irá jogar?-->"))
            while valor > moeda:
                print("Com esse valor não atingiu o minimo")
                moedanova = float(input("Qual o valor da moeda que você irá jogar?-->"))
                moeda +=moedanova
            print("Parabens, voce atingiu o limite!")
            print("****FIM****")

    elif escolha == "5":
            print("O Guardião do Tempo precisa ativar um portal dimensional")
            print("Mas ele só pode ser aberto depois de uma contagem regressiva.")
            contagem = 6
            while contagem > 0:
                contagem -= 1  
                print(contagem)
            print("Parabens, você ajudou o Guardião a ativar o portal!")
            print("****FIM****")

    elif escolha == "6":
            print("Uma antiga cidade possui um Oráculo dos Números, que pode revelar se um número é par ou ímpar")
            print("O oráculo funciona indefinidamente, a menos que o visitante digite 1 para sair.")
            numero=""
            while numero != 1:
                numero = int(input("Informe um numero ao Oráculo.-->"))
                conta = numero % 2
                if conta ==0:
                    print(f"O número {numero} é par")
                elif conta == 1:
                     print(f"O número {numero} é ímpar")
                     
    elif escolha == "7":
        saldo = 100

        while saldo > 0:
            print(f"Seu saldo é: {saldo}")
            saque = int(input("Informe o valor a ser sacado: "))

            if saque > saldo:
                print("Saldo insuficiente")
            else:
                saldo -= saque  
        print(f"Seu saldo é: {saldo}")

    elif escolha == '0':
            print("\nVocê encerrou sua jornada. Até a próxima!")
            break