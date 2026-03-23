nome_entrada = "harry potter"
nomes_partes = nome_entrada.split(" ")
nome_completo = ''
for nome in nomes_partes:
    nomeAjustado = nome[0].upper() + nome[1:]
    nome_completo += nomeAjustado + ' '
nome_completo = nome_completo.strip()
print(nome_completo)