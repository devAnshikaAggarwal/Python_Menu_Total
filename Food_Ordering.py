# Write a program to implement the idea of booking and discount system using functions

# Get User-details
def get_details():
    name = input("Enter your Name: ")
    number = input("Enter your Contact Number: ")
    address = input("Enter your Address: ")
    pincode = input("Enter your Pincode: ")
    return name, number, address, pincode
    
# Show User-details
def show_details(name, number, address, pincode):
    print("Your Details are: ")
    print(f"Name: {name}")
    print(f"Contact Number: {number}")
    print(f"Address: {address}")
    print(f"Pincode: {pincode}")
    
# Order Food
def order_food():
    food = {
        "Burger": 50,
        "Pizza": 100,
        "Pasta": 80,
        "Sandwich": 40,
        "Momos": 30,
        "Noodles": 60,
        "Manchurian": 70,
        "Fried Rice": 60,
        "Ice-cream": 20,
        "Cold-drinks": 30
    }
    
    print("Enter the food items you want to order: ")
    for item, price in food.items():
        print(f"{item}: Rs. {price}")
    print()
    
    order = {}
    while True:
        item = input("Enter the food item you want to order (or type 'done' to finish): ").title()
        if item.lower() == 'done':
            break
        if item in food:
            quantity = int(input(f"Enter the quantity for {item}: "))
            if item in order:
                order[item] += quantity
            else:
                order[item] = quantity
        else:
            print("Invalid item. Please enter a valid food item.")
    
    return order, food

# Calculate Bill
def calculate_bill(order, food):
    total = 0
    print("\nYour Order Summary:")
    for item, quantity in order.items():
        cost = food[item] * quantity
        gst = cost * 0.18
        total += cost + gst 
        print(f"{item}: {quantity} x Rs. {food[item]} = Rs. {cost}")
    print(f"Total GST: Rs. {gst}")
    print(f"Total Bill: Rs. {total}")
    return total

# Discount System
def discount_system(total):
    if total > 1000:
        print("You have got a discount of 20%")
        discount = total * 0.2
    elif total > 500:
        print("You have got a discount of 10%")
        discount = total * 0.1
        print(f"Total Amount after discount: Rs. {total - discount}")
    else:
        print("You have not got any discount")
        discount = 0
    total -= discount
    return total

# Main Function
def main():
    print("Welcome to Food Ordering System")
    print()
    name, number, address, pincode = get_details()
    print()
    order, food = order_food()
    print()
    show_details(name, number, address, pincode)
    total = calculate_bill(order, food)
    total_after_discount = discount_system(total)
    print(f"\nTotal Amount to be paid: Rs. {total_after_discount}")
    print("\nThank you for ordering from us!")

if __name__ == "__main__":
    main()