faturamento = 1000
custo = 700
lucro = faturamento - custo
margem_lucro = lucro / faturamento
print(f"faturamento da empresa: {faturamento}, custos: {custo}, lucro: {lucro} Margem Lucro: {margem_lucro}")

email_cliente = "email@gmail.com"

email_cliente = email_cliente.upper()
print(email_cliente)


email_cliente = email_cliente.lower()
print(email_cliente)

print(email_cliente.find("@"))
print(len (email_cliente))
print(email_cliente[5:])
novo_email = email_cliente.replace("gmail.com", "hotmail.com")
print(novo_email)
posicao = email_cliente.find("@")

servidor_email = email_cliente[posicao:]

print(servidor_email)
nome = "Marcos paulo"

posicao_espaco = nome.find(" ")

primeiro_nome = nome[:posicao_espaco]
sobre_nome = nome[posicao_espaco+1:]

print(primeiro_nome)
print(sobre_nome)

print(f"faturamento da empresa: {faturamento}, custos: {custo}, lucro: {lucro} Margem Lucro: {margem_lucro:.0%}")