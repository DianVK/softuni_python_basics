price_skumriq = float(input())
price_caca = float(input())
kg_palamud = float(input())
palamud_price = price_skumriq + (price_skumriq * 0.60)
sum_palamud = kg_palamud * palamud_price
kg_safrid = float(input())
safrid_price = price_caca + (price_caca * 0.80)
sum_safrid = kg_safrid * safrid_price
kg_midi = int(input())
sum_midi = kg_midi * 7.50
total_price = sum_midi + sum_palamud + sum_safrid
print(f"{total_price:.2f}")
