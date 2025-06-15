Project Title: Python Console-Based Kitchen Management System
Description:

This project is a console-based Kitchen Management System built entirely using Python and object-oriented programming principles. The application simulates a real-time food ordering experience, allowing customers to interact with a digital menu, place orders, and make payments.

Key Features:

Interactive Menu Ordering System:
Users can browse a predefined menu and order items. Each order dynamically updates a user cart (stored as a dictionary), tracking the item name, quantity, and cost.

Dynamic Quantity Handling:
If the same food item is selected more than once, the system increases the quantity and notifies the user accordingly.

Flexible Payment Options:
Users can choose between:

Cash on Delivery (COD): Adds ₹100 to the final bill.

UPI Payment: Offers a 20% discount on the total bill.
The payment method is selected after order completion, and the final amount is displayed based on the selected option.

Order Continuation:
After each transaction, users are asked whether they want to order more items, enabling multiple orders in one session.

Transaction Logging:
Each transaction is recorded in a central restaurant dictionary with the customer's name and the amount paid, enabling persistent tracking.

Menu Management (Admin):
The system includes class methods that allow modifying or deleting menu items (both name and price), giving flexibility to update the offerings as needed.

Restaurant Summary:
A dedicated class method calculates total earnings and displays overall transaction history for management review.

Information Display:
Another method is included to show basic information about the restaurant.

Language: Python

Core Concepts: Classes, Dictionaries, Conditional Statements, Loops, Input/Output Handling

Conclusion:
This project showcases effective use of Python classes to simulate a real-world kitchen order and management system. It emphasizes user interaction, dynamic data handling, and encapsulated business logic, making it a solid project for learning and demonstrating object-oriented programming in Python.


