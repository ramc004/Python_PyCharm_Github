favourite_pizzas = ['pepperoni', 'hawaiian', 'veggie']
friend_pizzas = favourite_pizzas[:]

favourite_pizzas.append("meat lover's")
friend_pizzas.append('pesto')

print("My favourite pizzas are:")
for pizza in favourite_pizzas:
    print("- " + pizza)

print("\nMy friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print("- " + pizza)