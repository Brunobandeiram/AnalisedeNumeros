numeros = []

while len(numeros) < 15:
    try:
        n = int(input(f"Digite o {len(numeros)+1}º número: "))
        if n in numeros:
            print("⚠️ Número repetido! Digite outro valor.")
        else:
            numeros.append(n)
    except ValueError:
        print("❌ Entrada inválida! Digite um número inteiro.")

numeros.sort()

maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)
media = soma / len(numeros)

pares = 0
impares = 0

for n in numeros:
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

print("\n------ Resultados ------")
print("Números em ordem crescente:", numeros)
print("Maior número:", maior)
print("Menor número:", menor)
print("Soma dos números:", soma)
print(f"Média: {media:.2f}")
print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)
