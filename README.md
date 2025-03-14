# Food Ordering and Discount System

This is a simple Python program that allows users to place food orders, calculate the total bill including GST, and apply discounts based on the total amount.

## Features
- Collect user details (Name, Contact, Address, Pincode)
- Display available food items with prices
- Allow users to select and order multiple food items
- Calculate the total bill including an 18% GST
- Apply discounts based on the total bill:
  - **10% discount** for orders above **Rs. 500**
  - **20% discount** for orders above **Rs. 1000**
- Display order summary and final payable amount

## How to Run
1. Clone the repository or copy the script.
2. Run the script using Python:
   ```sh
   python food_ordering.py
   ```
3. Follow the on-screen prompts to place an order.

## Example Output
```
Welcome to Food Ordering System

Enter your Name: John Doe
Enter your Contact Number: 1234567890
Enter your Address: 123 Main Street
Enter your Pincode: 456789

Your Order Summary:
Pizza: 2 x Rs. 100 = Rs. 200
Total GST: Rs. 36.0
Total Bill: Rs. 236.0
You have not got any discount
Total Amount to be paid: Rs. 236.0

Thank you for ordering from us!
```
