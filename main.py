from pyscript import display
#Restaurant Order System Python Data Types

#string data type
restaurant_name = "Max (Ancheta)'s Restaurant"
owner_name = "Maximus A. Ancheta"

#integers
year_Since = 1418

#Float
tax_rate = 0.08

#boolean
has_delivery = True 
is_dine_in = True
is_takeout = False

#list
product_name = ["Carbonara", "Fried Chicken Meal", "Hamburger and Fries","Caesar Salad"]
beverages = ["Iced Tea", "Water"]

#Tuple
business_hours = ("9:00 AM", "9:30 PM")

#dictonary
menu = {
    "Carbonara": 149.99,
    "Fried Chicken Meal": 229.00,
    "Hamburger and Fries": 299.99,
    "Caesar Salad": 150.00,
    "Iced Tea": 49.99,
    "Water":19.69,
    "Mango Fruit Shake": 99.59
}

#Set
common_allergens = ("gluten","dairy","nuts","shellfish")

#display resto information
display(restaurant_name, target="name1")
display(f"Owner:" (owner_name), target="owner")
display(f"Since"(year_Since), target="since")
display(f"Menu Pricelist", target="Reading1")

#displaying Menu items:
display(product_name[0], target="prod1")
display(f"P{menu['Carbonara']:.2f}", target="price1")

display(product_name[1], target="prod2")
display(f"P{menu['Fried Chicken Meal']:.2f}", target="price2")

display(product_name[2], target="prod3")
display(f"P{menu['Hamburger and Fries']:.2f}", target="price3")

display(product_name[3], target="prod4")
display(f"P{menu['Caesar Salad']:.2f}", target="price4")

#BEVERAGE prices, it goes back to 0 because we have another list
display(beverages[0], target="prod1")
display(f"P{menu['Iced Tea']:.2f}", target="price1")

display(beverages[1], target="prod2")
display(f"P{menu['Water']:.2f}", target="price2")

display(beverages[2], target="prod3")
display(f"P{menu['Mango Fruit Shake']:.2f}", target="price3")

#display additional Information
display(f"Open: {business_hours[0]} - {business_hours[1]}", target="openingHours")

#display order type
display(f"Dine In Available", target="orderType")
