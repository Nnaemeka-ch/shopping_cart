#ShoppingCart 

from collections import Counter

food_items = {"Rice":10, "Beans":20, "Ponmo":5, "Plaintain":5, "Spaghetti":20}
shopping_cart = []
Total = 0


user_order = input("Enter your order: ").strip().lower()  # Normalize input to lowercase

while user_order != 'q':
    if user_order.strip() == "":
        print("Please enter a valid order")
        user_order = input("Enter your order: ").strip().lower()  # Re-ask for input
        continue
        
    # Check if the item exists (case insensitive)
    if user_order not in [item.lower() for item in food_items.keys()]:
        print("Item not available!")
    else:
        # Append item in title case for display consistency
        shopping_cart.append(user_order.title())  
        Total += food_items[user_order.title()]

    user_order = input("Enter another order (q to quit): ").strip().lower()


# Count occurrences of each item in shopping_cart
item_counts = Counter(shopping_cart)

# Format the order list to include quantity if an item appears more than once
order_list = ", ".join(f"{item} ({count}x)" if count > 1 else item for item, count in item_counts.items())



# Display order summary
if shopping_cart:
    print(f"You have ordered: {order_list}. Your total cost is: ${Total:.2f}")
else:
    print("You didn't order anything.")  


