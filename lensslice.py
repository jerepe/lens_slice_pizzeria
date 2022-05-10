# Let's talk about pizzas:

# toppings' list:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# slices costs:
prices = [2, 6, 1, 3, 2, 7, 2]

# how many 2$ slices?
num_two_dollar_slices = prices.count(2)

# toppings lenght:
num_pizzas = len(toppings)

# advertise:
print()
print("We sell " + str(num_pizzas) + " different kinds of pizza! Here they are, sorted by ascending price:\n")

# using zip function to zip the content together::
pizza_prices = zip(prices, toppings)

# we gather the data stored in memory and turn it into a list, that we sort by ascending order of price:
pizza_and_prices = list(pizza_prices)
pizza_and_prices.sort()
print(pizza_and_prices)

# identifying cheapest pizza:
cheapest_pizza = pizza_and_prices[0]

# someone comes and buys the las piece of the  most expensive pizza, lets identify it to later remove it:
priciest_pizza = pizza_and_prices[-1]

# removing it:
pizza_and_prices.pop()

# adding new topping, respecting proper sorting order:
pizza_and_prices.insert(4, [2.5, "peppers"])
print("\nSomeone just bought the last piece of the anchovies pizza, but no worries, we have added another, spicy, one:\n\n" + str(pizza_and_prices))

# storing pizza slices for mice:
three_cheapest = pizza_and_prices[0:3]
print("\nAhhhhhhh .... actually today we give the following ones  to a few mice sniffing around: \n\n" + str(three_cheapest) + "\n")
