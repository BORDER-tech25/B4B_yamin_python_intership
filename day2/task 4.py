
notebook_price = 45
budget = 500
quantity_to_buy = 7


total_cost_7 = notebook_price * quantity_to_buy
print(f"Total cost for {quantity_to_buy} notebooks: {total_cost_7} rupees")


max_notebooks = budget // notebook_price
print(f"Number of notebooks you can buy with {budget} rupees: {max_notebooks}")


money_left = budget % notebook_price
print(f"Money left over after the purchase: {money_left} rupees")