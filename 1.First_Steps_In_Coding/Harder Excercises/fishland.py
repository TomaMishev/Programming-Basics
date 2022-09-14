mackerel_price_per_kg = float(input())
sprat_price_per_kg = float(input())
bonito_kg = float(input())
scad_kg = float(input())
clams_kg = float(input())

bonito_price_per_kg = mackerel_price_per_kg + (mackerel_price_per_kg * 0.60)
bonito_total_sum = bonito_price_per_kg * bonito_kg

scad_price_per_kg = sprat_price_per_kg + (sprat_price_per_kg * 0.80)
scad_total_sum = scad_price_per_kg * scad_kg
clams_total_sum = clams_kg * 7.50

total = bonito_total_sum + scad_total_sum + clams_total_sum

print(f"{total:.2f}")

