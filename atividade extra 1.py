import random
6
numero_secreto = random.randint(1, 100)
tentativas = 0

print("tu vai ter que adivinhar um número entre 1 a 100")

while True:
    tentativa = int(input("tente adivinhar o número: "))
    tentativas += 1

    if tentativa < numero_secreto:
        print("é maior que isso")
    elif tentativa > numero_secreto:
        print("nã, é menor que isso")
    else:
        print(f"Acerto miseravi, mas em {tentativas} vezes.")
        break