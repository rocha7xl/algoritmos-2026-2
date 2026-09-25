preco_bala = 0.10
total_float = preco_bala * 3
print(total_float)
print(total_float == 0.30)
print(type(total_float))
print(type(preco_bala))

quantidade = 3
total_cents = preco_bala * quantidade
reais = total_cents // 100
centavos = total_cents % 100

print(f"Total: {reais}, {centavos:02d}")