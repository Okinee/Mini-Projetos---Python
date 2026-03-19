pontuacao = 0
print("Seja bem vindo ao Quiz sobre Dachshund! \n")
answer_user = input("Deseja iniciar o Quiz? (S/N) \n")
if answer_user != "S" :
    quit()
print("\nComeçando...\n")
resposta1 = input("Qual é a principal característica física do Dachshund?\n(A) Orelhas curtas e corpo robusto\n(B) Corpo longo e pernas curtas\n(C) Pelagem encaracolada\n(D) Cauda curta e rígida\n(E) Cabeça achatada\n")
if resposta1 == "B":
    pontuacao += 1
    print("\nCorreto!\n")
else:
    print("\nIncorreto!")
resposta2 = input("Para qual finalidade o Dachshund foi originalmente criado?\n(A) Pastoreio de ovelhas\n(B) Caça de animais em tocas\n(C) Companhia para nobres\n(D) Corridas de velocidade\n(E) Guarda de propriedades\n")
if resposta2 == "B":
    pontuacao += 1
    print("\nCorreto!\n")
else:
    print("\nIncorreto!")
resposta3 = input("Qual país é considerado a origem da raça Dachshund?\n(A) França\n(B) Inglaterra\n(C) Alemanha\n(D) Suíça\n(E) Holanda\n")
if resposta3 == "C":
    pontuacao += 1
    print("\nCorreto!\n")
else:
    print("\nIncorreto!")
resposta4 = input("Quantos tipos de pelagem o Dachshund pode apresentar?\n(A) Apenas 1\n(B) 2 tipos\n(C) 3 tipos\n(D) 4 tipos\n(E) 5 tipos\n")
if resposta4 == "C":
    pontuacao += 1
    print("\nCorreto!\n")
else:
    print("\nIncorreto!")
resposta5 = input("O Dachshund é conhecido popularmente no Brasil por qual apelido?\n(A) Cachorro-lobo\n(B) Cachorro-salsicha\n(C) Terrier pequeno\n(D) Mini caçador\n(E) Cão anão\n")
if resposta5 == "B":
    pontuacao += 1
    print("\nCorreto!\n")
else:
    print("\nIncorreto!")



print("Quiz acabou... Pontuação: {}/5".format(pontuacao))
