import random

user_points = 0
computer_points = 0
jokenpo = ["pedra", "papel", "tesoura"]

print("==============================================\n")
print("Seja Bem vindo ao jogo de Pedra, Papel e Tesoura! \n")
print("==============================================\n")

start = input("Deseja começar o jogo? (S/N)\n")
if start != "S":
  print("Ate a proxima jogar!")
  quit()

while True:
  jokenpo_choice = jokenpo[random.randint(0,2)]
  user_choice = input("Digite sua escolha: \n")
  print("\nA pontuação do computador foi: {}".format(jokenpo_choice))
  if (user_choice == jokenpo_choice):
    print("\n==============================================\n")
    print("Empate!")
    print ("Sua pontuação foi: {}".format(user_points))
    print("\n==============================================\n")
    again = input("Deseja jogar novamente? (S/N)\n")
    if again != "S":
      break
    print("\n")
  elif (user_choice == "pedra" and jokenpo_choice == "tesoura"):
    user_points += 1
    print("\n==============================================\n")
    print("Você Ganhou!\n")
    print ("Sua pontuação foi: {}".format(user_points))
    print ("A pontuação do computador foi: {}".format(computer_points))    
    print("\n==============================================\n")
    again = input("Deseja jogar novamente? (S/N)\n")
    if again != "S":
      break
    print("\n")   
  elif (user_choice == "tesoura" and jokenpo_choice == "papel"):
    user_points += 1
    print("\n==============================================\n")
    print("Você Ganhou!\n")
    print ("Sua pontuação foi: {}".format(user_points))
    print ("A pontuação do computador foi: {}".format(computer_points))    
    print("\n==============================================\n")
    again = input("Deseja jogar novamente? (S/N)\n")
    if again != "S":
      break
    print("\n")  
  elif (user_choice == "papel" and jokenpo_choice == "pedra"):
    user_points += 1
    print("\n==============================================\n")
    print("Você Ganhou!\n")
    print ("Sua pontuação foi: {}".format(user_points))
    print ("A pontuação do computador foi: {}".format(computer_points))   
    print("\n==============================================\n")
    again = input("Deseja jogar novamente? (S/N)\n")
    if again != "S":
      break
    print("\n") 
  else:
    computer_points += 1
    print("\n==============================================\n")
    print("Você Perdeu!\n")
    print ("Sua pontuação foi: {}\n".format(user_points))
    print ("A pontuação do computador foi: {}".format(computer_points))
    print("\n==============================================\n")
    again = input("Deseja jogar novamente? (S/N)\n")
    if again != "S":
      break
    print("\n") 
