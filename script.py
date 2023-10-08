# Pizzas Preparation
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

# Count how many $2 slices there are
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# Number of different pizzas
num_pizzas = len(toppings)
print(f"We sell {num_pizzas} different kinds of pizza!")

# Pair the toppings with their prices
pizza_and_prices = list(zip(prices, toppings))
print(pizza_and_prices)

# Sort the pizzas by price
pizza_and_prices.sort()
print(pizza_and_prices)

# Display the cheapest and priciest pizzas
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

# Remove the priciest pizza and add Peppers priced at $2.5
pizza_and_prices.pop()
pizza_and_prices.append([2.5, "Peppers"])
print(pizza_and_prices)

# Display the three cheapest pizzas
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
