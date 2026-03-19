import random

user_points = 0

print("==============================================\n")
print("Seja Bem vindo ao jogo de adivinhar o numero! \n")
print("==============================================\n")
start = input("Deseja começar o jogo? (S/N) \n")
if start != "S":
    quit()
while True:
    choice_number = input("\nDigite o valor limite do desafio: ")
    if choice_number.isdigit():
        choice_number = int(choice_number)
        break
    else:
        print("Erro no codigo, Por favor, digite um número válido.")
        continue

computer_number = random.randint(0, choice_number)

while True:
    user_number = input("\nAdivinhe o numero: ")
    user_points += 1
    if user_number.isdigit():
        user_number = int(user_number)
    else:
        print("Erro no codigo, é necessario digitar um numero valido...\n\n")
        continue
    if user_number == computer_number:
        print("\n==============================================\n")
        print("Você acertou! \n")
        print("Numero de tentativas: {}\n".format(user_points))
        end = input("Deseja continuar? (S/N) \n")
        if end != "S":
            quit()   
        else: 
            computer_number = random.randint(0, choice_number)
            user_points = 0
            print("\n==============================================\n")
    elif user_number > computer_number:
        print("\nO numero digitado é maior que o numero aleatorio!")
    else: 
        print("\nO numero digitado é menor que o numero aleatorio!")
 
