# Dictionary containing the price of each fruit
price_list = {
    'apple': 1.20,
    'orange': 1.40,
    'watermelon': 6.50,
    'pineapple': 2.70,
    'pear': 0.90,
    'papaya': 2.95,
    'pomegranate': 4.95
}

# Dictionary containing the quantity of each fruit purchased
quantity_list = {
    'apple': 5,
    'orange': 5,
    'watermelon': 1,
    'pineapple': 2,
    'pear': 10,
    'papaya': 1,
    'pomegranate': 2
}

# Function to calculate the total cost of all fruits in the shopping list
def total_cost_shopping():
    total_cost = 0  # Initialize total cost

    # Iterate over each fruit name in the price list
    for key in price_list.keys():
        # Check if the fruit also exists in the quantity list
        if key in quantity_list:
            # Add the product of price and quantity to the total cost
            total_cost += quantity_list[key] * price_list[key]

    print("total cost = ", total_cost)

    
    return total_cost

# Function to calculate the cost of a specific fruit and quantity
def cost_of_fruits(fruit, quantity):
    # Loop through all the fruits in the price list
    for key in price_list.keys():
        if key == fruit:  # Find the matching fruit
            cost = quantity * price_list[key]  # Compute cost
            break  # No need to continue looping once the fruit is found

    print("cost of", quantity, fruit, "=", cost)
    return cost

# Main function to run the above-defined functions
def main():
    cost_of_fruits('apple', 10)  # Cost of buying 10 apples
    total_cost_shopping()        # Total cost of all fruits in the shopping list

# This ensures that main() runs only when this script is executed directly
if __name__ == "__main__":
    main()
