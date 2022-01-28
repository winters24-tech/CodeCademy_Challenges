# Your code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
print(toppings)

prices = [2, 6, 1, 3, 2, 7, 2]

# Your boss wants you to do research on $2 slices.Count the number of occurrences of 2
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# Find the length of the toppings list
num_pizzas = len(toppings)
print("We sell", num_pizzas, "different kinds of pizza!", "\n")

# Use the existing data about the pizza toppings and prices to create a new two-dimensional list
pizza_and_prices = [[2, "pepperoni"],
                    [6, "pineapple"],
                    [1, "cheese"],
                    [3, "sausage"],
                    [2, "olives"],
                    [7, "anchovies"],
                    [2, "mushrooms"]
                    ]
print(pizza_and_prices, "\n")

# Sorting and Slicing Pizzas
sorted_slices = pizza_and_prices.sort()
print(pizza_and_prices, "\n")

cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)

priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza, "\n")


# It looks like the most expensive pizza from the prev step was our last "anchovies" slice. Remove it from our list since the man bought the last slice.

pizza_and_prices.remove(pizza_and_prices[-1])
print(pizza_and_prices, "\n")

# Since there is no more "anchovies" pizza, we're adding a topping to our list called "peppers" making your customers excited about new toppings.

pizza_and_prices.append([2.5, "peppers"])
print(pizza_and_prices, "\n")

# Three mice walk into the store want different pizzas. Slice the pizza_and_prices list and store the 3 lowest cost pizzas 
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
