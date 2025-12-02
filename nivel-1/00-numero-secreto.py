import random
P = random.randint(1, 10)
while True:
    N = int(input("qual numero você pensa agora? "))
    if N > P:
	    print(f'Muito alto!')
    elif N < P:
	    print(f'Muito Baixo!')
    else:
        print('Acertou')
        break
print('conseguiu')	
