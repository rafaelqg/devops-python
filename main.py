p1 = float(input("Digite o preço do produto 1: "))
p2 = float(input("Digite o preço do produto 2: "))
p3 = float(input("Digite o preço do produto 3: "))

precoMedio = (p1 + p2 + p3)/3
print(precoMedio)

if( precoMedio < 80 ):
    print("O preço médio é baixo.")
elif( precoMedio == 80 ):
    print("O preço médio é médio.")
else:
    print("O preço médio é alto.")